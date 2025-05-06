person = {"name": "Alice", "age": 25}
print(person.get("name"))  # Output: Alice
print(person.get("email"))  # Output: None
print(person.get("email", "Not Provided"))  # Output: Not Provided

# print(person["email"])

my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError:
    print("Key not found in dictionary.")
