class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner="Mike"):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if self.pet_type not in self.PET_TYPES:raise ValueError("Upps")
        self.all.append(self)
    pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [owner for owner in Pet.all ]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet): pet.owner = self
        else: raise TypeError("Upps")
    pass

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
owner = Owner("Ben")
pet = Pet("Whiskers", "cat")
print(owner.add_pet(pet))