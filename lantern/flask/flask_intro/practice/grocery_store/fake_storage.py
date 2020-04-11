from itertools import count
from store import NoSuchUserError, NoSuchStoreID


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeStores:
    def __init__(self):
        self._stores = {}
        self._id_stores_counter = count(1)

    def add_store(self, store):
        store_id = next(self._id_stores_counter)
        self._stores[store_id] = store
        return store_id

    def get_store_by_id(self, store_id):
        try:
            return self._stores[store_id]
        except KeyError:
            raise NoSuchStoreID(store_id)

    def update_store_by_id(self, store_id: int, store: dict):
        if store_id in self._stores:
            self._stores[store_id] = store
        else:
            raise NoSuchStoreID(store_id)


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id: int, user) -> dict:
        if user_id in self._users:
            user = self._users[user_id]
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = []
        self._id_goods_counter = count(1)

    def add_goods(self, goods):
        for good in goods:
            good['id'] = next(self._id_goods_counter)
            self._goods.append(good)
        return len(self._goods)

    def get_goods(self):
        return self._goods

    def update_goods(self, goods):
        success_updated_goods, error = 0, []
        for good in goods:
            good_id = good['id']
            if good_id in self._goods:
                self._goods[good_id] = good
                success_updated_goods += 1
            else:
                error.append(good_id)
        return success_updated_goods, error

