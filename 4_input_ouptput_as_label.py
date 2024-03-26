import tkinter
import tkinter.messagebox


class KiloConverter:
    def __init__(self):
        # create the main window widget and assign it to the variable 'main window'.
        self.main_window = tkinter.Tk()

        #configure the main window
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        # create two frames, one for the top of the
        # window, and one for the bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in Kilometers: ')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')      
        self.kilo_entry.pack(side='left')


        self.desc_label = tkinter.Label(self.mid_frame, text='Converted to miles: ')

        # we need to StringVar object/variable to associate with
        # an output label. Use th eobject's set method
        # to store a string of blank characters

        self.miles_label_var = tkinter.StringVar()


        # create a label and associate it with the 
        # StringVar object. any value stored int he 
        # StringVar object will automatically be displayed
        # in the label

        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.miles_label_var)

        self.desc_label.pack(side='left')
        self.miles_label.pack(side='left')



        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')


        tkinter.mainloop()

    
    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = round(kilo * 0.6214,2)

        self.miles_label_var.set(miles)

        #tkinter.messagebox.showinfo('Result', str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles.')

# create an instance of the MyGUI class (otherwise it wont run)
my_gui = KiloConverter()

print('moving on...')       #this print once the user closes the window
