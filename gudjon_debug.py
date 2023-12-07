from Code_files.data.EmployeeData import EmployeeData


data_class = EmployeeData()
result = data_class.create_empoyee()
for elem in result: 
    print(elem)
