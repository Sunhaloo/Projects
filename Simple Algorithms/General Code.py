# Random Program Code 1

print()

# DECLARE anime: ARRAY[0:5] OF STRING
anime = ["EREN", "LEVI", "GOJO", "TANJIRO", "NEZUKO", "MAI"]

# DECLARE subject: ARRAY[0:5] OF STRING
subject = ["COMPUTER", "SOCIOLOGY", "ARABIC", "ENGLISH", "FRENCH", "JAPANESE"]

# DECLARE arrayStack: ARRAY[0:4] OF STRING
arrayStack = ["ROSE", "BOGAINLAVILLAIN", "LILY", "LAVENDER", "JASMINE"]

# DECLARE fruits: ARRAY[0:5] OF STRING
fruits = ["Grape", "Kiwi", "Apple", "Mango", "Banana", "Orange"]

# DECLARE num: ARRAY[0:4] OF INTEGER
num = [12, 45, 23, 45, 55]

# Functions and Procedures
# Functions To Display Arrays
# Function with identifier name "display_anime" which will display array "anime"
def display_anime():

 # If array is empty
 if not anime:

  print()
  print("Array Is Empty!")
  print()

 else:

  for x in anime:

   # Outputs the value of array on separate lines
   print(x)

# Function with identifier name "display_subject" to display the array "subject"
def display_subject():

 # If array is empty
 if not subject:

  print()
  print("Array Is Empty!")
  print()

 else:

  for x in subject: &nbsp;

   # Outputs the value of array on separate lines
   print(x)

# Function with identifier name "display_num" to display array "num"
def display_num():

 # If array is empty
 if not num:

  print()
  print("Array Is Empty!")
  print()

 else:

  for x in num:

   # Outputs the value of array on separate lines
   print(x)

# Function with identifier name "Inseriton_Sort_Number" which will sort our array "num"
# Function "Insertion_Sort_Number" will perform the calculation
def Insertion_Sort_Number(num):

 # Variable array_length will store the length of the array
 array_length = len(num)

 # Insertion Sort compares second values with previous value
 for i in range(1, array_length):

  # Storing the values stored at "i"
  value_i = num[i]

  # Storing the "previous" address of "i"
  j = i - 1

  # Condition to enter loop
  while j >= 0 and num[j] > value_i:

   # Swapping Part of Algorithm
   num[j + 1] = num[j]

   # Counter / Address of "j" decreases by 1
   j -= 1

  # If array is already sorted, "returns array"
  num[j + 1] = value_i

# Function with identifier name "Insertion_Sort_String" which will sort our array "anime"
# Function "Insertion_Sort_String" will perform the calculation
def Insertion_Sort_String(anime):

 # Variable array_length will store the length of the array
 array_length = len(anime)

 # Insertion Sort compares second values with previous value
 for i in range(1, array_length):

  # Storing the values stored at "i"
  value_i = anime[i]

  # Storing the "previous" address of "i"
  j = i - 1

  # Condition to enter loop
  while j >= 0 and anime[j] > value_i:

   # Swapping Part of Algorithm
   anime[j + 1] = anime[j]

   # Counter / Address of "j" decreases by 1
   j -= 1

  # If array is already sorted, "returns array"
  anime[j + 1] = value_i

