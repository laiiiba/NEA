from tkinter import *

def home_page_main(home_page):
    home_page.title("Home Page")
    title=Label(home_page, text="THE PUPIL AREA").grid(columnspan=5)
##possibly edit the desciption a little bit later
    description=Label(home_page, text="Welcome! This is a platform where you can connect with other students to get help with your subject questions. You can also reply to other student's questions to solidify your own learning and aid them too! There are professional tutors on hand to help (through the subsription service).")
    description.grid(columnspan=5)

####login section
    username_label=Label(home_page, text="Username").grid(row=3, column=2)
    username=StringVar()
    username_entry=Entry(home_page, textvariable=username).grid(row=3, column=3)

    password_label=Label(home_page, text="Password").grid(row=4, column=2)
    password=StringVar()
    password_entry=Entry(home_page, textvariable=password, show="*").grid(row=4, column=3)

    login_button = Button(home_page, text="Login"', command=validateLogin(username, password)').grid(row=5, column=3)

####other home page fucntionality
    sign_up = Button(home_page, text="Sign-up", command=lambda:home_page_change(home_page)).grid(row=2,column=1)
    join_clan = Button(home_page, text="Join Clan", command=lambda:home_page_change(home_page)).grid(row=3,column=1)
    create_clan = Button(home_page, text="Create Clan", command=lambda:home_page_change(home_page)).grid(row=4,column=1)
    create_membership = Button(home_page, text="Create Membership", command=lambda:change(home_page)).grid(row=5,column=1)
    
def home_page_change(home_page):
    home_page.destroy()
    ##add an if statement to identify which function to call. 
    sign_up_call()
    
def home_page_call():
    home_page=Tk()#'initialising' window
    home_page_main(home_page)
    home_page.mainloop() #this keeps the window open until the x is pressed

home_page_call()


##def validateLogin(username, password):#######need to add my validations 
