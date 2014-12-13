from Tkinter import *


def d_movie(label2):
    movie = ment.get()
    if len(movie) < 3:
        movie += '   '
    movie_list = {'All':['com1','com2','drama1','drama2','act1','act2','sci1','sci2']\
                      ,'Comedy':['com1','com2']\
                      ,'Drama' :['drama1','drama2']\
                      ,'Action':['act1','act2']\
                      ,'Sci-fi':['sci1','sci2']}
    check = 0
    movie_1 = ''
    for i in movie_list:
        if i == option1.get():
            for l in movie_list[i]:
                if movie.lower() in l:
                    movie_1 += l + '\n'
                    check += 1
                    changelabel(label2, movie_1)
                    
    if check == 0:
        text = 'Not Found'
        changelabel(label2, text)


def changelabel(before, after):
    before.config(text=after)


root = Tk()
root.title('Wat Movie ??')
root.geometry('500x500')
root.resizable(0, 0)

top = PhotoImage(file = 'top.gif')
labeltop = Label(root, image=top).pack()

photo = PhotoImage(file='bg2.gif')
label_pic = Label(root, image=photo).place(relx=.5, rely=.14, anchor="n")

l_option = ['All', 'Comedy', 'Drama', 'Action', 'Sci-fi']
option1 = StringVar()
option1.set(l_option[0])
ment = StringVar()

#label1 = Label(root, text='Search Movie and Choose Categories').place(relx=.5, rely=.1, anchor="c")
label2 = Label(root, text = 'Movie', bg = 'black', fg = 'white', font = 15)

m_entry = Entry(root, textvariable = ment).place(relx=.5, rely=.2, anchor="c")
m_search = Button(root, text = 'SEARCH', command = lambda : d_movie(label2)).place(relx=.5, rely=.3, anchor="c")
m_option = apply(OptionMenu,(root, option1) + tuple(l_option)).place(relx=.5, rely=.4, anchor="c")
label2.place(relx=.5, rely=.5, anchor="c")



root.mainloop()