# Insertion Sort Page ( Sub Page )
# Function with identifier name "InsertionSort" will be our sub page ( for insertion sort )
def InsertionSort():

 # Insertion Sort Main Page ( Overall it's a sub page )
 print()
 print("Insertion Sort Sub Page")
 print()
 print("----------")
 print()
 print("Insertion Sort Integers: 1")
 print()
 print("Insertion Sort Strings: 2")
 print()
 print("Exit Program: 3")
 print()

 # Ask the user to enter his choice for insertion sort sub-page
 # Exception Handling
 try:

  # Ask the user to enter a choice for insertion sort sub-page
  choice_insertion_sort = int(input("Please Enter A Choice From The Above Choices: "))

 # If users anything character except of integers
 except ValueError:

  # Outputs appropriate message
  print()
  print("Please Enter Integer Values Only!")
  print()

 # Provides Corresponding Respond To User Choice
 if choice_insertion_sort == 1:

  print()
  print("Array Before Insertion Sort:")
  print()

  # Calling function "display_num" to display the contents of array "num"
  # This is to show the user what the array looked like BEFORE applying Insertion Sort
  display_num()

  print()
  print("Array After Insertion Sort:")

  # Calling the function "Insertion_Sort_Number" to arrange the numbers in ascending order
  Insertion_Sort_Number(num)

  print()

  # Displaying the array again
  # This is show the user what the array looks AFTER applying Insertion Sort

  display_num()

  print()

 elif choice_insertion_sort == 2:

  print()
  print("Array Before Insertion Sort:")
  print()

  # Calling function "display_anime" to display the contents of array "anime"
  # This is to show the user what the array looked like BEFORE applying Insertion Sort

  display_anime()

  print()
  print("Array After Insertion Sort:")

  # Calling the function "Insertion_Sort_Number" to arrange the numbers in ascending order
  Insertion_Sort_String(anime)

  print()

  # Displaying the array again
  # This is show the user what the array looks AFTER applying Insertion Sort

  display_anime()
  print()

# Function with identifier name "BubbleSort_Number" which will sort our array "num"
# Function "BubbleSort_Number" will perfom the calculation
def BubbleSort_Number(num):

 # Calculating the length of array "num"
 length_array = len(num)

 # Variable "update" will "tell" up if the value has been swapped
 update = True

 # Variable "swap" will keep track of how many times valus has been swapped
 swap = 0

 # Condition to enter "while" loop
 while update == True and length_array > 0:

  # "update" need to become "False" to be "updated"
  update = False

  # Number of times it will sort the array
  for x in range(0, length_array - 1):

   # Checks ever value in the array
   for y in range(0, length_array - 1):

    # Sorting the array in Ascending Order
    if num[y] > num[y +1]:

     # Sorting Part of Algorithm
     temp = num[y]
     num[y] = num[y + 1]
     num[y + 1] = temp

     # "update" become "True"
     update = True

     # "swap" increases by 1
     swap += 1

# Function with identifier name "BubbleSort_Anime" which will sort our array "num"
# Function "BubbleSort_Anime" will perfom the calculation
def BubbleSort_Anime(anime):

 # Calculating the length of array "anime"
 length_array = len(anime)

 # Variable "update" will "tell" up if the value has been swapped
 update = True

 # Variable "swap" will keep track of how many times valus has been swapped
 swap = 0

 # Condition to enter "while" loop
 while update == True and length_array > 0:

  # "update" need to become "False" to be "updated"
  update = False

  # number of times it will sort the array
  for x in range(0, length_array - 1):

   # Checks ever value in the array
   for y in range(0, length_array - 1):

    # Sorting the array in Ascending Order
    if anime[y] > anime[y +1]:

     # Sorting Part of Algorithm
     temp = anime[y]
     anime[y] = anime[y + 1]
     anime[y + 1] = temp

     # "update" become "True"
     update = True

     # "swap" increases by 1
     swap += 1

