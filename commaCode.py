# Define spam as an empty list.
list1 = []

# Have the user input how many items they want their list to have.
n = int(input("length of list:"))

for i in range(n):
    element = input("enter a list item:")
    list1.append(element)

# Print all of the list values except the last one.
for l in range(len(list1)-1):
    print(list1[l] + ', ', end='')
try: # Print the last value of the list with formatting for the end of a sentence.
    print(list1[len(list1)-1] + '.')
# If the user passes an empty list, display an error.
except:
    print('Error: The list is empty')