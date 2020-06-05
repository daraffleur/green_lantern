import inject
import json

from store import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'Andrew Derkach'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexistent_user(self):
        resp = self.client.get(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_successful_update_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.put(f'/users/{user_id}', json={'name': 'Johanna Doe'})
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_update_unexistent_user(self):
        resp = self.client.put(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):
    def setup_post_goods(self):
        with open('goods.json') as list_of_goods:
            response = self.client.post(
                '/goods',
                json=json.load(list_of_goods)
            )
            return response


    def setup_goods_with_id(self):
        with open('goods_with_id.json') as list_of_goods_with_id:
            return json.load(list_of_goods_with_id)


    def test_goods_post(self):
        response = self.setup_post_goods()
        assert response.status_code == 201
        assert response.json == {'Number of items created': 10}


    def test_goods_get(self):
        self.setup_post_goods()
        response = self.client.get('/goods')
        assert response.status_code == 200
        assert response.json == self.setup_goods_with_id()


    def test_update_goods(self):
        self.setup_post_goods()
        with open('goods_what_need_update.json') as list_of_goods_for_updating:
            response = self.client.put(
                '/goods',
                json=json.load(list_of_goods_for_updating)
            )
        assert response.status_code == 200
        assert response.json == {'Successfully updated': 3, 'errors': {'No such id in goods': [18, 19, 20]}}


class TestStores(Initializer):
    def setup_user_data(self):
        user_name = {'name': "John Doe"}
        response = self.client.post(
            '/users',
            json=user_name
        )
        return response

    def setup_store_data(self, user_id):
        response = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': user_id}
        )
        return response

    def test_create_store(self):
        user_id = self.setup_user_data().json['user_id']
        response = self.setup_store_data(user_id)
        assert response.status_code == 201
        assert response.json == {'store_id': 1}

        response = self.setup_store_data(user_id=2)
        assert response.status_code == 404
        assert response.json == {'error': "No such user_id 2"}

    def test_get_store_by_id(self):
        user_id = self.setup_user_data().json['user_id']
        self.setup_store_data(user_id)
        response = self.client.get(f'/store/{user_id}')
        assert response.status_code == 200
        assert response.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': user_id}

        response = self.client.get(f'/store/{5 + user_id}')
        assert response.status_code == 404
        assert response.json == {'error': f"No such store_id {5 + user_id}"}

    def test_update_store(self):
        user_id = self.setup_user_data().json['user_id']
        self.setup_store_data(user_id)
        resp = self.client.put(f'/store/{user_id}',
                               json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': user_id})
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

        resp = self.client.put(f'/store/{user_id}',
                               json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 5 + user_id})
        assert resp.status_code == 404
        assert resp.json == {'error': f'No such user_id {5 + user_id}'}


