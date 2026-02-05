grades = {}
line = input()

while line != "":
    parts = line.split()
    subject = parts[0]
    score = int(parts[1])
    grades[subject] = score
    line = input()

total = sum(grades.values())
count = len(grades)
average = total / count
print(f"{average:.2f}")