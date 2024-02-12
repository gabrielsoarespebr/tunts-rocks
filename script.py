import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

credentials = Credentials.from_service_account_file("credentials.json",scopes=scopes)
client = gspread.authorize(credentials)
sheet_id = "1jA9bxN9YNrEqZA_WQMBolywSyjpU4HPxVN1TAxPkdtg"

sheet = client.open_by_key(sheet_id).sheet1

firstRowIndex = 4
lastRowIndex = 27

gradeColumnList = ["D","E","F"]
attendanceColumnLetter = "C"

situationColumnLetter = "G"

for currentRow in range(firstRowIndex,lastRowIndex+1):
    cellValueNumber = int(sheet.acell(f"{attendanceColumnLetter}{currentRow}").value)
    if (cellValueNumber > 15):
        sheet.update_acell(f"{situationColumnLetter}{currentRow}","Reprovado por Falta")