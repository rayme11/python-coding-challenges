#  Implement Function to find who does specific hobbies
#  using a dictionary or list values

# Exercise: implement a function that takes the list object above
# and return true if the person does a specific Hobbie

def check_hobbie(names_and_likes, hobbie):

    persons_that_like_something = []

    for name, info in names_and_likes.items():
        for key in info:
            if key == 'hobbie' and info[key] == hobbie:
                persons_that_like_something.append(name)
    return persons_that_like_something


names_and_hobbies = {
    "Ray": {"color": "Blue", "hobbie": "Yoga"},
    "karen": {"color": "Red", "hobbie": "Soccer"},
    "Isa": {"color": "Orange", "hobbie": "Baseball"},
    "Oray": {"color": "Blue", "hobbie": "Yoga"},
    "Alex": {"color": "Blue", "hobbie": "Tennis"},
    "Mike": {"color": "Blue", "hobbie": "Tennis"},
    "Pippen": {"color": "Blue", "hobbie": "Tennis"},
    "Axl": {"color": "Blue", "hobbie": "Yoga"},
}


persons = check_hobbie(names_and_hobbies, 'Yoga')
print('Persons that like Yoga: ', persons)
