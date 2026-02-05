prices = {}
line = input()

while line != "":
    parts = line.split()
    product = parts[0]
    price = int(parts[1])
    prices[product] = price
    line = input()

max_price = -1
max_product = ""

for product in prices:
    if prices[product] > max_price:
        max_price = prices[product]
        max_product = product

print(max_product)