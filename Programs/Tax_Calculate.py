
salary = float(input("Enter Salary = "))

if salary < 30000:
    tax_rate = 5
    slab = "Below 30000"

elif salary <= 70000:
    tax_rate = 15
    slab = "30000 - 70000"

else:
    tax_rate = 25
    slab = "Above 70000"

tax_amount = (tax_rate/100) * salary
final_salary = salary - tax_amount

print("Gross Salary = ", salary)
print("Salary slab = ", slab)
print("Tax Rate = ", tax_rate,"%")
print("Tax Amount = ", tax_amount)
print("Final Salary = ", final_salary)