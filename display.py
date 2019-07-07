from world import Direction

class Display:
    def drawWorld(self, _w):
        wDim = _w.get("worldDimensions")
        display = []
        for i in range(wDim[0]):
            i
            line = ''
            for j in range(wDim[1]):
                j
                line = line + ' '
            display.append(line)

        walls = _w.get("walls")
        for wall in walls:
            line = display[wall[1]]
            line = line[:wall[0]] + "#" + line[wall[0]+1:]
            display[wall[1]] = line

        tails = _w.get("snake").get("tails")
        for tail in tails:
            line = display[tail[1]]
            line = line[:tail[0]] + "O" + line[tail[0]+1:]
            display[tail[1]] = line

        food = _w.get("food")
        line = display[food[1]]
        line = line[:food[0]] + "X" + line[food[0]+1:]
        display[food[1]] = line 

        head = _w.get("snake").get("head")
        if head[2] == Direction.UP:
            direction = '^'
        elif head[2] == Direction.DOWN:
            direction = '~'
        elif head[2] == Direction.LEFT:
            direction = '<'
        else:
            direction = '>'
        line = display[head[1]]
        line = line[:head[0]] + direction + line[head[0]+1:]
        display[head[1]] = line

        for line in display:
            print(line)

    def drawMenu(self):
        print('##############################################')
        print("########## WELCOME FROM SNAKE WORLD ##########")
        print('##############################################')
        print(' SELECT                                       ')
        print(' enter) play                                  ')
        print(' esc) exit                                    ')
        print('                                              ')
        print(' You can exit with ESC while playing          ')
        print('                                              ')
        print('##############################################')

    def drawGameover(self):
        print("##############################################")
        print('##############################################')
        print('##############################################')
        print('##############################################')
        print('################# GAMEOVER ###################')
        print('##############################################')
        print('##########    Press enter to MENU   ##########')
        print('##########     Press esc to exit    ##########')
        print('##############################################')
        print('##############################################')
    