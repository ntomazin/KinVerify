import time
from PIL import ImageTk, Image
import PIL.Image
import tkinter
from resizeimage import resizeimage
from tkinter import *
from tkinter import filedialog
from src.program import Program

n_test_data = 10
path = '/home/piki/Desktop/faks/Computer_vision/KinFaceW-I_rezultati/KinFaceW-I'

class Settings:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x420")
        self.root.resizable(False, False)
        self.root.title('Settings for Kinship Verification')
        super().__init__()
        #self.n_test_data = n_test_data
        self.main_frame()
        self.root.mainloop()

    def set_num(self, value):
        global n_test_data
        n_test_data = value
        #print(n_test_data)

    def main_frame(self):
        self.f1 = tkinter.Frame(self.root, width=500, height=420, bg='white')
        self.f1.pack(fill=tkinter.X)

        #chose dir
        question = 'Choose the directory you want to test'
        question_label = tkinter.Label(self.f1, text=question, font=("Calibri", 16), bg='white')
        question_label.place(x=0, y=0)

        self.chose_btn = tkinter.Button(self.f1, text='Chose Directory!', bg='black', fg='white', font=("Calibri", 18),
                                    activebackground='white', activeforeground='black',
                                    command=lambda: (self.chose_dir()))
        self.chose_btn.place(x=130, y=50)


        #chose number of pictures
        question = 'Choose how many pictures you want to test'
        question_label = tkinter.Label(self.f1, text=question, font=("Calibri", 16), bg='white')
        question_label.place(x=0, y=100)

        # DROPDOWN MENU
        global n_test_data
        variable = StringVar(self.root)
        variable.set(n_test_data)  # default value
        self.option_menu = OptionMenu(self.root, variable, "  5", "10", "20", "50")
        self.option_menu.place(x=200, y=150)

        # about button
        self.about_btn = tkinter.Button(self.f1, text='About', bg='black', fg='white', font=("Calibri", 18),
                                       activebackground='white', activeforeground='black',
                                       command=lambda: (self.about()))
        self.about_btn.place(x=200, y=200)

        #next button
        self.next_btn = tkinter.Button(self.f1, text='Next!', bg='black', fg='white', font=("Calibri", 18),
                                       activebackground='white', activeforeground='black',
                                       command=lambda: (self.set_num(variable.get()), self.root.destroy()))
        self.next_btn.place(x=200, y=300)

    def chose_dir(self):
        self.root.filename = filedialog.askdirectory(
            initialdir=path,
            title="Select directory"
        )
            # print(self.root.filename)

    def about(self):
        self.f1.destroy()
        self.f2 = tkinter.Frame(self.root, width=500, height=420, bg='white')
        self.f2.pack(fill=tkinter.X)

        result = 'This is a project that lets you identify\n if two people are kin related.\n' \
                 'After you have chosen yes/no you will get\n feedbackon what the computer answered\n' \
                 'and what is correct(The answer will be\n adequately colored)'
        last = tkinter.Label(self.f2, text=result, font=("Calibri", 15), fg='black', bg='white')
        last.place(x=40, y=0)

        self.you_label = tkinter.Label(self.f2, text='You', font=("Calibri", 15), bg='green')
        self.you_label.place(x=115, y=180)

        self.comp_label = tkinter.Label(self.f2, text='Computer', font=("Calibri", 15), bg='red')
        self.comp_label.place(x=195, y=180)

        self.corr_label = tkinter.Label(self.f2, text='Correct', font=("Calibri", 15), bg='green')
        self.corr_label.place(x=315, y=180)

        result2 = '(This means: you guessed \"yes\", the computer \nguessed \"no\" and the correct \nanswer is \"yes\")'
        explain = tkinter.Label(self.f2, text=result2, font=("Calibri", 15), fg='black', bg='white')
        explain.place(x=20, y=210)

        self.back_btn = tkinter.Button(self.f2, text='Back', bg='black', fg='white', font=("Calibri", 18),
                                       activebackground='white', activeforeground='black',
                                       command=lambda: (self.f2.destroy(), self.main_frame()))
        self.back_btn.place(x=200, y=300)








