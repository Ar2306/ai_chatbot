import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('microsoft/DialoGPT-medium')  
model = GPT2LMHeadModel.from_pretrained('microsoft/DialoGPT-medium')
model.eval()
tokenizer.pad_token = tokenizer.eos_token  # Set pad_token to eos_token
def chatbot(input_text):
    inputs = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')  
    with torch.no_grad():
        output = model.generate(
            inputs, 
            max_length=100, 
            num_return_sequences=1, 
            no_repeat_ngram_size=2, 
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True 
        )
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response
if __name__ == "__main__":
    print("AI Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'bye':
            print("AI Chatbot: Goodbye!")
            break
        response = chatbot(user_message)
        print(f"AI Chatbot: {response}")
