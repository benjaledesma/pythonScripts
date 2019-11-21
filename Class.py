import arcpy
fc = r"H:\PythonGIS\Ledesma\Hw9\us_major_cities\us_major_cities.shp"

where = '"POPULATION" > 950000'
where1 = """"NAME" = 'San Diego'""" 
where2 = """"NAME" Like 'S%'""" # % is ue like it can be any kind of character


#with arcpy.da.SearchCursor(fc,("NAME",),where_clause = where2) as cursor:
#    for row in cursor:
#        print row[0]

#with * you can access all the columns


###access using tokens as Shape@xy 
##with arcpy.da.SearchCursor(fc,("NAME","POPULATION", "SHAPE@XY"),where_clause = where2) as cursor:
##    for row in cursor:
##        print row[0] , row[1], row[2]
##
###
###access using tokens as Shape@xy 
##with arcpy.da.SearchCursor(fc,("NAME","POPULATION", "SHAPE@X"),where_clause = where2) as cursor:
##    for row in cursor:
##        print row[0] , row[1], row[2]

where3 = """"CAPITAL" = 'State'"""

with arcpy.da.UpdateCursor(fc,"CAPITAL",where3) as cursor:
    for row in cursor:
        row[0] = "State capital"
        cursor.updateRow(row)
