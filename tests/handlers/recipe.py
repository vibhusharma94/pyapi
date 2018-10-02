import json
from src.common.constants import status
from tests.base import BaseTestCase


class RecipeHandlerTestCase(BaseTestCase):

    def test_recipe_list_200(self):
        headers = {'Content-Type': 'application/json'}
        resp = self.test_client.get("/recipe", headers=self.headers)
        resp_dict = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, status.HTTP_STATUS_200)
        self.assertEqual( ("results" in resp_dict.keys()), True)
        self.assertEqual( ("total" in resp_dict.keys()), True)

    def test_recipe_get_200(self):
        headers = {'Content-Type': 'application/json'}
        endpoint = '/recipe/%s' % self.recipe.id
        resp = self.test_client.get(endpoint, headers=self.headers)
        resp_dict = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, status.HTTP_STATUS_200)
        self.assertEqual(resp_dict['id'], self.recipe.id)
        self.assertEqual(resp_dict['name'], self.recipe.name)

    def test_recipe_get_404(self):
        headers = {'Content-Type': 'application/json'}
        endpoint = '/recipe/%s' % 465465
        resp = self.test_client.get(endpoint, headers=self.headers)
        self.assertEqual(resp.status_code, status.HTTP_STATUS_404)

    def test_recipe_post_201(self):
        post_data = {
            "name":"Coffee",
            "difficulty": 1,
            "preptime": 5,
            "vegetarian": True
        }

        resp = self.test_client.post('/recipe', data=json.dumps(post_data), headers=self.headers)
        resp_dict = json.loads(resp.data.decode())
        self.assertEqual( resp.status_code, status.HTTP_STATUS_201)
        self.assertEqual( post_data['name'], resp_dict['name'])
        self.assertEqual( post_data['difficulty'], resp_dict['difficulty'])
        self.assertEqual( post_data['preptime'], resp_dict['preptime'])
        self.assertEqual( post_data['vegetarian'], resp_dict['vegetarian'])

    def test_recipe_post_400(self):
        post_data = {
            "name":"",
            "difficulty": -1,
            "preptime": 6,
            "vegetarian": "1"
        }

        resp = self.test_client.post('/recipe', data=json.dumps(post_data), headers=self.headers)
        self.assertEqual( resp.status_code , status.HTTP_STATUS_400)

    def test_recipe_put_200(self):
        post_data = {
            "name":"Coffee",
            "difficulty": 1,
            "preptime": 5,
            "vegetarian": True
        }
        endpoint = '/recipe/%s' % self.recipe.id
        resp = self.test_client.put(endpoint, data=json.dumps(post_data), headers=self.headers)
        resp_dict = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, status.HTTP_STATUS_200)
        self.assertEqual(post_data['name'], resp_dict['name'])
        self.assertEqual(post_data['difficulty'], resp_dict['difficulty'])
        self.assertEqual(post_data['preptime'], resp_dict['preptime'])
        self.assertEqual(post_data['vegetarian'], resp_dict['vegetarian'])

    def test_recipe_put_404(self):
        post_data = {
            "name":"Coffee",
            "difficulty": 1,
            "preptime": 5,
            "vegetarian": True
        }
        endpoint = '/recipe/%s' % 16576576
        resp = self.test_client.put(endpoint, data=json.dumps(post_data), headers=self.headers)
        self.assertEqual(resp.status_code, status.HTTP_STATUS_404)

    def test_recipe_put_400(self):
        post_data = {
            "name":"",
            "difficulty": 1,
            "preptime": 5,
            "vegetarian": True
        }
        endpoint = '/recipe/%s' % self.recipe.id
        resp = self.test_client.put(endpoint, data=json.dumps(post_data), headers=self.headers)
        self.assertEqual(resp.status_code, status.HTTP_STATUS_400)

    def test_recipe_delete_404(self):
        endpoint = '/recipe/%s' % 156757
        resp = self.test_client.delete(endpoint, headers=self.headers)
        self.assertEqual(resp.status_code, status.HTTP_STATUS_404)

    def test_recipe_delete_204(self):
        endpoint = '/recipe/%s' % self.recipe.id
        resp = self.test_client.delete(endpoint, headers=self.headers)
        self.assertEqual(resp.status_code, status.HTTP_STATUS_204)
    
