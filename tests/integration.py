import unittest
import psycopg2

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        # Закрываем соединение с базой данных после каждого теста
        return
    
    def test_database_connection(self):
        # Проверяем, что соединение с базой данных установлено
        return

    def test_database_connection2(self):
        # Проверяем, что соединение с базой данных установлено
        return


if __name__ == '__main__':
    unittest.main()