# Bubble Sort ( Sub-Page )
# Function with identifier name "BubbleSort" will be our sub page ( for bubble sort )
def BubbleSort():

 # Bubble Sort Main Page ( Overall sub page )
 print()
 print("Bubble Sort Sub Page")
 print()
 print("----------")
 print()
 print("Bubble Sort Integers: 1")
 print()
 print("Bubble Sort Strings: 2")
 print()
 print("Exit Program: 3")
 print()

 # Ask the user to enter his choice for bubble sort sub-page
 # Exception Handling
 try:

  # Ask the user to enter a choice for bubble sort sub-page
  choice_bubble_sort = int(input("Please Enter A Choice From The Above Choices: "))

 # If users anything character except of integers
 except ValueError:

  # Outputs appropriate message
  print()
  print("Please Enter Integer Values Only!")
  print()

 # Provides Corresponding Respond To User Choice
 if choice_bubble_sort == 1:

  print()
  print("Array Before Bubble Sort:")
  print()

  # Calling function "display_num" to display the contents of array "num"
  # This is to show the user what the array looked like BEFORE applying Bubble Sort
  display_num()

  print()
  print("Array After Bubble Sort:")

  # Calling the function "Bubble_Sort_Number" to arrange the numbers in ascending order

  BubbleSort_Number(num)

  print()

  # Displaying the array again
  # This is show the user what the array looks AFTER applying Bubble Sort

  display_num()

  print()

 elif choice_bubble_sort == 2:

  print()
  print("Array Before Insertion Sort:")
  print()

  # Calling function "display_anime" to display the contents of array "anime"
  # This is to show the user what the array looked like BEFORE applying Insertion Sort

  display_anime()

  print()
  print("Array After Insertion Sort:")

  # Calling the function "BubbleSort_Anime" to arrange the numbers in ascending order
  BubbleSort_Anime(anime)

  print()

  # Displaying the array again
  # This is show the user what the array looks AFTER applying Insertion Sort

  display_anime()

  print()

 else:

  # Exits program entirely
  print()
  print("Exiting Program")
  print()

  exit

# Function with identifier name "LinearSearch_Number" which will search for a value in array "num"
# Function "LinearSearch_Number" will perfom the calculation

def LinearSearch_Number(num):

 # A variable that will be used to use in for LinearSearch_Number
 # Exception Handling

 try:

  # Ask the user to enter a value to search
  Linear_Input_Number = int(input("Please Enter A Value To Search: "))

 except ValueError:

  print()
  print("Please Enter Integer Values!")
  print() 

 # Calculating the length of array "num"
 length_array = len(num)

 # Stepping through the num
 for i in range(0, length_array):

  # If "value" is found
  if num[i] == Linear_Input_Number:

   # It returns the Address of the array
   return i

 # If "Linear_Input_Num" has not been found
 # "return - 1" == Error / Not Found
 return - 1

# Function with identifier name "LinearSearch_String" which will search for a value in array "anime"
# Function "LinearSearch_String" will perfom the calculation
def LinearSearch_String(anime):

 # A variable that will be used to use in for LinearSearch_String
 # Exception Handling
 try:

  # Ask the user to enter a value to search
  Linear_Input_String = str(input("Please Enter A Value To Search: "))

 except ValueError:

  print()
  print("Please Enter Integer Values!")
  print()

 # Calculating the length of array "anime"
 length_array = len(anime)

 # Stepping through the array "anime"
 for i in range(0, length_array):

  # If "value" is found
  if anime[i] == Linear_Input_String:

   # It returns the Address of the array
   return i

 # If "Linear_Input_String" has not been found
 # "return - 1" == Error / Not Found
 return - 1

