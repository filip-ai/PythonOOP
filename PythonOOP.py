class Company:
    def __init__(self, name, address, company_id):
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []
    def make_offer(self, employee, salary, position):
        if not isinstance(employee, Employee):
            print("{} is not an instnace of class Employee. Can not hire.".format(employee))
            return
        Offer(self, employee, salary, position)
    def fire(self, employee):
        if not isinstance(employee, Employee):
            raise Exception('Can not fire, {} is not an instance of Employee'.format(employee))
        if employee.company.company_id != self.company_id:
            raise Exception('{} can not fire {}. Not employed in this company'.format(self, employee ))
        print ('{} is firing {}'.format(self, employee ))
        self.employee_list.remove(employee)
        employee.company = None
        employee.salary = None
        employee.position = None
    def get_salary_costs(self):
        total_salary_costs = 0
        for employee in self.employee_list:
            total_salary_costs += employee.salary
        return total_salary_costs
    def __str__(self):
        return self.name
class Employee:
    minimum_pay = 14000
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.company = None
        self.salary = None
        self.position = None
        self.offers = {}
    def __str__(self):
        return self.full_name()
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    def receive_offer(self, offer):
        if not isinstance(offer, Offer):
            raise Exception("{} is not an instnace of class Offer. Can not receive offer.".format(offer))
        self.offers[offer.company.company_id] = offer
    def accept_offer(self, company):
        if self.company is not None:
            raise Exception ("{} is already employed, must quit first".format(self))
        if not isinstance(company, Company):
            raise Exception ("{} is not an instnace of class Company. Can not accept offer.".format(company))
        offer = self.offers.get(company.company_id)
        if not offer:
            print("No offer found from company {}".format(company))
            return
        self.company = offer.company
        self.salary = offer.salary
        self.company.employee_list.append(self)
        print('{} accepted offer from {}.'.format(self, self.company) )
        del self.offers[company.company_id]
    def quit(self):
        if self.company is None:
            print ("{} is not employed, can not quit".format(self))
        print('{} is quitting from {}.'.format(self, self.company) )
        self.company.employee_list.remove(self)
        self.company = None
        self.salary = None
class Offer:
    minimum_salary = 14500
    def __init__(self, company, employee, salary, position):
        if not isinstance(employee, Employee):
            raise Exception("{} is not an instnace of class Employee. Can not create offer.".format(employee))
        if not isinstance(company, Company):
            raise Exception("{} is not an instnace of class Company. Can not craete offer.".format(company))
        if not isinstance(salary, int):
            raise Exception("Salary ({}) is not an interger. Can not craete offer.".format(salary))
        if not isinstance(position, str):
            raise Exception("Position ({}) is not a string. Can not craete offer.".format(position))
        if salary < Offer.minimum_salary:
            print("Salary ({}) is smaller than the allowed minimum salary. Can not craete offer.".format(salary))
        self.company = company
        self.employee = employee
        self.salary = salary
        self.position = position
        employee.receive_offer(self)
    def __str__(self):
        return "Offer from {} to {}".format(self.company, self.employee)
print ('### CODE EXECUTION STARTS HERE ###')
semos = Company("Semos Edukacija", "Kuzman Josifovski Pitu XXX", "1234" )
quipu = Company('Quipu', 'Ilindenska XXX', "3456")
petko = Employee("Petko", "Petkov", "petko@mailinator.com")
janko = Employee("Janko", "Jankov", "janko@mailinator.com")
stanko = Employee("Stanko", "sankov", "stanko@mailinator.com")
semos.make_offer(petko, 30000, 'Developer')
petko.accept_offer(semos)
quipu.make_offer(janko, 40000, 'Developer')
janko.accept_offer(quipu)
semos.make_offer(stanko, 35000, 'Accountant')
stanko.accept_offer(semos)
print('semos total salary before Stanko left', semos.get_salary_costs())
stanko.quit()
#semos.fire(stanko)
print('semos total salary after Stanko left', semos.get_salary_costs())