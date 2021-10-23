#
# Katherine Sanders - "CrisisConnect"
# Creatica 2021
# Congressional App Challenge 2021
# August 22
#
#

import time
import random
import functionsmodule

#------------------------possible responses
stopConnect = "QUIT"
#------------yes or no
yes = "YES"
yea = "YEA"
no = "NO"
dontKnow = "DONT KNOW"
#------------chat bot or coping mechanisms
hotline = "HOTLINE"
helpline = "HELPLINE"
coping = "COPING"
cope = "COPE"
#------------emotions
#---bad
sad = "SAD"
depressed = "DEPRESSED"
empty = "EMPTY"
numb = "NUMB"
bad = "BAD"
useless = "USELESS"
#---good
good = "GOOD"
okay = "OK"
better = "BETTER"
happy = "HAPPY"
calm = "CALM"
#------------check right responses
isHelpful = "IS HELPFUL"
wasHelpful = "WAS HELPFUL"
helpful = "HELPFUL"
keepTalking = "KEEP TALKING"
#------------key words 
abuseWord = "ABUSE"
suicideWord = "SUICID"
helpWord = "HELP"
dieWord = "DIE"
killWord = "KILL"
#-------------------------------NEW VARIABLES-----------------------
#----------------general terms
hate = "HATE"
life = "LIFE"
myself = "MYSELF"
cantLive = "CANT LIVE"
dont = "DONT"
idk = "IDK"
feel = "FEEL"
not1 = "NOT"
im = "IM"
want = "WANT"
#----------------domestic abuse
girlfriend = "GIRLFRIEND"
boyfriend = "BOYFRIEND"
bf = "BF"
gf = "GF"
partner = "PARTNER"
wife = "WIFE"
husband = "HUSBAND"
spouse = "SPOUSE"
mom = "MOM"
mother = "MOTHER"
dad = "DAD"
father = "FATHER"
sister = "SISTER"
brother = "BROTHER"
grandma = "GRANDMA"
grandpa = "GRANDPA"
family = "FAMILY"
hit = "HIT"
hurt = "HURT"
#---------------Rape, Incest 
touch = "TOUCH"
nonconsensual = "NONCONSENSUAL"
consent = "CONSENT"
grope = "GROP"
make = "MAKE"
#---------------LGBTQ & identity 
like = "LIKE"
love = "LOVE"
gay = "GAY"
gender = "GENDER"
#----------------substance abuse
drugs = "DRUGS"
alcohol = "ALCOHOL"
vape = "VAPE"
vaping = "VAPING"
#-----------------eating disorder/body image issues
cantEat = "CANT EAT"
wontEat = "WONT EAT"
throwUp = "THROW UP"
body = "BODY"
fat = "FAT"
disgusting = "DISGUSTING"
gross = "GROSS"
#--------------------------------

class UserInformation():
    def __init__(self, name):
        self.name = name


#------------------------introduction
print("\n")
print("Welcome to CrisisConnect. I will be here to guide you through your crisis.")
time.sleep(3.75)
print("\n")
print("Throughout this process, I will ask simple questions that will help clear your mind and lead you to the right helpline.")
time.sleep(4.25)
print("\n")
print("If you want to stop talking, type and enter 'quit' at anytime.")
time.sleep(3.75)
print("\n")

#------------------------chat bot or coping mechanisms?
print("Would you like to find a hotline, or look at some coping mechanisms today?")
chatDecideQ = raw_input("> ")
chatDecide = chatDecideQ.upper()

if coping in chatDecide:

    functionsmodule.breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    functionsmodule.interestsFunction()

    functionsmodule.goodbye()

elif cope in chatDecide:

    functionsmodule.breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    functionsmodule.interestsFunction()

    functionsmodule.goodbye()

elif stopConnect in chatDecide:
    exit()

elif abuseWord in chatDecide:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in chatDecide:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in chatDecide:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in chatDecide:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else:
    print("\n")
    print("I'm glad you reached out for help. I will ask you some questions to help guide you to the correct hotline.")
    time.sleep(4.75)
    print("\n")
    pass

#----------------------------what is the situation - see what it can do with a description. 
print("What is your situation, and how are you feeling?")
generalSituationQ = raw_input("> ")
generalSituation = generalSituationQ.upper()


