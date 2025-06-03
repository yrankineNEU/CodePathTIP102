# Unit 1.1
# Adv. Set 1

# Problem 1: Hunny Hunt
# Write a function linear_search() to help Winnie the Pooh locate his lost items. 
# The function accepts a list items and a target value as parameters.
# The function should return the first index of target in items, 
# and -1 if target is not in the lst. Do not use any built-in functions.

def linear_search(lst, target):
	
 # Loop through all the items in the list using its index
	for index in range(len(lst)):
     # if the target word matches the current word in list, return target
		if target == lst[index]:
			return target

	# if all else fails, return -1
	return -1
			
  
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
result = linear_search(items, target)		

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
result_2 = linear_search(items, target)
print(result_2)

# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# Tigger has developed a new programming language Tiger with only four operations 
# and one variable tigger.

# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Given a list of strings operations containing a list of operations, 
# return the final value of tigger after performing all the operations.

def final_value_after_operations(operations):
	# Initially, the value of tigger is 1 because he's the only tigger around! 
	tigger = 1
 
	for word in operations:
		if word == "bouncy" or word == "flouncy":
			tigger+=1
		elif word == "trouncy" or word == "pouncy":
			tigger-=1

	return tigger


# Test Case #1
operations = ["trouncy", "flouncy", "flouncy"]
actual = final_value_after_operations(operations)
expected = 2

print(f"Expect value: ", expected, "|| Actual: ", actual)

# Test Case #2
operations = ["bouncy", "bouncy", "flouncy"]
actual = final_value_after_operations(operations)
expected = 4

print(f"Expect value: ", expected, "|| Actual: ", actual)
