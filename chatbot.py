# chatbot.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Initialize conversation history | limiting the conversation history is needed
conversation_history = [] # only  the last 5 entries will kept in the memory

# Function to get the bot's response
def get_response(input_text, conversation_history, num_beams = 5):
    # Update history string
    conversation_history = conversation_history[-5:]
    history_string = "\n".join(conversation_history)
    
    # Tokenize user input and chat history
    inputs = tokenizer.encode_plus(history_string + input_text, return_tensors="pt", truncation=True)
    
    # Generate the output from the model
    outputs = model.generate(**inputs,
                             num_beams=num_beams,  # Number of beams to explore
                             no_repeat_ngram_size=2,  # Prevent repetition (optional)
                            )
    
    # Decode the output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    # Update conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
    
    return response, conversation_history

if __name__ == "__main__":
    import sys
    input_text = " ".join(sys.argv[1:])
    response, conversation_history = get_response(input_text, conversation_history)
    print(response)
