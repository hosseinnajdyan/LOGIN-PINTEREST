from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import font
root = Tk()
root.title('pinterest')
root.geometry('800x500')
root.resizable(False,False)
root.configure(bg='white')
#عکس پس زمینه
imgg = PhotoImage(file="161947.png")
Label(root, image=imgg,bg='white').place(x=5, y=5)
root.iconbitmap('pinterest.ico')
#فونت زیبا
txt=Label(root,text='Enter & enjoy',fg='red',font=("Script", 50, 'bold'),bg='white')
txt.place(x=20,y=370)

lblLogiein=Label(root,text='sign up',fg='red',font=("vazir", 25, 'bold'),bg='white')
lblLogiein.place(x=505,y=20)

def show():
    pas.configure(show=PassValue.get())
    show1.configure(bg='white',text='OFF',command=un_show)

def un_show():
    pas.configure(show='*')
    show1.configure(bg='white',text='ON',command=show)

def show22():
    pas2.configure(show=PassValue2.get())
    show2.configure(bg='white',text='OFF',command=un_show22)

def un_show22():
    pas2.configure(show='*')
    show2.configure(bg='white',text='ON',command=show22)


def text_1(event):
    user.delete(0, "end")
    user.config(fg="red")

def text_2(event):
    pas.delete(0, "end")
    pas.config(fg="red")

def text_3(event):
    pas2.delete(0, "end")
    pas2.config(fg="red")

def text_4(event):
    number.delete(0, "end")
    number.config(fg="red")

def on_leavee2(e):
    name = user.get().strip()
    if name == "":
        user.insert(0, "User name")

def on_leavee(e):
    name = pas.get().strip()
    if name == "":
        pas.insert(0, "Password")


def on_leavee3(e):
    name = pas2.get().strip()
    if name == "":
        pas2.insert(0, "Password again")
    
def on_leavee4(e):
    name = number.get().strip()
    if name == "":
        number.insert(0, "Phone number")

def signinn():
    global username,password
    username = user.get().strip()
    password = pas.get().strip()
    pas22 = pas2.get().strip()
    number1 = number.get().strip()
    
    if not username.isalnum():
        Label(frame, text="Enter valid username!", bg="white", fg="red", pady=15).place(x=116, y=300)
    elif pas22 != password:
        Label(frame, text="Passwords do not match!", bg="white", fg="red", pady=15).place(x=110, y=300)
    elif not number1.isdigit():
        Label(frame, text="Enter valid number!", bg="white", fg="red", pady=15).place(x=110, y=300)
    else:
        Label(frame, text="SIGN UP SUCCESSFUL!", bg="white", fg="green", pady=15).place(x=110, y=300)
        login()  # فراخوانی تابع login برای باز کردن صفحه جدید


UserValue = StringVar()
PassValue = StringVar()
PassValue2 = StringVar()
numbervalue = StringVar()

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=390, y=70)


user = Entry(frame, width=25, fg="red", textvariable=UserValue, border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=45)
user.insert(0, "User name")
user.bind("<Button>", text_1)
user.bind("<FocusOut>", on_leavee2)
Frame(frame, width=295, height=2, bg="red").place(x=25, y=70)

