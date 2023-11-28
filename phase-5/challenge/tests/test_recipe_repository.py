from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe


# Test all method returns all recipe objects
def test_all(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    assert repository.all() == [
        Recipe(1, 'tikka masala', 60, 5),
        Recipe(2, 'shepherds pie', 70, 3),
        Recipe(3, 'lasagna', 50, 4)
    ]

# Test find method returns recipe onject with id
# paramenter
def test_find(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    assert repository.find(2) == Recipe(2, 'shepherds pie', 70, 3)