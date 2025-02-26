employees = {
    "emp_101": {"name": "Alice", "department": "HR", "salary": 50000, "projects": ["Recruitment", "Payroll"]},
    "emp_102": {"name": "Bob", "department": "IT", "salary": 70000, "projects": ["App Development", "Security"]},
    "emp_103": {"name": "Charlie", "department": "Finance", "salary": 65000, "projects": ["Budgeting", "Taxation"]},
    "emp_104": {"name": "David", "department": "IT", "salary": 80000, "projects": ["Cloud Migration", "Support"]},
}

#Implement get_unique_departments(employees), which returns a set of unique department names.
def get_unique_departments(employees):
    unique = set()
    for x in employees.values():
        unique.add(x["department"])
    return unique
# print(get_unique_departments(employees))


#Implement get_total_salary_by_department(employees), which returns a dictionary where keys are department names and values are the total salary of employees in that department.
def get_total_salary_by_department(employees):
    # we will create an empty dictionary
    result = {}
    # iterate over employees and get the values of employee from employee_id  
    for key, value in employees.items():  # key = emp_101, value = {"name": "Alice", "department": "HR", "salary": 50000, "projects": ["Recruitment", "Payroll"]}
    
    # get the values of department and salary and add it in the empty dictionary 
        department = value["department"]   # department = "HR" and
        salary = value["salary"]
        result[department] = salary       # result =  {'HR' : 50000}
    
    # if department is duplicate or already present in the dictionary, add the salary 
    if department in result:
        # a = b + c
        result[department] = result[department] + salary      # result = {'It'}  It = 70000 + 80000
    # return the dictionary 
    return result
# print the values 
print(get_total_salary_by_department(employees))
#{'hr' : 50000, 'it' : 150000, 'finance' : 65000}

#Implement get_highest_paid_employee(employees), which returns the name of the employee with the highest salary.
def get_highest_paid_employee(employees):
# set highest_salary as the minimum value 
    highest_salary = 0
    highest_paid_employee = None
# iterate over employees and get the values of employees salary
    for y, x in employees.items():
# over the iteration if value of salary > highest_salary
        if x["salary"] > highest_salary:  # 
# then highest_salary would be equal to value of salary 
            highest_salary = x["salary"]
# and highest_paid_employee will be david             
            highest_paid_employee = x["name"]

    return highest_paid_employee
# print(get_highest_paid_employee(employees))

#Implement get_employees_by_project(employees, project_name), which returns a list of employee names working on the given project.
def get_employees_by_project(employees, project_name):
# create an empty list which stores the data add the names of employees and projects in the list
    emp_name = []
#iterate over the dictionary and get the details about the employee
    for y, x in employees.items():
# if project_name existes in projects 
        if project_name in x["projects"]:
# append the value of employee name in the empty list
            emp_name.append(x["name"])
# return the employee name 
    return emp_name
# print 
# print(get_employees_by_project(employees, "Support"))

#Implement get_department_with_max_employees(employees), which returns the department name that has the most employees.
def get_department_with_max_employees(employees):
    most_employees = {}
    for y, x in employees.items():
        department = x["department"]
        if department in most_employees:
            most_employees[department] += 1
        else:
            most_employees[department] = 1

    max_dept = None
    most_emp = 0
    for y, x in most_employees.items():
        if x > most_employees:
            most_employees = x
            max_dept = y
    return most_employees

print(get_department_with_max_employees(employees))