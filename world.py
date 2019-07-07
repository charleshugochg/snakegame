from enum import Enum
import random

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    
class Head(Tile):
    def __init__(self, x, y, direction):
        super().__init__(x, y)
        self.__direction = direction
    
    def setDirection(self, direction):
        if isinstance(direction, Direction):
            if ((direction == Direction.UP and
                self.__direction != Direction.DOWN) or
                (direction == Direction.DOWN and
                self.__direction != Direction.UP) or
                (direction == Direction.LEFT and
                self.__direction != Direction.RIGHT) or
                (direction == Direction.RIGHT and
                self.__direction != Direction.LEFT)):
                self.__direction = direction
        else:
            return False

    def getDirection(self):
        return self.__direction

class Tail(Tile):
    pass

class Wall(Tile):
    pass

class Food(Tile):
    pass

class Snake:
    def __init__(self, head, tails):
        self.head = head
        self.tails = tails
        self.bakTile = Tail(None, None)

    def move(self):
        x, y = self.head.x, self.head.y
        direction = self.head.getDirection()
        if direction == Direction.UP:
            self.head.y = self.head.y - 1
        elif direction == Direction.DOWN:
            self.head.y = self.head.y + 1
        elif direction == Direction.LEFT:
            self.head.x = self.head.x - 1
        elif direction == Direction.RIGHT:
            self.head.x = self.head.x + 1

        popTail = self.tails.pop()
        self.bakTile.x, self.bakTile.y = popTail.x, popTail.y
        popTail.x, popTail.y = x, y
        self.tails.insert(0, popTail)

    def addTail(self):
        self.tails.append(Tail(self.bakTile.x, self.bakTile.y))

class World:
    def __init__(self, numX, numY):
        self.__numX, self.__numY = numX, numY
        self.__isSnakeDead = False

        self.__initializeWalls()
        self.__initializeSnake()
        self.__generateFood()

    def moveSnake(self):
        if self.__isSnakeDead:
            return True

        self.__snake.move()
        if self.__detectOverlap(self.__snake.head, [self.__food]):
            self.__snake.addTail()
            self.__generateFood()

        if self.__detectOverlap(self.__snake.head, self.__snake.tails + self.__walls):
            self.__isSnakeDead = True
            return True
        
        return False

    def changeSnakeDirection(self, direction):
        self.__snake.head.setDirection(direction)

    def getWorld(self):
        d = {}
        d.update({"worldDimensions": (self.__numX, self.__numY)})
        tails = []
        for tail in self.__snake.tails:
            tails.append((tail.x, tail.y))
        d.update({"snake": {"head": (self.__snake.head.x, self.__snake.head.y, self.__snake.head.getDirection()), "tails": tails}})
        walls = []
        for wall in self.__walls:
            walls.append((wall.x, wall.y))
        d.update({"walls": walls})
        d.update({"food": (self.__food.x, self.__food.y)})

        return d

    def __initializeWalls(self):
        self.__walls = []
        for i in range(self.__numX):
            self.__walls.append(Wall(i, 0))
            self.__walls.append(Wall(i, self.__numY - 1))
        for i in range(self.__numY - 2):
            self.__walls.append(Wall(0, i + 1))
            self.__walls.append(Wall(self.__numY - 1, i + 1))

    def __initializeSnake(self):
        tails = []
        head = Head(int(self.__numX/2), int(self.__numY/2) - 1, Direction.UP)
        tails.append(Tail(head.x, head.y + 1))
        tails.append(Tail(head.x, head.y + 2))
        self.__snake = Snake(head, tails)

    def __generateFood(self):
        while True:
            x = random.randint(1, self.__numX - 2)
            y = random.randint(1, self.__numY - 2)
            food = Food(x, y)
            if self.__detectOverlap(food, list([self.__snake.head]) + self.__snake.tails):
                continue
            else:
                self.__food = food
                break

    def __detectOverlap(self, tile, tiles):
        for t in tiles:
            if t.x == tile.x:
                if t.y == tile.y:
                    return True
        return False



    
