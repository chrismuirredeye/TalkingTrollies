import os
from random import randint
from array import *
import time

male = 'true' #this is a global flag that defines if this is the male or the female basket


basket_a = '0010580093' # Basket A - Sticker
basket_b = '0008342310' # Basket B - Non Sticker

#shopping items
newspaper = '0004002434'
marshmallows = '0001080972'
mint_tea = '0008032566'
rhubarb_and_custard = '0008043331'
energy_drink = '0008035839'
peroni = '0015644579'


baskets_hello = [
    'Oh Hello',
    'Hi There'
]

basket_a_speak = [
    'Have you heard about the oyster, who went into a disco and pulled a muscle',
    'Och! Damn, I forgot to go to the gym today. Thatll be 10 years in a row now...'
]

basket_b_speak = [
    'I am learning the hokey cokey. Not all of it. But  Ive got the ins and outs.',
    'Ive got very sensitive teeth. Theyll probably be upset Ive told you.'
]

baskets_laughs = [
    'Ha Ha Ha Ha Ha Ha Ha',
    'He He He He He He He'
]


while True:

#for x in range(0, 10):

    x = raw_input() # get the input from the keyboard buffer which in our case is the raspberry

    time.sleep(1) # this is agrace period that stops the basket from talking too soon after the beep on the scanner

    phrase_n = randint(0,1) # this randonly picks a response

    # -- CONVERSATION between baskets
    if x == basket_a:
        
        # 1 Say Hello
        phrase = baskets_hello[phrase_n]
        os.system("espeak -ven-sc+f2 -p70 -k5 -s180 '" + phrase + "'")
        # 2 Wait
        time.sleep(3)
        # 3 Say a Joke
        phrase = basket_a_speak[phrase_n]
        os.system("espeak -ven-sc+f2 -p70 -k5 -s180 '" + phrase + "'")
        time.sleep(3)
     
    elif x == basket_b:

        # 1 Wait
        time.sleep(2)
        # 2 Say Hello Back
        phrase = baskets_hello[phrase_n]
        os.system("espeak -ven-wi+m7 -k5 -s150 '" + phrase + "'")
        # 3 Wait
        time.sleep(7)
        # 4 Laugh at Joke
        phrase = 'Ha Ha Ha Ha Ha Ha Ha Ha Ha Ha Ha Ha'
        os.system("espeak -ven-wi+m7 -k5 -s150 '" + phrase + "'")

    # -- END CONVERSATION BETWEEN BASKETS

    # -- START OF ITEMS SCANNING
    
    # NEWSPAPER
    elif x == newspaper:

        if male == 'true':
            os.system("espeak -ven-wi+m7 -k5 -s150 'Newspaper'")
            print 'male newspaper'
        else:
            os.system("espeak -ven-sc+f2 -p70 -k5 -s180 'Newspaper'")
            print 'female newspaper'

    # MARSHMALLOWS
    elif x == marshmallows:
        
        if male == 'true':
            os.system("espeak -ven-wi+m7 -k5 -s150 'Marsmallows'")
            print 'male marshmallows'
        else:
            os.system("espeak -ven-sc+f2 -p70 -k5 -s180 'Marshmallows'")
            print 'female marshmallows'

    # MINT TEA
    elif x == mint_tea:

        if male == 'true':
            os.system("espeak -ven-wi+m7 -k5 -s150 'Mint Tea'")
            print 'male mint tea'
        else :
            os.system("espeak -ven-sc+f2 -p70 -k5 -s180 'Mint Tea'")
            print 'female mint tea'

    # RHUBARB AND CUSTARD
    elif x == rhubarb_and_custard:

        if male == 'true':
            os.system("espeak -ven-wi+m7 -k5 -s150 'Rhubarb and custard'")
            print 'male rhubarb and custard'
        else:
            os.system("espeak -ven-sc+f2 -p70 -k5 -s180 'Rhubarb and custard'")
            print 'female rhubarb and custard'

    # ENERGY DRINK
    elif x == energy_drink:

        if male == 'true':
            os.system("espeak -ven-wi+m7 -k5 -s150 'Energy Drink'")
            print 'male energy drink'
        else:
            os.system("espeak -ven-sc+f2 -p70 -k5 -s180 'Energy Drink'")
            print 'female energy drink'

    # PERONI
    elif x == peroni:

        if male == 'true':
            os.system("espeak -ven-wi+m7 -k5 -s150 'Peroni'")
            print 'male peroni'
        else:
            os.system("espeak -ven-sc+f2 -p70 -k5 -s180 'Peroni'")
            print 'female peroni'
