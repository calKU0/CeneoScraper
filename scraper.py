import requests

#product_code = input("Podaj kod produktu")
product_code="100361771"

url=f"https://www.ceneo.pl/{product_code}#tab=reviews"

respons = request.get(url)
print(respons.status_code)

