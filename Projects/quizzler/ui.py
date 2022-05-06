from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    # The QuizBrain after : in the below code define the datatype which the quiz_brain variable should have so
    # anything passed except outputs from QuizzBrain class is not accepted
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text='Score : 0', bg=THEME_COLOR, fg='#fff')
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='#fff', highlightthickness=0)
        self.q_text = self.canvas.create_text(150, 125, width=280, text="Lorem Ipsum", fill='#000', font=('Arial', 20, 'italic'))
        self.canvas.grid_configure(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, bd=0, command=self.check_answer_true)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, bd=0, command=self.check_answer_false)
        self.false_btn.grid(column=1, row=2)

        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg='#fff')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            ques_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=ques_text)
        else:
            self.canvas.itemconfig(self.q_text, text=f"You have reach the end of the questions!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_ques)