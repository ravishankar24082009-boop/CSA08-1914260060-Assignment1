def calculate_total(m1, m2, m3):
    """Returns the total marks."""
    return m1 + m2 + m3

def calculate_average(total):
    """Returns the average marks."""
    return total / 3

def get_result(average):
    """Returns the result."""
    if average >= 40:
        return "Pass"
    return "Fail"

m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))

total = calculate_total(m1, m2, m3)
average = calculate_average(total)
result = get_result(average)

print("Total:", total)
print("Average:", round(average, 2))
print("Result:", result)
