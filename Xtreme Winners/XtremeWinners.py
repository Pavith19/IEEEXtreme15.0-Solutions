# Get user input
user_input = input()

# Repeat the input string four times
repeated_input = user_input * 4

# Check if the repeated string is long enough
if len(repeated_input) >= 16:
    # Access the 16th character (index 15)
    character_to_find = repeated_input[15]
    
    # Find the index of the character in the specified string and print the index
    index = " mKSpCDsveFhrlo".find(character_to_find)
    print(index)
else:
    print("Input is too short to process.")

