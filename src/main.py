from classes.food import Food
from classes.job import Job
from classes.house import House
from classes.sim import Sim


pizza = Food(name='Pizza', description='Italiano food', price='200', energy=20)
print(pizza)

programmer = Job(name='Programmer', description='Night owl', pay_per_hour=10.5, max_hours=10)
print(programmer)
print(programmer.calculate_salary(10))

andara = House(name='Andara', description='Rumah sultan', area=50, rent_per_week=10)
print(andara)

deborah = Sim(first_name='Deborah', last_name='Tampubolon', house=andara, job=programmer)
print(deborah)