import tkinter as tk
from gamelib import Sprite,GameApp

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY =33
GRAVITY = 1.0


class Banana(Sprite):

    def init_sprite(self):
        self.vx = 0
        self.vy = 0

    def set_speed(self,vx,vy):
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x +=5
        self.y -= self.vy
        self.vy -= GRAVITY



class MonkeyGame(GameApp):


    def create_sprite(self):
        self.banana = Banana(self,'banana.png',100,400)
        self.banana.set_speed(15,25)

        self.monkey = Sprite(self,'monkey.png',100,400)


        self.sprite.append(self.banana)
        self.sprite.append(self.monkey)

    def init_game(self):
        self.create_sprite()




if __name__ == '__main__':
    root = tk.Tk()
    root.title("Monkey Game")

    root.resizable(False,False)
    app = MonkeyGame(root,CANVAS_WIDTH,CANVAS_HEIGHT,UPDATE_DELAY)
    app.start()
    root.mainloop()
