import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        #create the main window widget and assign it to the variable 'main window'.
        self.main_window = tkinter.Tk()

        #configure the main window
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        #create two frames, one for the top of the
        #window, and one for the bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create an IntVar object/variable to use with
        # the Radiobuttons.

        self.radio_var = tkinter.IntVar()

        self.radio_var.set(1)       #if you dont want a default... comment this line out

        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 1',
                                       variable=self.radio_var,
                                       value=1,
                                       command=self.show_choice)
        

        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 2',
                                       variable=self.radio_var,
                                       value=2)
        

        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 3',
                                       variable=self.radio_var,
                                       value=3)
        

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()




        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='right')


        tkinter.mainloop()

    
    def show_choice(self):
        tkinter.messagebox.showinfo('Selection', 'You have selected option ' + str(self.radio_var.get()))

#create an instance of the MyGUI class (otherwise it wont run)
my_gui = MyGUI()

print('moving on...')       #this print once the user closes the window