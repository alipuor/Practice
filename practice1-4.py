weight = int(input())
height = int(input())

bmi=weight/(height**2) * height**2

if bmi > 2:
    print("وضعیت مناسب ")
else:
    print("وضعیت نامناسب ")

