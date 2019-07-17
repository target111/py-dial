class Keyboard(object):
    def __init__(self):
        self.keys = {"1": ["1"], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n",  "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"], "0": ["0"]}
        self.vowels = ["a", "e", "i", "o", "u"]

    def get_vowel(self, list):
        for letter in list:
            if letter in self.vowels:
                return letter

        return None
            

    def get_letters(self, number):
        letters = []

        for number in number:
            if len(letters) < 1:
                letters.append(self.keys[number][0])
                continue

            if letters[-1] not in self.vowels:
                if self.get_vowel(self.keys[number]):
                    letters.append(self.get_vowel(self.keys[number]))
                    continue

            for letter in self.keys[number]:
                if letter not in self.vowels and letter != letters[-1]:
                    letters.append(letter)
                    break

                elif letter == letters[-1] and len(self.keys[number]) == 1:
                    letters.append(letter)
                
        return letters