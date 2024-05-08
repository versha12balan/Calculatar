from tkinter import*

data = ""
def get_data(value):
    global data 
    
    data = data+str(value)
    var.set(data)

def equal_data():
    global data
    try:
        total = str(eval(data))
        var.set(total)
    except :
        var.set("error")

def clear():
    global data
    data = ""
    var.set(data)


win=Tk()#start

win.title("Calculator")
win.config(bg="black")
win.geometry("500x560")
win.resizable(False,False)

label_title=Label(win,text="Calculator",font=("Times New Roman",30,"bold"))
label_title.place(x=90,y=20,height=70,width=340)

var=StringVar()
entry =Entry(win,font=("Times New Roman",30,"bold"),bd=5,textvariable=var)
entry.place(x=20,y=110,height=60,width=460)
#---------------------------------------------

button_1 = Button(win,text="1",font=("Times New Roman",30,"bold"),command=lambda:get_data(1))
button_1.place(x=20,y=190,height=70,width=115)

button_2 = Button(win,text="2",font=("Times New Roman",30,"bold"),command=lambda:get_data(2))
button_2.place(x=135,y=190,height=70,width=115)

button_3 = Button(win,text="3",font=("Times New Roman",30,"bold"),command=lambda:get_data(3))
button_3.place(x=250,y=190,height=70,width=115)

button_add = Button(win,text="+",font=("Times New Roman",30,"bold"),command=lambda:get_data("+"))
button_add.place(x=365,y=190,height=70,width=115)
#----------------------------------------------
button_4 = Button(win,text="4",font=("Times New Roman",30,"bold"),command=lambda:get_data(4))
button_4.place(x=20,y=260,height=70,width=115)

button_5 = Button(win,text="5",font=("Times New Roman",30,"bold"),command=lambda:get_data(5))
button_5.place(x=135,y=260,height=70,width=115)

button_6 = Button(win,text="6",font=("Times New Roman",30,"bold"),command=lambda:get_data(6))
button_6.place(x=250,y=260,height=70,width=115)

button_minus = Button(win,text="-",font=("Times New Roman",30,"bold"),command=lambda:get_data("-"))
button_minus.place(x=365,y=260,height=70,width=115)
#----------------------------------------------
button_7 = Button(win,text="7",font=("Times New Roman",30,"bold"),command=lambda:get_data(7))
button_7.place(x=20,y=330,height=70,width=115)

button_8 = Button(win,text="8",font=("Times New Roman",30,"bold"),command=lambda:get_data(8))
button_8.place(x=135,y=330,height=70,width=115)

button_9 = Button(win,text="9",font=("Times New Roman",30,"bold"),command=lambda:get_data(9))
button_9.place(x=250,y=330,height=70,width=115)

button_multi = Button(win,text="*",font=("Times New Roman",30,"bold"),command=lambda:get_data("*"))
button_multi.place(x=365,y=330,height=70,width=115)
#----------------------------------------------
button_dot = Button(win,text=".",font=("Times New Roman",30,"bold"),command=lambda:get_data("."))
button_dot.place(x=20,y=400,height=70,width=115)

button_zero = Button(win,text="0",font=("Times New Roman",30,"bold"),command=lambda:get_data("0"))
button_zero.place(x=135,y=400,height=70,width=115)

button_clear = Button(win,text="C",font=("Times New Roman",30,"bold"),command=clear)
button_clear.place(x=250,y=400,height=70,width=115)

button_divide = Button(win,text="/",font=("Times New Roman",30,"bold"),command=lambda:get_data("/"))
button_divide.place(x=365,y=400,height=70,width=115)

button_equal = Button(win,text="=",font=("Times New Roman",30,"bold"),command=equal_data)
button_equal.place(x=135,y=470,height=70,width=230)







win.mainloop()#end





