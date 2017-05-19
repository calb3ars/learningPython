class Employee:

    emp_count = 0

    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_employee(self):
        print("name: %s, salary: %s" % (self.name, self.salary))

    def give_raise(self, percent):
        self.salary += self.salary * percent

    def display_count(self):
        print("count: %d" % Employee.emp_count)
