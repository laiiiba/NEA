from tkinter import *

'''to do:
- sort out the sizing
- validate_login function
- sign_up function'''

##this function will bring the frame that I want to the top
def show_frame(frame):
    frame.tkraise()##works 

window=Tk()
window.state=("zoomed")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

##setting up the other frames
home_page=Frame(window)
sign_up=Frame(window)
join_clan=Frame(window)
create_clan=Frame(window)
create_membership=Frame(window)

for frame in (home_page,sign_up,join_clan,create_clan,create_membership):
    frame.grid(row=0,column=0,stick="nsew")

##this is the first frame that I want displayed to the user. 
show_frame(home_page)

####home_page code
def validate_login(username, password):
    pass

title=Label(home_page, text="THE PUPIL AREA").grid(columnspan=5)
#possibly edit the desciption a little bit later
description=Label(home_page, text="Welcome! This is a platform where you can connect with other students to get help with your subject questions. You can also reply to other student's questions to solidify your own learning and aid them too! There are professional tutors on hand to help (through the subsription service).")
description.grid(columnspan=5)

#login section
username_label=Label(home_page, text="Username").grid(row=3, column=2)
username=StringVar()
username_entry=Entry(home_page, textvariable=username).grid(row=3, column=3)

password_label=Label(home_page, text="Password").grid(row=4, column=2)
password=StringVar()
password_entry=Entry(home_page, textvariable=password, show="*").grid(row=4, column=3)

login_button = Button(home_page, text="Login", command=validate_login(username, password)).grid(row=5, column=3)

#buttons to send the user to a different frame 
relocate_sign_up = Button(home_page, text="Sign-up", command=lambda:show_frame(sign_up)).grid(row=2,column=1)
relocate_join_clan = Button(home_page, text="Join Clan",command=lambda:show_frame(join_clan)).grid(row=3,column=1)
relocate_create_clan = Button(home_page, text="Create Clan", command=lambda:show_frame(create_clan)).grid(row=4,column=1)
relocate_create_membership = Button(home_page, text="Create Membership", command=lambda:show_frame(create_membership)).grid(row=5,column=1)
###end of home_page code

####sign_up code
def create_login(new_username, new_password):
    pass

title=Label(sign_up, text="Create a username and password:").grid(columnspan=5)

new_username_label=Label(sign_up, text="Username").grid(row=3, column=2)
new_username=StringVar()
new_username_entry=Entry(sign_up, textvariable=username).grid(row=3, column=3)

new_password_label=Label(sign_up, text="Password").grid(row=4, column=2)
new_password=StringVar()
new_password_entry=Entry(sign_up, textvariable=password, show="*").grid(row=4, column=3)

sign_up_button = Button(sign_up, text="Sign up!", command=create_login(new_username, new_password)).grid(row=5, column=3)

####end of sign_up code

window.mainloop()

#https://codingshiksha.com/python/python-3-tkinter-user-registration-form-with-username-and-password-validation-using-regular-expression-full-project-for-beginners/ 
