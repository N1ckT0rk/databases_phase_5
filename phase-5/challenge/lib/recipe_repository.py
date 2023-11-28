from lib.recipe import Recipe

class RecipeRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes_list = []
        for row in rows:
            recipe = Recipe(row['id'], row['recipe_name'], row['cook_time'], row['rating'])
            recipes_list.append(recipe)
        return recipes_list

    def find(self, id):
        rows = self._connection.execute('SELECT * from recipes where id = %s', [id])
        row = rows[0]
        return Recipe(row['id'], row['recipe_name'], row['cook_time'], row['rating'])
