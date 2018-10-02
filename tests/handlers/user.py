import json
from src.common.constants import status
from tests.base import BaseTestCase


class UserHandlerTestCase(BaseTestCase):

    def test_usersignup_post_201(self):
        post_data = {
            "email":"abcdef@gmail.com",
            "password": "verystrongpass"
        }

        resp = self.test_client.post('/user-signup', data=json.dumps(post_data), headers=self.headers)
        resp_dict = json.loads(resp.data.decode())
        self.assertEqual( resp.status_code, status.HTTP_STATUS_201)
        self.assertEqual( post_data['email'], resp_dict['email'])


    def test_usersignup_post_400(self):
        post_data = {
            "email":"Invalid@email",
            "password": "pass"
        }

        resp = self.test_client.post('/user-signup', data=json.dumps(post_data), headers=self.headers)
        self.assertEqual( resp.status_code, status.HTTP_STATUS_400)


class UserAuthHandlerTestCase(BaseTestCase):

    def test_userlogin_post_200(self):
        post_data = {
            "email":"abcdef@gmail.com",
            "password": "verystrongpass"
        }

        self.test_client.post('/user-signup', data=json.dumps(post_data), headers=self.headers)
        resp = self.test_client.post('/user-login', data=json.dumps(post_data), headers=self.headers)
        resp_dict = json.loads(resp.data.decode())
        self.assertEqual( resp.status_code, status.HTTP_STATUS_200)
        self.assertEqual( 'Access-Token' in resp_dict.keys(), True)


    def test_userlogin_post_400(self):
        post_data = {
            "email":"Invalid@email",
            "password": "pass"
        }

        resp = self.test_client.post('/user-login', data=json.dumps(post_data), headers=self.headers)
        self.assertEqual( resp.status_code, status.HTTP_STATUS_400)
