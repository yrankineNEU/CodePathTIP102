
'''
Problem 1: Manage Performance Stage Changes
At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

You are given a list changes of strings where each string represents a change action. The actions can be:

"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.
'''

def manage_stage_changes(changes):
  finalList = []
  poppedList = []
  
  for change in changes:
    changeArray = change.split()
    
    if changeArray[0] == "Schedule":
      finalList.append(changeArray[1])
    elif changeArray[0] == "Cancel" and len(finalList) > 0:
      popped = finalList.pop()
      poppedList.append(popped)
    elif changeArray[0] == "Reschedule" and len(poppedList) > 0:
      popped = poppedList.pop()
      finalList.append(popped)
    else:
      print("Invalid Keyword") 
      
  return finalList

# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 


'''
Problem 2: Queue of Performance Requests
You are organizing a festival and want to manage the queue of requests to perform. 

Each request has a priority. 
Use a queue to process the performance requests in the order they arrive but ensure 
that requests with higher priorities are processed before those with lower priorities. 

Return the order in which performances are processed.
'''
def process_performance_requests(requests):
    # initialize final list
    final_list = []
    priority_dict = {}
    sorted_list = []
    
    # create the dictionary of all numbers and values
    for priority, genre in requests:
        priority_dict.update({ priority : genre })
        sorted_list.append(priority)
        
    # sort the list
    sorted_list.sort(reverse = True)
    
    # get the values from the sorted_list
    for each in sorted_list:
        final_list.append(priority_dict[each])
    
    return final_list

# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))


"""
Problem 3: Collecting Points at Festival Booths
At the festival, there are various booths where visitors can collect points. Each booth has a specific number of points available. Use a stack to simulate the process of collecting points and return the total points collected after visiting all booths.

def collect_festival_points(points):
    pass
Example Usage:

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 
"""

def collect_festival_points(points):
    # initialize the total points
    total_points = 0

    # 
    for point in points:
       total_points += point

    return total_points

# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8])) 


def booth_navigation(clues):
    finalList = []
    
    for each in clues:
      if each == "back":
        if len(finalList) > 0:
          finalList.pop()
      else:
        finalList.append(each)
        
    return finalList
  
# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 

# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues)) 

'''
Problem 5: Merge Performance Schedules
You are organizing a cultural festival and have two performance schedules, schedule1 and schedule2, 
each represented by a string where each character corresponds to a performance slot. 
Merge the schedules by adding performances in alternating order, starting with schedule1. 
If one schedule is longer than the other, append the additional performances onto the end of the merged schedule.

Return the merged performance schedule.

''' 
def merge_schedules(schedule1, schedule2):
    # initalize final schedule
    final =[]
    
    ptr_1 = 0
    ptr_2 = 0
    
    # add letters to final list from both schedules as long as lengths are equal
    while ptr_1 < len(schedule1) and ptr_2 < len(schedule2):
        final.append(schedule1[ptr_1])
        final.append(schedule2[ptr_2])
        
        ptr_1 += 1
        ptr_2 += 1
        
    # if schedule 2 is shorter, keep adding letters from schedule 1
    while ptr_1 < len(schedule1):
        final.append(schedule1[ptr_1])
        ptr_1 += 1

        
    while ptr_2 < len(schedule2):
        final.append(schedule2[ptr_2])
        ptr_2 += 1

    
    return "".join(final)
        

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 

'''
Problem 6: Count Balanced Terrain Subsections
During your global expedition, you are analyzing a binary terrain string, terrain, 
where 0 represents a valley and 1 represents a hill.

You need to count the number of non-empty balanced subsections in the terrain. 
A balanced subsection is defined as a contiguous segment of the terrain where an 
equal number of valleys (0s) and hills (1s) appear, and all the 0s and 1s are grouped consecutively.

Your task is to return the total number of these balanced subsections. 
Note that subsections that occur multiple times should be counted each time they appear.
'''
def count_balanced_terrain_subsections(terrain):
  counter = 0
  
  # use a stack to pop from the end
  lst = []
  for each in terrain:
    lst.append(each)
    
  subsection = []

  while len(subsection) < 3 and len(lst) > 0:
      # if empty, add last two to subsection
      if len(subsection) < 2:
        subsection.append(lst.pop())
      
      elif len(subsection) == 2:
        if subsection[0] == subsection[1]:
          counter += 1
          subsection.clear()
        else: 
          subsection.remove(subsection[0])
    
  return counter
    

print(count_balanced_terrain_subsections("00110011")) 
print(count_balanced_terrain_subsections("10101"))