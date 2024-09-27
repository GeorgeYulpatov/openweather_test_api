import os
import unittest

import requests
from dotenv import load_dotenv

load_dotenv()


class TestOpenWeatherMapAPI(unittest.TestCase):
    """
    Тестовый набор для проверки работы API OpenWeatherMap.
    Включает тесты для получения текущей погоды по названию города,
    по координатам, а также прогноз на 5 дней.
    Основные проверяемые данные:
        - успешность ответа (код 200)
        - наличие ключевых полей
        - соответствие города
        - валидность значения температуры (по Цельсию)
    """

    def setUp(self):
        """
        Метод, который выполняется перед каждым тестом.
        Используется для инициализации общих данных, таких как API ключ,
        базовый URL для запросов, и параметры для тестов (город, координаты).
        """
        self.api_key = os.getenv("API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.city = "Moscow"
        self.lat = 55.7558
        self.lon = 37.6173

    def make_request(self, endpoint, params):
        """
        Вспомогательный метод для выполнения запросов к API.
        :param endpoint: Конечный путь (например, '/weather' или '/forecast')
        :param params: Параметры запроса (например, город или координаты)
        :return: JSON-ответ от API
        """
        url = f"{self.base_url}/{endpoint}"
        params['appid'] = self.api_key
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        return response.json()

    def common_weather_checks(self, data):
        """
        Вспомогательный метод для проверки общих полей в ответе погоды.
        :param data: JSON-ответ от API
        """
        self.assertIsNotNone(data)
        self.assertIn("name", data)
        self.assertIn("sys", data)
        self.assertIn("country", data["sys"])
        self.assertIn("main", data)
        self.assertIn("temp", data["main"])
        # Проверка температуры в диапазоне от -90 до 60 градусов Цельсия
        self.assertTrue(-90 < data["main"]["temp"] - 273.15 < 60)

    def test_in_the_selected_city(self):
        """ Тест получения текущей погоды по названию города. """
        data = self.make_request('weather', {'q': self.city})
        self.assertEqual(data["name"], self.city)
        self.common_weather_checks(data)

    def test_by_coordinates(self):
        """ Тест получения текущей погоды по географическим координатам. """
        data = self.make_request('weather', {'lat': self.lat, 'lon': self.lon})
        self.assertEqual(data["name"], self.city)
        self.common_weather_checks(data)

    def test_weather_for_five_days(self):
        """ Тест получения прогноза погоды на 5 дней по названию города. """
        data = self.make_request('forecast', {'q': self.city, 'cnt': 5})
        self.assertIn("city", data)
        self.assertEqual(data["city"]["name"], self.city)
        self.assertIn("list", data)
        self.assertEqual(len(data["list"]), 5)  # Проверка, что возвращаемый список содержит прогнозы на 5 дней.
        for item in data["list"]:
            self.assertIn("main", item)
            self.assertIn("temp", item["main"])
            self.assertTrue(-90 < item["main"]["temp"] - 273.15 < 60)


if __name__ == "__main__":
    unittest.main()
