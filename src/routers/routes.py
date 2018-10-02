from src.handlers import (
    RecipeHandler, RecipeRatingHandler,
    UserHandler, UserAuthHandler,)


__all__ = ('ROUTES',)


ROUTES = [
        ("/user-signup", UserHandler()),
        ("/user-login", UserAuthHandler()),

        ("/recipe", RecipeHandler()),
        ("/recipe/([0-9]+)", RecipeHandler()),
        ("/recipe/([0-9]+)/rating", RecipeRatingHandler()),
	]


