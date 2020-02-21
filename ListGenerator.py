import random

class Generator:
    def __init__(self, maxLength, largestValue):
        self.maxLength = maxLength
        self.largestValue = largestValue

    def generate_random_list(self):
        random_list = []
        for _ in range(self.maxLength):
            random_list.append(random.randint(0, self.largestValue))
        return random_list