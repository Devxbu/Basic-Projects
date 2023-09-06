class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, ans):
        if self.answer == ans:
            return True
        else:
            return False

q1 = Question("What is the color of the sky?",["Blue", "Red", "Yellow", "Green"], "Blue")
q2 = Question("What is the color of the sun?",["Blue", "Red", "Yellow", "Green"],"Yellow")
q3 = Question("What is the color of the grass?", ["Blue", "Red", "Yellow", "Green"], "Green")


class Quizz:
    def __init__(self, questions, questionIndex = 0, score = 0):
        self.questions = questions
        self.questionIndex = questionIndex
        self.score = score
    
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        text = 'Soru: ' + self.getQuestion().text + ' Secenekler: '
        for i in self.getQuestion().choices:
            text += (i + ' ')
        x = input(text)
        return x
    
    def loadQuestion(self):
        while self.questionIndex != len(self.questions):
            if self.getQuestion().checkAnswer(self.displayQuestion()) == True:
                self.score += 1
            self.questionIndex += 1
            print(self.displayScore())
            print(self.displayProgress())
        return 'Tebrikler!'
    
    def displayScore(self):
        return f"Puaniniz: {self.score}"
    
    def displayProgress(self):
        return f"{len(self.questions)} sorunun {self.questionIndex}.sorusundasiniz"

quizz = Quizz([q1,q2,q3])

print(quizz.loadQuestion())