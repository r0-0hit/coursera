shirt_color = "pink"


def display_color_works(shirt_color):
    print("First shirt color is:", shirt_color)


def display_color_failure(shirt_color):
    # Try to access 'color' directly (this will cause an error)
    try:
        print("Your shirt color is:", shirt_color)
    except Exception as e:
        print("Exception occured ", e)


# The shirt_color variable is in scope in this function
display_color_works(shirt_color)

# The shirt_color variable is not in scope in this function
display_color_failure(shirt_color)