# Linear Search ( Sub-Page )
# Function with identifier name "LinearSearch" will be our sub page ( for linear search )
def LinearSearch():

 # Linear Search Main Page ( Overall sub page )
 print()
 print("Linear Search Sub Page")
 print()
 print("----------")
 print()
 print("Linear Search Integers: 1")
 print()
 print("Linear Search Strings: 2")
 print()
 print("Exit Program: 3")
 print()

 # Ask the user to enter his choice for linear search sub-page
 # Exception Handling
 try:

  # Ask the user to enter a choice for linear search sub-page
  choice_linear_search = int(input("Please Enter A Choice From The Above Choices: "))

 # If users anything character except of integers
 except ValueError:

  # Outputs appropriate message
  print()
  print("Please Enter Integer Values Only!")
  print()

 if choice_linear_search == 1:

  print("----------")
  print("Linear Search String")
  print("----------")

  # Calling the function "LinearSearch_Number" to allow user to search for value in array
  result_linear_number = LinearSearch_Number(num)

  # Output the "answer" of "LinearSearch_Number" in a appropriate message
  if result_linear_number != -1:

   # If "Linear_Input_Num" has been found
   print()
   print("Has been found at address: " + str(result_linear_number))
   print()

  else:

   # If "Linear_Input_Num" has NOT been found
   print()
   print("Has NOT been found!")
   print()

 elif choice_linear_search == 2:

  print("----------")
  print("Linear Search String")
  print("----------")

  # Calling the function "LinearSearch_String" to allow user to search for value in array
  result_linear_string = LinearSearch_String(anime)

  # Output the "answer" of "LinearSearch_String" in a appropriate message
  if result_linear_string != -1:

   # If "Linear_Input_Num" has been found

   print()
   print("Has been found at address: " + str(result_linear_string))
   print()

  else:

   # If "Linear_Input_Num" has NOT been found
   print()
   print("Has NOT been found!")
   print()

 else:

  # Exits program entirely
  print()
  print("Exiting Program")
  print()

  # Exits Program
  exit

# Function with identifier name "BinarySearch_Number" which will be used to allow the user to find a value in array "num"
def BinarySearch_Number(num, Binary_Input_Number):

 # It will return the function "BinarySearch_Number_Calc" which perform the "searching" function
 return BinarySearch_Number_Calc(num, 0, len(num), Binary_Input_Number)

def BinarySearch_Number_Calc(num, lower, upper, Binary_Input_Number):

 # Condition to enter "while" loop
 while lower <= upper:

  # Calculate the middle ( address ) of array "num"
  mid = (lower + upper) // 2

  # Searching for the value
  if num[mid] == Binary_Input_Number:

   # It will return the address of the searched value
   return mid

  # If value to search is NOT found
  # If value to be found is less than the value at mid
  elif num[mid] < Binary_Input_Number:

   # Cuts the BOTTOM half of the array
   # Only upper part is now left
   lower= mid + 1

  else:

   # Cut the TOP half of the array as
   # value to be found is greater than the value at mid
   # Only lower part is not left
   upper = mid - 1

 # If "Binary_Input_Number" has not been found
 return - 1

# Function with identifier name "BinarySearch_String" which will be used to allow the user to find a value in array "anime"
def BinarySearch_String(anime, Binary_Input_String):

 # It will return the function "BinarySearch_Number_Calc" which perform the "searching" function
 return BinarySearch_String_Calc(anime, 0, len(num), Binary_Input_String)

def BinarySearch_String_Calc(anime, lower, upper, Binary_Input_String):

 # Condition to enter "while" loop
 while lower <= upper:

  # Calculate the middle ( address ) of array "anime"
  mid = (lower + upper) // 2

  # Searching for the value
  if anime[mid] == Binary_Input_String:

   # It will return the address of the searched value
   return mid

  # If value to search is NOT found
  # If value to be found is less than the value at mid
  elif anime[mid] < Binary_Input_String:

   # Cuts the BOTTOM half of the array
   # Only upper part is now left
   lower= mid + 1

  else:

   # Cut the TOP half of the array as
   # value to be found is greater than the value at mid
   # Only lower part is not left
   upper = mid - 1

 # If "Binary_Input_String" has not been found
 return - 1

