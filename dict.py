def func():
    employee = {"Salary": 20000, "Department": "Developer"}
    print(f"{employee} and type = {type(employee)}")
    print(f"Salary: {employee['Salary']}")
    print(f"Department: {employee['Department']}")

    print(employee.keys())
    print(employee.values())


func()
