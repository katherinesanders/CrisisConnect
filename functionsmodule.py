import random
import time

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
deadWord = "DEAD"
#------------interests responses
shows = "SHOWS"
movies = "MOVIES"
reading = "READING"
music = "MUSIC"
draw = "DRAW"
write = "WRITE"
sleep = "SLEEP"
eat = "EAT"
food = "FOOD"
nothing = "NOTHING"
prompts = ["Challenges", "Gratitude", "Elementary School", "Fear", "The Past", "The Present", "The Future", "Religion", "Environment"]
activities = ["Paint a random object", "Go outside without shoes on", "Sew something"]
activities1 = ["Meditate", "Online shop", "Organize your space", "Redecorate"]
activities2 = ["Learn a new skill", "Play video games"]



def immediateEmergencyFunction():
    print("If you or someone else is in serious danger, contact 911.")

def suicidePrevention():
    print("If you are thinking of hurting yourself, are worried about a loved one, or need emotional support, the National Suicide Prevention Hotline is available at all times in the US.")
    time.sleep(5)
    print("\n")
    print("NATIONAL SUICIDE PREVENTION HOTLINE: (800) 273-8255")

def domesticAbuseFunction():
    print("The domestic abuse hotline will connect you to a professional to have a conversation about how you are being treated by those you currently live with.")
    time.sleep(5)
    print("\n")
    print("When you call, you can talk about your situation without fear of judgement, and brainstorm ideas on how to help you become safe.")
    time.sleep(4.25)
    print("\n")
    print("DOMESTIC ABUSE HOTLINE: (800) 799-7233 or Text 'LOVEIS' to 22522")

def abuseFunction():
    print("If you or someone you know is being abused:")
    time.sleep(2)
    print("\n")
    print("CALL or TEXT the CHILD ABUSE HOTLINE: (800) 422-4453")

def rainnFunction():
    print("RAINN, or the Rape, Abuse & Incest National Network, offers a 24/7 hotline to support survivors of sexual violence.")
    time.sleep(3.5)
    print("\n")
    print("RAINN HOTLINE: 1-800-656-4673")

def identityIssuesFunction():
    print("The Trevor Project is a non-profit focused on preventing suicide among LGBTQ+ and questioning youth.")
    time.sleep(3.25)
    print("\n")
    print("They offer a free 24/7 confidential hotline.")
    time.sleep(2.25)
    print("\n")
    print("TREVOR PROJECT HOTLINE: 1-866-488-7386")
    time.sleep(1.5)
    print("\n")
    print("TREVOR PROJECT TEXT-LINE: Text 'START' to 678678")

def lgbtqFunction():
    print("The LGBTQ+ Hotline is a free hotline for teens with questions about their sexuality.")
    time.sleep(3.25)
    print("\n")
    print("This hotline is available for certain hours on certain days.")
    time.sleep(2)
    print("\n")
    print("MONDAY - FRIDAY: 1:00pm to 9:00pm PST")
    print("SATURDAY: 9:00am to 2:00pm PST")
    time.sleep(3)
    print("\n")
    print("LGBTQ HOTLINE: 1-888-843-4564")

def substanceAbuseFunction():
    print("SAMHSA stands for 'Substance Abuse and Mental Health Services Administration'.")
    time.sleep(3.5)
    print("\n")
    print("They offer a free 24/7 confidential hotline.")
    time.sleep(2)
    print("\n")
    print("SAMHSA HELPLINE: 1-800-662-4357")

def eatingDisorderFunction():
    print("The National Eating Disorders Association, or NEDA, is a nonprofit organization that works to help teens struggling with eating disorders and body image.")
    time.sleep(5)
    print("\n")
    print("The hotline is open Monday through Friday.")
    time.sleep(2)
    print("\n")
    print("NEDA HELPLINE: 1-800-931-2237")

def namiFunction():
    print("NAMI is the National Alliance on Mental Illness.")
    time.sleep(2.25)
    print("\n")
    print("It is a peer support hotline, and can offer care and identify resources.")
    time.sleep(3)
    print("\n")
    print("This hotline is available only for certain hours on certain days.")
    time.sleep(2)
    print("\n")
    print("MONDAY - FRIDAY: 7:00am to 5:00pm PST")
    time.sleep(3)
    print("\n")
    print("NAMI HOTLINE: 1-800-950-6264")

