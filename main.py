import turtle as jerry


class Flower():
    """docstring for Flower GUI object"""

    def __init__(self, num_petals, color, petal_length, petal_size, x, y):
        self.num_petals = num_petals
        self.color = color
        self.petal_length = petal_length
        self.petal_size = petal_size
        self.x = x
        self.y = y

    def get_turn_degrees(self):
        return 360 / self.num_petals

    def draw(self):
        jerry.goto(self.x,self.y)
        jerry.pendown()
        jerry.pencolor(self.color)
        jerry.pensize(self.petal_size)

        deg = self.get_turn_degrees()
        for _ in range(self.num_petals):
            jerry.forward(self.petal_length)
            jerry.backward(self.petal_length)
            jerry.right(deg)
        jerry.penup()

class Frame():
    """docstring for Frame GUI object."""

    def __init__(self, color):
        self.color = color

    def draw(self):
        jerry.goto((jerry.window_width()/2)-40,(jerry.window_height()/2)-40)
        jerry.pendown()
        jerry.pencolor(self.color)
        jerry.pensize(20)

        jerry.backward(jerry.window_width()-80)
        jerry.right(-90)
        jerry.backward(jerry.window_height()-80)
        jerry.right(-90)
        jerry.backward(jerry.window_width()-80)
        jerry.right(-90)
        jerry.backward(jerry.window_height()-80)
        jerry.penup()

flower = Flower(6,"pink", 100, 40, 0, 0)
frame = Frame("green")
flower.draw()
frame.draw()
jerry.done()
