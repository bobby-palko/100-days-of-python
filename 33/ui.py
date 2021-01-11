from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 14, "italic")
SCORE_FONT = ("Arial", 10, "bold")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=SCORE_FONT)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.q_text = self.canvas.create_text(
            150, 
            125,
            width=280, 
            font=QUESTION_FONT, 
            text="Hello!", 
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=lambda: self.btn_pressed("True"))
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=lambda: self.btn_pressed("False"))
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=question)
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def btn_pressed(self, answer: str):
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)