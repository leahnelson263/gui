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
        self.button_frame = tkinter.Frame(self.main_window)


        self.label1 = tkinter.Label(self.top_frame, text='John')
        self.label2 = tkinter.Label(self.top_frame, text='James')
        self.label3 = tkinter.Label(self.top_frame, text='Jack')

        self.label1.pack(side='left')      
        self.label2.pack(side='left')      
        self.label3.pack(side='left')


        self.label4 = tkinter.Label(self.bottom_frame, text='Jill')
        self.label5 = tkinter.Label(self.bottom_frame, text='Jamie')
        self.label6 = tkinter.Label(self.bottom_frame, text='Jennifer')

        self.label4.pack(side='left')      
        self.label5.pack(side='left')      
        self.label6.pack(side='left')


        #create a Button widget. the text 'Click Me!'
        #should appear on the face of the Button. the 
        #do_something mehtod should be exeuted when
        #the user clicks the Button

        self.my_button = tkinter.Button(self.button_frame, text='Click Me!', command=self.do_something)       #Button(where you want to create the Button, text, what you want to happen when clicked)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()

        self.my_button.pack(side='left')
        self.quit_button.pack(side='right')




        tkinter.mainloop()

    
    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button!')

#create an instance of the MyGUI class (otherwise it wont run)
my_gui = MyGUI()

print('moving on...')       #this print once the user closes the window
