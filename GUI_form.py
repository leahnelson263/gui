import tkinter
import tkinter.messagebox


class Form:

    def __init__(self):
        self.main_window = tkinter.Tk()

        #main window design
        self.main_window.geometry('350x550')
        self.main_window.title('Responsive Registration Form')
        self.main_window.configure(padx=30, pady=20)


        #create frames
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)
        self.frame7 = tkinter.Frame(self.main_window)
        self.frame8 = tkinter.Frame(self.main_window)  
        self.frame9 = tkinter.Frame(self.main_window)  
        

        #main title (frame 1)
        self.title = tkinter.Label(self.frame1, text='Responsive Registration \n Form', 
                                   fg='royalblue', font=('Arial', 12, 'bold'))
        
        self.frame1.pack(pady=10)
        self.title.pack()


        #USER INPUT (frames 2,3,4,5) --------------------------------------------------------------------------------------------------------
        #email (frame 2)
        self.email_var = tkinter.StringVar()
        self.email = tkinter.Entry(self.frame2, textvariable=self.email_var, width=40, font=('Arial', 10))
        self.email_var.set('Email')  # Set placeholder text
        self.email.configure(fg='grey')  # Set placeholder text color
        
  
        #creating icon (mail)
        self.email_icon = tkinter.PhotoImage(file='mail.png')
        self.email_icon = self.email_icon.subsample(9, 9)  # Resizing the image to 1/9 of its original size
        self.email_icon_label = tkinter.Label(self.frame2, image=self.email_icon)


        self.frame2.pack(pady=10)
        self.email_icon_label.pack(side='left')
        self.email.pack()



        #Password (frame 3)
        self.password = tkinter.Label(self.frame3, text='Password:')
        self.password_entry = tkinter.Entry(self.frame3, width=40, show='*')

        #creating icon 
        self.lock_icon = tkinter.PhotoImage(file='lock.png')
        self.lock_icon = self.lock_icon.subsample(9, 9)  # Resizing the image to 1/9 of its original size
        self.lock_icon_label = tkinter.Label(self.frame3, image=self.lock_icon)

        
        self.frame3.pack(pady=10)
        self.lock_icon_label.pack(side='left')
        self.password.pack(side='left')
        self.password_entry.pack()


        #Re-type Password (frame 4)
        self.retype = tkinter.Label(self.frame4, text='Re-type Password:')
        self.retype_entry = tkinter.Entry(self.frame4, width=40, show='*') 

        #create icon (lock)
        self.lock_icon1 = tkinter.PhotoImage(file='lock2.png')
        self.lock_icon1 = self.lock_icon1.subsample(9, 9)  # Resizing the image to 1/9 of its original size
        self.lock_icon1_label = tkinter.Label(self.frame4, image=self.lock_icon1)

        
        self.frame4.pack(pady=10)
        self.lock_icon1_label.pack(side='left')
        self.retype.pack(side='left')
        self.retype_entry.pack()


        #First Name & Last Name (frame 5)
        self.first_name_var = tkinter.StringVar()
        self.last_name_var = tkinter.StringVar()
        
        self.first_name = tkinter.Entry(self.frame5, textvariable=self.first_name_var, 
                                        width=15, font=('Arial', 10))
        self.last_name = tkinter.Entry(self.frame5, textvariable=self.last_name_var, 
                                       width=20, font=('Arial', 10))
        
        self.first_name_var.set('First Name')  
        self.last_name_var.set('Last Name')  
        
        self.first_name.configure(fg='grey')  
        self.last_name.configure(fg='grey') 

        # Creating icon (first name)
        self.first_icon = tkinter.PhotoImage(file='person.png')
        self.first_icon = self.first_icon.subsample(9, 9)  # Resizing the image to 1/9 of its original size
        self.first_icon_label = tkinter.Label(self.frame5, image=self.first_icon)

         # Creating icon (last name)
        self.last_icon = tkinter.PhotoImage(file='person2.png')
        self.last_icon = self.last_icon.subsample(9, 9)  # Resizing the image to 1/9 of its original size
        self.last_icon_label = tkinter.Label(self.frame5, image=self.last_icon)


        self.frame5.pack(pady=10)
        self.first_icon_label.pack(side='left')
        self.first_name.pack(side='left')
        self.last_icon_label.pack(side='left')
        self.last_name.pack(side='left')


        #RADIO BOXES - gender (frame 6) ----------------------------------------------------------------------------------------------------
        self.radio_var = tkinter.IntVar()

        self.male = tkinter.Radiobutton(self.frame6,
                                        text='Male',
                                        variable=self.radio_var,
                                        value=1)
        
        self.female = tkinter.Radiobutton(self.frame6,
                                          text='Female',
                                          variable=self.radio_var,
                                          value=2)
        
        self.frame6.pack(anchor='w', pady=10)
        self.male.pack(side='left')
        self.female.pack(side='left')


        #DROP DOWN BOX - country (frame 7) --------------------------------------------------------------------------------------------------

        self.options = [
            "United States of America",
            "Brazil",
            "Kenya",
            "Mexico",
            "Norway"
        ]

        self.selected = tkinter.StringVar()
        self.selected.set('Select a country')    #set a placeholder
        self.drop = tkinter.OptionMenu(self.frame7, self.selected, *self.options)
        self.drop.configure(width=40, font=('Arial', 8, 'bold'), fg='white', bg='royalblue')
        self.drop['menu'].configure(font=('Arial', 8))


        self.frame7.pack(pady=10)
        self.drop.pack(side='left')



        #CHECK BOXES (frame 8) - need to check both -----------------------------------------------------------------------------------------
        self.cb1_var = tkinter.IntVar()
        self.cb2_var = tkinter.IntVar()

        self.cb1_var.set(0)
        self.cb2_var.set(0)

        self.cb1 = tkinter.Checkbutton(self.frame8,
                                       text='I agree with terms and conditions',
                                       variable=self.cb1_var)
        
        self.cb2 = tkinter.Checkbutton(self.frame8,
                                       text='I want to receive the newsletter',
                                       variable=self.cb2_var)
        
        self.frame8.pack(anchor='w', pady=10)
        self.cb1.pack()
        self.cb2.pack(anchor='w')


        #REGISTER BUTTON (frame 9) - validate -----------------------------------------------------------------------------------------------
        self.register = tkinter.Button(self.frame9, text='Register', width=40, 
                                       font=('Arial', 8, 'bold'), fg='white', 
                                       bg='royalblue', command=self.validate)

        self.frame9.pack(pady=10)
        self.register.pack()

        tkinter.mainloop()


    def validate(self):

        message = ''
        #gender - one is selected
        if self.radio_var.get() not in [1, 2]:
            message += '\nYou must select a gender.'
            
        #check boxes - both need to be checked
        if self.cb1_var.get() ==0 or self.cb2_var.get() == 0:
            message += '\nYou must check both boxes.'


        #password inputs - they both match
        if self.password_entry.get() != self.retype_entry.get():
            message += '\nYour passwords do no match.'

        #password hidden - only has ***
        if self.password_entry.get() == '***' or self.retype_entry.get() == '***':
            message += '\nPassword is not hidden.'

        if message:
            tkinter.messagebox.showinfo('ERRORS:', message)
        else:
            tkinter.messagebox.showinfo('SUCCESS', 'You have registered!')

    

instance = Form()