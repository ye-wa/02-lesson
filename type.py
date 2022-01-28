# type 

a = 10
b = 10.2
c = "Canadian lad"
d = 2+3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# type conversion
# string to int conversion
age = int(input("Enter your age : "))
print(age)
print(type(age))
# string to float conversion
age2 = float(input("Enter your age : "))
print(age2)
print(type(age2))

a = "Hello"
b = "python"
c = str(3)

print(a + b + c)
print(f"{a} {b} {c}")

# Enter hours
a = float(input("Enter hours : "))
# Enter minutes
b = float(input("Enter rate : "))
# the pay
print(f"The gross pay is : {a * b}")

# Enter base
a = float(input("Enter base : "))
# Enter height
b = float(input("Enter height: "))
# the area
print(f"The area of the triangle is : { 0.5 * a * b}cm2")
