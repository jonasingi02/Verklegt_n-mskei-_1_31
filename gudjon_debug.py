from Code_files.data.EmployeeData import EmployeeData


data_class = EmployeeData()
result = data_class.get_all_employees()
for elem in result: 
    print(elem)