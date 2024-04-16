import unittest
import psycopg2

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(self.db_connection)

    def tearDown(self):
        # Закрываем соединение с базой данных после каждого теста
        self.db_connection.close()

    def test_database_connection(self):
        # Проверяем, что соединение с базой данных установлено
        self.assertIsNotNone(self.db_connection)

    def test_database_connection2(self):
        # Проверяем, что соединение с базой данных установлено
        self.assertIsNotNone(self.db_connection)


if __name__ == '__main__':
    unittest.main()