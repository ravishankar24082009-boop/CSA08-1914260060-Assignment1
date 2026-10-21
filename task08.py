total = 0.0

for i in range(10):
    litres = float(input("Enter litres: "))
    rate = float(input("Enter rate per litre: "))
    amount = round(litres * rate, 2)
    total += amount
    print("Payment:", amount)

print("Ten-day total:", round(total, 2))
