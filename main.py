def separator():
  print('\n' + 20 * "=" + '\n')

# function to print custom message

def getWelcome(name, year):
  message = "Welcome to John Jay Class of " + year + ", " + name
  print(message)

getWelcome("Brayan", "2024")


separator()

# function to convert number
# grade to letter
def convertGrade(numericGrade):
  if numericGrade >= 90:
    return "A"
  elif numericGrade >= 80:
    return "B"
  elif numericGrade >= 70:
    return "C"
  elif numericGrade >= 60:
    return "D"
  else:
    return "F"

# printing single grade
print(convertGrade(86))


separator()


def hasStudentID():
  customerID = input("Do you have a student ID? (y/n)")
  if customerID == "y":
    return True
  else:
    return False

def getAge():
  customerAge = int(input("Enter age: "))
  return customerAge

if hasStudentID() or getAge() >= 65:
  print("Discount Ticket $5")
else:
  print("Full Price Ticket $10")

separator()

def calculateBonus(score):
  if score >= 5000:
    return score * .10
  elif score >= 2500:
    return score * .08
  elif score >= 1000:
    return score * .05
  else:
    return 0

score = int(input("Enter score: "))
print("Your score with bonus is", score + calculateBonus(score))



