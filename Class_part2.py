import arcpy
from arcpy import env

env.workspace = r'H:\PythonGIS\Ledesma\data\data\geoportal.gdb'

arcpy.CreateFeatureclass_management(env.workspace, "inserPoint2", geometry_type = "Point", template = "Fire", spatial_reference = "Fire" )

#file 3

inX = 790000
inY = 325367

fc = "InsertPoint2"
colname = "FACILITY_ZIP"
inPoint = arcpy.Point(inX, inY)

rowInserter = arcpy.InsertCursor(fc)
newIncident = rowInserter.newRow()

NewIncident.SHAPE = inPoint
newIncident.setValue(colname, "value Inserted")

rowInserter.insertRow(newincident)



