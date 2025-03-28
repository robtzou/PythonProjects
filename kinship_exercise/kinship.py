# Model Input : 'python kinship.py family.json Nora Avery' 
# Model Output: f'{iname}'s LCA to {cname} is {lca}'

# import statements: 
from argparse import ArgumentParser
import demjson3 as bujs # Backup if json fails
from json import load
from relationships import relationships # <- pre-defines combined path relationships.
import sys

class Person:
    """
 Representing a person from the family data

 Attr:
    name: the person’s name (a string)
    gender: the person’s gender (a string); should have one of the following values: 'f', 'm', 'n'
    parents: the person’s parents, if known (a list of instances of Person; may be empty)
    spouse: the person’s spouse, if applicable (an instance of Person, or None)
    
    """
    def __init__(self, name: str, gender: str, parents = None):
        self.name = name 
        self.gender = gender # should take a name and a gender as arguments
        self.parents = parents if parents else []
        self.spouse = None # create an attribute called parents 
                           # (set this equal to an empty list) and an attribute called spouse (set this equal to None).      
        
    def add_parent(self):
        return [parent.name for parent in self.parents]
    
    def set_spouse(self, partner):
        if not isinstance(partner, Person):
            raise TypeError("Spouse must an instance of a person.")
        self.spouse = partner
        partner.spouse = self # Checks for a relationship.

    def connections(self):
        cdict = {self: ""}  # dictionary of connections (cdict) only including direct partners one 'S' and parents 'P'
        queue = [self] # Queue containing only self initially, then adding in a spouse or parent(s)
        
        while len(queue) > 0:
            queue.append(self.name)
            person = queue[0]
            cdict[person] # personpath -> returns person parents
            personpath = []

            if cdict[person] not in self.parents: # executes if self.person's parent isn't on the dictionary
                personpath.append["P"] # adds P to personpath when parents aren't on list.
                queue.append(cdict[person]) # adds that persons parents onto the list
                queue.pop([0])
            
            elif "S" not in personpath and self.spouse == True and "S" not in cdict:
                queue.append(self.spouse)

        if len(queue) == 0:
                return "End of Queue."
            
    def relation_to(self):
        
        pass

class Family:
    """
    which will track all the people about whom you have relationship information
    
    """
    def __init__(self):
        pass   
    def relation(self):
        pass

def main():
    pass

def parse_args(family_file, relfile, name1, name2):
    family_file = "family.json"

    with open(family_file) as f:
        family_data = load(f)   
        pass

if __name__ == "__main__":
    parse_args
    main

    pass

