import tkinter

class MyGUI:
    def __init__(self):
        #create the main window widget and assign it to the variable 'main window'.
        self.main_window = tkinter.Tk()

        #configure the main window
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        #create a label widget containing the text 'Hello World!'
        #the 'label1' is part of the root widget 'main_window'
        #this means we are creating a lable in the main window

        self.label1 = tkinter.Label(self.main_window, text='Hello World!')
        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program')


        #call the pack method for each label
        #the pack method determines where a widget should be positioned and makes
        #the widget visible when the main window is displayed.

        #if you leave the () empty it is the default and it is 'top'

        self.label1.pack(side='left')      #if you dont have these nothing will print
        self.label2.pack(side='right')      #if you comment out the label1 it will print out label2 at the top


        #enter the tkinter main loop. this function runs like a infinite
        #loop until you close the main window

        tkinter.mainloop()

#create an instance of the MyGUI class (otherwise it wont run)
my_gui = MyGUI()

print('moving on...')       #this print once the user closes the window
