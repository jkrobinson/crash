rivers = {
    'murray': 'australia',
    'yangtzhi': 'china',
    'missisippi': 'usa',
}

# display river and country in dictionary
for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}")

# display rivers in dictionary
for river in rivers.keys():
    print(river.title())

# display countries in dictionary
for country in rivers.values():
    if country == 'usa':
        print(country.upper())
    else:
        print(country.title())