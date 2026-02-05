profile = {}

n = int(input())
for _ in range(n):
    line = input()
    if line == "":
        break
    parts = line.split(maxsplit=1)
    key = parts[0]
    value = parts[1]
    profile[key] = value

empty = input()  # пустая строка

m = int(input())
for _ in range(m):
    line = input()
    parts = line.split(maxsplit=1)
    key = parts[0]
    value = parts[1]
    profile[key] = value

sorted_keys = sorted(profile.keys())

for key in sorted_keys:
    print(f"{key}: {profile[key]}")