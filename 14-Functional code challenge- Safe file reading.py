def read_file_contents(file_path):
    try:
        with open(file_path, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("Error: File not found -", file_path)


# C:\Users\Rohith\Desktop\Python\sample.txt
read_file_contents("/Users/Example/Documents/my_file.txt")
read_file_contents("coursera\\test.txt")
