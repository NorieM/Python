from tkinter import Button, Frame, Tk  # Python 3
#from Tkinter import Button, Frame, Tk    # Python 2

class MyClass:
    def __init__(self, master):
       frame = Frame(master)
       frame.pack()

       for num in range(1, 11): 
            self.button = Button(frame, text=str(num), command=self.func)
            self.button.pack(side='left')
            master.bind(num, self.func)

    def func(self, event=None):
        if event:
            print(event.char)

root = Tk()
abc = MyClass(root)
root.mainloop()