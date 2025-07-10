'''
Problem 1: Building a Playlist
The assignment statement to the top_hits_2010s variable below creates the 
linked list Uptown Funk -> Party Rock Anthem -> Bad Romance. 

Break apart the assignment statement into multiple lines with one call 
to the Node constructor per line to recreate the list.
'''
class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
		
top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

'''
Problem 2: Top Artists
Given the head of a linked list playlist, 
return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. 
Define your variables and provide a rationale for why you 
believe your solution has the stated time and space complexity.

'''

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
	# create freq  map
    artist_freq = {}
 
    # move threough map
    current = playlist
    while current:
        artist_freq[current.artist] = artist_freq.get(artist_freq.get(current.artist), 0) + 1
        current = current.next

print("problem 2")
playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

get_artist_frequency(playlist)

'''

'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head.next
    while current:
        if current.song == song:
            current = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))

'''
Problem 4: On Repeat
A variation of the two-pointer technique introduced in previous units is 
to have a slow and a fast pointer that increment at different rates.

We would like to check whether our playlist loops or not. Given the head of a linked list playlist_head, 
return True if the playlist has a cycle in it and False otherwise. 
A linked list has a cycle if at some point in the list, the node’s next pointer 
points back to a previous node in the list.

Evaluate the time and space complexity of your solution.
Define your variables and provide a rationale for why you believe your solution
has the stated time and space complexity.
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
	# initalize slow and fast pointers
    slow = playlist_head
    fast = playlist_head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # if fast node is the same as slow node, its a cycle
        if slow == fast:
            return True
    
    return False  
    
    

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print("--------------problem 4")
print(on_repeat(song1))

'''
Problem 5: Looped
Given the head of a linked list playlist_head that may contain a cycle, 
use the fast and slow pointer method to return the length of the cycle. 
If the list does not contain a cycle, return 0.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale 
for why you believe your solution has the stated time and space complexity.
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
	# initalize slow and fast pointers
    slow = playlist_head
    fast = playlist_head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # if fast node is the same as slow node, its a cycle
        if slow == fast:
            counter = 1
            current = slow.next
            while current != slow:
                counter += 1
                current = current.next
                
            print(slow.song)
            print(fast.song)
            return counter
    
    return 0  
    
print("------problem 5")
song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))