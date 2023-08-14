from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'Fields cannot to be empty')

    elif usernameEntry.get()=='Tasnim' and passwordEntry.get()=='2112003':
        window.destroy() 
        import sms
        

    else:
        messagebox.showerror('Error', 'Please enter correct information')

window = Tk()

window.geometry('1280x700+0+0')
window.title('Login System of student mangement system')

window.resizable(False,False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window,image = backgroundImage)
bgLabel.place(x = 0, y = 0)

loginFrame=Frame(window, bg = 'paleTurquoise')
loginFrame.place(x = 400, y = 150)

logoImage = PhotoImage(file = 'logo.png')

logoLabel = Label(loginFrame, image = logoImage, bg ='paleTurquoise' )
logoLabel.grid(row=0, column=0, columnspan = 2, pady = 10)

usernameImage = PhotoImage(file = 'user.png')
usernameLabel = Label(loginFrame, image = usernameImage, text = ' Username', compound = LEFT,
                      font = ('times new roman', 20, 'bold'), bg = 'hot pink',fg='steel blue')
usernameLabel.grid(row = 1, column = 0, pady = 10, padx = 20)

usernameEntry = Entry(loginFrame, font = ('times new roman', 20, 'bold'), bd = 5, fg ='steel blue')
usernameEntry.grid(row = 1, column = 1, pady = 10, padx = 20)


passwordImage = PhotoImage(file = 'password.png')
passwordLabel = Label(loginFrame, image = passwordImage, text = ' Password', compound = LEFT,
                      font = ('times new roman', 20, 'bold'), bg = 'hot pink',fg='steel blue')
passwordLabel.grid(row = 2, column = 0, pady = 10, padx = 20)

passwordEntry = Entry(loginFrame, font = ('times new roman', 20, 'bold'), bd = 5, fg ='steel blue',show='*')
passwordEntry.grid(row = 2, column = 1, pady = 10, padx = 20)

loginButton = Button(loginFrame, text = 'Login',
                     font = ('times new roman', 20, 'bold'), width = 15, fg = 'paleGreen4',
                     bg = 'gold', activebackground='gold', activeforeground='paleGreen4', cursor='hand2', command=login)
loginButton.grid(row = 3, column = 1, pady = 10)
window.mainloop()