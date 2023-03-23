from maslomart import Parser, Converter
import time

def main(url, page_count):
    maslomart_parser = Parser(url, page_count)
    result_parse = maslomart_parser.parser()
    converter = Converter()
    converter.array_to_csv(result_parse["result"], f"{result_parse['name']}{int(time.time())}")

if __name__ == "__main__":
    res = main(
        "https://maslomart.com/catalog/smazochnye-materialy/", # ссылка на каталог
        56 # колличество страниц в каталоге
        )
