Простой асинхронный парсер, который получает название и цену товара с Wildberries по артикулу.

Как использовать

Установите зависимости:

pip install aiohttp

Запустите скрипт:

python wb_parser.py

Введите артикул товара (например, 400682365).

В ответ получите словарь с названием и ценой товара или сообщение об ошибке.

Основная функция

async def get_wb_info(article: int) -> dict | None

Принимает артикул товара (int)

Возвращает словарь с ключами "title" и "price" или None, если товар не найден

Пояснение:


Мы получаем данные о товаре с Wildberries через открытое API, отправляя асинхронный HTTP-запрос по артикулу. Вместо парсинга HTML берём готовый JSON с названием и ценой товара. Цена переводится из копеек в рубли. Если товар не найден или ошибка — возвращаем None.