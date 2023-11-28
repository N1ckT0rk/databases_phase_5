from lib.recipe import Recipe

# Test initialisation of a recipe includes id, recipe_name
# cook_time and rating
def test_init():
    recipe = Recipe(1, "test name", 60, 3)
    assert recipe.id == 1
    assert recipe.recipe_name == "test name"
    assert recipe.cook_time == 60
    assert recipe.rating == 3



