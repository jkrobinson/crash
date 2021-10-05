pizzas = ['meat lovers', 'hawaiian', 'cheesy']
pizzas.append('supreme')

friend_pizzas = pizzas[:]
friend_pizzas.append('bbq chicken')

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
