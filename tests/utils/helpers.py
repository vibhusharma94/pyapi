from src.common.exceptions import httperrors
from src.utils import (
    encode_auth_token, decode_auth_token,
    get_object_or_404)

from src.models import Recipe
from tests.base import BaseTestCase


class TestUtilsMethods(BaseTestCase):

    def test_encode_auth_token(self):
        user_id = 1
        token = encode_auth_token(user_id)
        self.assertIsInstance(token, bytes)
        self.assertGreater(len(token), 1)

    def test_decode_auth_token(self):
        user_id = 1
        token = encode_auth_token(user_id)
        self.assertEqual(user_id, decode_auth_token(token))

    def test_get_object_or_404(self):
        self.assertIsInstance(get_object_or_404(self.session, Recipe, pk=self.recipe.id), Recipe)
        with self.assertRaises(Exception) as context:
            get_object_or_404(self.session, Recipe, pk=1234)
        self.assertIsInstance(context.exception, httperrors.Http404)