pas = Entry(frame, width=25, fg="red", textvariable=PassValue.get(), border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
pas.place(x=30, y=100)
pas.insert(0, "Password")
pas.bind("<FocusOut>", on_leavee)
pas.bind("<Button>", text_2)
Frame(frame, width=295, height=2, bg="red").place(x=25, y=122)

pas2 = Entry(frame, width=25, fg="red", textvariable=PassValue2.get(), border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
pas2.place(x=30, y=150)
pas2.insert(0, "Password again")
pas2.bind("<FocusOut>", on_leavee3)
pas2.bind("<Button>", text_3)
Frame(frame, width=295, height=2, bg="red").place(x=25, y=178)

number = Entry(frame, width=25, fg="red", textvariable=numbervalue, border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
number.place(x=30, y=200)
number.insert(0, "Phone number")
number.bind("<FocusOut>", on_leavee4)
number.bind("<Button>", text_4)
Frame(frame, width=295, height=2, bg="red").place(x=25, y=230)


#صفحه ورود
def login():
    root.destroy()
    window = Tk()
    window.title('pinterest')
    window.geometry('800x500')
    window.resizable(False,False)
    window.configure(bg='white')
    #عکس پس زمینه
    img = PhotoImage(file="161947.png")
    Label(window, image=img,bg='white').place(x=5, y=5)
    window.iconbitmap('pinterest.ico')
    #فونت زیبا
    txt=Label(window,text='Enter & enjoy',fg='red',font=("Script", 50, 'bold'),bg='white')
    txt.place(x=20,y=370)

    lblLogiein=Label(window,text='Log in',fg='red',font=("vazir", 25, 'bold'),bg='white')
    lblLogiein.place(x=505,y=20)
    def show4():
        pas11.configure(show=PassValue20.get())
        show111.configure(bg='white',text='OFF',command=un_show44)

    def un_show44():
        pas11.configure(show='*')
        show111.configure(bg='white',text='ON',command=show4)


    def temp_text_1(event):
        user.delete(0, "end")
        user.config(fg="red")

    def temp_text_2(event):
        pas11.delete(0, "end")
        pas11.config(fg="red")

    def on_leave2(e):
        name = user.get().strip()
        if name == "":
            user.insert(0, "User name")

    def on_leave(e):
        name = pas11.get().strip()
        if name == "":
            pas11.insert(0, "Password")
    def signin2():
        username2 = user.get()
        password2 = pas11.get()
        if username2 == username and password2 == password:
            Label(frame, text="LOGIN SUCCESSFUL!", bg="white", fg="green", pady=15).place(x=116, y=250)
            screen = Toplevel(window)
            screen.geometry('1000x600')
            screen.resizable(False,False)
            screen.title("pinterest")
            screen.configure(bg='white')
            screen.iconbitmap('pinterest.ico')
            firstlabel=Label(screen,text='✨Chose on button to see photo✨',fg='red',font=("Script", 50, 'bold'),bg='white')
            firstlabel.place(x=155,y=240)
            pic1 = Frame(screen, width=900, height=600)
            pic2 = Frame(screen, width=900, height=600)
            pic3 = Frame(screen, width=900, height=600)
            pic4 = Frame(screen, width=900, height=600)
            pic5 = Frame(screen, width=900, height=600)
            pic6 = Frame(screen, width=900, height=600)
            pic7 = Frame(screen, width=900, height=600)
            pic8 = Frame(screen, width=900, height=600)
            pic9 = Frame(screen, width=900, height=600)
            pic10 = Frame(screen, width=900, height=600)
            
            img2 = Image.open("photo1.jpg")
            global img1
            img1 = ImageTk.PhotoImage(img2)
            label1 = Label(pic1, image=img1)
            label1.pack()

            img3 = Image.open("photo2.jpg")
            global img33
            img33 = ImageTk.PhotoImage(img3)
            label2 = Label(pic2, image=img33)
            label2.pack()

            img4 = Image.open("photo3.jpg")
            global imgh
            imgh = ImageTk.PhotoImage(img4)
            label3 = Label(pic3, image=imgh)
            label3.pack()

            img5 = Image.open("photo4.jpg")
            global imgh2
            imgh2 = ImageTk.PhotoImage(img5)
            label4 = Label(pic4, image=imgh2)
            label4.pack()

            img6 = Image.open("photo5.jpg")
            global imgh3
            imgh3 = ImageTk.PhotoImage(img6)
            label5 = Label(pic5, image=imgh3)
            label5.pack()

            img7 = Image.open("photo6.jpg")
            global imgh4
            imgh4 = ImageTk.PhotoImage(img7)
            label6 = Label(pic6, image=imgh4)
            label6.pack()

            img8 = Image.open("photo7.jpg")
            global imgh5
            imgh5 = ImageTk.PhotoImage(img8)
            label7 = Label(pic7, image=imgh5)
            label7.pack()

            img9 = Image.open("photo8.jpg")
            global imgh6
            imgh6 = ImageTk.PhotoImage(img9)
            label8 = Label(pic8, image=imgh6)
            label8.pack()

            img10 = Image.open("photo9.jpg")
            global imgh7
            imgh7 = ImageTk.PhotoImage(img10)
            label9 = Label(pic9, image=imgh7)
            label9.pack()

            img11 = Image.open("photo10.jpg")
            global imgh8
            imgh8 = ImageTk.PhotoImage(img11)
            label10 = Label(pic10, image=imgh8)
            label10.pack()

            def hide_all_frames():
                pic1.pack_forget()
                pic2.pack_forget()
                pic3.pack_forget()
                pic4.pack_forget()
                pic5.pack_forget()
                pic6.pack_forget()
                pic7.pack_forget()
                pic8.pack_forget()
                pic9.pack_forget()
                pic10.pack_forget()

            def change_to_pic1():
                hide_all_frames()
                pic1.pack(fill="both", expand=1)

            def change_to_pic2():
                hide_all_frames()
                pic2.pack(fill="both", expand=1)

            def change_to_pic3():
                hide_all_frames()
                pic3.pack(fill="both", expand=1)

            def change_to_pic4():
                hide_all_frames()
                pic4.pack(fill="both", expand=1)

            def change_to_pic5():
                hide_all_frames()
                pic5.pack(fill="both", expand=1)

            def change_to_pic6():
                hide_all_frames()
                pic6.pack(fill="both", expand=1)

            def change_to_pic7():
                hide_all_frames()
                pic7.pack(fill="both", expand=1)

            def change_to_pic8():
                hide_all_frames()
                pic8.pack(fill="both", expand=1)

            def change_to_pic9():
                hide_all_frames()
                pic9.pack(fill="both", expand=1)

            def change_to_pic10():
                hide_all_frames()
                pic10.pack(fill="both", expand=1)

            btn1 = Button(screen, width=5, text="1", command=change_to_pic1)
            btn1.place(x=20, y=550)

            btn2 = Button(screen, width=5, text="2", command=change_to_pic2)
            btn2.place(x=120, y=550)

            btn3 = Button(screen, width=5, text="3", command=change_to_pic3)
            btn3.place(x=220, y=550)

            btn4 = Button(screen, width=5, text="4", command=change_to_pic4)
            btn4.place(x=320, y=550)

            btn5 = Button(screen, width=5, text="5", command=change_to_pic5)
            btn5.place(x=420, y=550)

            btn6 = Button(screen, width=5, text="6", command=change_to_pic6)
            btn6.place(x=520, y=550)

            btn7 = Button(screen, width=5, text="7", command=change_to_pic7)
            btn7.place(x=620, y=550)

            btn8 = Button(screen, width=5, text="8", command=change_to_pic8)
            btn8.place(x=720, y=550)

            btn9 = Button(screen, width=5, text="9", command=change_to_pic9)
            btn9.place(x=820, y=550)

            btn10 = Button(screen, width=5, text="10", command=change_to_pic10)
            btn10.place(x=920, y=550)
            
        else:
            Label(frame, text="Enter Details first!", bg="white", fg="red", pady=15).place(x=121, y=250)

        
    UserValue20 = StringVar()
    PassValue20 = StringVar()

    frame = Frame(window, width=350, height=350, bg="white")
    frame.place(x=390, y=70)

    user = Entry(frame, width=25, fg="red", textvariable=UserValue20, border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "User name")
    user.bind("<Button>", temp_text_1)
    user.bind("<FocusOut>", on_leave2)
    Frame(frame, width=295, height=2, bg="red").place(x=25, y=107)

    pas11 = Entry(frame, width=25, fg="red", textvariable=PassValue20.get(), border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    pas11.place(x=30, y=150)
    pas11.insert(0, "Password")
    pas11.bind("<FocusOut>", on_leave)
    pas11.bind("<Button>", temp_text_2)
    Frame(frame, width=295, height=2, bg="red").place(x=25, y=177)

    Button(frame, width=39, pady=7, text="Log in", command=signin2, bg="#57a1f8", fg="white", border=0).place(x=35, y=204)
    show111 = Button(window,text='ON',bg='white',command=show4,fg='red')
    show111.place(x=720,y=222)
    window.mainloop()



Button(frame, width=39, pady=7, text="sign up", command=signinn, bg="#57a1f8", fg="white", border=0).place(x=35, y=260)
show1 = Button(root,text='ON',bg='white',command=show,fg='red')
show1.place(x=720,y=168)

show2 = Button(root,text='ON',bg='white',command=show22,fg='red')
show2.place(x=720,y=224)


root.mainloop()
print('thanks to choose my login code')