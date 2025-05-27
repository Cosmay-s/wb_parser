import aiohttp
import asyncio

async def fetch_product_json(session, article):
    """
    Запрос данных товара по артикулу.
    """
    url = f"https://card.wb.ru/cards/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}"
    try:
        async with session.get(url) as resp:
            if resp.status != 200:
                return None
            data = await resp.json()
            return data["data"]["products"][0]
    except:
        return None

def extract_title_and_price(product):
    """
    Получение названия и цены из данных.
    """
    return {
        "title": product.get("name", "Без названия"),
        "price": product.get("salePriceU", 0) // 100
    }

async def get_wb_info(article: int) -> dict | None:
    """
    Возвращает словарь с названием и ценой товара по артикулу.
    Если товар не найден — возвращает None.
    """
    async with aiohttp.ClientSession() as session:
        product = await fetch_product_json(session, article)
        if not product:
            return None
        return extract_title_and_price(product)

async def main():
    article_str = input("Введите артикул: ").strip()
    if not article_str.isdigit():
        print("Артикул должен быть числом")
        return
    article = int(article_str)
    info = await get_wb_info(article)
    if info:
        print(info)
    else:
        print("Товар не найден или ошибка.")

if __name__ == "__main__":
    asyncio.run(main())
