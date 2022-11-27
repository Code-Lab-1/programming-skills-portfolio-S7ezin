pets = []
pet_1= {
    'animal':'cat',
    'name':'macho',
    'owner':'sam',
}
pets.append(pet_1)
pet_2= {
    'animal':'dog',
    'name':'sam',
    'owner':'mike',
}
pets.append(pet_2)

pet_3= {
    'animal':'parrot',
    'name':'peso',
    'owner':'eric',
}
pets.append(pet_3)
for pet in pets:
    print("\nEverything I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ":" + str(value))