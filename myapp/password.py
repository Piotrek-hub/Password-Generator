import string
import random 
class Password():

    def __init__(self, password_length):
        self.letters = list(string.ascii_letters)
        self.digits = list(string.digits)
        self.punctuation = list(string.punctuation)
        self.password_length = password_length

        while self.password_length % 3 != 0:
            self.password_length += 1

    def generateLetters(self):
        res = []
        for x in range(int(self.password_length / 3)):
            rand = random.randint(0,len(self.letters) -1)
            res.append(self.letters[rand])
        return res

    def generateDigits(self):
        res = []
        for x in range(int(self.password_length / 3)):
            rand = random.randint(0,len(self.digits) -1)
            res.append(self.digits[rand])
        return res

    def generatePunctuations(self):
        res = []
        for x in range(int(self.password_length / 3)):
            rand = random.randint(0,len(self.punctuation) -1)
            res.append(self.punctuation[rand])
        return res

    def generateFullPassword(self):
        password = self.generateLetters() + self.generateDigits() + self.generatePunctuations()
        random.shuffle(password)
        password = ''.join(password)
        return password
