from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = BASE_RATE + Decimal(fat_steps) * FAT_STEP_VALUE + Decimal(snf_steps) * SNF_STEP_VALUE
    return rate.quantize(Decimal("0.01"))

def payout(litres, fat, snf):
    return (litres * rate_per_litre(fat, snf)).quantize(Decimal("0.01"))

litres = Decimal(input("Enter litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))

if litres < 0 or not 2 <= fat <= 7 or snf < 0:
    print("Invalid input")
else:
    print("Rate:", rate_per_litre(fat, snf))
    print("Payment:", payout(litres, fat, snf))
