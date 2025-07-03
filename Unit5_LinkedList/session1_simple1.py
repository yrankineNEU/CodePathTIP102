# Session 1: Standard Ver. 1

'''
Problem 1: New Horizons
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing.
Store the instance in a variable named apollo.

The Villager object created should have the name "Apollo", the species "Eagle", 
and the catchphrase "pah".

# Instantiate your villager here
Example Usage:

Example Output:

Apollo
Eagle
pah
[]
'''
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
        
    # Problem 2
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    # Problem 4: Setter method
    def set_catchphrase(self, new_catchphrase):
		# Check if catchphrase is alpha with white spaces
        lst_phrase = new_catchphrase.split()
        
        # If len is greater than 20, return invalid
        if len(new_catchphrase) > 20:
            return "Invalid catchphrase"
        
        for each in lst_phrase:
            if not each.isalpha(): 
                print("Invalid catchphrase.")
                return
            
        # Update Catchphrase and return success message
        self.catchphrase = new_catchphrase
        print("Catchphrase updated.")
    
    # Problem 5: Add Furniture
    def add_item(self, item_name):
        # initialize valid furniture names
        valid_furniture = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
         
        if item_name in valid_furniture and item_name not in self.furniture: 
            self.furniture.append(item_name)
    
    # Problem 6: Print Inventory
    def print_inventory(self):
        if self.furniture is None:
            print("Inventory is empty")

        # add to dictionary
        f_dict = {}
                
        for each in self.furniture:
            if each in f_dict:
                f_dict[each] += 1
            else:
                f_dict[each] = 1        
        print(f_dict)
        

apollo = Villager("Apollo", "Eagle", "stern", "pah")

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 


'''
Problem 2: Greet Player
Step 1: Using the Villager class from Problem 1, add the following greet_player() 
method to your existing code:

def greet_player(self, player_name):
    return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
Step 2: Create a second instance of Villager in a variable named bones.

The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
Step 3: Call the method greet_player() with your name and print out
"Bones: Hey there, <your name>! How's it going, yip yip!". 
For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" 
would be printed out to the console.

Example Usage:

print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture) 
Example Output:

Bones
Dog
yip y
'''
# Create a second villager named bones
bones = Villager("Bones", "Dog", "dark", "yip yip")

print(bones.greet_player("Yana"))

'''
Problem 3: update catch phrase
'''
bones.catchphrase = "ruff it up"
print(bones.greet_player("Yana"))

'''
Problem 4: Setter methods
Update your Villager class with a method set_catchphrase() 
that takes in one parameter new_catchphrase.

If new_catchphrase is valid, it should update the villager's catchphrase attribute 
to have value new_catchphrase and print "Catchphrase updated".
Otherwise, it should print out "Invalid catchphrase".
Valid catchphrases are less than 20 characters in length. 

They must all contain only alphabetic and whitespace characters.

Example Usage:


Example Output:

Example 1:
Catchphrase Updated!
sweet dreams
Invalid catchphrase
'''
alice = Villager("Alice", "Koala", "cute", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

'''
Problem 5: Add Furniture

Update the Villager class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the players furniture attribute.
The method does not need to return any values.
'''
alice = Villager("Alice", "Koala", "cute", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

'''
Problem 6: Print Inventory

The method should print the name and quantity of each item in a villager’s furniture list.

The name and quantity should be in the format 
"item1: quantity, item2: quantity, item3: quantity" 
for however many unique items exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".
'''

alice = Villager("Alice", "Koala", "cute", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
print(alice.furniture)
alice.print_inventory()

'''
Problem 7: Personality groups
'''
# Problem 7: Group by personality 
def of_personality_type(townies, personality_type):
    # Check if townies list is empty
    if townies is None:
        return "No townies is listed."
        
    # initalize result list
    result = []
        
    # loop through townie and add match to list
    for each in townies:
        if each.personality is personality_type:
            result.append(each.name)
        
    # return result list
    return result


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))

'''
Problem 8: Telephone
The Villager constructor has been updated to include an additional attribute neighbor. 
A villager's neighbor is another Villager instance and represents their closest neighbor. 
By default, a Villager's neighbor is set to None.

Given two Villager instances start_villager and target_villager, 
write a function message_received() that returns True if you can pass a message 
from the start_villager to the target_villager through a series of neighbors and False otherwise.
'''

    # Print 8 : set neighbor
def message_received(start_villager, target_villager):
    # Return false if start_villager has no neighbors
    if start_villager.neighbor is None:
        return False
        
    # Check the neighbor of each neighbor and if target villager reach, then return true
    while start_villager.neighbor is not None:
        if start_villager.neighbor == target_villager:
            return True
        else:
            start_villager = start_villager.neighbor

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))

'''
Problem 9: LinkedList
Using the provided Node class below, create a linked list Tom Nook -> Tommy where the instance 
tom_nook has value "Tom Nook" which points to the instance tommy that has value "Tommy".
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next        
    
tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy 
print(tom_nook.value) 
print(tom_nook.next.value) 
print(tommy.value) 
print(tommy.next) 

'''
Problem 10: Timmy and Tommy
In a linked list, pointers can be redirected to any place in the list.

Using the linked list from Problem 9, create a new Node timmy with value "Timmy" 
and place it between tom_nook and tommy so the new linked list is tom_nook -> timmy -> tommy.
'''

timmy = Node("Timmy")
timmy.next = tommy
tom_nook.next = timmy

print(tom_nook.value)
print(tom_nook.next.value)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next)

'''
Problem 11: Saharah
Using the linked list from Problem 10, remove the tom_nook node and add in a node saharah with 
value "Saharah" to the end of the list so that the resulting list is timmy -> tommy -> saharah.
'''

saharah = Node("Saharah")
tommy.next = saharah
tom_nook.next = None

print(" ------------ PROBLEM 11 ---")
print(tom_nook.next) 
print(timmy.value) 
print(timmy.next.value)  
print(tommy.value) 
print(tommy.next.value)
print(saharah.value)  
print(saharah.next) 

'''
Problem 12: Print List
Write a function print_list() that takes in the head of a linked list 
and returns a string linking together the values of the list with the separator "->".

Note: The "head" of a linked list is the first element in the linked list. 
Equivalent to lst[0] of a normal list.
'''

def print_list(villager):
    lst = []
    
    lst.append(villager.value)
    while villager.next is not None:
        lst.append(villager.next.value)
        villager = villager.next
    
    return " -> ".join(lst)
        

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))