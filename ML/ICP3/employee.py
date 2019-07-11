class Employee:
  count = 0
  totalSal = 0
  x = 100

  def __init__(self, name, family, Address):
    self.name = name
    self.family = family
    self.salary = Employee.x
    self.address = Address
    Employee.count += 1
    Employee.totalSal += Employee.x

  def average(self):
    return self.totalSal/self.count

  def display(self):
    print("Name: ", self.name, " Family :", self.family, " Salary :", self.salary, " Address :",self.address)


class FulltimeEmployee(Employee):
    def __init__(self, n, f, a):
        Employee.__init__(self, n, f, a)


e1 = Employee("Nadal", "Tennis Family", "No man's land")
e2 = Employee("Smith", "Cricket Family", "Australia")
e3 = FulltimeEmployee("Bhavaz", "Royal Family","5305 Charlotte St")
e4 = FulltimeEmployee("Dwarka", "Bhikari Family","5425 Harrison St")
e5 = FulltimeEmployee("Kruthika", "Average Family","5421 Holmes St")
print(e4.average())
print(e5.average())
e3.display()
