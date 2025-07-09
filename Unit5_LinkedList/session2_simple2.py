'''
Problem 1: Mutual Friends
In the Villager class below, each villager has a friends attribute, \
which is a list of other villagers they are friends with.

Write a method get_mutuals() that takes one parameter, 
a Villager instance new_contact, and returns a list with the name of 
all friends the current villager and new_contact have in common.
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        # initialize list of names
        mutuals = []
        
        # get list of self friends and new contact friends
        self_set = set(self.friends)
        new_set = set(new_contact.friends)
        
        # get intersection
        mutual_set = self_set & new_set
        
        for each in mutual_set:
            mutuals.append(each.name)
        
        return mutuals
    
    
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))

'''
Problem 2: Linked Up

Connect the provided node instances below to create 
the linked list kk_slider -> harriet -> saharah -> isabelle.

A function print_linked_list() which accepts the head, or 
first element, of a linked list and prints the values of the list has also been provided for testing purposes.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print_linked_list(kk_slider)

'''
Problem 3: Daily Tasks


'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def add_first(head, task):
    # initalize new head node with new next
    new_head = Node(task, head)
    
    return new_head
    
    
task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))


'''
Problem 4: Halve List
Write a function halve_list() that accepts the head of a 
linked list whose values are integers and divides each value by two. Return the head of the modified list.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def halve_list(head):
    # initalize current pointer
    curr = head
    
    while curr is not None:
        curr.value = curr.value / 2
        curr = curr.next
        
    return head
    
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))
    
    
'''
Problem 5: Remove Last
Write a function delete_tail() that accepts the head of a linked list and removes the last node in the list. 

Return the head of the modified list.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_tail(head):
    curr = head
    while curr.next.next is not None:
        curr = curr.next
        
    curr.next = None
    
    return head

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))

'''
Problem 6: Find Minimum in Linked List
Write a function find_min() that takes in the head of a linked list 
and returns the minimum value in the linked list. 

You can assume the linked list will contain only numeric values.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_min(head):
    # Initalize minimum variable
    min_value = head.value
    
    curr = head
    
    # Loop through all values
    while curr is not None:
        if min_value > curr.value:
            min_value = curr.value
        curr = curr.next
    
    return min_value

head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))

'''
Problem 7: Remove From Inventory

'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_item(head, item):
    curr = head
    
    # check head
    if curr.value == item:
        return curr.next
    
    while curr.next is not None:
        # peek ahead 
        if curr.next.value == item:
            # remove item
            if curr.next.next == None:
                curr.next == None
            else:
                curr.next = curr.next.next
                
        curr = curr.next

    return head

slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))