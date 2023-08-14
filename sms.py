from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas


# functional Part

def exit_data():
   result=messagebox.askyesno('Confirm','Do you want to exit?')
   if result:
      root.destroy()
   else:
      pass
      

def export_data():
   url=filedialog.asksaveasfilename(defaultextension='.csv')
   indexing=studentTable.get_children()
   newlist=[]
   for index in indexing:
      content=studentTable.item(index)
      datalist=content['values']
      newlist.append(datalist)

   
   table = pandas.DataFrame(newlist,columns=['Id','Name','Phone','Email','Adress','Gender','Birth Date','Added Date','Added Time'])
   table.to_csv(url,index=False)
   messagebox.showinfo('Success','Database Table is save successfully!')

def update_student():
   def update_data():
      currentdate = time.strftime('%d/%m/%Y')
      currenttime = time.strftime('%H:%M:%S')
      query='update student set name=%s, phone=%s, email=%s, address=%s, gender=%s, birth=%s,date=%s,time=%s where id=%s'
      mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                              genderEntry.get(),bdEntry.get(),currentdate,currenttime,idEntry.get()))
      con.commit()
      messagebox.showinfo('Success',f'Student with Id: {idEntry.get()} is updated successfully!',parent=update_window)
      update_window.destroy()
      show_student()
 
   update_window=Toplevel()
   update_window.title('Update Student')
   update_window.grab_set()
   update_window.resizable(False,False)

   idLabel = Label(update_window, text='Id', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
   idEntry = Entry(update_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   idEntry.grid(row=0,column=1,padx=10,pady=15)

   nameLabel = Label(update_window, text='Name', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
   nameEntry = Entry(update_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   nameEntry.grid(row=1,column=1,padx=10,pady=15)

   phoneLabel = Label(update_window, text='Phone', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
   phoneEntry = Entry(update_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   phoneEntry.grid(row=2,column=1,padx=10,pady=15)

   emailLabel = Label(update_window, text='Email', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
   emailEntry = Entry(update_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   emailEntry.grid(row=3,column=1,padx=10,pady=15)

   addressLabel = Label(update_window, text='Address', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
   addressEntry = Entry(update_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   addressEntry.grid(row=4,column=1,padx=10,pady=15)

   genderLabel = Label(update_window, text='Gender', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
   genderEntry = Entry(update_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   genderEntry.grid(row=5,column=1,padx=10,pady=15)

   bdLabel = Label(update_window, text='Birth Date', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   bdLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
   bdEntry = Entry(update_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   bdEntry.grid(row=6,column=1,padx=10,pady=15)

   update_student_button = ttk.Button(update_window,text='Update Student', command=update_data)
   update_student_button.grid(row=7,columnspan=2,pady=15)

   indexing = studentTable.focus()
   content=studentTable.item(indexing)
   list_data=content['values']
   idEntry.insert(0,list_data[0])
   nameEntry.insert(0,list_data[1])
   phoneEntry.insert(0,list_data[2])
   emailEntry.insert(0,list_data[3])
   addressEntry.insert(0,list_data[4])
   genderEntry.insert(0,list_data[5])
   bdEntry.insert(0,list_data[6])
   
  
def show_student():
    query = 'select *from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
       studentTable.insert('',END,values=data)

def delete_student():
   indexing = studentTable.focus()
   content=studentTable.item(indexing)
   content_id=content['values'][0]
   query = 'delete from student where id=%s'
   mycursor.execute(query,content_id)
   con.commit()
   messagebox.showinfo('Deleted',f'Id: ({content_id}) is deleted successfully!')
   query='select *from student'
   mycursor.execute(query)
   studentTable.delete(*studentTable.get_children())
   fetched_data=mycursor.fetchall()
   for data in fetched_data:
      studentTable.insert('',END,values=data)
      

def add_student():
   def add_data():
      if idEntry.get()==''or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or bdEntry.get()=='':
         messagebox.showerror('Error','All fileds are required',parent = add_window)
      else:
         currentdate = time.strftime('%d/%m/%Y')
         currenttime = time.strftime('%H:%M:%S')
         try:
          query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),
                           addressEntry.get(),genderEntry.get(),bdEntry.get(),currentdate,currenttime))

          con.commit()
          result = messagebox.askyesno('Confirm','Data added successfully, Do you want to clear the form?', parent = add_window)
          if result:
             idEntry.delete(0,END)
             nameEntry.delete(0,END)
             phoneEntry.delete(0,END)
             emailEntry.delete(0,END)
             addressEntry.delete(0,END)
             genderEntry.delete(0,END)
             bdEntry.delete(0,END)
          else:
             pass
         except:
            messagebox.showerror('Error','Id can`t be repeted',parent = add_window)
            return
   
         
         query = 'select *from student'
         mycursor.execute(query)
         fetched_data=mycursor.fetchall()
         studentTable.delete(*studentTable.get_children())
         for data in fetched_data:
            studentTable.insert('',END,values=data)

   add_window=Toplevel()
   add_window.title('Add Student')
   add_window.grab_set()
   add_window.resizable(False,False)

   idLabel = Label(add_window, text='Id', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
   idEntry = Entry(add_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   idEntry.grid(row=0,column=1,padx=10,pady=15)

   nameLabel = Label(add_window, text='Name', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
   nameEntry = Entry(add_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   nameEntry.grid(row=1,column=1,padx=10,pady=15)

   phoneLabel = Label(add_window, text='Phone', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
   phoneEntry = Entry(add_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   phoneEntry.grid(row=2,column=1,padx=10,pady=15)

   emailLabel = Label(add_window, text='Email', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
   emailEntry = Entry(add_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   emailEntry.grid(row=3,column=1,padx=10,pady=15)

   addressLabel = Label(add_window, text='Address', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
   addressEntry = Entry(add_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   addressEntry.grid(row=4,column=1,padx=10,pady=15)

   genderLabel = Label(add_window, text='Gender', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
   genderEntry = Entry(add_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   genderEntry.grid(row=5,column=1,padx=10,pady=15)

   bdLabel = Label(add_window, text='Birth Date', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   bdLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
   bdEntry = Entry(add_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   bdEntry.grid(row=6,column=1,padx=10,pady=15)

   add_student_button = ttk.Button(add_window,text='Add Student',command=add_data)
   add_student_button.grid(row=7,columnspan=2,pady=15)

def search_student():
   def search_data():
      query = 'select * from student where id=%s or name=%s or phone=%s or email=%s or address=%s or gender=%s or birth=%s'
      mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),bdEntry.get()))
      studentTable.delete(*studentTable.get_children())
      fetched_data=mycursor.fetchall()
      for data in fetched_data:
         studentTable.insert('',END,values=data)
         search_window.destroy()
          
   
   search_window=Toplevel()
   search_window.title('Search Student')
   search_window.grab_set()
   search_window.resizable(False,False)
   idLabel = Label(search_window, text='Id', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
   idEntry = Entry(search_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   idEntry.grid(row=0,column=1,padx=10,pady=15)

   nameLabel = Label(search_window, text='Name', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
   nameEntry = Entry(search_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   nameEntry.grid(row=1,column=1,padx=10,pady=15)

   phoneLabel = Label(search_window, text='Phone', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
   phoneEntry = Entry(search_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   phoneEntry.grid(row=2,column=1,padx=10,pady=15)

   emailLabel = Label(search_window, text='Email', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
   emailEntry = Entry(search_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   emailEntry.grid(row=3,column=1,padx=10,pady=15)

   addressLabel = Label(search_window, text='Address', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
   addressEntry = Entry(search_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   addressEntry.grid(row=4,column=1,padx=10,pady=15)

   genderLabel = Label(search_window, text='Gender', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
   genderEntry = Entry(search_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   genderEntry.grid(row=5,column=1,padx=10,pady=15)

   bdLabel = Label(search_window, text='Birth Date', font=('times new roman',20,'bold'),bg='paleTurquoise', fg='steel blue')
   bdLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
   bdEntry = Entry(search_window,font=('roman',15,'bold'),width=24,fg='steel blue')
   bdEntry.grid(row=6,column=1,padx=10,pady=15)

   search_student_button = ttk.Button(search_window,text='Search Student',command=search_data)
   search_student_button.grid(row=7,columnspan=2,pady=15)
   

def connect_database():
    def connect():
        global mycursor, con
        try:
         con=pymysql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())
         mycursor=con.cursor()
         
        except:
            messagebox.showerror('Error','Invalid Details', parent=connectWindow )
            return

        try:
         query = 'create database studentmangementsystem'
         mycursor.execute(query)
         query='use studentmangementsystem'
         mycursor.execute(query)
         query='create table student(id int not null primary key, name varchar(50), phone varchar(20),email varchar(30),' \
               'address varchar(100),gender varchar(20),birth varchar(20),date varchar(50), time varchar(50))'
         mycursor.execute(query)
        except:
           query='use studentmangementsystem'
           mycursor.execute(query)
        messagebox.showinfo('Success','DB connection successfully', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(False,False)

    hostnamelabel =Label(connectWindow, text='Host Name',font=('arial',20,'bold'),bg='paleTurquoise', fg='steel blue')
    hostnamelabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('arial',15,'bold'),bd=2, fg='steel blue')
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernamelabel =Label(connectWindow, text='User Name',font=('arial',20,'bold'),bg='paleTurquoise', fg='steel blue')
    usernamelabel.grid(row=1,column=0,padx=20)

    userEntry=Entry(connectWindow,font=('arial',15,'bold'),bd=2, fg='steel blue')
    userEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordlabel =Label(connectWindow, text='Password',font=('arial',20,'bold'),bg='paleTurquoise', fg='steel blue')
    passwordlabel.grid(row=2,column=0,padx=20)

    passwordEntry=Entry(connectWindow,font=('arial',15,'bold'),bd=2, fg='steel blue',show='*')
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton=ttk.Button(connectWindow,text='Connect', command=connect)
    connectButton.grid(row=3, columnspan=2)




count = 0
text =''

def clock():
    date = time.strftime('%d/%m/%Y')
    timee = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {timee}')
    # loop for seconds
    datetimeLabel.after(1000,clock)

# GUI Part
root = ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('breeze')

root.geometry('1174x680+0+0')
root.resizable(False,False)
root.title('Student mangement system')


datetimeLabel = Label(root, font=('times new roman', 18, 'bold'), fg='steel blue')
datetimeLabel.place(x=5,y=5)
clock()


sLabel = Label(root, font=('arial',28, 'italic bold'),width=30, text='Student mangement system', fg='steel blue')
sLabel.place(x=320,y=10)



connectButton = ttk.Button(root, text='Connect to DB', command=connect_database)
connectButton.place(x=980, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)


logo_image = PhotoImage(file='proto.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0,column=0)


addstudentButton = ttk.Button(leftFrame, text='Add Student',width=25,state=DISABLED, command=add_student)
addstudentButton.grid(row=1,column=0, pady=20)

searchstudentButton = ttk.Button(leftFrame, text='Search Student',width=25, state=DISABLED, command=search_student)
searchstudentButton.grid(row=2,column=0, pady=20)

deletstudentButton = ttk.Button(leftFrame, text='Delete Student',width=25, state=DISABLED, command= delete_student)
deletstudentButton.grid(row=3,column=0, pady=20)

updatestudentButton = ttk.Button(leftFrame, text='Update Student',width=25, state=DISABLED, command=update_student)
updatestudentButton.grid(row=4,column=0, pady=20)

showstudentButton = ttk.Button(leftFrame, text='Show Students',width=25, state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0, pady=20)

exportstudentButton = ttk.Button(leftFrame, text='Export Data',width=25, state=DISABLED, command=export_data)
exportstudentButton.grid(row=6,column=0, pady=20)

exitButton =ttk.Button(leftFrame, text='Exit',width=25,command = exit_data)
exitButton.grid(row=7,column=0, pady=20)


rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)


scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Phone','Email','Address','Gender',
                                'Birth Date','Added Date','Added Time' ),
                                xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Phone',text='Phone')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('Birth Date',text='Birth Date')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=90,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Phone',width=200,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=200,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('Birth Date',width=200,anchor=CENTER)
studentTable.column('Added Date',width=200,anchor=CENTER)
studentTable.column('Added Time',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=40, font=('arial',10,'bold'),foreground='steel blue')
style.configure('Treeview.heading',font=('arial',20,'bold'),foreground='steel blue')
studentTable.config(show='headings')

root.mainloop()