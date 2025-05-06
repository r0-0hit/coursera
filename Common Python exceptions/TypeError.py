print("hello" + 5)
print(5 + "hi")
print(len(5))


def calculate_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers.")
    return length * width


print(calculate_area(5, "three"))  # TypeError: Length and width must be numbers.
