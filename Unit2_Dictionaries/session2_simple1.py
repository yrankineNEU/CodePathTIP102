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
    
    # intialize endangered variable
    endangered = 0
    population = 0
    
    # for loop through and replace variable 
    for each in range(len(species_list)):
        name = (species_list[each])['name']
        name_pop = (species_list[each])['population']
        
        if name_pop < population:
            endangered = each
            population = name_pop
        print(population)
        
    return (species_list[endangered])['name']
    
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
    print("------PROB 2")
    # edge case if empty
    if observed_species is None:
        return 0
    
    # .find for the exact pair
    print(endangered_species in observed_species)
 
    
    # return number of endagered species

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  