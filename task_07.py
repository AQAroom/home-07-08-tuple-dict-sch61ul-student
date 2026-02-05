grades = {}
line = input()

while line != "":
    parts = line.split()
    subject = parts[0]
    score = int(parts[1])
    grades[subject] = score
    line = input()

if len(grades) > 1:
    total = sum(grades.values())
    count = len(grades)
    average = total / count
else:
    average = score
print(f"{average:.2f}")
