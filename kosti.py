from tkinter import *

import random
import time
def bros():
    x = random.choice(['b1.png', 'b2.png', 'b3.png',
                       'b4.png', 'b5.png', 'b6.png'])
    return x

def img(event):
    global b1, b2
    for i in range(15):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.08)

root = Tk()
root.geometry('600x300')
root.title('Игра в кости!!!')
root.resizable(height = False, width = False)
root.iconphoto(True, PhotoImage(file=('iconka.png')))
font = PhotoImage(file=('holst.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely = 0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely = 0.5, anchor=CENTER)
root.bind('<Return>', img)
root.bind('<1>', img)
root.bind('<space>', img)
root.bind('<Escape>', lambda img: root.destroy())
root.mainloop()

