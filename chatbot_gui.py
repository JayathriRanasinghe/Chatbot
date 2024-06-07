# chatbot_gui.py
import tkinter as tk
from chatbot import get_response, conversation_history

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("400x500")
        
        self.text_area = tk.Text(root, wrap='word', state='disabled')
        self.text_area.pack(padx=10, pady=10, expand=True, fill='both')
        
        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=10, fill='x')
        self.entry.bind("<Return>", self.send_message)
        
        self.conversation_history = conversation_history

    def send_message(self, event):
        user_input = self.entry.get()
        if user_input.strip():
            self.entry.delete(0, tk.END)
            self.display_message("You: " + user_input)
            
            response, self.conversation_history = get_response(user_input, self.conversation_history)
            self.display_message("Bot: " + response)

    def display_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, message + '\n')
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
