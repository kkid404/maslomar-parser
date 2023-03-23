from bs4 import BeautifulSoup
import requests

class Parser:

    def __init__(self, url: str, page_count: int) -> None:
        self.url = url
        self.page_count = page_count

    def parser(self):
        names_oil = []
        price_oil = []
        for page in range(self.page_count):
            page+=1
            url = f"{self.url}?PAGEN_1={page}"
            page = requests.get(url)
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
                carts = soup.findAll("div", class_="inner_wrap TYPE_1")
                for cart in carts:
                    name = cart.find("div", class_="item-title")
                    names_oil.append(name.text)
                    price = cart.find("div", class_="cost prices clearfix")
                    if price.find("div", class_="price font-bold font_mxs"):
                        price_oil.append(price.find("div", class_="price font-bold font_mxs").get("data-value"))
                    else:
                        price_oil.append("Цена не установлена")
            else:
                return f"Не работает\nКод {page.status_code}"
        return {"result" : {"Наименование" : names_oil, "Цена" : price_oil}, "name" : "maslomart"}
        