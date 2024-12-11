import tkinter as tk
from utils.translation_api import translate_text
from utils.response_logic import get_response


class ChatbotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multi-Language Chatbot")

        tk.Label(self.root, text="Select Language :", font=("Helvetica", 12)).pack(pady=5)
        self.language_var = tk.StringVar(value="en")
        tk.OptionMenu(self.root, self.language_var, "en", "hi", "es").pack(pady=5)

        self.chat_display = tk.Text(self.root, height=20, width=60, state=tk.DISABLED)
        self.chat_display.pack(pady=10)

        self.user_input = tk.Entry(self.root, width=50, font=("Helvetica", 12))
        self.user_input.pack(pady=5)
        tk.Button(self.root, text="Send", command=self.send_message).pack(pady=5)

    def send_message(self):
        user_text = self.user_input.get()
        user_lang = self.language_var.get()

        if user_text.strip():
            self.display_message("You", user_text)
            translated_query = translate_text(user_text, user_lang, "en")
            response = get_response(translated_query, user_lang)
            self.display_message("Bot", response)
            self.user_input.delete(0, tk.END)

    def display_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def run(self):
        self.root.mainloop()
