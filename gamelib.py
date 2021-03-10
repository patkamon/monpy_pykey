import tkinter as tk
import tkinter.ttk as ttk

class Sprite():

    def __init__(self,Game_App,image_filename,x=0,y=0):
        self.x = x
        self.y = y
        self.image_filename = image_filename
        self.canvas = Game_App.canvas

        self.init_canvas_object()
        self.init_sprite()

    def init_sprite(self):
        pass

    def init_canvas_object(self):
        self.photo_image = tk.PhotoImage(file=self.image_filename)
        self.canvas_object_id = self.canvas.create_image(self.x,self.y,image = self.photo_image)

    def render(self):
        self.canvas.coords(self.canvas_object_id,self.x,self.y)

    def update(self):
        pass

class GameApp(ttk.Frame):

    def __init__(self,parent,canvas_width = 800,canvas_height = 500,delay = 33):
        super().__init__(parent)
        self.grid(sticky='news')
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.create_canvas()

        self.update_delay = delay


        self.sprite = []
        self.init_game()

    def create_canvas(self):
        self.canvas = tk.Canvas(self,borderwidth = 0,width = self.canvas_width,height  = self.canvas_height,highlightthickness = 0)
        self.canvas.grid(sticky="NEWS")

    def animate(self):
        for sprite in self.sprite:
            sprite.update()
            sprite.render()

        self.after(self.update_delay,self.animate)

    def start(self):
        self.after(0,self.animate)

    def init_game(self):
        pass