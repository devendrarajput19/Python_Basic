class Employee:
    """Represents an employee with leave details..."""

    Total_leaves = 20

    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.leave_balance = Employee.Total_leaves
        self.leave_requests = []                    # List of leave requests dictionaries

    def apply_leave(self, leave_type, start_date, end_date, days, reason):
        if days > self.leave_balance:
            print(f"Cannot apply... You only have {self.leave_balance} leaves remaining...")

        request = {
                "request_id": len(self.leave_requests) + 1,
                "leave_type": leave_type,
                "start_date": start_date,
                "end_date": end_date,
                "days": days,
                "reason": reason,
                "status": "Pending"
            }
        self.leave_requests.append(request)

        print(f"\n Leave request #{request['request_id']} submitted successfully...by {self.name}!")

    def view_leave_requests(self):

        """Display all leave requests for this employee..."""
        if not self.leave_requests:
            print(f"\n📋 No leave requests found for {self.name}.")
            return
        
        print(f"  Leave Requests for: {self.name} (ID: {self.emp_id})")

        for req in self.leave_requests:
            print(f"Request ID = #{req['request_id']}")
            print(f"Leave Type = {req['leave_type']}")
            print(f"  From - To   : {req['start_date']} → {req['end_date']}")
            print(f"  Days        : {req['days']}")
            print(f"  Reason      : {req['reason']}")
            print(f"  Status      : {req['status']}")

    def get_leave_balance(self):
        """Return and display remaining leave balance."""
        print(f"\n📊 Leave Balance for {self.name}:")
        print(f"   Total Leaves    : {Employee.Total_leaves}")
        print(f"   Used Leaves     : {Employee.Total_leaves - self.leave_balance}")
        print(f"   Remaining       : {self.leave_balance}")
        return self.leave_balance
    
class Manager:
    """Represents a manager who can approve or reject leave requests."""

    def __init__(self, name):
        self.name = name

    def approve_leave(self, employee, request_id):
        for req in employee.leave_requests:
            if req["request_id"] == request_id:
                if req["status"] == "Pending":
                    print(f"Request #{request_id} is already '{req['status']}'.")

                    return
                req["status"] == "Approved"
                employee.leave_balance -= req["days"]
                print(f"\n Manager {self.name} APPROVED leave request #{request_id} for {employee.name}.")

                print(f"   Remaining balance: {employee.leave_balance} days.")
                return
            
        print(f"\n Request ID #{request_id} not found for {employee.name}.")


if __name__ == "__main__":
    print(" EMPLOYEE LEAVE MANAGEMENT SYSTEM - DEMO....")

    emp1 = Employee(emp_id=101, name="Ravi", department="Engineering")
    
    mgr=Manager(name="Anil J")

    emp1.apply_leave(
        leave_type="Casual Leave",
        start_date="2026-05-10",
        end_date="2026-05-12",
        days=3,
        reason="Family function"
    )
    
     # --- View All Leave Requests ---
    print("\n STEP 2: View Leave Requests")
    emp1.view_leave_requests()

    # --- Manager Approves / Rejects ---

    print("\n STEP 3: Manager Takes Action")
    mgr.approve_leave(emp1, request_id=1)

    # --- Check Leave Balance ---
    print("\n STEP 4: Check Leave Balances")
    emp1.get_leave_balance()
        
    # --- Edge Case: Apply more than balance ---
    print("\n🔹 STEP 6: Edge Case - Apply Leave Beyond Balance")
    emp1.apply_leave(
        leave_type="Annual Leave",
        start_date="2026-04-01",
        end_date="2026-04-21",
        days=21,
        reason="Long holiday"
    )