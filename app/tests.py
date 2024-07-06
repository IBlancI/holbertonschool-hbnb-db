# app/tests.py
import os
import unittest
from app import create_app, db
from app.config import DevelopmentConfig, ProductionConfig

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(DevelopmentConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_sqlite_connection(self):
        os.environ['DATABASE_URL'] = 'sqlite:///test.db'
        self.assertTrue(os.path.exists('test.db'))

    def test_postgresql_connection(self):
        os.environ['DATABASE_URL'] = 'postgresql://user:password@localhost/testdb'
        self.app.config.from_object(ProductionConfig)
        with self.app.app_context():
            connection = db.engine.connect()
            self.assertIsNotNone(connection)

if __name__ == '__main__':
    unittest.main()
