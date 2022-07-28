import random
from tokenize import String

# ======================================= Random Question =======================================
def randombinary(diff):
    list = []
    if diff == 1 :
        number_digits = 4
    elif diff == 2 :
        number_digits = 6
    else :
        number_digits=8
    for x in range(number_digits):
        list.append(random.randint(0,1))
    return list

def randomoctal(diff):
    list = []
    if diff == 1 :
        number_digits = 2
    elif diff == 2 :
        number_digits = 3
    else :
        number_digits=6
    for x in range(number_digits):
        list.append(random.randint(0,7))
    return list

def randomhex(diff):
    list = []
    if diff == 1 :
        number_digits = 2
    elif diff == 2 :
        number_digits = 3
    else :
        number_digits=4
    hexlist = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
    for x in range(number_digits):
        list.append(random.choice(hexlist))
    return list
###
#Paramiter diff คือ ระดับความยาก
#number_digits คือ ตัวแปลที่เกบค่าจำนวนตัวเลบว่าควรมีกี่หลัก
###

# ======================================= Check Condition =======================================
def chkmode(mode,diff):
    if mode == 1 :
        return randombinary(diff)
    elif mode == 2 :
        return randomoctal(diff)
    else:
        return randomhex(diff)
def chkbinary(question):
    decimal = 0
    for digit in question:
        decimal = decimal*2 + int(digit)
    return decimal

def chkoctal(question):
    octal = 0
    res=0
    n=len(question)-1
    for i in question :
        octal = i*(8**(n))
        res+=octal
        n-=1
    return res

def chkhex(question):
    hex = int(0)
    res= int(0)
    n=len(question)-1
    for i in question :
        if i == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 :
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
    return res
###
#Paramiter question คือ Paramiter ที่รับค่าของดจทย์ที่สุ่มมาเอามาหาคำตอบ
#res คือตัวแปลที่เกบค่าผลรับเอาไว้แล้วส่งค่ากลับไป
###

# ======================================= Condition ressult in game ======================================= 

def win(score,life):
    score += 1 
    print("✅✅✅ You Win ✅✅✅ ")
    print(f'Your score is {score} {"🏆"*score}')
    print("Your life is","💖"*life)
    return score

def lose(life,score):
    print("❌❌❌ You Loss ❌❌❌")
    life -=1
    
    print("Your life is","💖"*life)
    print(f'Your score is {score} {"🏆"*score}')
    return life
   
def chklife(life):
    if life == 0 :
        print(f'Game Over')
        return False
    else :
        return True
def regame():
    return True
def rescore():
    return 0
def relife():
    return 5


# ======================================= Main game =======================================


chkgame = regame()
chkdiff = True
run = True
life = relife()
score = rescore()
strlist = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
chkans = True
testmode = True
# ======================================= Game Start =======================================

while chkgame :
    testmode = True
    chkans = True
    chkdiff = True
    print("===== Select difficult =====")
    print("1.Easy")
    print("2.Normal")
    print("3.Hard")
    print("4.Exit")
    while chkdiff :
        try:
            input_diff=input("Select Your difficult or exit (1-4):")
            if input_diff.isdigit() :
                diff = int(input_diff)
                chkdiff = False                            
                if diff < 0 or diff > 4 :
                    print("Please enter only number(1-4)")
                    chkdiff = True 
                elif diff == 4 :
                    print(f'Your score is {score} {"🏆"*score}')
                    exit()
            else : print("Please enter only number(1-4)")
        except exit():
            pass
        
        
        
    
    
    if diff == 4 : exit()
    if diff in range(1,5):
        chkgame = False 
        while run :
            print("===== Select Mode =====")
            print("1.Binary")
            print("2.Octal")
            print("3.Hexadecimal")
            print("4.Reset")
            print("5.Exit")
            
            while testmode :
                try:
                    input_mode=input("Select Your Mode or exit (1-5):")
                    if input_mode.isdigit() :
                        mode = int(input_mode)
                        print(mode)
                        testmode = False
                        if mode == 4 : 
                            chkgame = regame()
                            life = relife()
                            score = rescore()
                            testmode = False
                            break                           
                        if mode < 0 or mode > 5 :
                            print("Please enter only number(1-5)")
                            testmode = True 
                    else : print("Please enter only number(1-5)")
                except ValueError:
                    pass                     
                    
                    
            if mode == 4 : 
                chkgame = regame()
                life = relife()
                score = rescore()
                
                break 
                    
            if mode in range(1,6):
                if mode == 5 :
                    print(f'Your score is {score} {"🏆"*score}')
                    break
                else :
                    question = chkmode(mode,diff)
                    print("question is : ", end="")
                    for x in question:
                        print(x, end="")
                    print()
                    while chkans :
                        chkfrist=input("Enter your Answer :")
                        if chkfrist.isdigit() :
                            ans = int(chkfrist)
                            chkans = False                            
                        else :
                            print("Please enter only number")
                            chkans = True
                    if mode == 1 :
                        if ans==chkbinary(question) :
                            score=win(score,life)
                            print(f'Right answer is {chkbinary(question)}')
                        else :
                            life = lose(life,score)
                            run = chklife(life)
                            ans=chkbinary(question)
                            print(f'Right answer is {ans}')
                    elif mode == 2 :
                        if ans==int(chkoctal(question)) :
                            score=win(score,life)
                            print(f'Right answer is {chkoctal(question)}')
                        else :
                            life = lose(life,score)
                            run = chklife(life)
                            ans=chkoctal(question)
                            print(f'Right answer is {ans}')
                    else  :
                        if ans==int(chkhex(question)) :
                            score=win(score,life)
                            print(f'Right answer is {chkhex(question)}')
                        else :
                            life = lose(life,score)
                            run = chklife(life)
                            ans=chkhex(question)
                            print(f'Right answer is {ans}')
            testmode = True
            chkans = True
            chkdiff = True