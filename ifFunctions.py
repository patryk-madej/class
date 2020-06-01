#calculates the best shipping option given the weight of the parcel

def cost_ground(weight):
  if weight <= 2:
    return weight*1.50+20
  elif weight > 2 and weight <=6:
    return weight*3+20
  elif weight > 6 and weight <=10:
    return weight*4+20
  else: 
    return weight*4.75+20

#print(cost_ground(8.4)) #test

def cost_drone(weight):
  if weight <= 2:
    return weight*4.50
  elif weight > 2 and weight <=6:
    return weight*9.0
  elif weight > 6 and weight <=10:
    return weight*12.0
  else: 
    return weight*14.25

#print(cost_drone(6.5)) #test

premium=125

def compare(weight):
  if cost_ground(weight)>premium or cost_drone(weight)>premium:
    return f"It's cheaper to use premium shipping. It will cost £{premium}"
  elif cost_ground(weight)>cost_drone(weight):
    return f"It's cheaper to use drone shipping. It will cost £{cost_drone(weight)}"
  elif cost_ground(weight)<cost_drone(weight):
    return f"It's cheaper to use ground shipping. It will cost £{cost_ground(weight)}"
  else:
    return f'Either shipping option costs the same. It will cost £{cost_ground(weight)}'

#print(compare(1.0)) #test
