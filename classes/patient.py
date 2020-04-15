# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

# [x] Social security number
# [x] Date of birth
# [x] Health insurance account number
# [x] First name
# [x] Last name
# [x] Address
# [x] The first three properties should be read-only. 
# [x] First name and last name should not be exposed as properties at all, 
# [x] but instead expose a calculated property of full_name. 
# [x] Address should have a getter and setter.

class Patient:

    def __init__(self, ssn, dob, insurance_acct_num, fname, lname, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__insurance_acct_num = insurance_acct_num
        self.__fname = fname
        self.__lname = lname
        self.__address = address

    #ssn
    @property
    def ssn(self):
        try:
            return self.__ssn
        except AttributeError:
            return 0
          
    #dob
    @property
    def dob(self):
        try:
            return self.__dob
        except AttributeError:
            return 0


    #full_name
    @property
    def full_name(self):
        try:
            return f"{self.__fname} {self.__lname}"
        except AttributeError:
            return 0
          
    #address
    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0
          
    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a string for the address')

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# [x] This should not change the state of the object
# cashew.ssn = "838-31-2256"

# [x] Neither should this
# cashew.dob = "01-30-90"

# [x] But printing either of them should work
# print(cashew.ssn)   # "097-23-1003"

# [x] These two statements should output nothing
# print(cashew.fname)
# print(cashew.lname)

# [x] But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"