# Binary Search ( Sub-Page )
# Function with identifier name "BinarySearch" will be our sub page ( for binary search )
def BinarySearch():

 # Binary Search Main Page ( Overall sub page )
 print()
 print("Binary Search Sub Page")
 print()
 print("----------")
 print()
 print("Binary Search Integers: 1")
 print()
 print("Binary Search Strings: 2")
 print()
 print("Exit Program: 3")
 print()

 # Exception Handling
 try:

  # Ask the user to enter a choice for binary search sub-page
  choice_binary_search = int(input("Please Enter A Choice From The Above Choices: "))

 # If users anything character except of integers

 except ValueError:

  # Outputs appropriate message
  print()
  print("Please Enter Integer Values Only!")
  print() 

 if choice_binary_search == 1:

  print("----------")
  print("Binary Search String")
  print("----------")

  # Remember, the array need to be sorted for binary search to work
  BubbleSort_Number(num)

  # Exception Handling
  try:

   # Displaying a little message so that the programmer writing this does not get lost
   print()
   print("User!, This is for Binary Search for Numbers")
   print()

   # Asking the user to enter a value to find in array "num"
   Binary_Input_Number = int(input("Please Enter A Value To Search: "))

  # If user enter any character other than integer values
  except ValueError:

   # Outputs appropriate message
   print()
   print("Please Enter Integer Values Only")
   print()

  # Calling the function "BinarySearch_Number" to allow user to search for value in array
  result_binary_number = BinarySearch_Number(num, Binary_Input_Number)

  # Output the "answer" of "LinearSearch_Number" in a appropriate message
  if result_binary_number != -1:

   # If "Binary_Input_Num" has been found
   print()
   print(str(Binary_Input_Number) + " has been found at address: " + str(result_binary_number))
   print()

  else:

   # If "Binary_Input_Num" has NOT been found
   print()
   print("Has NOT been found!")
   print()

 elif choice_binary_search == 2:

  print("----------")
  print("Binary Search String")
  print("----------")

  # Remember, the array need to be sorted for binary search to work
  BubbleSort_Anime(anime)

  # Exception Handling
  try:

   # Displaying a little message so that the programmer writing this does not get lost
   print()
   print("User!, This is for Binary Search for Strings")
   print()

   # Asking the user to enter a value to find in array "num"
   Binary_Input_String = str(input("Please Enter A Value To Search: "))

  # If user enter any character other than integer values
  except ValueError:

   # Outputs appropriate message
   print()
   print("Please Enter Integer Values Only")
   print()

  # Calling the function "LinearSearch_String" to allow user to search for value in array
  result_binary_string = BinarySearch_String(anime, Binary_Input_String)

  # Output the "answer" of "BinarySearch_String" in a appropriate message
  if result_binary_string != -1:

   # If "Binary_Input_Num" has been found
   print()
   print("Has been found at address: " + str(result_binary_string))
   print()

  else:

   # If "Binary_Input_Num" has NOT been found
   print()
   print("Has NOT been found!")
   print()

 else:

  # Exits program entirely
  print()
  print("Exiting Program")
  print()

  # Exits Program
  exit

# Start Of Program
# Main Program ( Main Page )

print("Computer Science Programming Project")
print()
print("Main Page")
print()
print("----------")
print()
print("Please Select From The Choices Below!")
print()
print("----------")
print()
print("Insertion Sort: 1")
print()
print("Bubble Sort: 2")
print()
print("Binary Search: 3")
print()
print("Linear Search: 4")
print()
print("Exit Program: 5")
print()

# Asking the user to enter a choice ( chooses from above )
# Exception Handling
try:

 # Ask the user to enter his "choice"
 choice = int(input("Please Enter A Choice From The Above Choices: "))

# If user enters anything else other than integer characters
except ValueError:

 # Outputs appropriate values
 print()
 print("Please Enter Integer Values Only!")
 print()

# Program Will Provide Corresponding Respond To User Choice
# User chooses "Insertion Sort"
if choice == 1:

 InsertionSort()

# User chooses "Bubble Sort"
elif choice == 2:

 BubbleSort()

# User chooses "Binary Search"
elif choice == 3:

 BinarySearch()

# User chooses "Linear Search"
elif choice == 4:

 LinearSearch()

elif choice == 5:

 # Exits program entirely
 print()
 print("Exiting Program")
 print()

 # Exits Program
 exit

else:

 print()
 print("Something Went Wrong!")
 print()

# S.Sunhaloo
