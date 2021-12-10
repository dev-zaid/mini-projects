import random

"""
studentList.txt contains the student names arranged roll.no wise
groupResults.txt holds the list of groups
"""

studentNames = open("studentList.txt").readlines() 
groupResults = open("groupResults.txt","w")

numberOfStudents = 74
groupArray = list(range(1,numberOfStudents+1))   
nonParticipants = [2,11,49,55,58,63] # Array of roll no. that are not participating
participantsPerGroup = 5 # No. of participants per group 

# Removes non-participants from the groupArray
for i in nonParticipants:
    groupArray.remove(i)

random.shuffle(groupArray) # Shuffle the array

counter = 1
while len(groupArray) >= 1:
    groupResults.write("Group "+str(counter)+"\n")

    try:
        # Splitting the groups
        group =  groupArray[:5]
        del groupArray[:5]

        # Writing the teams into the file
        for i in group:
            groupResults.write(studentNames[i-1])
        groupResults.write("\n")
        counter += 1

    except(IndexError):
        # To write the last team
        for i in groupArray:
                groupResults.write(studentNames[i-1])
        break                       

groupResults.close()