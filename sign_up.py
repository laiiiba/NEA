def sign_up_main(sign_up):
    sign_up.title("Sign Up")
    title=Label(sign_up, text="hello").grid(columnspan=5)

def sign_up_change():
    sign_up.destroy()

def sign_up_call():
    sign_up=Tk()
    sign_up_start(sign_up)
    sign_up.mainloop()
