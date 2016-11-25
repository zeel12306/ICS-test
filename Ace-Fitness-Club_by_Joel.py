'''Ace Fitness Club'''
class ace_fitness_club():
  def __init__(self, first_name, last_name, age, gender, type_of_membership, weight):
    self.first_name = first_name 
    self.last_name = last_name
    self.age = age
    self.gender = gender
    self.type_of_membership = type_of_membership
    self.weight = weight
    self.weightKilo = round(weight/2.2, 0)

  def membership_Fee(self):
    fulltime_membership = 200
    if self.type_of_membership == "PartTime" and self.age < 65:
      return fulltime_membership
    elif self.type_of_membership == "PartTime":
      return fulltime_membership * 0.75
    else:
      return fulltime_membership * 0.5  
  
  #Convert Pounds To Kilograms
  def ConvertWeight(self):
    self.weight = self.weight/2.2
    return self.weight
    
class Weights(ace_fitness_club):
  pass
  
class gym(ace_fitness_club):
  pass
  
  
class pool(ace_fitness_club):
  mem_cost_pool = 400
  print(mem_cost_pool) 
    
#Membership Data   
member_1 = ace_fitness_club("Joel", "Williams", 17, "Male", "Youth", 150)
member_2 = ace_fitness_club("Mitch", "Benson", 16, "Male", "Youth", 145) 

print (member_1.first_name)
print (member_1.last_name)
print (member_1.age)
print (member_1.gender)
print (member_1.type_of_membership)
print (member_1.weight)
print (member_1.ConvertWeight())
print (member_1.membership_Fee)
