import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_response, conversation_history

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("400x500")
        
        # Chat window
        self.chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_window.pack(padx=10, pady=10, expand=True, fill='both')

        # Entry box
        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=10, fill='x')
        self.entry.bind("<Return>", self.send_message)
        
        # Conversation history
        self.conversation_history = conversation_history

    def send_message(self, event):
        user_input = self.entry.get()
        if user_input.strip():
            self.entry.delete(0, tk.END)
            self.display_message(f"You: {user_input}\n", "user")

            response, self.conversation_history = get_response(user_input, self.conversation_history)
            self.display_message(f"Bot: {response}\n", "bot")

    def display_message(self, message, sender):
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, message)
        self.chat_window.config(state='disabled')
        self.chat_window.see(tk.END)  # Auto-scroll to the latest message

        # Style user and bot messages differently
        if sender == "user":
            self.chat_window.tag_add("user", "end-2l", "end-1c")
            self.chat_window.tag_config("user", foreground="blue")
        elif sender == "bot":
            self.chat_window.tag_add("bot", "end-2l", "end-1c")
            self.chat_window.tag_config("bot", foreground="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
