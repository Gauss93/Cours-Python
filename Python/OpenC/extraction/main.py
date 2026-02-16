from bs4 import BeautifulSoup


with open("index.html", 'r', encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

title = soup.title
print(title)

id = soup.find(id='titre')
print(id)

produit = dict()
infos = soup.find_all("li")

for info in infos:
    name = info.find("h2").string
    price_str = info.find("p", class_="price").string

    
    produit[name] = {"prix": price_str.strip()}

    description = info.find_all("p")[-1].string
    produit[name]["description"] = description

print("Produits", produit)

for name in produit.keys():
    price_str = produit[name]["prix"]

    price = price_str.split(":")[-1].replace("€", "").strip()
    price = float(price)
    dollar_price = price * 1.1
    produit[name]["prix_dollar"] = f"{dollar_price}$"

print("Tous les produits:", produit)
