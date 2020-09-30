import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 
        "https://www.googleapis.com/auth/drive"]
credential = "CREDENTIAL_JSON_FILE""

class Sheets:
    def __init__(self, spreadsheet_name, sheet_name):
        self.credential =  gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name(credential, scope))
        self.spreadsheet = self.credential.open(spreadsheet_name)
        self.work_sheet = self.spreadsheet.worksheet(sheet_name)
    def line_writer(self, data):
        """Data argument must be a list with str and int. Every position will be insert in a column"""
        if type(data) == list:
            self.work_sheet.append_row(data, value_input_option='USER_ENTERED')
        else:
            raise Exception("Data arguments must be a list with str and int")
    def reader(self):
        work_sheet = self.work_sheet.get_all_records()
        return work_sheet