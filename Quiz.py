import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.score = 0
        self.current_question = 0
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Jupiter", "Venus", "Mercury"],
                "correct_answer": "Mars"
            },
            # Add more questions here
        ]
        
        self.question_label = tk.Label(root, text="", wraplength=300)
        self.question_label.pack(pady=10)
        
        self.option_var = tk.StringVar()
        self.option_var.set(None)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(root, text="", variable=self.option_var, value=i)
            self.option_buttons.append(button)
            button.pack(pady=5)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)
        
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
        else:
            self.show_results()
    
    def submit_answer(self):
        if self.option_var.get() is not None:
            selected_option = self.option_var.get()
            correct_answer = self.questions[self.current_question]["correct_answer"]
            
            if self.option_buttons[int(selected_option)].cget("text") == correct_answer:
                self.score += 1
            
            self.current_question += 1
            self.load_question()
    
    def show_results(self):
        result_text = f"You scored {self.score} out of {len(self.questions)}!"
        messagebox.showinfo("Quiz Results", result_text)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
