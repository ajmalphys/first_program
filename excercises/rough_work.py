# class Dog:
#     def make_sound(self):
#         return "Woof!"
# class Cat:
#     def make_sound(self):
#         return "Meow!"
# # here, two methods have same name and its called ---method over-riding---
# # This function accepts ANY object and commands it to make a sound.
# # It doesn't care if it's a dog, a cat, or a cow.
# def animal_chorus(animal_object):
#     print(animal_object.make_sound())
# # --- Demonstration ---
# dog_instance = Dog()
# cat_instance = Cat()
#
# # The same function call produces different results based on the object
# animal_chorus(dog_instance)  # Output: Woof!
# animal_chorus(cat_instance)  # Output: Meow!


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         # The __ makes this variable 'private', hiding it from direct access
#         self.__balance = balance
#
#     # Public Interface: The simple way to interact with the data
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ${amount}. Transaction secure.")
#
#     # Public Interface: You can look at the data, but only how we allow it
#     def get_balance(self):
#         return f"Account Balance: ${self.__balance}"
#
# account = BankAccount("Alice", 1000)
#
# # The user interacts ONLY with the high-level abstract methods
# account.deposit(500)
# print(account.get_balance())
#
# # They CANNOT accidentally mess with the internal complex data directly:
# # account.__balance = -50000  # This will fail or be ignored!


class UserAccount:
    def __init__(self, username, password):
        self.username = username
        # Step 1: Hide the password using double underscores (The Shield)
        self.__password = password

    # Step 2: Control how it is updated using validation (The Guard)
    def reset_password(self, current_password, new_password):
        # Verify identity first
        if current_password != self.__password:
            print("Access Denied: Current password incorrect.")
            return

        # Enforce validation rules using an if/else statement
        if len(new_password) >= 8:
            self.__password = new_password
            print("Password successfully updated!")
        else:
            print("Error: New password must be at least 8 characters long.")