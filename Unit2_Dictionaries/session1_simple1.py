# Unit 2 - Dictionaries
# Standard Problem Set Version 1

'''
Problem 1: Festival Lineup
Given two lists of strings artists and set_times of length n, write 
a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. 
Assume i <= 0 < n and len(artists) == len(set_times).


Example Usage:
{"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
{}
'''
def lineup(artists, set_times):
    # if string is empty return empty dictionary
    if artists is None and set_times is None:
        return {}
    
    # initialize dictionary
    lineup_lst = {}
    
    # Add one at a time and remove from list
    for each in range(len(artists)):
        lineup_lst.update({artists[each] : set_times[each]})
    
    return lineup_lst

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))


'''
Problem 2: Planning App
You are designing an app for your festival to help attendees 
have the best experience possible! As part of the application, 
users will be able to easily search their favorite artist and find out the day, time, 
and stage the artist is playing at. 

Write a function get_artist_info() 
that accepts a string artist and a dictionary festival_schedule mapping artist's 
names to dictionaries containing the day, time, and stage they are playing on. 
Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, 
return the dictionary {"message": "Artist not found"}.

Example Output:

{'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
{'message': 'Artist not found'}
'''
def get_artist_info(artist, festival_schedule):
    # Initalize message
    message = {'message' : 'Artist not found'}
    
    # Handle if festival schedule is empty
    if festival_schedule is None:
        return message
    
    # Use get key 
    if festival_schedule.get(artist) != None:
        return festival_schedule.get(artist)
    else:
        return message

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  

'''
Problem 3: Ticket Sales
A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
Return the total number of tickets of all types sold.

Example Usage: 4500
'''
def total_sales(ticket_sales):
    # initialize sum
    sum = 0
    
    # check for no ticket sales
    if ticket_sales is None:
        return sum
    
    # loop through all values to add
    for sales in ticket_sales.values():
        sum += sales
        
    return sum
    

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
print(total_sales(ticket_sales))

'''
Problem 4: Scheduling Conflict
Demand for your festival has exceeded expectations, 
so you're expanding the festival to span two different venues. 

Some artists will perform both venues, while others will perform at just one. 
To ensure that there are no scheduling conflicts, implement a function identify_conflicts() 
that accepts two dictionaries venue1_schedule and venue2_schedule 
each mapping the artists playing at the venue to their set times. 

Return a dictionary containing the key-value pairs that are the same in each schedule.

Example Output:
{"Stromae": "9:00 PM", "HARDY": "7:00 PM"}
'''

def identify_conflicts(venue1_schedule, venue2_schedule):
    # returned dictionary of conflicts
    conflicts = {}
    
    # Nested loop for each venue
    for artist, time in venue1_schedule.items():
        for artist2, time2 in venue2_schedule.items():
            if artist == artist2 and time == time2:
                conflicts.update({ artist : time })
    
    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

'''
Problem 5: Best Set
As part of the festival, attendees cast votes for their favorite set. 
Given a dictionary votes that maps attendees id numbers to the artist 
they voted for, return the artist that had the most number of votes. 

If there is a tie, return any artist with the top number of votes.

Example Output:

SZA
Ethel Cain
'''
def best_set(votes):
    # intializing frequency 
    freq = {}
        
    # loop through dictionary and add frequency count
    for id, artist in votes.items():
        # If key not found, add artist name and freq count
        if freq.get(artist) is None: 
            freq.update({ artist : 1 })
        elif freq.get(artist) is not None:
            # update count
            freq.update({ artist : freq.get(artist) + 1 })

    # use max(dictionary name, key of value = dictionary.get)
    results = max(freq, key = freq.get)
    return results

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))

'''
Problem 6: Performances with Maximum Audience
You are given an array audiences consisting of positive integers 
representing the audience size for different performances at a music festival.

Return the combined audience size of all performances in audiences with the maximum audience size.

The audience size of a performance is the number of people who attended that performance.

Example Output:
250
440
'''
def max_audience_performances(audiences):
    freq = {}
    
     # Create a frequency list of audiences
    for each in audiences:
        if freq.get(each) is None: 
            freq.update({ each : 1 })
        else: 
            freq.update({ each : freq.get(each) + 1 })
    
    # Find the max value
    max_size = max(freq)
    
    # find frequency of max audience size
    max_freq = freq.get(max_size)
    
    sum_of_max = max_size * max_freq
                
    return sum_of_max

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