def runawayFunction():
    print("If you or someone you know needs help with finding a home or has runaway from home, contact the National Runaway Safeline.")
    time.sleep(3.5)
    print("\n")
    print("NATIONAL RUNAWAY SAFELINE: 1-800-786-2929")

def racialEquityFunction():
    print("The Racial Equity Support Line offers support to those who are experience discrimination due to their background.")
    time.sleep(3.5)
    print("\n")
    print("RACIAL EQUITY SUPPORT LINE: 503-575-3764")

def youthLineFunction():
    print("The Youth Line is a crisis hotline for teens to talk to other teens while in a crisis.")
    time.sleep(2.75)
    print("\n")
    print("YOUTH HOTLINE: 877-968-8491")
    time.sleep(2)
    print("\n")
    print("YOUTH TEXT LINE: Text 'teen2teen' to 839863")

def textLineFunction():
    print("The crisis text-line is a 24 hour text service for every crisis. A trained responder will help guide you.")
    time.sleep(3.25)
    print("\n")
    print("CRISIS TEXT-LINE: Text 'HOME' or 'LEV' to 741741")
    time.sleep(2.5)

def cantTalk():
    print("If you cannot talk, the crisis text-line is a 24 hour text service for all crisis, and will guide you through yours.")
    time.sleep(4.25)
    print("\n")
    print("CRISIS TEXT-LINE: Text 'HOME' or 'LEV' to 741741")
    time.sleep(2.5)

def breathingExercise478():
    print("\n")
    print("First, let's do some breathing exercises:")
    time.sleep(2)
    print("\n")
    print("Breathe in...")
    time.sleep(1.5)
    print("\n")
    print("2")
    time.sleep(1)
    print("\n")
    print("3")
    time.sleep(1)
    print("\n")
    print("4")
    time.sleep(1.75)
    print("\n")
    print("Hold...")
    time.sleep(1.5)
    print("\n")
    print("2")
    time.sleep(1)
    print("\n")
    print("3")
    time.sleep(1)
    print("\n")
    print("4")
    time.sleep(1)
    print("\n")
    print("5")
    time.sleep(1)
    print("\n")
    print("6")
    time.sleep(1)
    print("\n")
    print("7")
    time.sleep(1.75)
    print("\n")
    print("And release...")
    time.sleep(1)
    print("\n")
    print("2")
    time.sleep(1)
    print("\n")
    print("3")
    time.sleep(1)
    print("\n")
    print("4")
    time.sleep(1)
    print("\n")
    print("5")
    time.sleep(1)
    print("\n")
    print("6")
    time.sleep(1)
    print("\n")
    print("7")
    time.sleep(1)
    print("\n")
    print("8")
    time.sleep(1.75)
    print("\n")

