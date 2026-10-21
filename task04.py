fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = 30 + fat_steps * 0.40 + snf_steps * 0.30

litres = float(input("Enter litres: "))
amount = round(litres * rate, 2)

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", round(rate, 2))
print("Amount:", amount)

print((4.2 - 3.5) / 0.1)
print(round((4.2 - 3.5) / 0.1))
print(int(-2.5))
print(round(-2.5))
