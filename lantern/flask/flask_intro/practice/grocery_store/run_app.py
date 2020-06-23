# RUN ON REAL SERVER

import inject
from store import app
from fake_storage import FakeStorage

def configure(binder):
    db = FakeStorage()
    binder.bind('DB', db)

inject.clear_and_configure(configure)

if __name__ == '__main__':
    app.run()
