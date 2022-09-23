import math

summa = 0
number = None

while True:
    try:
        number = input("Your number: ")
        if number =="sum":
            break
        else:
          number = float(number)
          summa = summa + number

    except:
        print("Enter number or sum!")
        continue
print("Total", summa)