if stopConnect in generalSituation:
    exit()
elif mom in generalSituation:
    if mom and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif mom and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif mom and touch in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif mom and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord or killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 
            users_name = UserInformation(name)
            print("\n")


        print("How is this making you feel?")
        howFeel1Q = raw_input("> ")
        howFeel1 = howFeel1Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel1:

            if sad or depressed in howFeel1: 
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel1: 
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif bad in howFeel1: 
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel1: 
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel1Q = raw_input("> ")
            generalCrisisYouthFeel1 = generalCrisisYouthFeel1Q.upper()

            if yes in generalCrisisYouthFeel1:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel1:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel1:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel1:
                exit()

            elif abuseWord in generalCrisisYouthFeel1:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel1:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel1:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel1:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel1:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel1:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif mother in generalSituation:

    if mother and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif mother and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif mother and touch in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif mother and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")
        
        print("How is this making you feel?")
        howFeel2Q = raw_input("> ")
        howFeel2 = howFeel2Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel2:

            if sad or depressed in howFeel2:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel2:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel2:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel2:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel2Q = raw_input("> ")
            generalCrisisYouthFeel2 = generalCrisisYouthFeel2Q.upper()

            if yes in generalCrisisYouthFeel2:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel2:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel2:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel2:
                exit()

            elif abuseWord in generalCrisisYouthFeel2:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel2:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel2:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel2:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel2:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel2:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif father in generalSituation:
    if father and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif father and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif father and touch in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif father and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel3Q = raw_input("> ")
        howFeel3 = howFeel3Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel3:

            if sad or depressed in howFeel3:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel3:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel3:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel3:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel3Q = raw_input("> ")
            generalCrisisYouthFeel3 = generalCrisisYouthFeel3Q.upper()

            if yes in generalCrisisYouthFeel3:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel3:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel3:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel3:
                exit()

            elif abuseWord in generalCrisisYouthFeel3:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel3:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel3:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel3:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel3:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel3:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif grandma in generalSituation:
    if grandma and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif grandma and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif grandma and touch in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif grandma and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel4Q = raw_input("> ")
        howFeel4 = howFeel4Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel4:

            if sad or depressed in howFeel4:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel4:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel4:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel4:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel4Q = raw_input("> ")
            generalCrisisYouthFeel4 = generalCrisisYouthFeel4Q.upper()

            if yes in generalCrisisYouthFeel4:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel4:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel4:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel4:
                exit()

            elif abuseWord in generalCrisisYouthFeel4:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel4:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel4:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel4:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel4:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel4:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif grandpa in generalSituation:
    if grandpa and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif grandpa and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    elif grandpa and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif grandpa and touch in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel6Q = raw_input("> ")
        howFeel6 = howFeel6Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel6:

            if sad or depressed in howFeel6:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel6:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel6:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel6:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel6Q = raw_input("> ")
            generalCrisisYouthFeel6 = generalCrisisYouthFeel6Q.upper()

            if yes in generalCrisisYouthFeel6:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel6:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel6:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel6:
                exit()

            elif abuseWord in generalCrisisYouthFeel6:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel6:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel6:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel6:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel6:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel6:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif dad in generalSituation:
    if dad and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif dad and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    elif dad and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif dad and touch in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel7Q = raw_input("> ")
        howFeel7 = howFeel7Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel7:

            if sad or depressed in howFeel7:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel7:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel7:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel7:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel7Q = raw_input("> ")
            generalCrisisYouthFeel7 = generalCrisisYouthFeel7Q.upper()

            if yes in generalCrisisYouthFeel7:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel7:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel7:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel7:
                exit()

            elif abuseWord in generalCrisisYouthFeel7:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel7:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel7:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel7:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel7:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel7:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif sister in generalSituation:
    if sister and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif sister and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    elif sister and touch in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif sister and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel8Q = raw_input("> ")
        howFeel8 = howFeel8Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel8:

            if sad or depressed in howFeel8:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel8:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel8:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel8:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel8Q = raw_input("> ")
            generalCrisisYouthFeel8 = generalCrisisYouthFeel8Q.upper()

            if yes in generalCrisisYouthFeel8:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel8:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel8:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel8:
                exit()

            elif abuseWord in generalCrisisYouthFeel8:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel8:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel8:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel8:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel8:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel8:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif brother in generalSituation:
    if brother and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif brother and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    elif brother and touch in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif brother and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.uicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.uicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel9Q = raw_input("> ")
        howFeel9 = howFeel9Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel9:

            if sad or depressed in howFeel9:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel9:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel9:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel9:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel9Q = raw_input("> ")
            generalCrisisYouthFeel9 = generalCrisisYouthFeel9Q.upper()

            if yes in generalCrisisYouthFeel9:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel9:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel9:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel9:
                exit()

            elif abuseWord in generalCrisisYouthFeel9:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel9:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel9:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel9:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel9:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel9:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif wife in generalSituation:
    if wife and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif wife and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif wife and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel10Q = raw_input("> ")
        howFeel10 = howFeel10Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel10:

            if sad or depressed in howFeel10:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel10:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel10:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel10:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel10Q = raw_input("> ")
            generalCrisisYouthFeel10 = generalCrisisYouthFeel10Q.upper()

            if yes in generalCrisisYouthFeel10:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel10:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel10:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel10:
                exit()

            elif abuseWord in generalCrisisYouthFeel10:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel10:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel10:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel10:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel10:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel10:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif husband in generalSituation:
    if husband and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif husband and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    elif husband and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel11Q = raw_input("> ")
        howFeel11 = howFeel11Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel11:

            if sad or depressed in howFeel11:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel11:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel11:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel11:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel11Q = raw_input("> ")
            generalCrisisYouthFeel11 = generalCrisisYouthFeel11Q.upper()

            if yes in generalCrisisYouthFeel11:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel11:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel11:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel11:
                exit()

            elif abuseWord in generalCrisisYouthFeel11:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel11:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel11:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel11:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel11:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel11:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif spouse in generalSituation:
    if spouse and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif spouse and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif spouse and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel12Q = raw_input("> ")
        howFeel12 = howFeel12Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel12:

            if sad or depressed in howFeel12:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel12:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel12:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel12:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel12Q = raw_input("> ")
            generalCrisisYouthFeel12 = generalCrisisYouthFeel12Q.upper()

            if yes in generalCrisisYouthFeel12:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel12:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel12:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel12:
                exit()

            elif abuseWord in generalCrisisYouthFeel12:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel12:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel12:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel12:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel12:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel12:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif body in generalSituation: 
    if body and hate in generalSituation:
        print("\n")
        functionsmodule.eatingDisorderFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif body and gross in generalSituation:
        print("\n")
        functionsmodule.eatingDisorderFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 

            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel13Q = raw_input("> ")
        howFeel13 = howFeel13Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel13:

            if sad or depressed in howFeel13:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel13:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel13:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel13:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)

            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel13Q = raw_input("> ")
            generalCrisisYouthFeel13 = generalCrisisYouthFeel13Q.upper()

            if yes in generalCrisisYouthFeel13:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel13:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel13:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel13:
                exit()

            elif abuseWord in generalCrisisYouthFeel13:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel13:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel13:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel13:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel13:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel13:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif family in generalSituation:
    if family and hurt in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif family and hit in generalSituation:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    elif family and touch in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()

    elif family and grope in generalSituation:
        print("\n")
        functionsmodule.rainnFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRightGeneral()

        functionsmodule.checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")

        print("What is your name?")
        name = raw_input('> ')

        if stopConnect in name:
            exit()

        elif abuseWord in name:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif want and dieWord in name:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else: 
            users_name = UserInformation(name)
            print("\n")

        print("How is this making you feel?")
        howFeel14Q = raw_input("> ")
        howFeel14 = howFeel14Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel14:

            if sad or depressed in howFeel14:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("The world is so much better with you in it.")
                print("\n")
                time.sleep(3)
                print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")

            elif empty or numb in howFeel14:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)
                
            elif bad in howFeel14:
                print("\n")
                print("I'm sorry you're feeling this way, %s. You are not alone."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for reaching out for help.")
                print("\n")
                time.sleep(3)

            elif useless in howFeel14:
                print("\n")
                print("The world is so much better with you in it, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
                print("\n")
                time.sleep(3)
                print("I'm proud of you.")
                print("\n")
                time.sleep(2)

            else: 
                print("\n")
                print("I'm sorry you're feeling this way, %s."%(users_name.name.capitalize()))
                print("\n")
                time.sleep(3)
                print("I admire you for finding help.")
                print("\n")
                time.sleep(3)
        
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel14Q = raw_input("> ")
            generalCrisisYouthFeel14 = generalCrisisYouthFeel14Q.upper()

            if yes in generalCrisisYouthFeel14:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif yea in generalCrisisYouthFeel14:
                print("\n")
                functionsmodule.youthLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif no in generalCrisisYouthFeel14:
                print("\n")
                functionsmodule.namiFunction()
                time.sleep(2)
                print("\n")
                functionsmodule.textLineFunction()
                time.sleep(2)
                print("\n")

                functionsmodule.checkRight()

            elif stopConnect in generalCrisisYouthFeel14:
                exit()

            elif abuseWord in generalCrisisYouthFeel14:
                print("\n")
                functionsmodule.domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif suicideWord in generalCrisisYouthFeel14:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif killWord in generalCrisisYouthFeel14:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif helpWord in generalCrisisYouthFeel14:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            elif want and dieWord in generalCrisisYouthFeel14:
                print("\n")
                functionsmodule.immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                functionsmodule.suicidePrevention()
                print("\n")
                time.sleep(2)

                functionsmodule.checkRight()

            else: 
                print("\n")
                pass

        elif want and dieWord in howFeel14:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif grope in generalSituation:
    print("\n")
    functionsmodule.rainnFunction()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()
    
elif nonconsensual in generalSituation:
    print("\n")
    functionsmodule.rainnFunction()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

#ED

elif fat in generalSituation: 
    print("\n")
    functionsmodule.eatingDisorderFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

elif wontEat in generalSituation: 
    print("\n")
    functionsmodule.eatingDisorderFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

elif throwUp in generalSituation: 
    print("\n")
    functionsmodule.eatingDisorderFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

elif cantEat in generalSituation: 
    print("\n")
    functionsmodule.eatingDisorderFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

#Substance abuse 

elif drugs in generalSituation: 
    print("\n")
    functionsmodule.substanceAbuseFunction()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

elif alcohol in generalSituation: 
    print("\n")
    functionsmodule.substanceAbuseFunction()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

elif vape in generalSituation: 
    print("\n")
    functionsmodule.substanceAbuseFunction()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

elif vaping in generalSituation: 
    print("\n")
    functionsmodule.substanceAbuseFunction()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

#LGBTQ and Trevor Project

elif gay in generalSituation: 
    print("\n")
    functionsmodule.identityIssuesFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.lgbtqFunction()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

elif gender in generalSituation:
    print("\n")
    functionsmodule.identityIssuesFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.lgbtqFunction()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

#hate life 

elif hate and life in generalSituation:
    print("\n")
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)
    functionsmodule.namiFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.textLineFunction()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRightGeneral()

    functionsmodule.checkRight()

#general emotions

elif sad or depressed in generalSituation:
    print("\n")
    print("I'm sorry you're feeling this way. You are not alone.")
    time.sleep(3)
    print("\n")
    print("The world is so much better with you in it.")
    time.sleep(3)
    print("\n")
    print("Overcoming feelings of sadness is really tough. It's progress to be reaching out like this.")
    time.sleep(3)
    print("\n")
    print("I'm proud of you.")
    time.sleep(2)

    print("\n")
    print("Would you like to talk to another teen about your feelings?")
    generalCrisisYouthFeel15Q = raw_input("> ")
    generalCrisisYouthFeel15 = generalCrisisYouthFeel15Q.upper()

    if yes in generalCrisisYouthFeel15:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif yea in generalCrisisYouthFeel15:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif no in generalCrisisYouthFeel15:
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif stopConnect in generalCrisisYouthFeel15:
        exit()

    elif abuseWord in generalCrisisYouthFeel15:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif suicideWord in generalCrisisYouthFeel15:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif killWord in generalCrisisYouthFeel15:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif helpWord in generalCrisisYouthFeel15:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif want and dieWord in generalCrisisYouthFeel15:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    else: 
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

elif empty or numb in generalSituation:
    print("\n")
    print("I'm sorry you're feeling this way. You are not alone.")
    print("\n")
    time.sleep(3)
    print("It's hard to approach these types of feelings. I admire you for reaching out for help.")
    print("\n")
    time.sleep(3)

    print("\n")
    print("Would you like to talk to another teen about your feelings?")
    generalCrisisYouthFeel16Q = raw_input("> ")
    generalCrisisYouthFeel16 = generalCrisisYouthFeel16Q.upper()

    if yes in generalCrisisYouthFeel16:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif yea in generalCrisisYouthFeel16:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif no in generalCrisisYouthFeel16:
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif stopConnect in generalCrisisYouthFeel16:
        exit()

    elif abuseWord in generalCrisisYouthFeel16:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif suicideWord in generalCrisisYouthFeel16:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif killWord in generalCrisisYouthFeel16:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif helpWord in generalCrisisYouthFeel16:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif want and dieWord in generalCrisisYouthFeel16:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    else: 
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

elif useless in generalSituation:
    print("\n")
    print("The world is so much better with you in it.")
    print("\n")
    time.sleep(3)
    print("What you're going through is real and hard. Reaching out for help was an admirable first step.")
    print("\n")
    time.sleep(3)
    print("I'm proud of you.")
    print("\n")
    time.sleep(2)

    print("\n")
    print("Would you like to talk to another teen about your feelings?")
    generalCrisisYouthFeel17Q = raw_input("> ")
    generalCrisisYouthFeel17 = generalCrisisYouthFeel17Q.upper()

    if yes in generalCrisisYouthFeel17:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif yea in generalCrisisYouthFeel17:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif no in generalCrisisYouthFeel17:
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif stopConnect in generalCrisisYouthFeel17:
        exit()

    elif abuseWord in generalCrisisYouthFeel17:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif suicideWord in generalCrisisYouthFeel17:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif killWord in generalCrisisYouthFeel17:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif helpWord in generalCrisisYouthFeel17:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif want and dieWord in generalCrisisYouthFeel17:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    else: 
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

elif bad in generalSituation:
    print("\n")
    print("I'm sorry you're feeling this way. You are not alone.")
    print("\n")
    time.sleep(3)
    print("I admire you for reaching out for help.")
    print("\n")
    time.sleep(3)

    print("\n")
    print("Would you like to talk to another teen about your feelings?")
    generalCrisisYouthFeel18Q = raw_input("> ")
    generalCrisisYouthFeel18 = generalCrisisYouthFeel18Q.upper()

    if yes in generalCrisisYouthFeel18:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif yea in generalCrisisYouthFeel18:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif no in generalCrisisYouthFeel18:
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif stopConnect in generalCrisisYouthFeel18:
        exit()

    elif abuseWord in generalCrisisYouthFeel18:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif suicideWord in generalCrisisYouthFeel18:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif killWord in generalCrisisYouthFeel18:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif helpWord in generalCrisisYouthFeel18:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif want and dieWord in generalCrisisYouthFeel18:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    else: 
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

elif abuseWord in generalSituation:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in generalSituation:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in generalSituation:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in generalSituation:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in generalSituation:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else:
    print("\n")
    print("I'm sorry that's happening to you.")
    time.sleep(2)
    print("\n")
    print("I'll be asking some yes or no questions to help you to the best of my abilities.")
    time.sleep(2)
    print("\n")



#-------------------------------------are you in immediate danger?
print("Are you currently thinking about hurting yourself or others?")
emergencyQ = raw_input("> ")
immediateEmergency = emergencyQ.upper()

if yes in immediateEmergency:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(3.5)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(3.5)

    functionsmodule.checkRight()

elif yea in immediateEmergency:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(3.5)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(3.5)

    functionsmodule.checkRight()


elif no in immediateEmergency:
    print("\n")
    print("I am glad you're keeping yourself and others safe.")
    print("\n")
    time.sleep(2.5)

elif stopConnect in immediateEmergency:
    exit()

elif abuseWord in immediateEmergency:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in immediateEmergency:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in immediateEmergency:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in immediateEmergency:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in immediateEmergency:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else:
    pass 


#------------------------check if they can talk 
print("Are you able to talk out loud?")
talkAloudQ = raw_input("> ")
talkAloud = talkAloudQ.upper()

if no in talkAloud:
    print("\n")
    functionsmodule.cantTalk()
    print("\n")

    #check right

    print("Are you completely sure you still cannot talk aloud?")
    checkTalkAloudQ = raw_input("> ")
    checkTalkAloud = checkTalkAloudQ.upper()

    if no in checkTalkAloud:
        print("The text hotline is a great resource for when you cannot talk aloud on the phone.")
        time.sleep(2)
        print("\n")
        print("Text 'HOME' to 741741")
        time.sleep(1.75)
        print("\n")
        print("The following questions will provide hotlines that require you to talk aloud. However, we will continue to chat.")
        time.sleep(2)
        print("\n")
    elif yes in checkTalkAloud: 
        print("\n")
        print("The following questions will provide hotlines that require you to talk aloud. We will continue to chat.")
        time.sleep(2)
    elif yea in checkTalkAloud: 
        print("\n")
        print("The following questions will provide hotlines that require you to talk aloud. We will continue to chat.")
        time.sleep(2)

    elif stopConnect in checkTalkAloud:
        exit()

    elif abuseWord in checkTalkAloud:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif suicideWord in checkTalkAloud:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif killWord in checkTalkAloud:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif helpWord in checkTalkAloud:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif want and dieWord in checkTalkAloud:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

elif yea in talkAloud:
    pass

elif yes in talkAloud:
    pass

elif stopConnect in talkAloud:
    exit()

elif abuseWord in talkAloud:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in talkAloud:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in talkAloud:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in talkAloud:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in talkAloud:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else:
    pass


#------------------------domestic abuse
print("\n")
print("Are you in a safe environment with people you trust?")
safeEnvironmentQ = raw_input("> ")
safeEnvironment = safeEnvironmentQ.upper()

if no in safeEnvironment: 
    print("\n")
    print("Is a family member, romantic partner, or platonic partner causing you to be in danger?")
    domesticAbuseQ = raw_input("> ")
    domesticAbuse = domesticAbuseQ.upper()

    if yes in domesticAbuse:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        time.sleep(3.5)
        print("\n")

        print("\n")
        functionsmodule.rainnFunction()
        time.sleep(3.5)
        print("\n")
        
        functionsmodule.checkRight()

    elif yea in domesticAbuse:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        time.sleep(3.5)
        print("\n")

        print("\n")
        functionsmodule.rainnFunction()
        time.sleep(3.5)
        print("\n")
        
        functionsmodule.checkRight()
        
    elif no in domesticAbuse:
        print("\n")
        print("Are you fearful for the safety of yourself or others?")
        abuseQ = raw_input("> ")
        abuse = abuseQ.upper()

        if yes or yea in abuse:
            print("\n")
            functionsmodule.abuseFunction()
            time.sleep(3.5)
            print("\n")

            print("\n")
            functionsmodule.rainnFunction()
            time.sleep(3.5)
            print("\n")
            
            functionsmodule.checkRight()

        elif yea in abuse:
            print("\n")
            functionsmodule.abuseFunction()
            time.sleep(3.5)
            print("\n")

            print("\n")
            functionsmodule.rainnFunction()
            time.sleep(3.5)
            print("\n")
            
            functionsmodule.checkRight()

        elif stopConnect in abuse:
            exit()
        
        elif abuseWord in abuse:
            print("\n")
            functionsmodule.domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif suicideWord in abuse:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif killWord in abuse:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()

        elif helpWord in abuse:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()
        
        elif want and dieWord in abuse:
            print("\n")
            functionsmodule.immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            functionsmodule.suicidePrevention()
            print("\n")
            time.sleep(2)

            functionsmodule.checkRight()
        
        else:
            pass

    elif stopConnect in domesticAbuse:
        exit()
    
    elif abuseWord in domesticAbuse:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif suicideWord in domesticAbuse:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif killWord in domesticAbuse:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif helpWord in domesticAbuse:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif want and dieWord in domesticAbuse:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

elif yes in safeEnvironment: 
    print("\n")
    print("I'm glad you're in a safe environment.")
    time.sleep(1.5)

elif yea in safeEnvironment: 
    print("\n")
    print("I'm glad you're in a safe environment.")
    time.sleep(1.5)

elif stopConnect in safeEnvironment:
    exit()

elif abuseWord in safeEnvironment:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in safeEnvironment:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in safeEnvironment:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in safeEnvironment:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in safeEnvironment:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else:
    pass 


#------------------------hurting others
print("\n")
print("Do you fear that you are putting others in danger?")
othersSafetyQ = raw_input("> ")
othersSafety = othersSafetyQ.upper()

if no in othersSafety:
    print("\n")
    pass

elif yes in othersSafety:
    print("\n")
    print("The National Domestic Hotline can also be used if you feel you are causing pain and want to stop.")
    time.sleep(3.75)
    print("\n")
    print("When you call, you can talk about your situation without fear of judgement, and brainstorm ideas on how to help you be safe.")
    time.sleep(4.25)
    print("\n")
    print("DOMESTIC ABUSE HOTLINE: (800) 799-7233 or Text 'LOVEIS' to 22522")

    functionsmodule.checkRight()

elif yea in othersSafety:
    print("\n")
    print("The National Domestic Hotline can also be used if you feel you are causing pain and want to stop.")
    time.sleep(3.75)
    print("\n")
    print("When you call, you can talk about your situation without fear of judgement, and brainstorm ideas on how to help you be safe.")
    time.sleep(4.25)
    print("\n")
    print("DOMESTIC ABUSE HOTLINE: (800) 799-7233 or Text 'LOVEIS' to 22522")

    functionsmodule.checkRight()

elif stopConnect in othersSafety:
    exit()

elif abuseWord in othersSafety:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in othersSafety:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in othersSafety:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in othersSafety:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    functionsmodule.time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in othersSafety:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else:
    print("\n")
    pass


#------------------------identity issues
print("Are you or someone you know dealing with any identity issues?")
identityIssuesQ = raw_input("> ")
identityIssues = identityIssuesQ.upper()

if yes in identityIssues:
    print("\n")
    functionsmodule.identityIssuesFunction()
    time.sleep(3)
    print("\n")

    functionsmodule.lgbtqFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif yea in identityIssues:
    print("\n")
    functionsmodule.identityIssuesFunction()
    time.sleep(3)
    print("\n")

    functionsmodule.lgbtqFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif no in identityIssues: 
    print("\n")
    pass

elif stopConnect in identityIssues:
    exit()

elif abuseWord in identityIssues:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in identityIssues:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in identityIssues:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in identityIssues:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in identityIssues:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else: 
    print("\n")
    pass 


#------------------------substance abuse
print("Are you or someone you know struggling with substance issues: drinking excessively, smoking, etc.?")
substanceAbuseQ = raw_input("> ")
substanceAbuse = substanceAbuseQ.upper()

if yes in substanceAbuse:
    print("\n")
    functionsmodule.substanceAbuseFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif yea in substanceAbuse:
    print("\n")
    functionsmodule.substanceAbuseFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif no in substanceAbuse: 
    print("\n")
    pass

elif stopConnect in substanceAbuse:
    exit()

elif abuseWord in substanceAbuse:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in substanceAbuse:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in substanceAbuse:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in substanceAbuse:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in substanceAbuse:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else: 
    print("\n")
    pass 


#------------------------eating disorder
print("Are you or someone you know struggling with an eating disorder or body image?")
eatingDisorderQ = raw_input("> ")
eatingDisorder = eatingDisorderQ.upper()

if yes in eatingDisorder:
    print("\n")
    functionsmodule.eatingDisorderFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif yea in eatingDisorder:
    print("\n")
    functionsmodule.eatingDisorderFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif no in eatingDisorder: 
    print("\n")
    pass

elif stopConnect in eatingDisorder:
    exit()

elif abuseWord in eatingDisorder:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in eatingDisorder:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in eatingDisorder:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in eatingDisorder:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in eatingDisorder:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else: 
    print("\n")
    pass 


#------------------------runaway/homelessness
print("Have you or someone you know ran away from home or do not have a home to go to?")
runawayQ = raw_input("> ")
runaway = runawayQ.upper()

if yes in runaway:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    time.sleep(2)
    print("\n")

    print("\n")
    functionsmodule.runawayFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif yea in runaway:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    time.sleep(2)
    print("\n")

    print("\n")
    functionsmodule.runawayFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif no in runaway: 
    print("\n")
    pass

elif stopConnect in runaway:
    exit()

elif abuseWord in runaway:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in runaway:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in runaway:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in runaway:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in runaway:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else: 
    print("\n")
    pass 


#------------------------racial discrimination
print("Are you being discriminated against due to your race?")
racialEquityQ = raw_input("> ")
racialEquity = racialEquityQ.upper()

if yes in racialEquity:
    print("\n")
    functionsmodule.racialEquityFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif yea in racialEquity:
    print("\n")
    functionsmodule.racialEquityFunction()
    time.sleep(2)
    print("\n")

    functionsmodule.checkRight()

elif stopConnect in racialEquity:
    exit()

elif abuseWord in racialEquity:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in racialEquity:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in racialEquity:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in racialEquity:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in racialEquity:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()


elif no in racialEquity:
    print("\n")
    pass


else: 
    print("\n")
    pass


#------------------------general crisis - asking emotions
print("How are you feeling right now?")
generalCrisisQ = raw_input("> ")
generalCrisis = generalCrisisQ.upper()

if sad or depressed or empty or numb or bad or useless in generalCrisis:
    print("\n")
    print("Would you like to talk to another teen about your feelings?")
    generalCrisisYouthQ = raw_input("> ")
    generalCrisisYouth = generalCrisisYouthQ.upper()

    if yes in generalCrisisYouth:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif yea in generalCrisisYouth:
        print("\n")
        functionsmodule.youthLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif no in generalCrisisYouth:
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()

    elif stopConnect in generalCrisisYouth:
        exit()

    elif abuseWord in generalCrisisYouth:
        print("\n")
        functionsmodule.domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif suicideWord in generalCrisisYouth:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif killWord in generalCrisisYouth:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif helpWord in generalCrisisYouth:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    elif want and dieWord in generalCrisisYouth:
        print("\n")
        functionsmodule.immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        functionsmodule.suicidePrevention()
        print("\n")
        time.sleep(2)

        functionsmodule.checkRight()

    else: 
        print("\n")
        functionsmodule.namiFunction()
        time.sleep(2)
        print("\n")
        functionsmodule.textLineFunction()
        time.sleep(2)
        print("\n")

        functionsmodule.checkRight()



elif good or okay or better or happy or calm in generalCrisis:
    print("I am so glad you are feeling better!")
    time.sleep(2)
    print("\n")
    print("Before you go, let's walk through some coping mechanisms.")
    time.sleep(3)

    functionsmodule.breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    functionsmodule.interestsFunction()

    functionsmodule.goodbye()

elif stopConnect in generalCrisis:
    exit()

elif abuseWord in generalCrisis:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in generalCrisis:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in generalCrisis:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in generalCrisis:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in generalCrisis:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else: 
    print("\n")
    pass 


# add an overall question about mood that directly points to the previous hotlines 
print("Are you feeling better?")
feelingOverallQ = raw_input("> ")
feelingOverall = feelingOverallQ.upper()

if yes in feelingOverall:
    #------------------------final support/coping mechanisms
    print("\n")
    print("I am so glad you are feeling better!")
    time.sleep(2)
    print("\n")
    print("Before you go, let's walk through some coping mechanisms.")
    time.sleep(3)

    functionsmodule.breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    functionsmodule.interestsFunction()

    functionsmodule.goodbye()

elif yea in feelingOverall:
    #------------------------final support/coping mechanisms
    print("\n")
    print("I am so glad you are feeling better!")
    time.sleep(2)
    print("\n")
    print("Before you go, let's walk through some coping mechanisms.")
    time.sleep(3)

    functionsmodule.breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    functionsmodule.interestsFunction()

    functionsmodule.goodbye()

elif stopConnect in feelingOverall:
    exit()

elif abuseWord in feelingOverall:
    print("\n")
    functionsmodule.domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif suicideWord in feelingOverall:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif killWord in feelingOverall:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif helpWord in feelingOverall:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

elif want and dieWord in feelingOverall:
    print("\n")
    functionsmodule.immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    functionsmodule.suicidePrevention()
    print("\n")
    time.sleep(2)

    functionsmodule.checkRight()

else:
    print("Before you go, let's walk through some coping mechanisms.")
    time.sleep(3)

    functionsmodule.breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    functionsmodule.interestsFunction()

    functionsmodule.goodbye()
