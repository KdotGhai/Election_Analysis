from re import X


"""
print("Hello World")

print(type(73.81))
print(type("Hello World"))
print(type('True'))
print(type(True))
x = (8 // 5) # This is floor Division: Essentially just like division but will retrun the lowest whole number only
print(x)
"""

counties = ["Arapahoe","Denver","Jefferson"]
#print(counties)

#print(counties[-1]) #Negative indexes are used to identify a list item's position relative to the end of the list.This will output Jefferson or any last index item regardless of length
                    #if we type print(counties[-3]) it will be same as print(counties[0]): "Arapahoe" 
List_length = len(counties)

#print(List_length) 

#counties.append("El Paso") #When Appending, it will attach to the end of a list, further info needed to append at a certain index
#print(counties)

#counties.insert(0,"Ghai")  simply testing the insert function for lists
#print(counties)

#counties.remove("El Paso") this will remove the first instance of "El paso" || will not remove duplicates

counties.insert(1,"El PAso")
counties.remove("Arapahoe")
counties[2]= "Denver"
counties[1]= "Jefferson"
counties.append("Arapahoe")
#print(counties)

#TUPLES : Similar to list but cannot changed
my_tuple = tuple() # This is one way of making a blank tuple
my_tuple = ( ) #Second method

counties_tuple = ("Arapahoe","Denver","Jefferson")

#print(counties_tuple[:2], counties_tuple[:-1]) #remember when you set endpoint using ":" is beginning, the nedpoint is excluded
# "counties_tuple[:2] "essentially reads as everything upto index[2] but excluding it || "counties_tuple[:-1]" reads everything but last index item

#Dictionary 
# is wrapped in "{}" squiggly brackets to indicate a dictionary has been made
#Each key is seperated by a comma
#the first word wrapped in quotes with colon is the "KEY"(Word)
#After the colon is the "VALUE"(Definition)
counties_dict = {'Arapahoe': 422829,
                 'Denver' :463353,
                 'Jefferson': 432438}
#print(counties_dict)
#print(counties_dict.items()) #This will list BOTH Key and Value
counties_dict.keys()#will show Key
counties_dict.values()#Will show Value
counties_dict['Arapahoe'] # Another Method of getting VAlUE is dictionary_name[key]

#List of Dictionaries(And manipulating them)
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#print(voting_data)
#print(len(voting_data))
voting_data.insert(1,{"county":"El Paso", "registered_voters":461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data[2] = {"county":"Denver", "registered_voters": 463353}
voting_data[1] = {"county":"Jefferson", "registered_voters": 432438}
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#print(voting_data)

'''
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
'''

'''
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
'''

'''
#to iterate through dictionary with for loop
#method 1
counties_dict = {"Arapahoe": 422829, 
                 "Denver": 463353, 
                 "Jefferson": 432438}

#for county in counties_dict:
   # print(county)

#method 2    
for county in counties_dict.keys():
    print(county)
    
#For iterating to get values
for voters in counties_dict.values():
    print(voters)
    
#********** For Both Key And Value
for county in counties_dict.items():
    print(county)

#Alternativ eKey and Value
for county, voters in counties_dict.items():
    print(county, voters)
'''

'''
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for i in range(len(voting_data)): # This will get County only which is the key
    
 #     print(voting_data[i]['county'])
 
 #Alternative for getting County only or key name is
for county_dict in voting_data:
        print(county_dict['county'])
      
for county_dict in voting_data: #For Value and Key
    for value in county_dict.values():
        print(value)
        
for county_dict in voting_data: #For the Entire Dictionary listed
    print(county_dict)
    
for i in range(len(voting_data)): # This will get Value only which is the Definitions
    
      print(voting_data[i]['registered_voters'])
      
#alternative for getting values from list of dictionary is 
for county_dict in voting_data:
    
     print(county_dict['registered_voters'])
'''

'''
# Using F-String with Dictionaries
# First example is standard method of output 
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# Second Method enacts f-string:
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.") #the entire line is converted to string thus not requiring "+" to join variables with string or individual conversion to string

# Multiline F-string(being used in a list)    
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"\nYou received {candidate_votes} number of votes.\n"
    f"The total number of votes in the election was {total_votes}.\n"
    #f"You received {candidate_votes / total_votes * 100}% of the total votes.")
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.") #here we are formatting the percentage to give more accurate answersimply adding ":.2f" for thousandth place
print(message_to_candidate)
'''

#Example using list of dictionaries(still part of F-string example and practice)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
               {"county":"Denver", "registered_voters": 463353}, 
               {"county":"Jefferson", "registered_voters": 432438}]
#method 1()
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")
#for i in voting_data:
 #   county_name= i['county']
  #  voters_registered = i['registered_voters']
   # print(county_name + " county has: " + str(voters_registered) + " registered voters." )
for county, voters in voting_data.items():
    print(f"{county} has: {voters} registered voters.")


################
#using csv files(reading them and writing in them)
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load, "r") as election_data: #the "r" inidcates that we only want to read the data from here
    # Print the file object.
     print(election_data)
'''
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w") # the "w" suggests we want to write in this data
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()
'''
#Cleaner Code to acces and write to file
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in Election\n---------------")
    txt_file.write("\nArapahoe \nDenver \nJefferson")
    '''
    # Write three counties to the file.(second method)
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")
    '''
    
    
    