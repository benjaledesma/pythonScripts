import arcpy
from arcpy import env
env.workspace = 'C:\data' 

fc = 'us_major_cities.shp'

# Cursor considering Population and some of the sub classes 
cursor= arcpy.da.SearchCursor(fc, ['POPULATION','WHITE','BLACK','ASIAN','MALES','FEMALES','AGE_25_34'])

#List to storage population values
P=[]
#Intial variables to start summation 
W=0
B=0
A=0
M=0
F=0
A25_34=0

#Loop for getting the values
for row in cursor:
    P.append(row[0])
    W = W+row[1]
    B = B+row[2]
    A = A+row[3]
    M = M+row[4]
    F = F+row[5]
    A25_34 = A25_34+row[6]

#Printing 
print 'The average population per city is: '+str(sum(P)/len(P)) + ' inhabitants'
print str(round(((float(W)/sum(P))*100),2))+'% of the population is white'
print str(round(((float(B)/sum(P))*100),2))+'% of the population is black'
print str(round(((float(A)/sum(P))*100),2))+'% of the population is asian'
print str(round(((float(M)/sum(P))*100),2))+'% of the population are males'
print str(round(((float(F)/sum(P))*100),2))+'% of the population are females'
print str(round(((float(A25_34)/sum(P))*100),2))+'% of the population is between 25 and 34 year old'




