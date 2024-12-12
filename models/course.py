class Course:
    def __init__(self, mnemonic, number, title):
        self.mnemonic = mnemonic
        self.number = number
        self.title = title

    def __str__(self):
        return "{} {} {}".format(
            self.mnemonic,
            self.number,
            self.title
        )
    