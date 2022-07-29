# module
import random

# functions
def randomBinary(diff):
    list = []
    if diff == 1 :
        number_digits = 4
    elif diff == 2 :
        number_digits = 6
    else :
        number_digits=8
    for x in range(number_digits):
        list.append(str(random.randint(0,1)))
    return list

def randomOctal(diff):
    list = []
    if diff == 1 :
        number_digits = 2
    elif diff == 2 :
        number_digits = 3
    else :
        number_digits=6
    for x in range(number_digits):
        list.append(str(random.randint(0,7)))
    return list

def randomHex(diff):
    list = []
    if diff == 1 :
        number_digits = 2
    elif diff == 2 :
        number_digits = 3
    else :
        number_digits=4
    hexlist = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
    for x in range(number_digits):
        list.append(str(random.choice(hexlist)))
    return list

def ansBinary(question):
    decimal = 0
    for digit in question:
        decimal = decimal*2 + int(digit)
    return str(decimal)

def ansOctal(question):
    octal = int(0)
    res = int(0)
    n=len(question)-1
    for i in question :
        i = int(i)
        octal = i*(8**(n))
        res+=octal
        n-=1
    return str(res)

def ansHex(question):
    hex = int(0)
    res = int(0)
    n=len(question)-1
    for i in question :
        if i.isdigit() :
          i = int(i)
          hex = i*(16**(n))
        if i == "a":
          hex = 10*(16**(n))
        if i == "b":
          hex = 11*(16**(n))
        if i == "c":
          hex = 12*(16**(n))
        if i == "d":
          hex = 13*(16**(n))
        if i == "e":
          hex = 14*(16**(n))
        if i == "f":
          hex = 15*(16**(n))

        res += hex
        n-=1
    return str(res)

def randomNumber(diff, mode):
  question = str()
  true_ans = str()

  if mode == 1:
    question = randomBinary(diff)
    true_ans = ansBinary(question) 
  if mode == 2: 
    question = randomOctal(diff)
    true_ans = ansOctal(question) 
  if mode == 3: 
    question = randomHex(diff)
    true_ans = ansHex(question) 
  
  return {
    "answer": true_ans,
    "question": "".join(question)
  }

def youWin(score):
  print("Your win!!!")
  score += 1
  print(f"Your Score is {score} {'🏆'*score}")
  return {
    "life" : False,
    "score" : score,
    "gameStart" : False
  }

def youLose(life,score):
  print("Your Lose!!!")
  life -= 1

  if life <= 0:
    print("Game Over!!!")
    print(f"Your Score is {score} {'🏆'*score}")
    input("Please enter to continuous")
  if life > 0:
    print(f"Your Score is {score} {'🏆'*score}")
    print(f"You have {life} left!! {'💖'*life}")
    return {
      "life" : life,
      "score" : False,
      "gameStart" : False
    }

  return {
    "life" : life,
    "score" : False,
    "gameStart" : True
  }

def enterAns(diff, mode) :
  questionSet = randomNumber(diff, mode)
  true_ans = questionSet["answer"]
  question = questionSet["question"]

  # start looping for user answer
  while True: 
    try:
      print(f"Your question is {question}")
      ans_from_user = int(input("please enter your answer: "))
    except:
      print("!!! please enter only base 10 number !!!")
    else:
      break
  # end looping for user answer

  ans_from_user = str(ans_from_user)
  if ans_from_user == true_ans:
    gameResult = youWin(score)
  else:
    print(f"The answer is {true_ans}")
    gameResult = youLose(life, score)

  return gameResult

# variables
gameStart = True
loopDiff = True
loopMode = True

# game start
while gameStart:

  # start looping to wrong typing for difficult
  while loopDiff:
    try:
      print(f"{'='*10} Finding Base Number!! {'='*10}")
      print("1.Easy")
      print("2.Normal")
      print("3.Hard")
      print("4.Exit")
      
      diff = int(input("Select your difficulty (1-3): "))
      if diff in range(1, 5):
        life = 5 #initial life
        score = 0 #initial score
        break
      else:
        raise ValueError
    except:
        print("!!! Please enter number in range 1 - 3 !!!")
  # end of the difficult loop

  if diff == 4: exit()

  # start looping to wrong typing for mode
  while loopMode:
    try:
      print(f"{'='*10} What would you like to play? {'='*10}")
      print("1.Binary")
      print("2.Octal")
      print("3.Hexadecimal")
      print("4.Reset")
      print("5.Exit")
      
      mode = int(input("Select Game Mode (1-3): "))
      if mode in range(1, 6) :
        break
      else: 
        raise ValueError
    except:
      print("!!! Please enter number in range 1 - 3 !!!")

  if mode == 5: exit()
  if mode == 4: 
    loopDiff = True
  else: 
    
    # end of the select mode loop and actually start the game
    gameResult = enterAns(diff, mode)
    if gameResult["life"] : life = gameResult["life"] 
    if gameResult["score"] : score = gameResult["score"] 
    loopDiff = gameResult["gameStart"]
