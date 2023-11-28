class Recipe:
    
    def __init__(self, id, recipe_name, cook_time, rating):
        self.id = id
        self.recipe_name = recipe_name
        self.cook_time = cook_time
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Recipe({self.recipe_name}: Cook time = {self.cook_time} Rating = {self.rating})"