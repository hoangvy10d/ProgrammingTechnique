class Fanfic:
    def __init__(self, Title, Characters, DateReleased, Author, LinkFilm):
        self.Title = Title
        self.Characters = Characters
        self.DateReleased = DateReleased
        self.Author = Author
        self.LinkFilm = LinkFilm

    def __str__(self):
        return f"{self.Title}\t{self.Characters}\t{self.DateReleased}\t{self.Author}\t{self.LinkFilm}"