class Employee:

    def calculate_payroll(self):
        pass

class Hourly_employee(Employee):

    def calculate_payroll(self, x):
        return 20.8 * 8 * x

    def print_info(self):
        return self.calculate_payroll(self, 10)


class Fixed_term_employee(Employee):

    def calculate_payroll(self, x):
        return x

    def print_info(self):
        return self.calculate_payroll(self, 100)

kazax = Hourly_employee
ne_4e4enec = Fixed_term_employee

print(kazax.print_info(kazax))
print(ne_4e4enec.print_info(ne_4e4enec))
