# ОpenWeather API Test
## Описание

Этот проект содержит тестовый набор для проверки работы API OpenWeatherMap.  

Включает тесты для получения:  
- текущей погоды по названию города
- по координатам
- прогноз на 5 дней  


Основные проверяемые данные:
- успешность ответа
- наличие ключевых полей
- соответствие города
- валидность значения температуры (по Цельсию)

## Требования

- Python 3.x

## Установка и использование

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/GeorgeYulpatov/openweather_test_api.git
    cd openweather_test_api
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    venv\Scripts\activate  # для Windows
    source venv/bin/activate  # для Linux / macOS
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` для хранения переменных окружения (API-ключи, пароли и другие параметры конфигурации):

    ```bash
    echo "API_KEY=your_api_key" > .env
    ```

    - Замените `your_api_key` на ваш реальный API-ключ.

5. Запуск тестов:

    ```bash
    python test_api_unittest.py
## Лицензия  
Этот проект лицензирован под лицензией MIT.