def interestsFunction():
    print("What are some things that make you happy?")
    interestsQ = raw_input("> ")
    interests = interestsQ.upper()

    interestsResponse = interests.split()

    if sleep in interestsResponse:
        print("\n")
        print("Ah yes. Sleep is really nice.")
        time.sleep(2)
        print("\n")
        print("I recommend you draw, write, watch a show, or listen to some music before you sleep if you aren't feeling completely well.")
        time.sleep(4)
        print("\n")
        print("After that, you should take a big, long nap: you deserve it.")
        time.sleep(2.5)
        print("\n")

        
        print("\n")
        print("I challenge you to do something knew.")
        time.sleep(2.5)
        print("\n")
        print("I will randomize an easy activity for you to do:")
        time.sleep(2)
        print(random.choice(activities))
        time.sleep(4)
        print("\n")

        print("Do you want another activity?")
        another1ActivityQ = raw_input("> ")
        another1Activity = another1ActivityQ.upper()

        if yes in another1Activity:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            another1Activity1Q = raw_input("> ")
            another1Activity1 = another1Activity1Q.upper()

            if yes in another1Activity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in another1Activity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif no in another1Activity1:
                pass
            elif stopConnect in another1Activity1:
                exit()
            else: 
                pass

        elif yea in another1Activity:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            another1Activity1_2Q = raw_input("> ")
            another1Activity1_2 = another1Activity1_2Q.upper()

            if yes in another1Activity1_2:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in another1Activity1_2:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif no in another1Activity1_2:
                pass
            elif stopConnect in another1Activity1_2:
                exit()
            else: 
                pass
        elif stopConnect in another1Activity:
            exit()
        elif no in another1Activity:
                pass
        else: 
            pass
    elif stopConnect in interestsResponse:
        exit()
    else:
        pass

    if shows in interestsResponse:
        print("\n")
        print("Spoil yourself to your favorite movie or rewatch your favorite TV show - or start a new one.")
        time.sleep(3)
        print("\n")
        print("If you don't have anything to watch right now, here are some of my favorite shows right now:")
        time.sleep(2.5)
        print("\n")
        print("Never Have I Ever - Netflix \n") 
        time.sleep(1)
        print("Get Even - Netflix \n")
        time.sleep(1)
        print("You - Netflix, Prime \n")
        time.sleep(1)
        print("Making the Cut - Prime \n")
        time.sleep(1)
        print("Manifest - Netflix, Hulu \n")
        time.sleep(4)
        print("\n")
    else: 
        pass
    
    if reading in interestsResponse: 
        print("\n")
        print("Try to dig up an old book from your childhood and reread it.")
        time.sleep(4)
        print("\n")
    else: 
        pass

    if music in interestsResponse: 
        print("\n")
        print("Treat yourself to 30 minutes of listening to music.")
        time.sleep(2)
        print("\n")
        print("Or, create your own music!")
        time.sleep(4)
        print("\n")
    else:
        pass

    if write in interestsResponse: 
        print("\n")
        print("Journal for 5 minutes. I will randomly choose a word for you, and you write what comes to mind:")
        time.sleep(3)
        print("\n")
        print("Your prompt is:")
        print(random.choice(prompts))
        time.sleep(4)
        print("\n")
    else:
        pass

    if draw in interestsResponse:
        print("\n")
        print("Draw for 30 minutes. I will randomly choose a word for you, and you draw what comes to mind:")
        time.sleep(3)
        print("\n")
        print("Your prompt is:")
        print(random.choice(prompts))
        time.sleep(4)
        print("\n")
    else:
        pass

    if eat in interestsResponse:
        print("\n")
        print("I challenge you to create something knew.")
        time.sleep(2.5)
        print("What's something you've always wanted to try? Try to create a new meal out of the things you have at home!")
        time.sleep(4)
        print("\n")
    else:
        pass

    if dontKnow in interestsResponse:
        print("\n")
        print("I challenge you to do something knew.")
        time.sleep(2.5)
        print("\n")
        print("I will randomize an easy activity for you to do:")
        time.sleep(2)
        print(random.choice(activities))
        time.sleep(4)
        print("\n")

        print("Do you want another activity?")
        anotherActivityQ = raw_input("> ")
        anotherActivity = anotherActivityQ.upper()

        if yes in anotherActivity:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            anotherActivity1Q = raw_input("> ")
            anotherActivity1 = anotherActivity1Q.upper()

            if yes in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif stopConnect in anotherActivity1:
                exit()
            else: 
                pass

        elif yea in anotherActivity:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            anotherActivity1_2Q = raw_input("> ")
            anotherActivity1_2 = anotherActivity1_2Q.upper()

            if yes in anotherActivity1_2:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity1_2:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif stopConnect in anotherActivity1_2:
                exit()
            else: 
                pass
        elif stopConnect in anotherActivity:
            exit()
        else: 
            pass

    #or isnt working
    elif nothing in interestsResponse:
        print("\n")
        print("I challenge you to do something knew.")
        time.sleep(2.5)
        print("\n")
        print("I will randomize an easy activity for you to do:")
        time.sleep(2)
        print(random.choice(activities))
        time.sleep(4)
        print("\n")

        print("Do you want another activity?")
        anotherActivity2Q = raw_input("> ")
        anotherActivity2 = anotherActivity2Q.upper()

        if yes in anotherActivity2:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            anotherActivity2_1Q = raw_input("> ")
            anotherActivity2_1 = anotherActivity2_1Q.upper()

            if yes in anotherActivity2_1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity2_1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif stopConnect in anotherActivity2_1:
                exit()
            else: 
                pass

        elif yea in anotherActivity2:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            anotherActivity2_2Q = raw_input("> ")
            anotherActivity2_2 = anotherActivity2_2Q.upper()

            if yes in anotherActivity2_2:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity2_2:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif stopConnect in anotherActivity2_2:
                exit()
            else: 
                pass
        elif stopConnect in anotherActivity2:
            exit()
        else: 
            pass
    elif stopConnect in interestsResponse:
        exit()
    else:
        pass


    if stopConnect in interestsResponse: 
        exit()
    else:
        pass

    if abuseWord in interestsResponse:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()
    else:
        pass

    if suicideWord in interestsResponse:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()
    else:
        pass

    if killWord in interestsResponse:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()
    else:
        pass

    if helpWord in interestsResponse:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()
    else:
        pass

