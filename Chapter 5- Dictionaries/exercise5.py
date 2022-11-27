pets = []
pet_1= {
    'animal':'Dog',
    'name':'JK',
    'owner':'Princ',
}
pets.append(pet_1)
pet_2= {
    'animal':'cat',
    'name':'Leo',
    'owner':'Logan',
}
pets.append(pet_2)

pet_3= {
    'animal':'Lizard',
    'name':'Shep',
    'owner':'Meza',
}
pets.append(pet_3)
for pet in pets:
    print("\nEverything I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ":" + str(value))