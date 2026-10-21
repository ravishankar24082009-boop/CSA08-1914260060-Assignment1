PASS_MARK = 40
MAX_MARK = 100

name = input("Enter student name: ")
mark = int(input("Enter mark: "))

if 0 <= mark <= MAX_MARK:
    print("Student:", name)
    print("Mark:", mark)
    print("Pass:", mark >= PASS_MARK)
else:
    print("Invalid mark")

a = 10
b = 20
a, b = b, a
print(a, b)

value = 10
print(type(value))
value = "Hello"
print(type(value))
