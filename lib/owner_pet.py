class Pet:

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        if pet_type not in Pet.PET_TYPES:
            raise(Exception)

class Owner:

    def __init__(self, name, pets = None):
        self.name = name
        self.pet_arr = pets

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if type(pet) != Pet:
            raise TypeError("Not a pet")
        else:
            pet.owner = self
    def get_sorted_pets(self):
                return sorted(self.pets(), key = lambda pet: pet.name)