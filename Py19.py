from tkinter import *
def main():
    
    mainwin = Tk()
    color='dark gray'
    wcan = Canvas(mainwin,bg=color, width=600,height=800)

    wcan.pack()
    wcan.create_oval(391, 391, 165, 165, fill='yellow',outline="orange", width=5)
    
    wcan.create_oval(250, 250, 200, 200, fill='light blue',outline="black", width=5)
    wcan.create_oval(310, 250, 360, 200, fill='light pink',outline="black", width=5)
    
    wcan.create_line(280, 280, 280, 300, width=10, fill="orange")
    
    wcan.create_line(200, 325, 350, 325, width=5, fill="red")
    wcan.create_line(350, 325, 275, 375, width=5, fill="blue")
    wcan.create_line(200, 325, 275, 375, width=5, fill="green")

    mainwin.mainloop()
main()
