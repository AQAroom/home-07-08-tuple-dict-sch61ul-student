password = input()
n = int(input())

requirements = {}
for _ in range(n):
    line = input()
    parts = line.split()
    req_type = parts[0]
    req_value = parts[1]
    requirements[req_type] = req_value

valid = True

if "мин_длина" in requirements:
    min_len = int(requirements["мин_длина"])
    if len(password) < min_len:
        valid = False

if "цифры" in requirements and requirements["цифры"] == "да":
    has_digit = False
    for char in password:
        if '0' <= char <= '9':
            has_digit = True
            break
    if not has_digit:
        valid = False

if "заглавные" in requirements and requirements["заглавные"] == "да":
    has_upper = False
    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
            break
    if not has_upper:
        valid = False

if valid:
    print("Да")
else:
    print("Нет")