class Employee:
    def __init__(self, name, emp_id, dept, basic, hra, bonus):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept
        self.basic = basic
        self.hra = hra
        self.bonus = bonus

class Payroll:
    PF_RATE = 0.12
    PROF_TAX = 200

    def __init__(self, employee):
        self.emp = employee

    def calculate_gross(self):
        return self.emp.basic + self.emp.hra + self.emp.bonus

    # Calculate Tax
    def deduct_tax(self, annual_gross):
        if annual_gross <= 250000:
            return 0
        elif annual_gross <= 500000:
            return (annual_gross - 250000) * 0.05
        elif annual_gross <= 1000000:
            return 12500 + (annual_gross - 500000) * 0.20
        else:
             return 112500 + (annual_gross - 1000000) * 0.30
        
    def generate_payslip(self, month):
        gross = self.calculate_gross()
        annual_tax = self.deduct_tax (gross * 12)
        monthly_tax = annual_tax/12
        pf = self.emp.basic * self.PF_RATE
        total_deduction = monthly_tax + pf + self.PROF_TAX
        net = gross - total_deduction

        return {
            "name": self.emp.name,
            "month": month,
            "gross": gross,
            "tax": monthly_tax,
            "pf": pf,
            "net": net
        }


emp = Employee("Devendra Rajput", "EMP-2024", "Engineering",
               basic=50000, hra=20000, bonus=5000)

payroll = Payroll(emp)
slip    = payroll.generate_payslip("Jan 2026")

print(f"Net Salary: ₹{slip['net']:,.2f}")