def capitalize_animals(animals):
    new_animals = []

    for animal in animals:
        new_animals.append(animal[0].upper() + animal[1:])

    return new_animals

if __name__ == "__main__":
    print(capitalize_animals(['cheetah', 'hare', 'reindeer', 'calf']))
