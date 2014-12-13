from Tkinter import *
import random
import os

movie_list = ['the hobbit 3', 'interstellar', 'not found']
random = (random.choice(movie_list))
random_gif = random+'.gif'

def mnext():
    os.startfile('minigame.pyw')
    m_gui.destroy()
    
def d_random(label_2, random, label_3):
    enter = ment.get()
    answer = random
    if len(enter) < 4:
        enter += '   '
    if enter in answer:
        ans = 'Correct'
    else:
        ans = 'Wrong'
    changelabel(label_2, ans, label_3)
    
def changelabel(before, after, before2):
    ''' change label when click search '''
    before.config(text=after)
    movie = random_gif
    before2.config(text = random)
    ooo = PhotoImage(file = movie)
    label = Label(image=ooo).place(relx=.35, rely=.6)
    pic(ooo)

def mquit():
    ''' close app '''
    mexit = tkMessageBox.askyesno(title='Quit',message='Are you Sure')
    if mexit > 0:
        m_gui.destroy()

m_gui = Tk()
m_gui.title('Mini Game')
m_gui.geometry('500x600')
m_gui.resizable(0, 0)
ment = StringVar()

top = PhotoImage(file = 'top.gif')
labeltop = Label(m_gui, image=top).pack()

photo = PhotoImage(file='bg2.gif')
label_pic = Label(m_gui, image=photo).place(relx=.5, rely=.14, anchor="n")

pic = PhotoImage(file = random_gif)
label_1 = Label(m_gui, image = pic, bg = 'black', height = 80, width = 80).place(relx=.5, rely=.3, anchor="c")
label_2 = Label(m_gui, text = '???', font = 15)
label_2.place(relx=.5, rely=.45, anchor="c")
label_3 = Label(m_gui, text = '---', font = 15)
label_3.place(relx=.5, rely=.55, anchor="c")
m_entry = Entry(m_gui, textvariable = ment).place(relx=.5, rely=.4, anchor="c")
m_enter = Button(m_gui, text = 'Enter', bg='#5fbfc5',command = lambda : d_random(label_2, random, label_3))
m_enter.place(relx=.7, rely=.4, anchor= 'c')
quit_button = Button(m_gui, text = 'Close',bg = 'pink',font=15, command = mquit).place(relx=.1, rely=.9, anchor='c')
next_button = Button(m_gui, text = 'Next',bg = 'yellow',font=15, command = mnext).place(relx=.9, rely=.9, anchor='c')


m_gui.mainloop()