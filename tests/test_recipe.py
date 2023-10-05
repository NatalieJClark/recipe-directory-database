from lib.recipe import Recipe

"""
When we construct a recipe object
With an id, title, cooking_time and rating
We can get those properties back
"""
def test_constructs():
    recipe = Recipe(1, "Test Title", 50, 3)
    assert recipe.id == 1
    assert recipe.title == "Test Title"
    assert recipe.cooking_time == 50
    assert recipe.rating == 3

"""
We can compare two identical Recipe objects
And they are considered equal
"""
def test_recipes_are_equal():
    recipe_1 = Recipe(1, "Test Title", 50, 3)
    recipe_2 = Recipe(1, "Test Title", 50, 3)
    assert recipe_1 == recipe_2

"""
We can format Recipe objects to readable strings
"""
def test_format_recipe_as_readable_string():
    recipe = Recipe(1, "Test Title", 50, 3)
    assert str(recipe) == "1. Test Title - 50 minutes - 3 out of 5"