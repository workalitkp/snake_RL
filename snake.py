import consts
from game_manager import GameManager

class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.alive = True
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def get_tail(self):
        return self.cells[0]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        from time import sleep
        # sleep(2)
        head = self.get_head()
        tail = self.get_tail()
        
        # new_head = (head[0] + Snake.dx[self.direction],head[1]+Snake.dy[self.direction])

        if(head[0] >= consts.table_size - 1 and self.direction == "RIGHT"):
            new_head = (0,head[1])
        elif(head[0] <= 0 and self.direction == "LEFT"):
            new_head = (consts.table_size - 1,head[1])
        elif(head[1] >= consts.table_size - 1 and self.direction ==  "DOWN"):
            new_head = (head[0],0)
            
        elif(head[1] <= 0 and self.direction == "UP"):
            new_head = (head[0],consts.table_size - 1)
        else:
            new_head = (head[0] + Snake.dx[self.direction],head[1]+Snake.dy[self.direction])
        # print(list(self.game.snakes))
        for snake in self.game.snakes:
            if(new_head in snake.cells):
                self.game.kill(self)
                self.alive = False
        if(list(new_head) in consts.block_cells):
            self.game.kill(self)
            self.alive = False
        if(self.alive):
            if(new_head not in self.game.fruits):
                self.cells.pop(0)
            self.cells.append(new_head)
            self.game.get_cell(new_head).set_color(self.color)
            self.game.get_cell(tail).set_color(consts.back_color)
    def handle(self, keys):
        key_pairs = [('UP','DOWN'),('LEFT','RIGHT')]
        for key in keys:
            if(key in self.keys):
                if(self.keys[key] in key_pairs[0] and self.direction in key_pairs[1]):
                    self.direction = self.keys[key]
                elif(self.keys[key] in key_pairs[1] and self.direction in key_pairs[0]):
                    self.direction = self.keys[key]
