class Course:
    def __init__(self, mnemonic, number, title):
        self.mnemonic = mnemonic
        self.number = number
        self.title = title
        self.reviews = []

    def __str__(self):
        return "{} {} {}".format(
            self.mnemonic,
            self.number,
            self.title
        )
    
    def getReviews(self):
        return self.reviews
