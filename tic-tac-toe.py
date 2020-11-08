from sys import exit
# board object
class Board:
    def __init__(self):
        self.rows = ['top','mid','low']
        self.cols = ['l','m','r']
        self.positions = dict()
        for row in self.rows:
            for col in self.cols:
                self.positions[row+col] = row+col


    def update(self, key, val):
        self.positions[key] = val

    def show(self):
        for row in self.rows:
            for col in self.cols:
                print(self.positions[row+col],end="|")
            print()


class Players:
    def __init__(self, p1,p2):
        self.p1 = [p1,True]
        self.p2 = [p2,False]

    def player_turn(self,player):
        if "1" in player:
            self.p1[1] = True
            self.p2[1] = False

        elif "2" in player:
            self.p1[1] = False
            self.p2[1] = True



class Game:
    def __init__(self,p1,p2):
        self.rows = ['top','mid','low']
        self.cols = ['l','m','r']
        self.players = Players(p1,p2)
        self.board = Board()

    def check(self):
        #rows check
        for row in self.rows:
            if self.board.positions[row+self.cols[0]] == self.board.positions[row+self.cols[1]] == self.board.positions[row+self.cols[2]]:
                return True
        #cols check
        for col in self.cols:
            if self.board.positions[self.rows[0]+col] == self.board.positions[self.rows[1]+col] == self.board.positions[self.rows[2]+col]:
                return True
        #diag check
        if self.board.positions[self.rows[0]+self.cols[0]] ==self.board.positions[self.rows[1]+self.cols[1]]  == self.board.positions[self.rows[2]+self.cols[2]] :
                return 'col match'
        elif self.board.positions[self.rows[0]+self.cols[-1]] ==self.board.positions[self.rows[1]+self.cols[1]]  == self.board.positions[self.rows[2]+self.cols[0]] :
                return True

        return False

    def start(self):

        while True:

            x = input("x(p1/p2): ")
            if "1" in x:

                self.players.p1[1] = True
                self.players.p2[1] = False
                print("Player1 goes first!")
                self.players.p1.append('x')
                self.players.p2.append('o')
                break

            elif "2" in x:

                self.players.p2[1] = True
                self.players.p1[1] = False
                print("Player2 goes first!")
                self.players.p1.append('o')
                self.players.p2.append('x')
                break

            else:
                print("Invalid input")
                continue

        self.play()

    def play(self):
        count = 0
        while True:
            count += 1

            print("---------------------")
            self.board.show()
            print("---------------------")


            if count >= 10:
                print("Match Draw!")
                rspns = input("Like to playe again? (y/n) ")
                if "y" in rspns.lower():
                    new_game = Game(self.players.p1[0],self.players.p2[0])
                    del self
                    new_game.start()
                else:
                    exit()

            if self.players.p1[1]:
                print(f"{self.players.p1[0]}'s turn")
                self.board.update(input("position: "), self.players.p1[2])
                if self.check():
                    print(f"{self.players.p1[0]} wins")
                    rspns = input("Like to playe again? (y/n) ")
                    if "y" in rspns.lower():
                        new_game = Game(self.players.p1[0],self.players.p2[0])
                        del self
                        new_game.start()
                    else:
                        exit()
                else:
                    self.players.player_turn("p2")
                    continue
            elif self.players.p2[1]:
                print(f"{self.players.p2[0]}'s turn")
                self.board.update(input("position: "), self.players.p2[2])
                if self.check():
                    print(f"{self.players.p2[0]} wins")
                    rspns = input("Like to playe again? (y/n) ")
                    if "y" in rspns.lower():
                        new_game = Game(self.players.p1[0],self.players.p2[0])
                        del self
                        new_game.start()
                    else:
                        exit()
                else:
                    self.players.player_turn("p1")
                    continue





new_game = Game(input("player1: "),input("player2: "))
new_game.start()
