import requests
from bs4 import BeautifulSoup as bs
import json

URL_TEMPLATE = "https://www.tazabek.kg/valuta/"
r = requests.get(URL_TEMPLATE)
print(r.status_code)


soup = bs(r.text, "html.parser")


def parse():
    data = {}
    data['bank_сurrency'] = []
    banks_names = soup.find_all('tr', class_='sortable')
    print(banks_names)
    for name in banks_names:
        if name.text == "Покупка" or name.text == "Продажа":
            pass
        else:
            bank_name = name.span.text
            bank_img_url = "https://www.tazabek.kg/" + name.td.img['src']
            buying_USD = name.span.next.next.text
            sealing_USD = name.find_next('td', class_="td-colored text-center").text
            buying_EUR = name.find_next('td', class_="td-dotted text-center").text
            sealing_EUR = name.find_next('td', class_="text-center").find_next('td', class_="text-center")\
                .find_next('td', class_="text-center").find_next('td', class_="text-center").text
            buying_RUB = name.find_next('td', class_="td-colored td-dotted text-center").\
                find_next('td', class_="td-colored td-dotted text-center").div.text
            sealing_RUB = name.find_next('td', class_="td-colored td-dotted text-center").\
                find_next('td', class_="td-colored td-dotted text-center").\
                find_next('td', class_="td-colored text-center").text
            buying_KZT = name.find_next('td', class_="td-dotted text-center").\
                find_next('td', class_="td-dotted text-center").div.text
            sealing_KZT = name.find_next('td', class_="td-dotted text-center").\
                find_next('td', class_="td-dotted text-center").find_next('td', class_="text-center").text
            refresh_date = name.find_next('td', class_="td-datetime").text
            refresh_date = name.find_next('td', class_="td-datetime").span.text
            if len(refresh_date) > 8:
                refresh_date = refresh_date[5:]

            data["bank_сurrency"].append({
                "bank_name": f"{bank_name}",
                "bank_img_url": f"{bank_img_url}",
                "buying_USD": f"{buying_USD}",
                "sealing_USD": f"{sealing_USD}",
                "buying_EUR": f"{buying_EUR}",
                "sealing_EUR": f"{sealing_EUR}",
                "buying_RUB": f"{buying_RUB}",
                "sealing_RUB": f"{sealing_RUB}",
                "buying_KZT": f"{buying_KZT}",
                "sealing_KZT": f"{sealing_KZT}",
                "refresh_date": f"{refresh_date}"
            })
    return data

