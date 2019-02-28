from Tkinter import Tk, Scrollbar, Listbox, RIGHT, Y, Label, Canvas
import pyperclip
import time
from paste_manager import PasteManager



class PasteUI:
    def __init__(self):
        self.tk = Tk()
        self.pm = PasteManager()
        self.scrollbar = Scrollbar(self.tk)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas = Canvas(self.tk, yscrollcommand=self.scrollbar.set)
        self.render_rows()
        self.canvas.config(width=300,height=300)
        self.tk.mainloop()

    def render_rows(self, table='default'):
        rows = self.pm.get_value(table)
        for k, item in rows.iteritems():
            label=Label(self.canvas, text=item, height=10, width=50, wraplength=400, justify='left')
            label.bind("<Button-1>",lambda e,item=item,label=label:self.paste(item, label))
            label.bind("<Enter>", lambda e,label=label:self.on_enter(label))
            label.bind("<Leave>", lambda e,label=label:self.on_leave(label))
            label.pack()
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.pack()

    def paste(self, text, element):
        print text
        pyperclip.copy(text)
        element.config(fg="red")
        element.pack()
        self.tk.destroy()

    def on_enter(self, element):
        element.config(fg="#4f4f4f")
        element.pack()
    
    def on_leave(self, element):
        element.config(fg="black")
        element.pack()

if __name__ == '__main__':
    ui = PasteUI()