def goodbye():
    print("\n")
    print("I hope you found the help you needed. You are an important part of this world. <3")
    time.sleep(2)
    print("\n")
    print("Goodbye!")
    print("\n")
    exit()

def checkRightGeneral():
    print("Was this information helpful, or would you like to keep talking?")
    checkRightGeneralResponse = raw_input("> ")
    checkRightGeneralAnswer = checkRightGeneralResponse.upper()

    if wasHelpful or isHelpful or helpful in checkRightGeneralAnswer:
        print("\n")
        print("I hope you found the help you needed. You are an important part of this world. <3")
        time.sleep(2)
        print("\n")
        print("Goodbye!")
        print("\n")
        exit()

    elif yes in checkRightGeneralAnswer:
        print("I'm sorry, I didn't quite get that - would you like to continue talking?")
        generalCheckRightAgainQ = raw_input("> ")
        generalCheckRightAgain = generalCheckRightAgainQ.upper()

        if yes in generalCheckRightAgain:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

            #ask how user is FEELING. from there give responses
            print("How are you feeling right now?")
            generalCheckRightAgainFeeling1Q = raw_input("> ")
            generalCheckRightAgainFeeling1 = generalCheckRightAgainFeeling1Q.upper()

            if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling1:
                print("\n")
                print("Would you like to talk to another teen about your feelings?")
                generalCrisisYouthCheckRightAgain1Q = raw_input("> ")
                generalCrisisYouthCheckRightAgain1 = generalCrisisYouthCheckRightAgain1Q.upper()

                if yes in generalCrisisYouthCheckRightAgain1:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif yea in generalCrisisYouthCheckRightAgain1:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif no in generalCrisisYouthCheckRightAgain1:
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif stopConnect in generalCrisisYouthCheckRightAgain1:
                    exit()

                elif abuseWord in generalCrisisYouthCheckRightAgain1:
                    print("\n")
                    domesticAbuseFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif suicideWord in generalCrisisYouthCheckRightAgain1:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif killWord in generalCrisisYouthCheckRightAgain1:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif helpWord in generalCrisisYouthCheckRightAgain1:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                else: 
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

            elif abuseWord in generalCheckRightAgainFeeling1:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCheckRightAgainFeeling1:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCheckRightAgainFeeling1:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCheckRightAgainFeeling1:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif stopConnect in generalCheckRightAgainFeeling1:
                exit()

            else:
                print("\n")
                print("I will ask you some yes or no questions to help guide you to the correct hotline.")
                time.sleep(4.75)
                print("\n")
                pass


        elif yea in generalCheckRightAgain:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

            #ask how user is FEELING. from there give responses
            print("How are you feeling right now?")
            generalCheckRightAgainFeeling2Q = raw_input("> ")
            generalCheckRightAgainFeeling2 = generalCheckRightAgainFeeling2Q.upper()

            if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling2:
                print("\n")
                print("Would you like to talk to another teen about your feelings?")
                generalCrisisYouthCheckRightAgain2Q = raw_input("> ")
                generalCrisisYouthCheckRightAgain2 = generalCrisisYouthCheckRightAgain2Q.upper()

                if yes in generalCrisisYouthCheckRightAgain2:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif yea in generalCrisisYouthCheckRightAgain2:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif no in generalCrisisYouthCheckRightAgain2:
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif stopConnect in generalCrisisYouthCheckRightAgain2:
                    exit()

                elif abuseWord in generalCrisisYouthCheckRightAgain2:
                    print("\n")
                    domesticAbuseFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif suicideWord in generalCrisisYouthCheckRightAgain2:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif killWord in generalCrisisYouthCheckRightAgain2:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif helpWord in generalCrisisYouthCheckRightAgain2:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                else: 
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

            elif abuseWord in generalCheckRightAgainFeeling2:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCheckRightAgainFeeling2:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCheckRightAgainFeeling2:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCheckRightAgainFeeling2:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif stopConnect in generalCheckRightAgainFeeling2:
                exit()

            else:
                print("\n")
                print("I will ask you some yes or no questions to help guide you to the correct hotline.")
                time.sleep(4.75)
                print("\n")
                pass


        elif no in generalCheckRightAgain:
            print("\n")
            print("I hope you found the help you needed. You are an important part of this world. <3")
            time.sleep(2)
            print("\n")
            print("Goodbye!")
            print("\n")
            exit()

        elif abuseWord in generalCheckRightAgain:
            print("\n")
            domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif suicideWord in generalCheckRightAgain:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif killWord in generalCheckRightAgain:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif helpWord in generalCheckRightAgain:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif stopConnect in generalCheckRightAgain:
            exit()

        else: 
            print("\n")
            print("I'm sorry, I didn't quite get that. We will continue to talk. Remember, if you would like to stop, type 'quit' at anytime.")
            time.sleep(4)
            print("\n")

            #ask how user is FEELING. from there give responses
            print("How are you feeling right now?")
            generalCheckRightAgainFeeling3Q = raw_input("> ")
            generalCheckRightAgainFeeling3 = generalCheckRightAgainFeeling3Q.upper()

            if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling3:
                print("\n")
                print("Would you like to talk to another teen about your feelings?")
                generalCrisisYouthCheckRightAgain3Q = raw_input("> ")
                generalCrisisYouthCheckRightAgain3 = generalCrisisYouthCheckRightAgain3Q.upper()

                if yes in generalCrisisYouthCheckRightAgain3:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif yea in generalCrisisYouthCheckRightAgain3:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif no in generalCrisisYouthCheckRightAgain3:
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif stopConnect in generalCrisisYouthCheckRightAgain3:
                    exit()

                elif abuseWord in generalCrisisYouthCheckRightAgain3:
                    print("\n")
                    domesticAbuseFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif suicideWord in generalCrisisYouthCheckRightAgain3:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif killWord in generalCrisisYouthCheckRightAgain3:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif helpWord in generalCrisisYouthCheckRightAgain3:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                else: 
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

            elif abuseWord in generalCheckRightAgainFeeling3:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCheckRightAgainFeeling3:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCheckRightAgainFeeling3:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCheckRightAgainFeeling3:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif stopConnect in generalCheckRightAgainFeeling3:
                exit()

            else:
                print("\n")
                print("I will ask you some yes or no questions to help guide you to the correct hotline.")
                time.sleep(4.75)
                print("\n")
                pass


    elif yea in checkRightGeneralAnswer:
        print("I'm sorry, I didn't quite get that - would you like to continue talking?")
        generalCheckRightAgain2Q = raw_input("> ")
        generalCheckRightAgain2 = generalCheckRightAgain2Q.upper()

        if yes in generalCheckRightAgain2:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

            #ask how user is FEELING. from there give responses
            print("How are you feeling right now?")
            generalCheckRightAgainFeeling4Q = raw_input("> ")
            generalCheckRightAgainFeeling4 = generalCheckRightAgainFeeling4Q.upper()

            if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling4:
                print("\n")
                print("Would you like to talk to another teen about your feelings?")
                generalCrisisYouthCheckRightAgain4Q = raw_input("> ")
                generalCrisisYouthCheckRightAgain4 = generalCrisisYouthCheckRightAgain4Q.upper()

                if yes in generalCrisisYouthCheckRightAgain4:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif yea in generalCrisisYouthCheckRightAgain4:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif no in generalCrisisYouthCheckRightAgain4:
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif stopConnect in generalCrisisYouthCheckRightAgain4:
                    exit()

                elif abuseWord in generalCrisisYouthCheckRightAgain4:
                    print("\n")
                    domesticAbuseFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif suicideWord in generalCrisisYouthCheckRightAgain4:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif killWord in generalCrisisYouthCheckRightAgain4:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif helpWord in generalCrisisYouthCheckRightAgain4:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                else: 
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

            elif abuseWord in generalCheckRightAgainFeeling4:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCheckRightAgainFeeling4:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCheckRightAgainFeeling4:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCheckRightAgainFeeling4:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif stopConnect in generalCheckRightAgainFeeling4:
                exit()

            else:
                print("\n")
                print("I will ask you some yes or no questions to help guide you to the correct hotline.")
                time.sleep(4.75)
                print("\n")
                pass


        elif yea in generalCheckRightAgain2:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

            #ask how user is FEELING. from there give responses
            print("How are you feeling right now?")
            generalCheckRightAgainFeeling5Q = raw_input("> ")
            generalCheckRightAgainFeeling5 = generalCheckRightAgainFeeling5Q.upper()

            if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling5:
                print("\n")
                print("Would you like to talk to another teen about your feelings?")
                generalCrisisYouthCheckRightAgain5Q = raw_input("> ")
                generalCrisisYouthCheckRightAgain5 = generalCrisisYouthCheckRightAgain5Q.upper()

                if yes in generalCrisisYouthCheckRightAgain5:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif yea in generalCrisisYouthCheckRightAgain5:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif no in generalCrisisYouthCheckRightAgain5:
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif stopConnect in generalCrisisYouthCheckRightAgain5:
                    exit()

                elif abuseWord in generalCrisisYouthCheckRightAgain5:
                    print("\n")
                    domesticAbuseFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif suicideWord in generalCrisisYouthCheckRightAgain5:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif killWord in generalCrisisYouthCheckRightAgain5:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif helpWord in generalCrisisYouthCheckRightAgain5:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                else: 
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

            elif abuseWord in generalCheckRightAgainFeeling5:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCheckRightAgainFeeling5:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCheckRightAgainFeeling5:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCheckRightAgainFeeling5:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif stopConnect in generalCheckRightAgainFeeling5:
                exit()

            else:
                print("\n")
                print("I will ask you some yes or no questions to help guide you to the correct hotline.")
                time.sleep(4.75)
                print("\n")
                pass


        elif no in generalCheckRightAgain2:
            print("\n")
            print("I hope you found the help you needed. You are an important part of this world. <3")
            time.sleep(2)
            print("\n")
            print("Goodbye!")
            print("\n")
            exit()

        elif abuseWord in generalCheckRightAgain2:
            print("\n")
            domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif suicideWord in generalCheckRightAgain2:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif killWord in generalCheckRightAgain2:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif helpWord in generalCheckRightAgain2:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif stopConnect in generalCheckRightAgain2:
            exit()
            
        else: 
            print("\n")
            print("I'm sorry, I didn't quite get that. We will continue to talk. Remember, if you would like to stop, type 'quit' at anytime.")
            time.sleep(4)
            print("\n")

            #ask how user is FEELING. from there give responses
            print("How are you feeling right now?")
            generalCheckRightAgainFeeling6Q = raw_input("> ")
            generalCheckRightAgainFeeling6 = generalCheckRightAgainFeeling6Q.upper()

            if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling6:
                print("\n")
                print("Would you like to talk to another teen about your feelings?")
                generalCrisisYouthCheckRightAgain6Q = raw_input("> ")
                generalCrisisYouthCheckRightAgain6 = generalCrisisYouthCheckRightAgain6Q.upper()

                if yes in generalCrisisYouthCheckRightAgain6:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif yea in generalCrisisYouthCheckRightAgain6:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif no in generalCrisisYouthCheckRightAgain6:
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif stopConnect in generalCrisisYouthCheckRightAgain6:
                    exit()

                elif abuseWord in generalCrisisYouthCheckRightAgain6:
                    print("\n")
                    domesticAbuseFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif suicideWord in generalCrisisYouthCheckRightAgain6:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif killWord in generalCrisisYouthCheckRightAgain6:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif helpWord in generalCrisisYouthCheckRightAgain6:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                else: 
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

            elif abuseWord in generalCheckRightAgainFeeling6:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCheckRightAgainFeeling6:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCheckRightAgainFeeling6:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCheckRightAgainFeeling6:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif stopConnect in generalCheckRightAgainFeeling6:
                exit()

            else:
                print("\n")
                print("I will ask you some yes or no questions to help guide you to the correct hotline.")
                time.sleep(4.75)
                print("\n")
                pass


    elif keepTalking in checkRightGeneralAnswer:
        print("\n")
        print("Alright, we will continue to talk.")
        time.sleep(2)
        print("\n")

        #ask how user is FEELING. from there give responses
        print("How are you feeling right now?")
        generalCheckRightAgainFeeling7Q = raw_input("> ")
        generalCheckRightAgainFeeling7 = generalCheckRightAgainFeeling7Q.upper()

        if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling7:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthCheckRightAgain7Q = raw_input("> ")
            generalCrisisYouthCheckRightAgain7 = generalCrisisYouthCheckRightAgain7Q.upper()

            if yes in generalCrisisYouthCheckRightAgain7:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthCheckRightAgain7:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthCheckRightAgain7:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthCheckRightAgain7:
                exit()

            elif abuseWord in generalCrisisYouthCheckRightAgain7:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthCheckRightAgain7:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCrisisYouthCheckRightAgain7:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthCheckRightAgain7:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            else: 
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        elif abuseWord in generalCheckRightAgainFeeling7:
            print("\n")
            domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif suicideWord in generalCheckRightAgainFeeling7:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()
        
        elif killWord in generalCheckRightAgainFeeling7:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif helpWord in generalCheckRightAgainFeeling7:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif stopConnect in generalCheckRightAgainFeeling7:
            exit()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

    elif no in checkRightGeneralAnswer:
        print("I'm sorry, I didn't quite get that - would you like to continue talking?")
        generalCheckRightAgain3Q = raw_input("> ")
        generalCheckRightAgain3 = generalCheckRightAgain3Q.upper()

        if yes in generalCheckRightAgain3:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

            #ask how user is FEELING. from there give responses
            print("How are you feeling right now?")
            generalCheckRightAgainFeeling8Q = raw_input("> ")
            generalCheckRightAgainFeeling8 = generalCheckRightAgainFeeling8Q.upper()

            if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling8:
                print("\n")
                print("Would you like to talk to another teen about your feelings?")
                generalCrisisYouthCheckRightAgain8Q = raw_input("> ")
                generalCrisisYouthCheckRightAgain8 = generalCrisisYouthCheckRightAgain8Q.upper()

                if yes in generalCrisisYouthCheckRightAgain8:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif yea in generalCrisisYouthCheckRightAgain8:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif no in generalCrisisYouthCheckRightAgain8:
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif stopConnect in generalCrisisYouthCheckRightAgain8:
                    exit()

                elif abuseWord in generalCrisisYouthCheckRightAgain8:
                    print("\n")
                    domesticAbuseFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif suicideWord in generalCrisisYouthCheckRightAgain8:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif killWord in generalCrisisYouthCheckRightAgain8:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif helpWord in generalCrisisYouthCheckRightAgain8:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                else: 
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

            elif abuseWord in generalCheckRightAgainFeeling8:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCheckRightAgainFeeling8:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCheckRightAgainFeeling8:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCheckRightAgainFeeling8:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif stopConnect in generalCheckRightAgainFeeling8:
                exit()

            else:
                print("\n")
                print("I will ask you some yes or no questions to help guide you to the correct hotline.")
                time.sleep(4.75)
                print("\n")
                pass

        elif yea in generalCheckRightAgain3:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

            #ask how user is FEELING. from there give responses
            print("How are you feeling right now?")
            generalCheckRightAgainFeeling9Q = raw_input("> ")
            generalCheckRightAgainFeeling9 = generalCheckRightAgainFeeling9Q.upper()

            if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling9:
                print("\n")
                print("Would you like to talk to another teen about your feelings?")
                generalCrisisYouthCheckRightAgain9Q = raw_input("> ")
                generalCrisisYouthCheckRightAgain9 = generalCrisisYouthCheckRightAgain9Q.upper()

                if yes in generalCrisisYouthCheckRightAgain9:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif yea in generalCrisisYouthCheckRightAgain9:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif no in generalCrisisYouthCheckRightAgain9:
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif stopConnect in generalCrisisYouthCheckRightAgain9:
                    exit()

                elif abuseWord in generalCrisisYouthCheckRightAgain9:
                    print("\n")
                    domesticAbuseFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif suicideWord in generalCrisisYouthCheckRightAgain9:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif killWord in generalCrisisYouthCheckRightAgain9:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif helpWord in generalCrisisYouthCheckRightAgain9:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                else: 
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

            elif abuseWord in generalCheckRightAgainFeeling9:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCheckRightAgainFeeling9:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCheckRightAgainFeeling9:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCheckRightAgainFeeling9:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif stopConnect in generalCheckRightAgainFeeling9:
                exit()

            else:
                print("\n")
                print("I will ask you some yes or no questions to help guide you to the correct hotline.")
                time.sleep(4.75)
                print("\n")
                pass

        elif no in generalCheckRightAgain3:
            print("\n")
            print("I hope you found the help you needed. You are an important part of this world. <3")
            time.sleep(2)
            print("\n")
            print("Goodbye!")
            print("\n")
            exit()

        elif abuseWord in generalCheckRightAgain3:
            print("\n")
            domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif suicideWord in generalCheckRightAgain3:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif killWord in generalCheckRightAgain3:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif helpWord in generalCheckRightAgain3:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif stopConnect in generalCheckRightAgain3:
            exit()
            
        else: 
            print("\n")
            print("I'm sorry, I didn't quite get that. We will continue to talk. Remember, if you would like to stop, type 'quit' at anytime.")
            time.sleep(4)
            print("\n")

            #ask how user is FEELING. from there give responses
            print("How are you feeling right now?")
            generalCheckRightAgainFeeling10Q = raw_input("> ")
            generalCheckRightAgainFeeling10 = generalCheckRightAgainFeeling10.upper()

            if sad or depressed or empty or numb or bad or useless in generalCheckRightAgainFeeling10:
                print("\n")
                print("Would you like to talk to another teen about your feelings?")
                generalCrisisYouthCheckRightAgain10Q = raw_input("> ")
                generalCrisisYouthCheckRightAgain10 = generalCrisisYouthCheckRightAgain10Q.upper()

                if yes in generalCrisisYouthCheckRightAgain10:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif yea in generalCrisisYouthCheckRightAgain10:
                    print("\n")
                    youthLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif no in generalCrisisYouthCheckRightAgain10:
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

                elif stopConnect in generalCrisisYouthCheckRightAgain10:
                    exit()

                elif abuseWord in generalCrisisYouthCheckRightAgain10:
                    print("\n")
                    domesticAbuseFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif suicideWord in generalCrisisYouthCheckRightAgain10:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif killWord in generalCrisisYouthCheckRightAgain10:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                elif helpWord in generalCrisisYouthCheckRightAgain10:
                    print("\n")
                    immediateEmergencyFunction()
                    print("\n")
                    time.sleep(2)
                    suicidePrevention()
                    print("\n")
                    time.sleep(2)

                    checkRight()

                else: 
                    print("\n")
                    namiFunction()
                    time.sleep(2)
                    print("\n")
                    textLineFunction()
                    time.sleep(2)
                    print("\n")

                    checkRight()

            elif abuseWord in generalCheckRightAgainFeeling10:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCheckRightAgainFeeling10:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif killWord in generalCheckRightAgainFeeling10:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCheckRightAgainFeeling10:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif stopConnect in generalCheckRightAgainFeeling10:
                exit()

            else:
                print("\n")
                print("I will ask you some yes or no questions to help guide you to the correct hotline.")
                time.sleep(4.75)
                print("\n")
                pass

    elif abuseWord in checkRightGeneralAnswer:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif suicideWord in checkRightGeneralAnswer:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif killWord in checkRightGeneralAnswer:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif helpWord in checkRightGeneralAnswer:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif stopConnect in checkRightGeneralAnswer:
        exit()
    else: 
        print("\n")
        print("I'm sorry, I didn't quite get that. We will continue to talk. Remember, if you would like to stop, type 'quit' at anytime.")
        time.sleep(4)
        print("\n")

