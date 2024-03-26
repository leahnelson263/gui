import tkinter


class Score:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #main window design
        self.main_window.geometry('550x275')
        self.main_window.title('Student Test Average')
        self.main_window.configure(bg='green') 


        #create frames
        self.one_frame = tkinter.Frame(self.main_window)
        self.two_frame = tkinter.Frame(self.main_window)
        self.three_frame = tkinter.Frame(self.main_window)
        self.four_frame = tkinter.Frame(self.main_window)
        self.five_frame = tkinter.Frame(self.main_window)



        #user input (frames 1,2,3)
        self.exam1 = tkinter.Label(self.one_frame, text='Enter the score for test 1:', bg='green', fg='yellow', font=('Comic Sans MS', 15))
        self.exam1_entry = tkinter.Entry(self.one_frame, width=10, bg='green', fg='yellow', font=('Comic Sans MS', 15))

        self.exam2 = tkinter.Label(self.two_frame, text='Enter the score for test 2:', bg='green', fg='yellow', font=('Comic Sans MS', 15))
        self.exam2_entry = tkinter.Entry(self.two_frame, width=10, bg='green', fg='yellow', font=('Comic Sans MS', 15))

        self.exam3 = tkinter.Label(self.three_frame, text='Enter the score for test 3:', bg='green', fg='yellow', font=('Comic Sans MS', 15))
        self.exam3_entry = tkinter.Entry(self.three_frame, width=10, bg='green', fg='yellow', font=('Comic Sans MS', 15))

        #packing
        self.one_frame.pack(anchor='w')
        self.two_frame.pack(anchor='w')
        self.three_frame.pack(anchor='w')

        self.exam1.pack(side='left')
        self.exam1_entry.pack(side='left')

        self.exam2.pack(side='left')
        self.exam2_entry.pack(side='left')

        self.exam3.pack(side='left')
        self.exam3_entry.pack(side='left')



        #average display (frame 4)
        self.desc_label = tkinter.Label(self.four_frame, text='Average: ', bg='green', fg='yellow', font=('Comic Sans MS', 15))
        self.avg_label_var = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.four_frame, textvariable=self.avg_label_var, bg='green', fg='yellow', font=('Comic Sans MS', 15))
        
        #packing
        self.four_frame.pack()

        self.desc_label.pack(side='left')
        self.avg_label.pack(side='left')


        #buttons (frame 5)
        self.avg_button = tkinter.Button(self.five_frame, text='Average', command=self.average, bg='green', fg='yellow', font=('Comic Sans MS', 15))
        self.quit_button = tkinter.Button(self.five_frame, text='Quit', command=self.main_window.destroy, bg='green', fg='yellow', font=('Comic Sans MS', 15))


        #packing
        self.five_frame.pack()

        self.avg_button.pack(side='left')
        self.quit_button.pack(side='right')




        tkinter.mainloop()


    def average(self):
        avg = round((float(self.exam1_entry.get()) + float(self.exam2_entry.get()) + float(self.exam3_entry.get())) / 3, 2)
        self.avg_label_var.set(avg)

instance = Score()