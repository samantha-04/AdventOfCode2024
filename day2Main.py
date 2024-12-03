#reading file
file = open("input.txt", "r")
data = [list(map(int, line.split())) for line in file] #inputting data into a 2d array
unsafeReports = []

#---------- Problem 1 ---------#

# modified for use in problem 2. Determines if a row is safe
def isSafe(row):
    increasing = True
    decreasing = True

    for i in range(len(row) - 1):
        difference = row[i + 1] - row[i]

        # Check if gradual
        if not (1 <= abs(difference) <= 3):
            return False

        # Check increasing or decreasing consistency
        if difference > 0:
            decreasing = False
        elif difference < 0:
            increasing = False
    return increasing or decreasing

            
def compareData(data):
    safeReports = 0 #initial count of safe reports
    for row in data:
        if isSafe(row):
            safeReports += 1
        else:
            unsafeReports.append(row)

    return safeReports, unsafeReports


#---------- Problem 2 ---------#

def problemDampener(safeReports, unsafeReports):
 
    for row in unsafeReports:
        
        for i in range(len(row)):
            #creating a new row and deleting one element
            newRow = row.copy()
            del newRow[i]

            if isSafe(newRow):
                safeReports += 1
                break
    return safeReports

safeReports, unsafeReports = compareData(data)
print("The number of safe reports: ", safeReports)


safeReportsWithDampener = problemDampener(safeReports, unsafeReports)
print("The number of safe reports with the Problem Dampener: ", safeReportsWithDampener)

           
    