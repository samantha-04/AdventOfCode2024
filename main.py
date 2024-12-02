
#creating arrays for each list
list1 = []
list2 = []

#--------------- PROBLEM 1 ----------------#
def parseList():
    
    input = open("input.txt", "r")

    for line in input:

        col1, col2 = line.strip().split() #splitting each line at the whitespace

        list1.append(int(col1))
        list2.append(int(col2))
    

def bubbleSort(array):
    for i in range(len(array)): #for the length of the array
        for j in range(0, len(array) - i - 1): #compare each element
            
            if array[j] > array[j + 1]:

                #swapping
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


def compareDistance(array1, array2):
    sum = 0
    for i in range(len(array1)): #for the length of array 1
        difference = abs(array1[i] - array2[i])
        sum += difference

    print("The sum of the distances is: ", sum)

    
parseList()
bubbleSort(list1)
bubbleSort(list2)
compareDistance(list1, list2)

#--------------- PROBLEM 2 ----------------#

def similarityScore(array1, array2):
    similarity = 0
    for i in range(len(array1)):
        count = 0
        for j in range(len(array2)):
            if (array1[i] == array2[j]):
                count += 1 #keeping track of how many times the number appears in list 2
               
        increase = count * array1[i]
        similarity += increase #increassing similarity score
        
    print("The similarity score is: ", similarity)

 
similarityScore(list1, list2)   
    
