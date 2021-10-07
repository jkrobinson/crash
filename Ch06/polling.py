favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll = ['danny', 'alex', 'terry', 'jen', 'phil']

for name in sorted(poll[:]):
    if name in favourite_languages:
        print(f"Hi {name.title()}.  You've already taken the poll. Thank you for that!")
    else:
        print(f"Hi {name.title()}. I see you haven't taken the poll yet. I highly recommend you do it!")

