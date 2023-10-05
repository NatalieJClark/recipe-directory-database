class Recipe:
    def __init__(self, id, title, cooking_time, rating):
        self.id = id
        self.title = title
        self.cooking_time = cooking_time
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id}. {self.title} - {self.cooking_time} minutes - {self.rating} out of 5"