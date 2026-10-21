BASE_RATE = 30.00
FAT_STEP = 0.40
SNF_STEP = 0.30

farmer_id = input("Enter ID: ")
litres = float(input("Enter litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
shift = input("Enter shift: ")

rate = BASE_RATE + round((fat - 3.5) / 0.1) * FAT_STEP + round((snf - 8.5) / 0.1) * SNF_STEP
amount = round(litres * rate, 2)

print("Farmer ID:", farmer_id)
print("Shift:", shift)
print("Rate per litre:", round(rate, 2))
print("Amount:", amount)
