from tkinter import *    

def validation():
    try:    
        zx = len(txtbox11.get())  
        if zx == 0:
            answer.config(text='It cannot be blank')
            return  
        else:
            zz = float(txtbox11.get())  
    except ValueError:  
        zz = None  
        answer.config(text='You must type a number')
   
    if zz is None:  
        return
    elif zz == 0 or zz < 0:
        answer.config(text='The number cannot be zero or negative')
    else:
        ce = zz - 273.15
        fa = (9/5)*(zz-273)+32
        print("Converted temperature:", ce)
        print("converted temperature:",fa)
        txtbox2.delete(0,END)
        txtbox2.insert(END,f"{ce:.2f}")
        txtbox3.delete(0,END)
        txtbox3.insert(END,f"{fa:.2f}")
        answer.config(text="conversion complete")
       
def clear():
    txtbox11.delete(0,END)
    txtbox2.delete(0,END)
    txtbox3.delete(0,END)
    answer.config(text="")
   
def main():
    print('--> start <--')
winmain = Tk()
winmain.geometry('345x300')
lbltext = Label( winmain,text="Temperature Conversion",
font=("Arial Bold", 21))
 
lbltext.place(x=3,y=3)
winmain.configure(bg='light blue')
winmain.title('P18')

txtboxlbl=Label(font=('Arial Bold',10),text='Temp in Kelvin:',
                    fg='yellow',bg='dark blue')
txtboxlbl.place(x=15,y=70)
txtbox11=Entry(width=15,font=('Arial Bold',10))
txtbox11.place(x=225,y=70)

txtboxlbl2=Label(font=('Arial Bold',10),text='Temp in Celsius:',
                    fg='yellow',bg='green')
txtboxlbl2.place(x=15,y=100)
txtbox2=Entry(width=15,font=('Arial Bold',10))
txtbox2.place(x=225,y=100)

txtboxlbl3=Label(font=('Arial Bold',10),text='Temp in Fahrenheit:',
                    fg='yellow',bg='red')
txtboxlbl3.place(x=15,y=130)
txtbox3=Entry(width=15,font=('Arial Bold',10))
txtbox3.place(x=225,y=130)

answer=Label(width=40,font=('Arial Bold',10))
answer.place(x=10,y=160)

btnclear = Button(font=("Arial Bold", 10),text="Clear",
    command=clear)
btnclear.place(x=200,y=200)

btncalc = Button(font=("Arial Bold", 10),text="Calc",
    command=validation)
btncalc.place(x=100,y=200)

btnquit = Button(font=("Arial Bold", 10),
    text="QUIT", fg="red",command=quit)
btnquit.place(x=150,y=250)

winmain.mainloop()
main()
