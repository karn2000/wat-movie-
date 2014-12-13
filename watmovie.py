''' Wat Movie ?? '''
import sys
from Tkinter import *
import os
import tkMessageBox

def d_movie(label2, ment, option1):
    ''' find movie '''
    movie = ment.get()
    if len(movie) < 3 or movie == 'the':
        movie += '   '
    movie_list = {'All':['Night at The Museum Secret of The Tomb','Gone girl','Step Up 5','Begin Again','Brick Mansions','Transcendence','Oculus','Mr. Peabody and Sherman','Robocop','300 Rise of an Empire','Godzilla','The Amazing Spider-Man 2','Sex Tape','Captain America The Winter Soldier','Neighbors','Whiplash','How to Train Your Dragon 2','Transformers Age of Extinction','Edge of Tomorrow','The Fault in Our Stars','Dracula Untold','The Lego Movie','John Wick','Hercules','22 Jump Street','X-Men: Days of Future Past','Maleficent','Boyhood','Lucy','The Babadook','Divergent','Dawn of the Planet of the Apes','The Expendables 3','Annie','Teenage Mutant Ninja Turtles','Into the Woods','Dumb and Dumber To','Big Hero 6','Nightcrawler','Penguins of Madagascar,''Guardians of the Galaxy','Fury','The Hunger Games Mockingjay - Part 1','Interstellar','The Maze Runner','Exodus Gods and Kings','Horrible Bosses 2']\
                      ,'Comedy':['Step Up 5','Mr. Peabody and Sherman','Sex Tape','Neighbors','How to Train Your Dragon 2','The Lego Movie','22 Jump Street','Boyhood','Annie','Teenage Mutant Ninja Turtles','Into the Woods','Dumb and Dumber To','Horrible Bosses 2','Penguins of Madagascar','Big Hero 6','Night at The Museum Secret of The Tomb']\
                      ,'Drama' :['Transcendence','Oculus','300: Rise of an Empire','Whiplash','The Fault in Our Stars','Dracula Untold','The Babadook','Dawn of the Planet of the Apes','Annie','Gone Girl','Exodus: Gods and Kings','Fury','Nightcrawler','Begin Again']\
                      ,'Sci-fi':['Transcendence','Robocop','Godzilla','Captain America The Winter Soldier','Transformers Age of Extinction','Edge of Tomorrow','X-Men: Days of Future Past','Lucy','Divergent','Teenage Mutant Ninja Turtles','Guardians of the Galaxy ','The Hunger Games Mockingjay - Part 1', 'Interstellar','Big Hero 6']\
                      ,'Action':['Night at The Museum Secret of The Tomb','Brick Mansions','Transcendence','300 Rise of an Empire','Godzilla','The Amazing Spider-Man 2','Captain America The Winter Soldier','How to Train Your Dragon 2','Transformers: Age of Extinction','Edge of Tomorrow','The Lego Movie','John Wick','Hercules','22 Jump Street','X-Men: Days of Future Past','Maleficent','Lucy','Divergent','Dawn of the Planet of the Apes','The Expendables 3','Teenage Mutant Ninja Turtles','Big Hero 6','Guardians of the Galaxy','The Maze Runner','Exodus Gods and Kings','Fury']}
    check = 0
    movie_1 = ''
    for i in movie_list:
        if i == option1.get():
            for l in movie_list[i]:
                if movie.lower() in l:
                    check += 1
                    if check > 1:
                        movie_1 += '\n'
                    movie_1 += l
            if check >= 1:
                changelabel(label2, movie_1)
                    
    if check == 0:
        text = 'Not Found'
        changelabel(label2, text)


def changelabel(before, after):
    ''' change label when click search '''
    before.config(text=after.capitalize())
    movie = after.lower()+'.gif'
    ooo = PhotoImage(file = movie)
    label = Label(image=ooo).place(relx=.69, rely=.57)
    pic(ooo)
    pic2(ooo)

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

def openmini():
    os.startfile('minigame.pyw')

class main(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Wat Movie ??')
        self.root.geometry('500x500')
        self.root.resizable(0, 0)

        # logo
        top = PhotoImage(file = 'top.gif')
        labeltop = Label(self.root, image=top).pack()

        # background
        photo = PhotoImage(file='bg2.gif')
        label_pic = Label(self.root, image=photo).place(relx=.5, rely=.14, anchor="n")

        # category
        l_option = ['All', 'Action', 'Comedy', 'Drama', 'Sci-fi']
        option1 = StringVar()
        option1.set(l_option[0])
        ment = StringVar()

        label2 = Label(self.root, text = '---', bg = 'black', fg = 'white', font = 15)
        label2.place(relx=.5, rely=.55, anchor = 'c')

        label_category = Label(self.root, bg='#5fbfc5', text = 'Category   : ').place(relx=.4, rely=.3, anchor= 'c')

        m_entry = Entry(self.root, textvariable = ment).place(relx=.5, rely=.2, anchor = 'c')
        m_option = apply(OptionMenu,(self.root, option1) + tuple(l_option)).place(relx=.57, rely=.3, anchor= 'c')
        m_search = Button(self.root, text = 'SEARCH', bg='#5fbfc5',command = lambda : d_movie(label2, ment, option1)).place(relx=.5, rely=.4, anchor= 'c')

        m_minigame = Button(self.root, text = 'Mini Game', command = openmini, bg = 'yellow').place(relx=.1, rely=.4, anchor='c')

        # menubar
        menubar = Menu(self.root)
        # help menu
        helpmenu = Menu(menubar,tearoff=0)
        helpmenu.add_command(label='View Help', command=wmhelp)
        helpmenu.add_command(label='About Us',command=about_us)
        menubar.add_cascade(label='Help',menu=helpmenu)

        quit_button = Button(self.root, text = 'Close',bg = 'pink',font=15, command = mquit)
        quit_button.place(relx=.1, rely=.9, anchor='c')

        self.root.config(menu=menubar)
        self.root.mainloop()


main()
