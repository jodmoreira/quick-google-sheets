from Quick_Sheets import Sheets


#define your spreadsheet name and worksheet name and instanciate it
sheet = Sheets("My data", "Sheet1")
#define a list to write. Every item on a list is one column. Itms can't be float numbers
sheet.line_writer('column one value')