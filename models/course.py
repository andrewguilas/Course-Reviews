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
    
    def get_reviews(self):
        return self.reviews

    def get_user_review(self, user):
        for review in self.reviews:
            if review.author == user:
                return review

    def add_review(self, review):
        self.reviews.append(review)
