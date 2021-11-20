class Player:
    def __init__(self, identityCode, age):
        self.identityCode = identityCode
        self.age = age
        self.ability = 20 - self.age

    def printInfo(self):
        print(self.identityCode,self.ability,self.age)

    def Run(self):
        self.ability -= 2

class Master:
    def __init__(self, fund, toltal):
        self.fund = fund
        self.PlayerList = []
        self.total = toltal

    def buyPlayer(self,player:Player):
        if self.fund >= 1000:
            self.PlayerList.append(player)
            self.fund -= 1000
        else:
            print('Insufficient funds!')
    
    def startRun(self):
        while self.total > 0:
            tempToltal = self.total
            for i in self.PlayerList:
                if i.ability > 0:
                    i.Run()
                    self.total -= 2
                else:
                    continue

            if tempToltal == self.total:
                print('More player needed!')
                break
        else:
            self.endRun()
            print('Run compeleted!')
                

    def endRun(self):
        print(f'Left:{self.total}')
        for i in self.PlayerList:
            print(f'{i.identityCode}:{i.ability}')


if __name__ == '__main__':
    master = Master(fund=10000, toltal=48)
    for i in range(3):
        player = Player(identityCode=i, age=1+3)
        master.buyPlayer(player)

    master.startRun()

