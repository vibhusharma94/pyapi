from decimal import Decimal
from src.utils import get_object_or_404
from src.models import RecipeRating
from tests.base import BaseTestCase


class TestModelMethods(BaseTestCase):

    def test_recipe_avg_rating(self):
        for value in range(1, 6):
            self.session.add(RecipeRating(value=value, recipe_id=self.recipe.id))
            self.session.commit()

        queryset = self.session.query(RecipeRating).filter_by(recipe_id=self.recipe.id)
        total_score = sum([o.value.value for o in queryset])
        avg_rating = total_score
        if total_score:
            value = Decimal(total_score / queryset.count())
            avg_rating = float(round(value, 1))

        self.assertEqual(avg_rating, self.recipe.avg_rating)
        
