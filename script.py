import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

credentials = Credentials.from_service_account_file("credentials.json",scopes=scopes)
client = gspread.authorize(credentials)
sheet_id = "1jA9bxN9YNrEqZA_WQMBolywSyjpU4HPxVN1TAxPkdtg"

sheet = client.open_by_key(sheet_id).sheet1

# 1. DINAMIC SEARCHING SHEET SIZE, IMPORTANT ROWS AND COLUMNS
# 1.1. Searching first and last student row
firstRowIndex = int(sheet.find("Matricula").address[1])+1
lastRowIndex = 1

while True:
    tempIndex = 1
    tempCellValue = sheet.acell(f"A{tempIndex}").value
    
    while tempCellValue != None:
        tempIndex += 10
        tempCellValue = sheet.acell(f"A{tempIndex}").value
        
    while tempCellValue == None:
        tempIndex -= 1
        tempCellValue = sheet.acell(f"A{tempIndex}").value
        
    lastRowIndex = tempIndex
    break

# 1.2. Searching grade columns
firstGradeColumnLetter = sheet.find("P1").address[0]
secondGradeColumnLetter = sheet.find("P2").address[0]
thirdGradeColumnLetter = sheet.find("P3").address[0]

gradeColumnList = [firstGradeColumnLetter,secondGradeColumnLetter,thirdGradeColumnLetter]

# 1.3. Searching attendance, situation columns
attendanceColumnLetter = sheet.find("Faltas").address[0]
situationColumnLetter = sheet.find("Situação").address[0]

for currentRow in range(firstRowIndex,lastRowIndex+1):
    cellValueNumber = int(sheet.acell(f"{attendanceColumnLetter}{currentRow}").value)
    if (cellValueNumber > 15):
        sheet.update_acell(f"{situationColumnLetter}{currentRow}","Reprovado por Falta")