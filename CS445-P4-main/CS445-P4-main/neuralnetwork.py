import csv

#TRAIN
file = "trainset.csv"

fields = []
rows = []
rowCount = 0
with open(file, 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    
    fields = next(csvReader)
    for row in csvReader:
        rows.append(row)
    
    rowCount = csvReader.line_num
       
fieldCount = len(fields)

weights = [0.2]*fieldCount #CHANGE INITIAL WEIGHT VALUE
weights[0] = 0
t=3 #CHANGE T VALUE
stabilized = 0
iterations = 0
while(stabilized == 0 and iterations < 20): #CHANGE ITERATIONS VALUE
    stabilized = 1
    for i in range(0, rowCount-1):
    #for i in range(0, 50):   
        r = 0
        for j in range(1, fieldCount-1):
            r += float(rows[i][j]) * weights[j]
        
        actualVal = float(rows[i][fieldCount-1])
        
        #if r > t, but supposed to indicate 0   
        if((r >= float(t)) and (actualVal == 0)): 
            for k in range(1, fieldCount-1):
                columnVal = rows[i][k]
                if(int(columnVal) == 1):
                    weights[k] = weights[k] - 0.05 #CHANGE THIS VALUE
            stabilized = 0
                    
        #if r < t but supposed to indicate 1
        if((r <= float(t)) and (actualVal == 1)): 
            for k in range(1, fieldCount-1):
                columnVal = rows[i][k]
                if(int(columnVal) == 1):
                    weights[k] = weights[k] + 0.05 #CHANGE THIS VALUE
            stabilized = 0        
    iterations += 1
    
print(stabilized)
print(iterations)
print(weights)

#TEST 
testFile = "testset.csv"

testRows = []
testRowCount = 0
with open(testFile, 'r') as testcsvFile:
    testcsvReader = csv.reader(testcsvFile)
    
    for testrow in testcsvReader:
        testRows.append(testrow)
    
    testRowCount = testcsvReader.line_num  
   
tpCount = 0
fpCount = 0
fnCount = 0
tnCount = 0

for i in range(0, testRowCount):
    r = 0
    predictVal = 0
    for j in range(1, fieldCount-1):
        r += float(testRows[i][j]) * weights[j]
    
    if float(r) > float(t):
        predictVal = 1
    else:
        predictVal = 0
        
    #compare with actual value
    actualVal = int(testRows[i][fieldCount-1])
    
    #true positive
    if(predictVal == 1 and actualVal == 1):
        tpCount += 1
    
    #false positive
    if(predictVal == 1 and actualVal == 0):
        fpCount += 1
    
    #false negative
    if(predictVal == 0 and actualVal == 1):
        fnCount += 1
    
    #true negative
    if(predictVal == 0 and actualVal == 0):
        tnCount += 1

print("\n")       
print(tpCount)
print(fpCount)
print(fnCount)
print(tnCount)
print("CONFUSION MATRIX")
print("TPR = %f"%(tpCount/(tpCount+fnCount)))
print("TNR = %f"%(tnCount/(tnCount+fpCount)))
print("FPR = %f"%(fpCount/(fpCount+tnCount)))
print("PPV = %f"%(tpCount/(tpCount+fpCount)))


        
