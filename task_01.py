morning = float(input())
day = float(input())
evening = float(input())

temps = (morning, day, evening)
average = sum(temps) / len(temps)
print(f"{average:.2f}")
