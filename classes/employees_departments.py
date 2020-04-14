# Instructions
# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.

class Employee:
  
    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

# Create a Company type that employees can work for. A company should have a business name, address, and industry type.

class Company:
  
    def __init__(self, name, address, industry_type):
        self.name = name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()
        
    def summary_report(self):
        print(f"{self.name} is in the {self.industry_type} industry and has the following employees:")
        for employee in self.employees:
            print(f"  * {employee.name} ({employee.title})")

# Create two companies, and 5 people who want to work for them.

CHOAM = Company("CHOAM", "Old Empire", "Universal Development Corporation")
GloboChem = Company("GloboChem", "100 GloboChem Street", "Mega Corp")

Marvin = Employee("Marvin Hudson", "Engineer", "4/13/2020")
Lewis = Employee("Lewis Alexander", "Developer", "4/13/2020")
Denise = Employee("Denise White", "Mentat", "4/13/2020")
Fred = Employee("Fred Matthews", "Pilot", "4/13/2020")
Amber = Employee("Amber Riley", "Communications", "4/13/2020")

# Assign 2 people to be employees of the first company.
CHOAM.employees.append(Marvin)
CHOAM.employees.append(Denise)

# Assign 3 people to be employees of the second company.
GloboChem.employees.append(Lewis)
GloboChem.employees.append(Fred)
GloboChem.employees.append(Amber)

# Output a report to the terminal the displays a business name, and its employees.
# For example:

# Acme Explosives is in the chemical industry and has the following employees
#    * Michael Chang
#    * Martina Navritilova

# Jetways is in the transportation industry and has the following employees
#    * Serena Williams
#    * Roger Federer
#    * Pete Sampras

CHOAM.summary_report()
GloboChem.summary_report()