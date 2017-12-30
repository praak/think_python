from math import pi

def sphere(r):
    volume = (4 * math.pi * (r**3)) / 3
    return volume

def totalshippingcost(numOfCopies, coverPrice, discountPercent, shippingCost1, shippingCost2):
    costOfBook = numOfCopies*coverPrice*(1-(discountPercent/100))
    totalShippingCost = shippingCost1 + (shippingCost2*(numOfCopies-1))
    return costOfBook + totalShippingCost

#not importing time library.
#Assuming running is done in a perfect loop such that at the end of the run person returns home without having to run back again
# no variable change for miles run at given pace. Assumed to run 1 mile - easy -- 3 miles temp -- 1 mile easy
def runningtime(initialHour, initialMinute,easyPace, tempPace):
    totalTimeSeconds = easyPace * 1 + tempPace * 3 + easyPace * 1

    timeMin = totalTimeSeconds/60
    timeHour = initialHour

    if (totalTimeSeconds%60)!= totalTimeSeconds:
        timeMin = totalTimeSeconds/60 + timeMin
        finalTimeSec = totalTimeSeconds%60
    else:
        finalTimeSec = totalTimeSeconds
    if (timeMin%60)!= timeMin:
        timeHour = timeMin/60 + initialHour
        print(timeHour)
        finalTimeMin = timeMin%60
    else:
        finalTimeMin = timeMin
    if (timeHour%12)!= timeHour:
        finalTimeHour = timeHour%12
    else:
        finalTimeHour = timeHour

    return [finalTimeHour,finalTimeMin,finalTimeSec]

print('Problem 1: \n')
r = int(input('Enter the Radius of the sphere: '))
volumeofsphere = sphere(r)
print "Volume of sphere with radius %d is %f. \n" %(r,volumeofsphere)

print('Problem 2: \n')
coverPrice = float(input('Enter Cover Price: '))
discountPercent = float(input('Enter Discount % out of 100: '))
shippingCost1 = float(input('Enter shipping cost for 1st copy: '))
shippingCost2 = float(input('Enter remaining shipping cost: '))
numOfCopies = int(input('How many copes?: '))
totalCost = totalshippingcost(numOfCopies,coverPrice,discountPercent,shippingCost1,shippingCost2)
print "Total wholesale cost for %d of copies = %f. \n" %(numOfCopies, totalCost)

print('Problem 3: \n')
initialHour = int(input('Initial Hour time: '))
initialMinute = int(input('Initial Minute time: '))
easyPaceMin = int(input('Easy pace Min: '))
easyPaceSec = int(input('Easy pace Sec: '))
tempoPaceMin = int(input('Easy pace Min: '))
tempoPaceSec = int(input('Easy pace Sec: '))
[timeHour,timeMin,timeSec] = runningtime(initialHour,initialMinute,(easyPaceMin*60+easyPaceSec),(tempoPaceMin*60+tempoPaceSec))
print "Breakfast time will be %d:%d:%d \n" %(timeHour,timeMin,timeSec)
