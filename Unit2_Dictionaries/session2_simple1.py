'''
Problem 1: Most Endangered Species
Imagine you are working on a wildlife conservation database. 
Write a function named most_endangered() that returns the species 
with the highest conservation priority based on its population.

The function should take in a list of dictionaries 
named species_list as a parameter. 
Each dictionary represents data associated with a species, 
including its name, habitat, and wild population. 
The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, 
return the species with the lowest index.
'''
def most_endangered(species_list):
    # return empty string for empty species list
    if species_list is None:
        return ""
    
    # intialize endangered variable to negative variables
    endangered_index = -100000
    population = -1
    
    # for loop through and replace variable 
    for each in range(len(species_list)):
        name = (species_list[each])['name']
        name_pop = (species_list[each])['population']
        
        # if population hasn't been updated yet, update it.
        if population < 0:
            endangered_index = each
            population = name_pop
        elif name_pop < population:
            endangered_index = each
            population = name_pop
        
    return (species_list[endangered_index])['name']
    
species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print("------ PROBLEM 1 -------")
print(most_endangered(species_list))

'''
Problem 2: Identifying Endangered Species
As part of conservation efforts, certain species are 
considered endangered and are represented by the string endangered_species. 

Each character in this string denotes a different endangered species. 

You also have a record of all observed species in a particular region, 
represented by the string observed_species. Each character in observed_species denotes 
a species observed in the region.

Your task is to determine how many instances of the observed species 
are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.
'''

def count_endangered_species(endangered_species, observed_species):
    # create an empty set 
    e_set = set()
    
    # for each character in one, add to set
    for endangered in endangered_species:
        e_set.add(endangered)
    
    # initialize a counter variable to 0
    counter = 0
    
    # find intersection of endagered species and observed species
    
    
    # for each character in observed_species
    for animal in observed_species:
        for each in e_set:
            if animal == each:
                counter += 1
                        
    #return the count
    return counter

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print("------PROBlEM 2 ________")
print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

'''
PROBLEM 3: NAVIGATING THE RESEARCH STATION

In a wildlife research station, each letter of the alphabet represents 
a different observation point laid out in a single row. 

Given a string station_layout of length 26 indicating the layout of these 
observation points (indexed from 0 to 25), you start your journey at the first observation point (index 0). 
To make observations in a specific order represented by a string observations, you need to move from one point to another.

The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|

Write a function that returns the total time
it takes to visit all the required observation points in the given order with one movement.
'''
def navigate_research_station(station_layout, observations):# initalize total time variable 
    total_time = 0
    current_index = 0
  
  # initialize a dictionary that attach each letter in station_layout to its index
    distance = {}
    for index, station in enumerate(station_layout):
        distance.update({ station : index })
        
    
  # enumerate through layout using nested loop 
    for char in observations:
        for index, station in enumerate(station_layout):
        # if found, add station count to distance
            if char == station:
                distance.update({char : index})
            if char == station and index == 0:
                distance.update({char : 1})
                
    # now we have all the letters and their locations 
  
  # find abs difference between each character
    print(distance)
  # store previous distance
    
    prev_dist = 0
    
    for letter, value in distance.items():
        total_time = abs(total_time - value)
      
    return total_time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print("-------- PROBLEM 3 -----")
print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))