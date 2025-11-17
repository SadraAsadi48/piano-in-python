# imports======================
import tkinter as tk
import winsound
# window=======================
root = tk.Tk()
root.geometry("400x200")
root.title("Piano")
# notes========================
notes = {
"do":261,
"re":294,
"mi":329,
"fa":349,
"sol":392,
"la":440,
"si":493,
"do2":523
}
# defs==========================
def do ():
    winsound.Beep(261,350)

def re():
    winsound.Beep(294,350)

def mi():
   winsound.Beep(329,350)

def fa():
    winsound.Beep(349,350)

def sol():
    winsound.Beep(392,350)

def la():
    winsound.Beep(440,350)

def si ():
    winsound.Beep(493,350)

def sii():
    winsound.Beep(543,350)

def siii():
    winsound.Beep(592,350)

def melody_1():
    winsound.Beep(329,350) #mi
    winsound.Beep(294,350) #re
    winsound.Beep(261,350) #do
    winsound.Beep(294,350) #re
    winsound.Beep(329,350) #mi
    winsound.Beep(329,350) #mi
    winsound.Beep(329,350) #mi
    winsound.Beep(294,350) #re
    winsound.Beep(294,350) #re
    winsound.Beep(294,350) #re
    winsound.Beep(329,350) #mi
    winsound.Beep(392,350) #sol
    winsound.Beep(392,350) #sol
    winsound.Beep(329,350) #mi
    winsound.Beep(294,350) #re
    winsound.Beep(261,350) #do
    winsound.Beep(294,350) #re
    winsound.Beep(329,350) #mi
    winsound.Beep(329,350) #mi
    winsound.Beep(329,350) #mi
    winsound.Beep(329,350) #mi
    winsound.Beep(294,350) #re
    winsound.Beep(294,350) #re
    winsound.Beep(329,350) #mi
    winsound.Beep(294,350) #re
    winsound.Beep(261,350) #do
# buttons==================================================================
btn1 = tk.Button(root,text="1",command=do)
btn1.place(x=50,y=50)
 #=========================================================================
btn2 = tk.Button(root,text="2",command=re , bg = "black",fg = "white")
btn2.place(x=70,y=35)
 #=========================================================================
btn3 = tk.Button(root,text="3",command=mi)
btn3.place(x=90,y=50)
 #=========================================================================
btn4 = tk.Button(root,text="4",command=fa, bg = "black",fg = "white")
btn4.place(x=110,y=35)
 #=========================================================================
btn5 = tk.Button(root,text="5",command=sol)
btn5.place(x=130,y=50)
 #=========================================================================
btn6 = tk.Button(root,text="6",command=la, bg = "black",fg = "white")
btn6.place(x=150,y=35)
 #=========================================================================
btn7 = tk.Button(root,text="7",command=si)
btn7.place(x=170,y=50)
 #=========================================================================
btn9 = tk.Button(root,text="8",command=sii, bg = "black",fg = "white")
btn9.place(x=190,y=35) 
 #=========================================================================
btn10 = tk.Button(root,text="9",command=siii)
btn10.place(x=210,y=50)
 #=========================================================================
btn11 = tk.Button(root,text = "melody",command=melody_1 , bg = "green")
btn11.place(y=50,x=300)
# run======================================================================
root.mainloop()
