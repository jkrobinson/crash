car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'subaru'? I predcit False.")
print(car != 'subaru')

number = 23
print("\nIs number == '23'? I predict True.")
print(number == 23)

print("\nIs number <= '16'? I predict False.")
print(number <= 16)

print("\nIs car == 'subaru' and number == '23'? I predict True.")
print(car == 'subaru' and number == 23)
print(car == 'bmw' and number == 23)
print(car == 'subaru' or number == 76)

cars = ['subaru', 'toyota', 'ford', 'holden', 'bmw', 'audi']

for car in cars:
    if car != 'audi':
       print(f"\nSorry but I can't find a {car.title()}")
    else:
        print(f"\nI've found a {car.title()}")
