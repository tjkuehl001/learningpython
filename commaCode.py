
# Define the listmaker function.
def listmaker():
    list1 = []  # Set up an empty list.
    n = int(input("length of list:"))  # Have the user input how many items they want their list to have.
    for i in range(n):  # Have the user input their list items.
        element = input("enter a list item:")
        list1.append(element)
    for l in range(len(list1)-1):  # Print all of the list values except the last one.
        print(list1[l] + ', ', end='')
    try:  # Print the last value of the list with formatting for the end of a sentence.
        print(list1[len(list1)-1] + '.')
    except:  # If the user passes an empty list, display an error.
        print('Error: The list is empty')