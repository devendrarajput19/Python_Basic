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
        print(f"   Total Leaves    : {Employee.TOTAL_LEAVES}")
        print(f"   Used Leaves     : {Employee.TOTAL_LEAVES - self.leave_balance}")
        print(f"   Remaining       : {self.leave_balance}")
        return self.leave_balance
