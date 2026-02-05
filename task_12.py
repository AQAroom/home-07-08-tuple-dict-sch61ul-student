visits = {}
city = input()

while city != "":
    if city in visits:
        visits[city] += 1
    else:
        visits[city] = 1
    city = input()

sorted_cities = sorted(visits.keys())

for city in sorted_cities:
    print(f"{city}: {visits[city]}")