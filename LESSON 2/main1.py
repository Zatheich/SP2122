class Cat(object):
    def __init__(self, name:str, age:float, breed:str = ''):
        self.Name:str =  name
        self.Age:float = age
        self.Breed:str = breed
    def __str__(self):
        return (f"Name: {self.Name}\n"
                f"Age: {self.Age}\n"
                f"Breed: {self.Breed}")