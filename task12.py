from decimal import Decimal

def rate_per_litre(fat, snf, month):
    base_rate = Decimal("30.00")
    fat_step = Decimal("0.40")

    if month.lower() in ["april", "may", "june"]:
        base_rate = Decimal("32.00")
        fat_step = Decimal("0.45")

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = base_rate + Decimal(fat_steps) * fat_step + Decimal(snf_steps) * Decimal("0.30")
    return rate.quantize(Decimal("0.01"))

def payout(litres, fat, snf, month):
    return (litres * rate_per_litre(fat, snf, month)).quantize(Decimal("0.01"))

month = input("Enter month: ")
total_litres = Decimal("0")
total_payment = Decimal("0")

for i in range(10):
    litres = Decimal(input("Enter litres: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    rate = rate_per_litre(fat, snf, month)
    amount = payout(litres, fat, snf, month)

    total_litres += litres
    total_payment += amount

    print("Rate:", rate)
    print("Payment:", amount)

if total_litres > 500:
    total_payment += total_litres * Decimal("0.50")

print("Ten-day litres:", total_litres)
print("Final payment:", total_payment.quantize(Decimal("0.01")))
