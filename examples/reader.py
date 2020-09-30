from Quick_Sheets import Sheets


#define your spreadsheet name and worksheet name and instanciate it
sheet = Sheets("My data", "Sheet1")
#run the reader method to return all data from a worksheet as a json list. The first row will automaticaly be set as header
data = sheet.reader()
print(data)