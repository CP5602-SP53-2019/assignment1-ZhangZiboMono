# This is the program for the Assignment1 Task 1, it contains rNGeneration function and saveToFile function. This program is used for generating non-unique ranmdom numbers or unique random numbers and save the result into a file.

import random # Prepare for the random generator
import re # Prepare for the validation
import time # Prepare for the time spend calculation

lowerLimit = -35500 # The variable of lower limit, users can chenge the value here
upperLimit = 36600 # The variable of upper limit, users can chenge the value here
numOfValues = 50000 # The variable of number of random value, users can chenge the value here
noDuplicates = "t" # The variable of the unique switch's status, users can change the value here ("T","t","F" or "f")

def saveToFile(_resStr, _fileName): # The function to save file on your desktop and takes 2 parameters whcich are the content to save and the file name
   file = open(_fileName, mode = "w", encoding = "utf-8") # Mode is "w", which means old files will be overwritten
   file.write(_resStr)
   print("*------------------------*\nRandom number has been generated successfully, please check your desktop :)\n------------------------")
   file.close

def rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates): # The function to generate a series unique or non-unique random numbers with a certain range
   limit = re.compile(r'^[-+]?[0-9]+$') # For the validation
   if limit.match(str(lowerLimit)) == None or limit.match(str(upperLimit)) == None or str(numOfValues).isdigit() == False or not(noDuplicates == "T" or noDuplicates == "t" or noDuplicates == "F" or noDuplicates == "f"): # Check the limit variables must be integers and numOfValues must be positive integer and noDuplicates must be "T", "t", "F or "f"
      if limit.match(str(lowerLimit)) == None:
         print("Invalid input of '"+str(lowerLimit)+"', the parameter lowerLimit must be an integer.\n")
      else:
         pass
      if limit.match(str(upperLimit)) == None:
         print("Invalid input of '"+str(upperLimit)+"', the parameter upperLimit must be an integer.\n")
      else:
         pass
      if str(numOfValues).isdigit() == False:
         print("Invalid input of '"+str(numOfValues)+"', the parameter numOfValues must be an positive integer.\n")
      else:
         pass
      if not(noDuplicates == "T" or noDuplicates == "t" or noDuplicates == "F" or noDuplicates == "f"):
         print("Invalid input of '"+str(noDuplicates)+"', the parameter noDuplicates must be 'T', 't', 'F' or 'f'.\n")
      else:
         pass
      return
   elif lowerLimit >= upperLimit: # Check the lower limit must be less or equal to upper limit
      print("Invalid input, the parameter lowerLimit cannot be gearter than parameter upperLimit.\n")
      return
   elif numOfValues > (upperLimit - lowerLimit + 1) and (noDuplicates == "T" or noDuplicates == "t"): # Check the numOfValues cannot be bigger than the range of limit when the user want unique numbers
      print("Invalid input, the parameter numOfValues cannot be bigger than the range of limit when you want unique random numbers.")
      return
   elif noDuplicates == "F" or noDuplicates == "f": # Generate non-unique numbers
      resStr = ""
      for i in range(numOfValues):
         res = random.randint(lowerLimit, upperLimit)
         resStr += str(res) + "\n"
      saveToFile("lowerLimit: "+str(lowerLimit)+"\nupperLimit: "+str(upperLimit)+"\nnumOfValues: "+str(numOfValues)+"\nnoDuplicates: "+noDuplicates+"\n\n"+resStr,"Desktop/RandomNum_non-unique.txt")
      print("The algorithm spent {:.2f}s.\n*------------------------*".format(time.time()-startTime)) # Print the time spending
   else: # Generate unique numbers
      resStr = ""
      resLis = []
      while len(resLis) < numOfValues:
         res = random.randint(lowerLimit, upperLimit)
         if res in resLis:
            pass
         else:
            resStr += str(res) + "\n" # Use for printing in the file
            resLis.append(res) # Use for duplicates check
      saveToFile("lowerLimit: "+str(lowerLimit)+"\nupperLimit: "+str(upperLimit)+"\nnumOfValues: "+str(numOfValues)+"\nnoDuplicates: "+noDuplicates+"\n\n"+resStr,"Desktop/RandomNum_unique.txt")
      print("The algorithm spent {:.2f}s.\n*------------------------*".format(time.time()-startTime)) # Print the time spending

startTime = time.time() # Mark the start time at the beginning
rNGenerator(lowerLimit,upperLimit,numOfValues,noDuplicates) # Call the main function