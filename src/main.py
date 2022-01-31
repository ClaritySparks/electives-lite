import os
from typing import List

from classes.food import Food
from classes.job import Job
from classes.house import House
from classes.sim import Sim


def list_sims(sims):
  """
  This function prints the sim list and its number starting from 0
  """
  sim_number = 0
  for sim in sims:
    print(f"#{sim_number}")
    print(sim, end="\n")
    sim_number += 1 
  

def list_houses(houses):
  """
  This function prints the house list and its number starting from 0
  """
  house_number = 0
  for house in houses:
    print(f"#{house_number}")
    print(house, end="\n")
    house_number += 1


def list_jobs(jobs):
  """
  This function prints the job list and its number starting from 0
  """
  job_number = 0
  for job in jobs:
    print(f"#{job_number}")
    print(job, end="\n")
    job_number += 1


def list_foods(foods):
  """
  This function prints the food list and its number starting from 0
  """
  food_number = 0
  for food in foods:
    print(f"#{food_number}")
    print(food, end="\n")
    food_number += 1


def prompt_new_sim(houses, jobs):
  Sim(first_name='Deborah', last_name='Tampubolon', house=apartment, job=programmer)
  first_name = input('First name: ')
  last_name = input('Last name: ')

  # Choose house for new sim
  print("------- List Houses -------")
  list_houses(houses)
  house_option = int(input("Choose your house: "))
  if house_option >= 0 and house_option < len(houses):
    selected_house = houses[house_option]
  else:
    print("Please choose the correct number in list houses.")
  
  # Choose job for new sim
  print("-------- List Jobs --------")
  list_jobs(jobs)
  job_option = int(input("Choose your job: "))
  if job_option >= 0 and job_option < len(jobs):
    selected_job = jobs[job_option]
  else:
    print("Please choose the correct number in list jobs.")

  new_sim = Sim(first_name=first_name, last_name=last_name, house=selected_house, job=selected_job)
  return new_sim


def menu(houses, jobs, foods, sims):
  is_exit = False
  selected_sim = None

  # Loop the menus as long the is_exit variable not changed to True
  while not is_exit:
    menu_message = """
========== Menus ===========
0. New sim
1. List sims
2. Select sims
3. Exit

Choose your menu: """

    # Typecasting input from string to integer
    menu_option = int(input(menu_message))

    # Clear screen so give better experience
    os.system('cls' if os.name == 'nt' else 'clear')

    # Control flow when select some menus
    if menu_option == 0:
      print("--------- New Sim ---------")
      new_sim = prompt_new_sim(houses, jobs)
      sims.append(new_sim)

    elif menu_option == 1:
      print("-------- List Sims --------")
      list_sims(sims)
    
    elif menu_option == 2:
      print("------- Select Sims -------")
      list_sims(sims)
      sim_option = int(input("Choose your sim: "))
      if sim_option >= 0 and sim_option < len(sims):
        selected_sim = sims[sim_option]
      else:
        print("Please choose the correct number in list sims.")
    
    elif menu_option == 3:
      # Changed the is_exit variable so it will exit the while loop
      is_exit = True
    
    else:
      # If the user input is not in the menu
      print("Sorry we didn't understand you. Please choose the correct number in menus.")


if __name__ == "__main__":
  # Following codes is declarations of things we'll be using in the menu
  # Foods declarations
  pizza = Food(name='Pizza', description='Italiano food', price='200', energy=50)
  burger = Food(name='Burger', description='American food', price='50', energy=30)
  nasi_padang = Food(name='Nasi Padang', description='Indonesian food', price='10', energy=100)
  foods = [pizza, burger, nasi_padang]

  # Jobs declarations
  programmer = Job(name='Programmer', description='Do magic with codes', pay_per_hour=20.5, max_hours=10)
  designer = Job(name='Designer', description='Love to prettify things', pay_per_hour=20.5, max_hours=8)
  jobs = [programmer, designer]

  # Houses declarations
  andara = House(name='Andara', description='Rumah sultan', area=50, rent_per_week=30)
  apartment = House(name='Apartment', description='Future way of living', area=25, rent_per_week=10)
  houses = [andara, apartment]

  # Sims declaration
  deborah = Sim(first_name='Deborah', last_name='Tampubolon', house=apartment, job=programmer)
  deborah = Sim(first_name='Deborah', last_name='Tampubolon', house=apartment, job=programmer)
  sims = [deborah]

  print("Welcome to SimsLite!")
  _ = input("Press enter to continue")

  # Passing the declared houses, jobs, foods, and sims to the procedure menu
  menu(houses, jobs, foods, sims)

  print("Glad to play with you, bye!")