import os

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


def prompt_from_list(objects):
  """
  This function is prompt that request user to choose a number.
  The chosen number should be 0 <= chosen number < length of objects list.
  """
  # Choose any object from objects list
  object_option = int(input("Choose: "))
  selected_object = None

  # If the object option is not match with list index, we return None
  if object_option >= 0 and object_option < len(objects):
    selected_object = objects[object_option]
  else:
    print("Please choose the correct number in list.")
  return selected_object


def prompt_new_sim(houses):
  """
  This function is prompt that request use to fill new sim fields.
  The fields including first name, last name, and choose a house.
  """
  Sim(first_name='Deborah', last_name='Tampubolon', house=apartment, job=programmer)
  first_name = input('First name: ')
  last_name = input('Last name: ')

  # Choose house for new sim
  print("------- List Houses -------")
  list_houses(houses)
  selected_house = None
  while selected_house is None:
    selected_house = prompt_from_list(houses)

  new_sim = Sim(first_name=first_name, last_name=last_name, house=selected_house, job=None)
  return new_sim


def sim_actions(sim, jobs, foods):
  is_exit_sim = False
  selected_sim = None

  # Loop the menus as long the is_exit_sim variable not changed to True
  while not is_exit_sim and not sim.dead:
     # Clear screen so give better experience
    os.system('cls' if os.name == 'nt' else 'clear')

    sim_actions_message = f"""Your sim : {sim}

========== Sim Actions ===========
0. Exit to main menu
1. Drink
2. Shower
3. Use toilet
4. Sleep
5. Eat
6. Cook
7. Find job
8. Work
9. Pay rent

Choose your sim action: """
    # Typecasting input from string to integer
    sim_action_option = int(input(sim_actions_message))

    # Control flow when select some menus
    if sim_action_option == 0:
      is_exit_sim = True

    elif sim_action_option == 1:
      sim.drink()

    elif sim_action_option == 2:
      sim.shower()
    
    elif sim_action_option == 3:
      sim.use_toilet()
    
    elif sim_action_option == 4:
      total_hour = int(input("How long are you going to sleep? (hrs) "))
      sim.sleep(total_hour)
    
    elif sim_action_option == 5:
      if len(sim.inventory) > 0:
        # Choose food from inventory to eat
        print("------- List Foods -------")
        list_foods(sim.inventory)
        selected_food = None
        while selected_food is None:
          selected_food = prompt_from_list(sim.inventory)
        sim.eat(selected_food)
      else:
        _ = input("You don't have any foods. Please cook first. Enter to continue")
    
    elif sim_action_option == 6:
      # Choose food from known foods list
      print("------- List Foods -------")
      list_foods(foods)
      selected_food = None
      while selected_food is None:
        selected_food = prompt_from_list(foods)
      sim.cook(selected_food)
    
    elif sim_action_option == 7:
      # Choose new job
      print("-------- List Jobs --------")
      list_jobs(jobs)
      selected_job = None
      while selected_job is None:
        selected_job = prompt_from_list(jobs)
      
      # Set the selected job to sim
      sim.new_job(selected_job)
    
    elif sim_action_option == 8:
      total_hour = int(input("How long are you going to work? (hrs) Notes: We're not allowing overtime, if so you'll be paid to the max working hours. "))
      sim.work(total_hour)
    
    elif sim_action_option == 9:
      if not sim.house.is_due():
        print("There is no due for house rent.")
      else:
        total_week = int(input("How long are you going to pay the rent? (weeks) "))
        sim.work(total_week)
        sim.pay_rent(1)
    
    else:
      # If the user input is not in the menu
      print("Sorry we didn't understand you. Please choose the correct number in menus.")
    
  if sim.dead:
    print("Your sim is dead.")
  else:
    reset_input = input("Do you want to reset this sim condition? (y/n) ")
    if reset_input.lower() == "y":
      sim.reset()


def menu(sims, houses, jobs, foods):
  is_exit = False

  # Loop the menus as long the is_exit variable not changed to True
  while not is_exit:
    menu_message = """
========== Menus ===========
0. Quit game
1. New sim
2. List sims
3. Select sims

Choose your menu: """

    # Typecasting input from string to integer
    menu_option = int(input(menu_message))

    # Clear screen so give better experience
    os.system('cls' if os.name == 'nt' else 'clear')

    # Control flow when select some menus
    if menu_option == 0:
      # Changed the is_exit variable so it will exit the while loop
      is_exit = True

    elif menu_option == 1:
      print("--------- New Sim ---------")
      new_sim = prompt_new_sim(houses)
      sims.append(new_sim)

    elif menu_option == 2:
      print("-------- List Sims --------")
      list_sims(sims)
    
    elif menu_option == 3:
      print("------- Select Sims -------")
      list_sims(sims)
      selected_sim = None
      while selected_sim is None:
        selected_sim = prompt_from_list(sims)
      sim_actions(selected_sim, jobs, foods)
    
    else:
      # If the user input is not in the menu
      print("Sorry we didn't understand you. Please choose the correct number in menus.")


if __name__ == "__main__":
  # Following codes is declarations of things we'll be using in the sim actions
  # Jobs declarations
  programmer = Job(name='Programmer', description='Do magic with codes', pay_per_hour=20.5, max_hours=10)
  designer = Job(name='Designer', description='Love to prettify things', pay_per_hour=20.5, max_hours=8)
  jobs = [programmer, designer]

  # Foods declarations
  pizza = Food(name='Pizza', description='Italiano food', price=70, energy=50)
  burger = Food(name='Burger', description='American food', price=30, energy=30)
  nasi_padang = Food(name='Nasi Padang', description='Indonesian food', price=10, energy=100)
  foods = [pizza, burger, nasi_padang]

  # Houses declarations
  andara = House(name='Andara', description='Rumah sultan', area=50, rent_per_week=300)
  apartment = House(name='Apartment', description='Future way of living', area=25, rent_per_week=100)
  houses = [andara, apartment]

  # Sims declaration
  deborah = Sim(first_name='Deborah', last_name='Tampubolon', house=apartment, job=programmer)
  deborah = Sim(first_name='Deborah', last_name='Tampubolon', house=apartment, job=programmer)
  sims = [deborah]

  print("Welcome to SimsLite!")
  _ = input("Press enter to continue")

  # Passing the declared sims, houses, jobs, and foods to the procedure menu
  menu(sims, houses, jobs, foods)

  print("Glad to play with you, bye!")