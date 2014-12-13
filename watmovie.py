''' Wat Movie ?? '''
from Tkinter import *
import os
import tkMessageBox

def d_movie(label2):
    ''' find movie '''
    movie = ment.get()
    if len(movie) < 3:
        movie += '   '
    movie_list = {'All':['interstellar','com1','com2','drama1','drama2','act1','act2','sci1','sci2']\
                      ,'Comedy':['com1','com2']\
                      ,'Drama' :['drama1','drama2']\
                      ,'Action':['act1','act2']\
                      ,'Sci-fi':['sci1','sci2', 'interstellar']}
    check = 0
    movie_1 = ''
    for i in movie_list:
        if i == option1.get():
            for l in movie_list[i]:
                if movie.lower() in l:
                    movie_1 += l
                    check += 1
                    changelabel(label2, movie_1)
                    
    if check == 0:
        text = 'Not Found'
        changelabel(label2, text)


def changelabel(before, after):
    ''' change label when click search '''
    before.config(text=after)
    movie = str(after + '.gif')
    print movie
    img = PhotoImage(file=movie)
    label = Label(root, image=img).pack()


def about_us():
    ''' open file => about_us.txt '''
    os.startfile('about_us.txt')

def wmhelp():
    ''' open file => help.txt. '''
    os.startfile('help.txt')

def mquit():
    ''' close app '''
    mexit = tkMessageBox.askyesno(title='Quit',message='Are you Sure')
    if mexit > 0:
        root.destroy()

root = Tk()
root.title('Wat Movie ??')
root.geometry('500x500')
root.resizable(0, 0)

# logo
top = PhotoImage(file = 'top.gif')
labeltop = Label(root, image=top).pack()

# background
photo = PhotoImage(file='bg2.gif')
label_pic = Label(root, image=photo).place(relx=.5, rely=.14, anchor="n")

# category
l_option = ['All', 'Comedy', 'Drama', 'Action', 'Sci-fi']
option1 = StringVar()
option1.set(l_option[0])
ment = StringVar()

label2 = Label(root, text = '---', bg = 'black', fg = 'white', font = 15)
label2.place(relx=.5, rely=.55, anchor = 'c')

label_category = Label(root, bg='#5fbfc5', text = 'Category   : ').place(relx=.44, rely=.3, anchor= 'c')

m_entry = Entry(root, textvariable = ment).place(relx=.5, rely=.2, anchor = 'c')
m_option = apply(OptionMenu,(root, option1) + tuple(l_option)).place(relx=.57, rely=.3, anchor= 'c')
m_search = Button(root, text = 'SEARCH', bg='#5fbfc5',command = lambda : d_movie(label2)).place(relx=.5, rely=.4, anchor= 'c')


# menubar
menubar = Menu(root)
# help menu
helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label='View Help', command=wmhelp)
helpmenu.add_command(label='About Us',command=about_us)
menubar.add_cascade(label='Help',menu=helpmenu)

quit_button = Button(root, text = 'Close',bg = 'pink',font=15, command = mquit).place(relx=.1, rely=.9, anchor='c')

root.config(menu=menubar)
root.mainloop()


