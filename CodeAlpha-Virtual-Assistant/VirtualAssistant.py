import tkinter as tk
from tkinter import scrolledtext
import random
from difflib import SequenceMatcher
from datetime import datetime


class CorporateVirtualAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeAlpha Virtual Assistant")
        self.root.geometry("500x680")
        self.root.configure(bg="#F3F4F6")
        self.root.resizable(False, False)

        self.message_count = 0

        self.intents = [
            {
                "tag": "greeting",
                "patterns": ["hello", "hi", "good morning", "good afternoon", "greetings"],
                "responses": [
                    "Hello. How may I assist you today?",
                    "Good day. What can I help you with?",
                    "Greetings. Please let me know how I can assist."
                ]
            },

            {
                "tag": "status",
                "patterns": ["how are you", "status", "system status"],
                "responses": [
                    "All systems are functioning normally.",
                    "I am operating correctly and ready to assist."
                ]
            },

            {
                "tag": "identity",
                "patterns": ["your name", "who are you", "designation"],
                "responses": [
                    "I am the CodeAlpha Virtual Assistant.",
                    "I am an automated support system developed in Python."
                ]
            },

            {
                "tag": "capabilities",
                "patterns": ["help", "what can you do", "support", "options"],
                "responses": [
                    "Available commands:\n"
                    "- hello\n"
                    "- how are you\n"
                    "- your name\n"
                    "- time\n"
                    "- stats\n"
                    "- clear chat\n"
                    "- bye"
                ]
            },

            {
                "tag": "time",
                "patterns": ["time", "date", "current time", "today"],
                "responses": []
            },

            {
                "tag": "stats",
                "patterns": ["stats", "messages", "usage"],
                "responses": []
            },

            {
                "tag": "goodbye",
                "patterns": ["bye", "goodbye", "exit", "close"],
                "responses": [
                    "Goodbye. Have a productive day.",
                    "Session ended successfully.",
                    "Thank you for using CodeAlpha Virtual Assistant."
                ]
            }
        ]

        self.setup_ui()

        self.append_message(
            "System",
            "Connection established. Welcome to the CodeAlpha support portal.",
            "bot_tag"
        )

    def setup_ui(self):

        header = tk.Frame(self.root, bg="#1F2937", height=60)
        header.pack(fill=tk.X)

        title = tk.Label(
            header,
            text="CodeAlpha Virtual Assistant",
            bg="#1F2937",
            fg="white",
            font=("Segoe UI", 13, "bold")
        )
        title.pack(pady=15)

        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Segoe UI", 11),
            bg="white",
            fg="#111827"
        )

        self.chat_area.pack(
            padx=20,
            pady=20,
            fill=tk.BOTH,
            expand=True
        )

        self.chat_area.config(state=tk.DISABLED)

        self.chat_area.tag_config(
            "user_tag",
            foreground="#2563EB",
            font=("Segoe UI", 11, "bold")
        )

        self.chat_area.tag_config(
            "bot_tag",
            foreground="#4B5563",
            font=("Segoe UI", 11, "bold")
        )

        input_frame = tk.Frame(self.root, bg="#F3F4F6")
        input_frame.pack(fill=tk.X, padx=20, pady=10)

        self.user_input = tk.Entry(
            input_frame,
            font=("Segoe UI", 11)
        )

        self.user_input.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=(0, 10),
            ipady=7
        )

        send_btn = tk.Button(
            input_frame,
            text="Send",
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            command=self.handle_send
        )

        send_btn.pack(side=tk.LEFT)

        clear_btn = tk.Button(
            input_frame,
            text="Clear",
            bg="#6B7280",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            command=self.clear_chat
        )

        clear_btn.pack(side=tk.LEFT, padx=5)

        self.user_input.bind(
            "<Return>",
            lambda event: self.handle_send()
        )

    def append_message(self, sender, message, tag):

        self.chat_area.config(state=tk.NORMAL)

        self.chat_area.insert(
            tk.END,
            f"{sender}: ",
            tag
        )

        self.chat_area.insert(
            tk.END,
            f"{message}\n\n"
        )

        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def clear_chat(self):

        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.config(state=tk.DISABLED)

        self.append_message(
            "System",
            "Chat history cleared.",
            "bot_tag"
        )

    def similarity(self, a, b):

        return SequenceMatcher(
            None,
            a.lower(),
            b.lower()
        ).ratio()

    def analyze_input(self, message):

        msg = message.lower()

        if "clear chat" in msg:
            self.clear_chat()
            return None, None

        if any(word in msg for word in ["time", "date", "today"]):
            return (
                datetime.now().strftime(
                    "Current Date & Time: %d-%m-%Y %H:%M:%S"
                ),
                "time"
            )

        if any(word in msg for word in ["stats", "messages", "usage"]):
            return (
                f"Messages processed: {self.message_count}",
                "stats"
            )

        best_tag = None
        best_score = 0

        for intent in self.intents:

            for pattern in intent["patterns"]:

                score = self.similarity(msg, pattern)

                if pattern in msg:
                    score = max(score, 0.90)

                if score > best_score:
                    best_score = score
                    best_tag = intent["tag"]

        if best_score >= 0.65:

            for intent in self.intents:

                if intent["tag"] == best_tag:

                    return (
                        random.choice(intent["responses"]),
                        best_tag
                    )

        return (
            random.choice([
                "I am unable to process that request.",
                "Please try rephrasing your query.",
                "Type 'help' to see available commands."
            ]),
            None
        )

    def handle_send(self):

        user_msg = self.user_input.get().strip()

        if not user_msg:
            return

        self.message_count += 1

        self.append_message(
            "Client",
            user_msg,
            "user_tag"
        )

        self.user_input.delete(0, tk.END)

        response, tag = self.analyze_input(user_msg)

        if response:

            self.root.after(
                400,
                lambda: self.append_message(
                    "System",
                    response,
                    "bot_tag"
                )
            )

        if tag == "goodbye":

            self.root.after(
                2000,
                self.root.destroy
            )


if __name__ == "__main__":

    root = tk.Tk()

    app = CorporateVirtualAssistant(root)

    root.mainloop()
