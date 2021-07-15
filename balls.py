import tkinter

# Constants
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'
MAIN_BALL_RADIUS = 25
MAIN_BALL_COLOR = 'red'
INIT_DX = 1
INIT_DY = 1


class Balls:
    """Представление шарика."""

    def __init__(self, x, y, color, radius, dx=0, dy=0):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.dx = dx
        self.dy = dy

    def draw(self):
        """Прорисовка шарика"""
        canvas.create_oval(self.x - self.radius,
                           self.y - self.radius,
                           self.x + self.radius,
                           self.y + self.radius,
                           fill=self.color)

    def hide(self):
        """Удаление шарика с экрана"""
        canvas.create_oval(self.x - self.radius,
                           self.y - self.radius,
                           self.x + self.radius,
                           self.y + self.radius,
                           fill=BG_COLOR,
                           outline=BG_COLOR)

    def move(self):
        """Движение шарика"""
        # colliding with walls
        if (self.x + self.radius + self.dx) >= WIDTH or (self.x - self.radius + self.dx) <= 0:
            self.dx = -self.dx
        if (self.y + self.radius + self.dy) >= HEIGHT or (self.y - self.radius + self.dy) <= 0:
            self.dy = -self.dy
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()


# Mouseevent
def mouse_click(event):
    """doc"""
    global main_ball
    if event.num == 1:
        main_ball = Balls(event.x,
                          event.y,
                          MAIN_BALL_COLOR,
                          MAIN_BALL_RADIUS,
                          INIT_DX,
                          INIT_DY)
        main_ball.draw()
    else:
        main_ball.hide()


# main circle game
def main():
    if 'main_ball' in globals():
        main_ball.move()
    root.after(15, main)


root = tkinter.Tk()
root.title('Colliding Balls')
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
if 'main_ball' in globals():
    del main_ball
main()
root.mainloop()
