from Tkinter import *

root = Tk()

w = Label(root,text='Search Movie and Choose Categories')
w.pack()
movie = ['tekken', 'frozen', 'hadouken', 'tekken2']
e = Entry(root)
e.pack()
e.focus_set()
e.delete(0, END)
e.insert(0, "")

OPTIONS = ['All', 'Comedy', 'Drama', 'Action', 'Sci-fi']
    
variable = StringVar(root)
variable.set(OPTIONS[0])

w  = apply(OptionMenu,(root, variable) + tuple(OPTIONS))
w.pack(side=RIGHT)


class App:
    
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        
        
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        
        self.hi_there = Button(frame, text="SEARCH", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
    def say_hi(self):
        movie_list = {'All':['com1','com2','drama1','drama2','Act1','Act2','Sci1','Sci2']\
                      ,'Comedy':['com1','com2']\
                      ,'Drama' :['drama1','drama2']\
                      ,'Action':['Act1','Act2']\
                      ,'Sci-fi':['Sci1','Sci2']
                      }
        text = (e.get()).lower()
        check = 0
        for i in movie_list:
            if i == variable.get():
                for l in movie_list[i]:
                    if e.get() in l:
                        print l
                check = 1
        if check == 0:
            print 'NONE'
            

app = App(root)
root.mainloop()

root.destroy()


