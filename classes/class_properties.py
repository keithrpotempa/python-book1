# Practice: Solid Student
# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)

class Student:
  
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.

    #fname 
    @property
    def fname(self):
        try:
            return self.__fname
        except AttributeError:
            return 0
          
    @fname.setter
    def fname(self, new_name):
        if type(new_name) is str:
            self.__fname = new_name
        else:
            raise TypeError('Please provide a string for the first name')
          
    #lname
    @property
    def lname(self):
        try:
            return self.__lname
        except AttributeError:
            return 0
          
    @lname.setter
    def lname(self, new_name):
        if type(new_name) is str:
            self.__lname = new_name
        else:
            raise TypeError('Please provide a string for the last name')

    #age
    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0
          
    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide an integer for the age')

    #cohort
    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0
          
    @cohort.setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError('Please provide an integer for the cohort number')
          
    #fullname
    @property
    def fullname(self):
        try:
            return f"{self.fname} {self.lname}"
        except AttributeError:
            return 0


student1 = Student()
student1.fname = "Arby"
student1.lname = "Ross"
student1.age = 500
student1.cohort = 54
print(student1.fullname)