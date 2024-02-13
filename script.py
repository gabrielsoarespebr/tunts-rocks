import math

import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

credentials = Credentials.from_service_account_file("credentials.json",scopes=scopes)
client = gspread.authorize(credentials)
sheet_id = "1jA9bxN9YNrEqZA_WQMBolywSyjpU4HPxVN1TAxPkdtg"

sheet = client.open_by_key(sheet_id).sheet1

# 1. RULES
# Note: The problem statement refers to grades from 0 to 10, but the Google Sheets table refers to grades from 0 to 100. Considering this difference, I will follow the 0-100 model.
gradeMinFinals = 50
gradeMinApproval = 70
absenceMax = 15

# 2. DINAMIC SEARCHING SHEET SIZE, IMPORTANT ROWS AND COLUMNS
# 2.1. Searching first and last student row
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

# 2.2. Searching grade columns
firstGradeColumnLetter = sheet.find("P1").address[0]
secondGradeColumnLetter = sheet.find("P2").address[0]
thirdGradeColumnLetter = sheet.find("P3").address[0]

gradeColumnList = [firstGradeColumnLetter,secondGradeColumnLetter,thirdGradeColumnLetter]

# 2.3. Searching attendance, situation, required grade columns
attendanceColumnLetter = sheet.find("Faltas").address[0]
situationColumnLetter = sheet.find("Situação").address[0]
requiredGradeColumnLetter = sheet.find("Nota para Aprovação Final").address[0]

# 3. MATHEMATICAL CALCULATIONS AND GOOGLE SHEETS UPDATE
for currentRow in range(firstRowIndex,lastRowIndex+1):   
    gradeArithmeticMean = (int(sheet.acell(f"{firstGradeColumnLetter}{currentRow}").value) + int(sheet.acell(f"{secondGradeColumnLetter}{currentRow}").value) + int(sheet.acell(f"{thirdGradeColumnLetter}{currentRow}").value))/3
    
    if gradeArithmeticMean >= 70:
        sheet.update_acell(f"{situationColumnLetter}{currentRow}","Aprovado")
        sheet.update_acell(f"{requiredGradeColumnLetter}{currentRow}",0)
    else:
        if gradeArithmeticMean >= 50:
            sheet.update_acell(f"{situationColumnLetter}{currentRow}","Exame Final")
            requiredGrade = math.ceil(100 - gradeArithmeticMean)
            sheet.update_acell(f"{requiredGradeColumnLetter}{currentRow}",requiredGrade)
        else:
            sheet.update_acell(f"{situationColumnLetter}{currentRow}","Reprovado por Nota")
            sheet.update_acell(f"{requiredGradeColumnLetter}{currentRow}",0)
    
    cellValueNumber = int(sheet.acell(f"{attendanceColumnLetter}{currentRow}").value)
    if (cellValueNumber > absenceMax):
        sheet.update_acell(f"{situationColumnLetter}{currentRow}","Reprovado por Falta")
        sheet.update_acell(f"{requiredGradeColumnLetter}{currentRow}",0)