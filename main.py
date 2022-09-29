from asyncio.windows_events import NULL
from tkinter import *
from tkinter.tix import INTEGER

window = Tk()

begin = 1
end = 1*(10**5) # (= 100 000)
number = end//2
attempts = 0   
lastBegin, lastEnd, lastNumb = begin, end, number


#Functions
def inferior():
  global lastEnd, lastNumb, attempts, end, number
  lastEnd, lastNumb = end, number
  
  attempts = attempts + 1  
  end = number - 1
  number = end - ((end-begin)//2)

  btnPrevious.config(state="normal")

  updateNumber()
  
  if number == begin:
    equal()


def superior():
  global lastBegin, lastNumb, attempts, begin, number
  lastBegin, lastNumb = begin, number
  
  attempts = attempts + 1 
  begin = number + 1
  number = end - ((end-number)//2)

  btnPrevious.config(state="normal")

  updateNumber()
  
  if number == end:
    equal()


def equal():
  numbTxt.config(bg="#7CFF00")

  btnIsEqual.config(state="disabled")
  btnInferior.config(state="disabled")
  btnIsSuperior.config(state="disabled")
  btnPrevious.config(state="disabled")

def previous():
  global begin, end, number, attempts
  number, begin, end = lastNumb, lastBegin, lastEnd
  attempts = attempts-1

  btnPrevious.config(state="disabled")

  updateNumber()

def next():
  return

def updateNumber():
  strNumber.set(str(number))
  strAttemps.set("Attempts: "+str(attempts))

def reset():
  global begin, end, number, attempts, lastBegin, lastEnd, lastNumb
  begin = 1
  end = 1*(10**5)
  number = end//2
  attempts = 0

  lastBegin, lastEnd, lastNumb = begin, end, number
   
  strNumber.set("")
  strAttemps.set("Attempts: "+str(attempts))

  numbTxt.config(bg="#FF0000")
  btnReset.config(state="disabled")
  btnIsEqual.config(state="disabled")
  btnInferior.config(state="disabled")
  btnIsSuperior.config(state="disabled")
  btnPrevious.config(state="disabled")
  btnSelect.config(state="normal")
  numbTxt.config(bg="#161715")

  numberEntry.delete(0, END)
  numberEntry.insert(0, end)


def select():
  global end, number, lastEnd, lastNumb
  end = int(numberEntry.get())
  number = end//2
  lastEnd, lastNumb = end, number

  btnSelect.config(state="disabled")
  btnReset.config(state="normal")
  btnIsEqual.config(state="normal")
  btnInferior.config(state="normal")
  btnIsSuperior.config(state="normal")
  btnPrevious.config(state="normal")
  numbTxt.config(bg="#FF0000")

  updateNumber()

#Window Settings
window.geometry("640x360")
window.resizable(False, False)
window.title("Srb Number Finder")
window.configure(bg="#161715")
window.iconbitmap("icons8-search-70.ico")
window.update_idletasks() 

width = window.winfo_width()
height = window.winfo_height()


#Widgets
numberEntry = Entry(bd=1)
numberEntry.place(x=width//2, y=height//2+60, anchor="center")
numberEntry.insert(0, end)
numberEntry.update_idletasks()

strNumber, strAttemps = StringVar(), StringVar()
numbTxt = Label( textvariable=strNumber, bg="#161715", font="lucida 20 bold" )
numbTxt.place(x=width//2, y=numberEntry.winfo_y()-80, anchor="center")
numbTxt.update_idletasks()

btnSelect = Button( text="Select", command=(select), bg="#6AD400", font="lucida 10 bold" )
btnSelect.place(x=numberEntry.winfo_x()+160, y=numberEntry.winfo_y()+10, width=50, height=25, anchor="center")
btnSelect.update_idletasks() 

strAttemps.set("Attempts: "+str(attempts))
attemptsTxt = Label( textvariable=strAttemps, font="lucida 20 bold", bg="#161715", fg="#FFFFFF" )
attemptsTxt.place(x=width/2, y=30, anchor="center")

btnIsEqual = Button( text="=", command=(equal), bg="#6AD400", font="lucida 20 bold", state="disabled" )
btnIsEqual.place(x=width//2, y=height-40, width=50, height=50, anchor="center")
btnIsEqual.update_idletasks() 

btnInferior = Button( text="-", command=(inferior), bg="#0083FF", font="lucida 20 bold", state="disabled" )
btnInferior.place(x=btnIsEqual.winfo_x()-40, y=height-40, width=50, height=50, anchor="center")
btnInferior.update_idletasks() 

btnIsSuperior = Button( text="+", command=(superior), bg="#0083FF", font="lucida 20 bold", state="disabled" )
btnIsSuperior.place(x=btnIsEqual.winfo_x()+90, y=height-40, width=50, height=50, anchor="center")
btnIsSuperior.update_idletasks() 

btnPrevious = Button( text="<", command=(previous), bg="#989A9C", font="lucida 20 bold", state="disabled" )
btnPrevious.place(x=btnInferior.winfo_x()-40, y=height-40, width=50, height=50, anchor="center")

btnNext = Button( text=">", bg="#989A9C", font="lucida 20 bold", state="disabled" )
btnNext.place(x=btnIsSuperior.winfo_x()+90, y=height-40, width=50, height=50, anchor="center")

btnReset = Button( text="RESET", command=(reset), bg="#FF8300", font="lucida 10 bold", state="disabled" )
btnReset.place(x=10, y=10, width=60, height=40)

#Loop
window.mainloop()
