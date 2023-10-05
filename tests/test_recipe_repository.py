from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/recipes.sql")
    recipe_repository = RecipeRepository(db_connection)
    recipes = recipe_repository.all()
    assert recipes == [
        Recipe(1, 'Recipe 1', 50, 2),
        Recipe(2, 'Recipe 2', 35, 5),
        Recipe(3, 'Recipe 3', 120, 5),
        Recipe(4, 'Recipe 4', 60, 4),
        Recipe(5, 'Recipe 5', 45, 3)
    ]

"""
When we call RecipeRepository#find with an id
We get the record for that id
"""
def test_find_record_with_id(db_connection):
    db_connection.seed("seeds/recipes.sql")
    recipe_repository = RecipeRepository(db_connection)
    recipe = recipe_repository.find(3)
    assert recipe == Recipe(3, 'Recipe 3', 120, 5)