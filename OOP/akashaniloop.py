from abc import ABC , abstractmethod



class Employee(ABC):
    def __init__(self,employee_name, department , salary):
        self.employee_name = employee_name
        self.department = department
        self.__salary = salary


    @property

    def salary(self):
        return self.__salary

    def display_details(self):
        print('Nme :' , self.employee_name)
        print('Department :' , self.department)
        print('Salary :' , self.salary)
       

    @abstractmethod
    def calculate_salary(self):
        pass

class PermanentEmployee(Employee):
    def calculate_salary(self):
            allowance = self.salary * 0.20
            total = self.salary +  allowance
            print('The permentEmployee Salary -', total)
            return total

class ContractEmployee(Employee):
         def calculate_salary(self):
            allowance = self.salary * 0.05
            total = self.salary + allowance
            print('The ContractEmployee Salary -', total)
            return total


Permanent = PermanentEmployee('Akash','IT',60000)
Permanent.display_details()
Permanent.calculate_salary()

Contract = ContractEmployee('Ramanan' , 'IT', 40000)
Contract.display_details()
Contract.calculate_salary()
       


print('***********Q2****************')
#2



from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_name, vehicle_days, rental_price):
        self.vehicle_name = vehicle_name
        self.vehicle_days = vehicle_days
        self.__rental_price = rental_price

    @property
    def rental_price(self):
        return self.__rental_price

    def display_details(self):
         print('Vehicle name : ', self.vehicle_name)
         print('Vehicle rented days : ', self.vehicle_days)
         print('Rental price : ', self.rental_price)

    @abstractmethod

    def calculate_rent(days):
         pass

class Car(Vehicle):
     def calculate_rent(self):
          total_rent = (self.rental_price * self.vehicle_days) + 500
          print('The total car rent price is - ', total_rent)
          return total_rent

class Bike(Vehicle):
     def calculate_rent(self):
          total_rent = (self.rental_price * self.vehicle_days) + 100
          print('The total Bike rent price is - ', total_rent)
          return total_rent


Car = Car('Alto', 5 , 400)
Car.display_details()
Car.calculate_rent()

Bike = Bike('R15', 6 , 100)
Bike.display_details()
Bike.calculate_rent()





          


  

    

        
