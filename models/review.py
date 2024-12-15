from datetime import datetime

class Review:
    def __init__(self, rating, comment, author):
        self.rating = rating
        self.comment = comment
        self.date = datetime.today()
        self.author = author

    def __str__(self):
        return "{} {}\n{}".format(
            self.date,
            "⭐" * self.rating,
            self.comment
        )
