# Task 1 Find out which students both submitted their assignments and attended the class.
# Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_and_attended = ["Alice", "Charlie",]
submitted_only = ["Bob", "David"]
attended_only = ["Eve", "Frank"]
print(submitted_and_attended)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if submitted == attended:
    print("The lists are identitical")
else:
    print("The lists are not identical")


# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

attended = ["Charlie", "Eve", "Alice", "Frank"]

attended.remove("Eve")
print(attended)




