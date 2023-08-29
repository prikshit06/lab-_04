class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        result = [employee for employee in self.employees if employee.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [employee for employee in self.employees if employee.name.lower() == target_name.lower()]
        return result

    def search_by_salary(self, operator, target_salary):
        if operator == '<':
            result = [employee for employee in self.employees if employee.salary < target_salary]
        elif operator == '<=':
            result = [employee for employee in self.employees if employee.salary <= target_salary]
        elif operator == '>':
            result = [employee for employee in self.employees if employee.salary > target_salary]
        elif operator == '>=':
            result = [employee for employee in self.employees if employee.salary >= target_salary]
        else:
            result = []
        return result

def main():
    database = EmployeeDatabase()

    # Adding sample data to the database
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter target age: "))
        result = database.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter target name: ")
        result = database.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter operator (<, >, <=, >=): ")
        target_salary = int(input("Enter target salary: "))
        result = database.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return

    if result:
        print("Search Results:")
        for employee in result:
            print(f"Employee ID: {employee.employee_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("No matching results found.")

if __name__ == "__main__":
    main()
