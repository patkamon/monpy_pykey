import tkinter as tk
import tkinter.ttk as ttk

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

class Sprite():

    def __init__(self,canvas,image_filename,x=0,y=0):
        self.x = x
        self.y = y
        self.image_filename = image_filename
        self.canvas = canvas

        self.init_canvas_object()

    def init_canvas_object(self):
        self.photo_image = tk.PhotoImage(file=self.image_filename)
        self.canvas_object_id = self.canvas.create_image(self.x,self.y,image = self.photo_image)


class MonkeyGame(ttk.Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self.grid(sticky='news')
        self.create_widget()

        self.create_sprite()

    def create_widget(self):
        self.canvas = tk.Canvas(self,borderwidth = 0,width = CANVAS_WIDTH,height  = CANVAS_HEIGHT,highlightthickness = 0)
        self.canvas.grid(sticky="NEWS")

    def create_sprite(self):
        self.banana = Sprite(self.canvas,'banana.png',100,100)




if __name__ == '__main__':
    root = tk.Tk()
    root.title("Monkey Game")

    root.resizable(False,False)
    app = MonkeyGame(root)
    root.mainloop()
