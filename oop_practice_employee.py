"""
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)


"""


class Employee:

    def __init__(self, name, prename, salary):
        self.name = name
        self.prename = prename
        self.salary = salary

    def employee_description(self):
        print(self.name)
        print(self.prename)
        print(self.salary)

    def employee_complete_name(self):
        print(self.prename, self.name)

    def employee_monthly_salary(self):
        return self.salary

    def employee_anual_salary(self):
        return self.salary * 12

    def employee_salary_raise(self,percent):
        x=int(input('Please enter the desired percentage 1-100 format only'))
        if x in range(101):
            self.salary=self.salary+(self.salary*percent/100)
        else:
            print('incorrect input, please call the function again')

employee=Employee('Jack','Cousteau',1000)
employee.employee_description()
employee.employee_complete_name()
print(employee.employee_monthly_salary())
print(employee.employee_anual_salary())
print(employee.employee_salary_raise(10))
print(employee.employee_monthly_salary())
print(employee.employee_anual_salary())