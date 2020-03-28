import openpyxl

plan = openpyxl.load_workbook('D:/Box Sync/Documents/PyCharmProjects/openpyxl/example.xlsx', read_only=True)
plan.get_sheet_by_name("Plan1")
aba = plan.active

key = "Decker"

for x in aba.rows:
    for z in x:
        if z.value == key:
            print("A palavra Decker está na coluna:", z.column, "e linha:", z.row, ", ou na célula", z.coordinate)
            break