class Employee:

    def __init__(self, name, employee_id, department, basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.basic_salary = basic_salary

    # Calculate Bonus as per department

    def Cal_bonus(self):
        bonus_rules = {
            "IT"        : 20,   #20% bonus
            "Sales"     : 25,
            "HR"        : 10,
            "Development": 35,
        }

        bonus_percent = bonus_rules.get(self.department, 10)  # If no department found, then default bonus is 10%
        bonus_amount = ( bonus_percent / 100 ) * self.basic_salary   # Get bonus Amount
        return bonus_percent, bonus_amount
    
    def Cal_tax(self, gross_salary):
        if gross_salary < 30000:
            tax_rate = 5
        elif gross_salary <= 70000:
            tax_rate = 10
        else: 
            tax_rate = 25
        
        tax_amount = (tax_rate / 100) * gross_salary
        return tax_rate, tax_amount
    
    def Cal_Salary(self):
        bonus_percent, bonus_amount = self.Cal_bonus()
        gross_salary = self.basic_salary + bonus_amount
        tax_rate, tax_amount = self.Cal_tax(gross_salary)
        final_salary = gross_salary - tax_amount

        return {
            "bonus_percent": bonus_percent,
            "bonus_amount" : bonus_amount,
            "tax_rate" : tax_rate,
            "tax_amount": tax_amount,
            "gross_salary" : gross_salary,
            "final_salary" : final_salary,
        }
    
    def display_salary_slip(self):
        result = self.Cal_Salary()

        print(f"Name = {self.name}")
        print(f"EmployeeId = {self.employee_id}")
        print(f"Department = {self.department}")
        print(f"Basic Salary = {self.basic_salary}")
        print(f"Bonus Percent is {result['bonus_percent']:>2} and Bonus Amount is {result['bonus_amount']:>10.2f}")
        print(f"Gross Salary  = {result['gross_salary']:>10,.2f}")
        print(f"Final Salary = {result['final_salary']}")

emp1 = Employee("Devendra Rajput",   "EMP-101", "Development", 85000)
emp2 = Employee("Mahes",   "EMP-102", "IT", 55000)

employee = [emp1, emp2]
for emp in employee:
    emp.display_salary_slip()

    





    

    

        
 


        