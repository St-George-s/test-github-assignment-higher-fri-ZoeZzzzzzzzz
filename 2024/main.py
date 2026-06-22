import csv
def readFromFile():
    company = []
    numEmployees= []
    ceoSalary = []
    with open ("2024/companies.csv", "r") as file:
        print(file)
        reader = csv.reader(file)
        for row in reader:
            company.append(row[0])
            numEmployees.append(row[1])
            ceoSalary.append(row[2])
        print(company)

    return company, numEmployees, ceoSalary 
    
def findCeoDifference(company,ceoSalary):
    maxIndex = 0
    for salaryIndex in range(len[ceoSalary]):
        if ceoSalary[salaryIndex] > ceoSalary[maxIndex]:
            maxIndex = salaryIndex
    print(maxIndex)
    pass

for index in range(len(company))
findCeoDifference()

# def findHighestEmployees(numEmployees):
#     pass

# #mainprogram
company, numEmployees, ceoSalary = readFromFile()
findCeoDifference(company, ceoSalary)
# findCeoDifference(numEmployees)
readFromFile()

