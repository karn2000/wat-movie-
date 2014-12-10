from Tkinter import *

def d_movie(label2):
    movie = ment.get()
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
root.geometry('300x300')
root.resizable(0, 0)

l_option = ['All', 'Comedy', 'Drama', 'Action', 'Sci-fi']
option1 = StringVar()
option1.set(l_option[0])
ment = StringVar()

label1 = Label(root, text='Search Movie and Choose Categories').pack()
label2 = Label(root, text = 'Wat Movie??')

m_entry = Entry(root, textvariable = ment).pack()
m_search = Button(root, text = 'SEARCH', command = lambda : d_movie(label2)).pack()
m_option = apply(OptionMenu,(root, option1) + tuple(l_option)).pack()
label2.pack()


root.mainloop()


