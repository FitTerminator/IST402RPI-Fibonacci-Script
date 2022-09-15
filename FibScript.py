class test:
pass
num1 = 0
num2 = 1
counter = 0
try:
print("Welcome to my Fibonacci script. How many numbers do you want 
displayed: ")
nums = int(input())
except ValueError as error:
        exit(print("\nInvalid inputs: blank space and letters. Restart the script 
and try again."))
if nums <= 0:
print("\nThat number isn't positive... we don't do that here. Restart the 
script and try again.")
elif nums == 1:
print("\nReally? Only one number? Okay... fine:")
print(num1)
else:
print("\nHere are your new numbers:")
while counter < nums:
new = num1 + num2
num1 = num2
num2 = new
counter += 1
print(num1)
