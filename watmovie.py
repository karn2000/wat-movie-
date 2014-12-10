from Tkinter import *

def d_movie():
    movie = ment.get()
    movie_list = {'All':['com1','com2','drama1','drama2','Act1','Act2','Sci1','Sci2']\
                      ,'Comedy':['com1','com2']\
                      ,'Drama' :['drama1','drama2']\
                      ,'Action':['Act1','Act2']\
                      ,'Sci-fi':['Sci1','Sci2']}
    check = 0
    for i in movie_list:
        if i == option1.get():
            for l in movie_list[i]:
                if movie in l:
                    mlabel = Label(root, text=l).pack()
                    check += 1
    if check == 0:
        mlabel = Label(root, text = 'Not Found').pack()
    

root = Tk()
root.title('Wat Movie ??')
root.geometry('300x300')

l_option = ['All', 'Comedy', 'Action', 'Sci-fi']
option1 = StringVar()
option1.set(l_option[0])
ment = StringVar()

label1 = Label(root,text='Search Movie and Choose Categories')
label1.pack()


m_entry = Entry(root, textvariable = ment).pack()
m_search = Button(root, text = 'SEARCH', command = d_movie).pack()
m_option = apply(OptionMenu,(root, option1) + tuple(l_option)).pack()

root.mainloop()


