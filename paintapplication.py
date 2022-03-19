from tkinter import *
from tkinter.colorchooser import askcolor
import os
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog as fd


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'orange'

    def __init__(self):
        self.root = Tk()
        self.root.title("Paint App {}".format(os.getcwd()))

        self.pen_button = Button(self.root, text='Pen', command=self.use_pen,fg="red",borderwidth=2,width=5)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='Brush', command=self.use_brush,fg="red",borderwidth=2,width=5)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='Color', command=self.choose_color,fg="red",borderwidth=2,width=5)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser,fg="red",borderwidth=2,width=5)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=30, orient=HORIZONTAL,fg="red",borderwidth=2)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=500, height=500)
        self.c.grid(row=1, columnspan=5)

        '''self.menuBar=Menu(self.root)
        self.fileMenu=Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label='Open',command=self.open)
        self.fileMenu.add_command(label='Save as',command=self.save_as)
        self.menuBar.add_cascade(label="File",menu=self.fileMenu)
        self.root.configure(menu=self.menuBar)'''

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    '''def save_as(self):
         f = asksaveasfile(initialfile = 'Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

    def open(self):
        pass
        filename = fd.askopenfilename()'''


if __name__ == '__main__':
    Paint()
