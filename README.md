# usng
Steps completed to complete project

Folder structure
Created top-level folder usng_map finders with all data. The folder structure is the same as the ia.sharedgeo.net/index.html (aka Iowa) map except for the following changes to complete the project. 
In the data folder, the original iowa data is stored in its own folder iowa. Two other files have been added.
A new folder js was created that contains the javascript for the web map, and another file for the jquery.

Data Preparation
All data that is contained within the Iowa map was downloaded off the server and saved into their respective folders. In order to combine this map with the google fusion table on the USNG website, the following was completed:
The fusiontable spreadsheet was downloaded and cleaned:
In total, there were 490 records that represented areas, cities, counties and fire districts. After review, it was determined that there were unnecessary duplicates within the polygons.
210 centerpoints were eliminated
Duplicates were removed from: Monroe County, FL, Aransas TX, Calhoun TX, Dare NC, Dukes MA, Fairfax VA.
The records were divided into two:
Points (69) containing Fire Districts, Cities and Areas
Polygons (187) containing Counties and Parishes
Total of 256 records
Polygon layer preparation
Columns were cleaned and include the following:
A US Counties geoJSON dataset was downloaded from: eric.clst.org/tech/usgeojson
This dataset was joined to the polygon spreadsheet and saved as a new layer.
Point layer preparation
Columns were cleaned. 
Lat and Long columns were created that contain the centerpoint of each city and/or location based on the description.
