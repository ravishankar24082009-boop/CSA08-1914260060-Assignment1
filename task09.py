def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(30 + fat_steps * 0.40 + snf_steps * 0.30, 2)

def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)

try:
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    if litres < 0 or not 2 <= fat <= 7 or snf < 0:
        print("Invalid input")
    else:
        print("Rate:", rate_per_litre(fat, snf))
        print("Payment:", payout(litres, fat, snf))

except ValueError:
    print("Please enter valid numbers")
