try:
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    if litres < 0 or not 2 <= fat <= 7 or snf < 0:
        print("Invalid input")
    else:
        print(f"Litres: {litres:8.2f}")
        print(f"Fat: {fat:8.2f}")
        print(f"SNF: {snf:8.2f}")

except ValueError:
    print("Please enter valid numbers")