def checkRight():
    print("Was this information helpful, or would you like to keep talking?")
    checkRightResponse = raw_input("> ")
    checkRightAnswer = checkRightResponse.upper()
    
    if wasHelpful or isHelpful or helpful in checkRightGeneralAnswer:
        print("\n")
        print("I hope you found the help you needed. You are an important part of this world. <3")
        time.sleep(2)
        print("\n")
        print("Goodbye!")
        print("\n")
        exit()
        
    elif yes in checkRightAnswer:
        print("I'm sorry, I didn't quite get that - would you like to continue talking?")
        checkRightAgainQ = raw_input("> ")
        checkRightAgain = checkRightAgainQ.upper()

        if yes in checkRightAgain:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

        elif yea in checkRightAgain:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

        elif no in checkRightAgain:
            print("\n")
            print("I hope you found the help you needed. You are an important part of this world. <3")
            time.sleep(2)
            print("\n")
            print("Goodbye!")
            print("\n")
            exit()

        elif abuseWord in checkRightAgain:
            print("\n")
            domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif suicideWord in checkRightAgain:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif killWord in checkRightAgain:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif helpWord in checkRightAgain:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif stopConnect in checkRightAgain:
            exit()

        else: 
            print("\n")
            print("I'm sorry, I didn't quite get that. We will continue to talk. Remember, if you would like to stop, type 'quit' at anytime.")
            time.sleep(4)
            print("\n")