'''
Problem 7: Performances with Maximum Audience II
If you used a dictionary as part of your solution to max_audience_performances() 
in the previous problem, try reimplementing the function without using a dictionary. 

If you implemented max_audience_performances() without using a dictionary, 
try solving the problem with a dictionary.

Once you've come up with your second solution, compare the two. 
Is one solution better than the other? Why or why not?

Example Output:

250
440
'''
def max_audience_performances(audiences):
    # Find max in list
    max_value = max(audiences)
    
    # find frequency by looping through list 
    max_freq = audiences.count(max_value)
    
    return max_value * max_freq

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

'''
Problem 8: Popular Song Pairs
Given an array of integers popularity_scores representing the popularity scores 
of songs in a music festival playlist, return the number of popular song pairs.

A pair (i, j) is called popular if the songs have the same popularity score and i < j.

Hint: number of pairs = (n x n-1)/2

Example Output:

4
6
0
'''
def num_popular_pairs(popularity_scores):
    # lets try creating a frequency map 
    freq = {}
    
    for each in popularity_scores:
        value = 0
        # get count
        if freq.get(each) is None:
            value = 1
        else:
            value = freq.get(each) + 1
        
        # update value to dictionary
        freq.update({ each : value })
        
    # find count of scores
    score_count = []
    
    for score, freq_count in freq.items():
        if freq_count > 1:
            num_pairs = (freq_count * (freq_count - 1))/2
            score_count.append(num_pairs)
    
    total = 0
    
    # get sum of num_pairs
    for nums in score_count:
        total += nums
            
    return total

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 

'''
Problem 9: Stage Arrangement Difference Between Two Performances
You are given two strings s and t representing the stage arrangements of 
performers in two different performances at a music festival, 
such that every performer occurs at most once in s and t, and t is a permutation of s.

The stage arrangement difference between s and t is defined as the 
sum of the absolute difference between the index of the occurrence of 
each performer in s and the index of the occurrence of the same performer in t.

Return the stage arrangement difference between s and t.

A permutation is a rearrangement of a sequence. 
For example, [3, 1, 2] and [2, 1 , 3] are both permutations of the list [1, 2, 3].

Hint: Absolute value function
Example Output:
2
12
'''
def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
    # initialize dictionaries 
    dict_s = {}
    dict_t = {}
    
    sum = 0
    
    # create dictionary for each person and their index
    for index in range(len(s)):
         dict_s.update( {s[index] : index} )
    
    for index2 in range(len(t)):
         dict_t.update( {t[index2] : index2} )
    
    # compare indexes in both dictionary
    for s_name, s_spot in dict_s.items():
            t_spot = dict_t.get(s_name)
            
            # get abs difference
            sum += abs(s_spot - t_spot)
    
    # return sum
    return sum
            
s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
print(find_stage_arrangement_difference(s1, t1))

s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]
print(find_stage_arrangement_difference(s2, t2))

'''
Problem 10: VIP Passes and Guests
You're given strings vip_passes representing the types of guests that have VIP passes, 
and guests representing the guests you have at the music festival. 

Each character in guests is a type of guest you have. 
You want to know how many of the guests you have are also VIP pass holders.

Letters are case sensitive, so "a" is considered a different type of guest from "A".

Example Output:
3
0
'''
def num_VIP_guests(vip_passes, guests):
    # 1. Create an empty set called vip_set.
    vip_set = set()
    
    # 2. For each character in vip_passes, add it to vip_set.
    for char_vip in vip_passes:
        vip_set.add(char_vip)
    
    print(vip_set)
    # 3. Initialize a counter variable to 0.
    counter = 0
    
    # 4. For each character in guests:
    for each in guests:
        #    * If the character is in vip_set, increment the count by 1.
        if each in vip_set:
            counter += 1
    return counter

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))

'''
Problem 11: Performer Schedule Pattern
Given a string pattern and a string schedule, 
return True if schedule follows the same pattern. 
Return False otherwise.

Here, "follow" means a full match, such that there is a one-to-one correspondence between 
a letter in pattern and a non-empty word in schedule.

You are provided with a partially implemented and buggy version of the solution. 
Identify and fix the bugs in the code. 
Then, perform a thorough code review and suggest improvements.


Example Output:
True
False
False
'''
def schedule_pattern(pattern, schedule):
    
    # split each music genre in schedule into a list (genres)
    genres = schedule.split()
    
    # if the length of genres list matches the leng of the pattern string, return true
    if len(genres) == len(pattern):
        return True

    # initalize dictionaries 
    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] == genre:
                return True
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] == char:
                return True
        else:
            genre_to_char[genre] = char

    return False

pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))