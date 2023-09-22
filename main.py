import tkinter.ttk


class calculator:
    def __init__(self):
        self.root = tkinter.Tk()
        self.display_text = tkinter.StringVar()

    def add(self, value):
        self.display_text.set(self.display_text.get() + value)

    def add_to_sum(self):
        try:
            self.display_text.set(eval(self.display_text.get()))
        except:
            self.display_text.set(":ERROR:")

    def Clear_screen(self):
        self.display_text.set("")

    def SetupTkinter(self):
        self.root.title("calculator")
        self.root.geometry("300x360")

        tkinter.Entry(self.root, textvariable=self.display_text, width=50, font=('Arial 28')).place(x=0, y=30)

        tkinter.Button(self.root, text=".", height=3, width=9, command=lambda: self.add(".")).place(x=0, y=357 - 55)
        tkinter.Button(self.root, text="0", height=3, width=9, command=lambda: self.add("0")).place(x=75, y=357 - 55)
        tkinter.Button(self.root, text="/", height=3, width=9, command=lambda: self.add("/")).place(x=150, y=357 - 55)
        tkinter.Button(self.root, text="=", height=3, width=9, command=self.add_to_sum).place(x=225, y=357 - 55)

        tkinter.Button(self.root, text="1", height=3, width=9, command=lambda: self.add("1")).place(x=0, y=300 - 55)
        tkinter.Button(self.root, text="2", height=3, width=9, command=lambda: self.add("2")).place(x=75, y=300 - 55)
        tkinter.Button(self.root, text="3", height=3, width=9, command=lambda: self.add("3")).place(x=150, y=300 - 55)
        tkinter.Button(self.root, text="+", height=3, width=9, command=lambda: self.add("+")).place(x=225, y=300 - 55)

        tkinter.Button(self.root, text="4", height=3, width=9, command=lambda: self.add("4")).place(x=0, y=245 - 55)
        tkinter.Button(self.root, text="5", height=3, width=9, command=lambda: self.add("5")).place(x=75, y=245 - 55)
        tkinter.Button(self.root, text="6", height=3, width=9, command=lambda: self.add("6")).place(x=150, y=245 - 55)
        tkinter.Button(self.root, text="-", height=3, width=9, command=lambda: self.add("-")).place(x=225, y=245 - 55)

        tkinter.Button(self.root, text="7", height=3, width=9, command=lambda: self.add("7")).place(x=0, y=245 - 55 - 55)
        tkinter.Button(self.root, text="8", height=3, width=9, command=lambda: self.add("8")).place(x=75, y=245 - 55 - 55)
        tkinter.Button(self.root, text="9", height=3, width=9, command=lambda: self.add("9")).place(x=150, y=245 - 55 - 55)
        tkinter.Button(self.root, text="*", height=3, width=9, command=lambda: self.add("*")).place(x=225, y=245 - 55 - 55)

        tkinter.Button(self.root, text="Clear", height=3, width=9, command=self.Clear_screen).place(x=225, y=135 - 55)

        self.root.mainloop()


if __name__ == "__main__":
    calculator().SetupTkinter()
