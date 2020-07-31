import csv

%precision 2

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
mpg[:3] # The first three dictionaries in our list.

len(mpg) # Size of the list

mpg[0].keys() # return the names of the columns

sum(float(d['cty']) for d in mpg) / len(mpg) #This is how to find the average cty fuel economy across all cars. All values in the dictionaries are strings, so we need to convert to float

sum(float(d['hwy']) for d in mpg) / len(mpg) #Similarly this is how to find the average hwy fuel economy across all cars.

cylinders = set(d['cyl'] for d in mpg) # Use set to return the unique values for the number of cylinders the cars in our dataset have

#Here's a more complex example where we are grouping the cars by number of cylinder, and finding the average cty mpg for each group.
CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

#Use set to return the unique values for the class types in our dataset.
vehicleclass = set(d['class'] for d in mpg) # what are the class types
vehicleclass

#And here's an example of how to find the average hwy mpg for each class of vehicle in our dataset.
HwyMpgByClass = []

for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterate over all dictionaries
        if d['class'] == t: # if the cylinder amount type matches,
            summpg += float(d['hwy']) # add the hwy mpg
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
HwyMpgByClass