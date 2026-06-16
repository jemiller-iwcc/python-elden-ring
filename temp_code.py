
# create a variable with interactive input from the user

user_input = input("This text is prompted to the user asking for input: ").lower()

# adding .lower() to convert the input to lowercase to ensure case-insensitive comparison

#This is how to test if the user provided input and output a message based on whether input was provided
if user_input:
    print(f"You entered: {user_input}")
else:
    print("No input provided.")
    
    