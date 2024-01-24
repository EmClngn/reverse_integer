# Write a Program to extract each digit from an integer in the reverse order with a space separating them

# pseudo code

# ask user for number input
number = input("What is your desired number?: ")

reverse  = ""
# use for loop to reverse the numbers
for i in range (len(number), 0, -1):
    reverse += number[i - 1] + " "
print(reverse)
  

