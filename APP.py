from Tkinter import *
root=Tk()
root.title("The Bawse")
root.resizable(0,0)
e=Entry(root,width=16, font="Arial 30 bold", bd=7,bg='light grey',justify='right')
e.grid(row=0,column=0, columnspan=4)
def insert(n):
    e.insert(16,n)
def clear():
    e.delete(0,END)
def result():
    r=eval(e.get())
    clear()
    e.insert(16,r)
Button(root, text='7',font='10', width=5,height=5, command=lambda:insert(7)).grid(row=1,column=0, sticky=N+S+W+E)
Button(root, text='8',font='10', width=5,height=5,command=lambda:insert(8)).grid(row=1,column=1,sticky=N+S+W+E)
Button(root, text='9', font='10',width=5,height=5,command=lambda:insert(9)).grid(row=1,column=2,sticky=N+S+W+E)
Button(root, text='+', font='10',width=5,height=5,command=lambda:insert('+')).grid(row=1,column=3, sticky=N+S+W+E)
Button(root, text='4', font='10',width=5,height=5,command=lambda:insert(4)).grid(row=2,column=0, sticky=N+S+W+E)
Button(root, text='5', font='10',width=5,height=5,command=lambda:insert(5)).grid(row=2,column=1,sticky=N+S+W+E)
Button(root, text='6', font='10',width=5,height=5,command=lambda:insert(6)).grid(row=2,column=2,sticky=N+S+W+E)
Button(root, text='-', font='10',width=5,height=5,command=lambda:insert('-')).grid(row=2,column=3, sticky=N+S+W+E)
Button(root, text='1', font='10',width=5,height=5,command=lambda:insert(1)).grid(row=3,column=0, sticky=N+S+W+E)
Button(root, text='2', font='10',width=5,height=5,command=lambda:insert(2)).grid(row=3,column=1,sticky=N+S+W+E)
Button(root, text='3', font='10',width=5,height=5,command=lambda:insert(3)).grid(row=3,column=2,sticky=N+S+W+E)
Button(root, text='x', font='10',width=5,height=5,command=lambda:insert('x')).grid(row=3,column=3,sticky=N+S+W+E)
Button(root, text='=', font='10',width=5,height=5, command=result).grid(row=4,column=0, sticky=N+S+W+E)
Button(root, text='C', font='10',width=5,height=5,fg='red', command=clear).grid(row=4,column=1,sticky=N+S+W+E)
Button(root, text='0', font='10',width=5,height=5,command=lambda:insert(0)).grid(row=4,column=2,sticky=N+S+W+E)
Button(root, text='/', font='10',width=5,height=5,command=lambda:insert('/')).grid(row=4,column=3, sticky=N+S+W+E)
root.mainloop()
