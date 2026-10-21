from decimal import Decimal
import time

for n in [300, 6000, 150000]:
    payments = ["33.40"] * n + ["0.10"] * 3

    start = time.perf_counter()
    float_total = sum(float(x) for x in payments)
    float_time = time.perf_counter() - start

    start = time.perf_counter()
    decimal_total = sum((Decimal(x) for x in payments), Decimal("0.00"))
    decimal_time = time.perf_counter() - start

    print("Payments:", n)
    print("Float total:", float_total)
    print("Decimal total:", decimal_total)
    print("Difference:", Decimal(str(float_total)) - decimal_total)
    print("Float time:", float_time)
    print("Decimal time:", decimal_time)
