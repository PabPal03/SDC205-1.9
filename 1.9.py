name = input("Please enter your name: ")
student_id = input("Please enter your Student ID: ")

n1 = int(input("Please enter a whole number: "))
n2 = int(input("Please enter a different second whole number: "))

print(f"The result of {n1} times {n2} is: {n1 * n2:.2f}")
print(f"The result of {n1} divided by {n2} is: {n1 / n2:.2f}")
print(f"The result of {n1} plus {n2} is: {n1 + n2:.2f}")

if n1 > n2:
    print("Number 1 is larger than Number 2")
else:
    print("Number 1 is smaller than Number 2")

print(name)
print(student_id)
