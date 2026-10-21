BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Returns the rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    """Returns the payment amount."""
    return round(litres * rate_per_litre(fat, snf), 2)

litres = float(input("Enter litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))

rate = rate_per_litre(fat, snf)
amount = payout(litres, fat, snf)

print(f"Rate: {rate:.2f}")
print(f"Payment: {amount:.2f}")
