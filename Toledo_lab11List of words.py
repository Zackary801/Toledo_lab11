# List of words
words = ["kiwi", "apple", "banana", "bag", "pen", "pencil"]

# Get user input for desired word length
try:
    length = int(input("Enter a number (length): "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# List to store matching words
matching_words = []

# Using a for loop to find words with the specified length
for word in words:
    # Check if the word's length matches the user's input
    if len(word) == length:
        matching_words.append(word)
    else:
        continue  # Skip to the next word if the length does not match

# Using if/else to display results
if matching_words:
    print(f"Words with length {length}: {matching_words}")
else:
    print(f"No words found with length {length}.")