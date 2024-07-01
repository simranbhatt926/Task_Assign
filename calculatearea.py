def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

# Input values for length and width from the user
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Call the calculate_area function and display the result
result = calculate_area(length, width)
print(result)
