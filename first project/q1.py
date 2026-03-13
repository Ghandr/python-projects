class Person_YourName:
    def init(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

# Creating an object of the class with your own data
person = Person_YourName("Ghandr", 20, "Mansoura")

# Calling the method to print the information
person.print_info()




