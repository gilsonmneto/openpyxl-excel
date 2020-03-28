import openpyxl


plan = openpyxl.load_workbook('D:/Box Sync/Desktop/Projetos Programação/Python/PyCharmProjects/openpyxl/example.xlsx', read_only=False)
plan.get_sheet_by_name("Plan1")
aba = plan.active

frase = "Opa"

aba["A10"] = frase

plan.save('D:/Box Sync/Desktop/Projetos Programação/Python/PyCharmProjects/openpyxl/example.xlsx')

if frase == aba["A10"].value:
    print("Funcionou")
