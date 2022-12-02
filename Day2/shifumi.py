
class Rules():
    scores = {1: ["A", "X"], 2: ["B", "Y"], 3: ["C", "Z"]}
    results = {"win": 6, "draw": 3, "lose": 0}
    player1 = ["A", "B", "C"]
    player2 = ["X", "Y", "Z"]
    winning = { 
        player1[0]: [player2[2]],
        player1[1]: [player2[0]],
        player1[2]: [player2[1]]
    }

    @staticmethod
    def scoreBySign(sign):
        for k,v in Rules.scores.items(): 
            if sign in v:
                return k
        return None

    @staticmethod
    def scoreByResult(result):
        return Rules.results[result]

    @staticmethod
    def whatToPlay(signs):
        signToPlay = ""
        if signs[1] == Rules.player2[1]:
            signToPlay =  Rules.player2[Rules.player1.index(signs[0])]
            # print("draw", signs, signToPlay)
        elif signs[1] == Rules.player2[0]:
            for sign in Rules.player2:
                if Rules.isWinning(signs[0], sign):
                    signToPlay = sign
            # print("lose", signs, signToPlay)
        else:
            for sign in Rules.player2:
                if (not Rules.isWinning(signs[0], sign)) and not (Rules.player1.index(signs[0]) == Rules.player2.index(sign)):
                    signToPlay = sign
                    break
            # print("win", signs, signToPlay)
        return signToPlay

    @staticmethod
    def isWinning(sign1, sign2):
        if sign2 in Rules.winning[sign1]:
            return True
        return False

class Player():
    def __init__(self, signs):
        self.signs = signs
        self.score = 0
    
    def newScore(self, toAdd):
        self.score += toAdd

    def getScore(self):
        return self.score

class Match():
    def __init__(self, player1, player2, part, rounds):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.rounds = rounds
        self.part = part

    def resultRound(self, sign1, sign2):
        if self.player1.signs.index(sign1) == self.player2.signs.index(sign2):
            score = [Rules.scoreByResult("draw") + Rules.scoreBySign(sign1), Rules.scoreByResult("draw") + Rules.scoreBySign(sign2)]
        elif Rules.isWinning(sign1, sign2):
            score = [Rules.scoreByResult("win") + Rules.scoreBySign(sign1), Rules.scoreByResult("lose") + Rules.scoreBySign(sign2)]
        else:
            score = [Rules.scoreByResult("lose") + Rules.scoreBySign(sign1), Rules.scoreByResult("win") + Rules.scoreBySign(sign2)]
        # print(sign1, sign2, score)
        return score

    def calculateScores(self):
        for round in self.rounds:
            if self.part == 1:
                signs = round.split(' ')
            elif self.part == 2:
                signToPlay = Rules.whatToPlay(round.split(' '))
                signs = [round.split(' ')[0], signToPlay]
            roundScore = self.resultRound(signs[0], signs[1])
            # print(round.split(' '), signs, roundScore)
            self.player1.newScore(roundScore[0])
            self.player2.newScore(roundScore[1])

    def results(self):
        return "Final scores Part " + str(self.part) + " :\n\tPlayer 1 (Elf) : " + str(self.player1.getScore()) + "\n\tPlayer 2 (Human) : " + str(self.player2.getScore())

if __name__ == "__main__":
    f = open('inputs.txt')
    c = f.read()
    f.close()
    match1 = Match(Rules.player1, Rules.player2, 1, c.split('\n'))
    match1.calculateScores()
    print(match1.results())
    match2 = Match(Rules.player1, Rules.player2, 2, c.split('\n'))
    match2.calculateScores()
    print(match2.results())
