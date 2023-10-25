def calculate_average_marks():
    # Initialize an empty dictionary to store module names and marks
    module_marks = {}

    # Get input from the user and store it in the dictionary
    while True:
        module_name = input("Enter the module name (or 'done' to finish): ")
        if module_name == "done":
            break
        try:
            marks = int(input(f"Enter marks for {module_name}: "))
            module_marks[module_name] = marks
        except ValueError:
            print("Invalid input. Please enter a valid integer for marks.")

    # Calculate the average using the dictionary and len()
    total_marks = sum(module_marks.values())
    number_of_modules = len(module_marks)
    if number_of_modules > 0:
        average = total_marks / number_of_modules
        return average
    else:
        return 0  # Handle the case where no modules were entered

# Call the function to calculate the average
average_marks = calculate_average_marks()

# Display the result
print(f"The average marks for the modules is: {average_marks}")
