import time
import characters as ch
from random import randint as r

class Elements():
    """A class for most of the visual elements I use, besides characters."""

    def text(type: str, param):
        """A function that can take various paramaters to print out text."""
        # 'type' decides what type of text it's gonna spit out
        # 'param' is a set of paramaters that the function uses, dependingon the type.

        if type == "break":
            # This is basically a long line break of dots.
            # 'param' in this case won't affect anything.
            print("\n+........................................................................................+\n")

        elif type == "centre":
            # This centres the text that is inputted as 'param'.
            # It centres the text based on the width of the character frames.
            # If the text is longer, it just left justifies.
            print(" " * int(((91-len(param))/2)) + param)

        elif type == "left":
            # This left justifies the text that is inputted as 'param'
            # Note: I could have easily just used a regular print() statement
            # but this makes things more consistent in my opinion.
            print(param)

        elif type == "right":
            # This right justifies the text that is inputted as 'param'
            print(" " * int(91-len(param)) + param)

        elif type == "space":
            # This is basically just a line break, without the dots.
            # I could have easily just used a "\n"
            # but I can change how many line breaks occur universally using this function.
            print("\n" * param)

    def option(options):
        """A function that takes in an input from the user, and only accepts answers that are between 0 and the variable 'options'."""

        while True:
            try:
                choice = int(input(""))
                if 0 < choice <= options:
                    break
                else:
                    print("Please enter one of the options!")
            except:
                print("There was something wrong with your input! Please try again.")
        return choice
    
    def loading(loops, text, delays):
        """A function that creates a loading animation, with text that can be displayed at the bottom of the frame."""
        # 'loops' determines how many loops through the animation occur.
        # 'text' determines what text is displayed at the bottom of the frame.
        # 'delays' determines the amount of time before the animation switches frames.

        for i in range(0,loops):
            for k in range(1, 5):
                if k == 1:
                    print("\n"*8)
                    print(ch.Blank.blank(text))
                    Elements.text("centre", text)
                    time.sleep(delays)
                elif k == 2:
                    print("\n"*8)
                    print(ch.Loading.one(0))
                    Elements.text("centre", text)
                    time.sleep(delays)
                elif k == 3:
                    print("\n"*8)
                    print(ch.Loading.two(0))
                    Elements.text("centre", text)
                    time.sleep(delays)
                elif k == 4:
                    print("\n"*8)
                    print(ch.Loading.three(0))
                    Elements.text("centre", text)
                    time.sleep(delays)

    def pick_up_call(known):
        """A function that carries out the 'call from Kita' sequence."""
        # I made this into a function because I go through this sequence twice in my code.
        # It doesn't really fit into this class, but it's more organized this way I think.

        while True:
            print(ch.Blank.inc_call(0))
            if known == False:
                Elements.text("centre", "You get a call from an unknown number.")
            else:
                Elements.text("centre", "You get a call from Kita.")
            time.sleep(1)
            Elements.text("space", 1)
            Elements.text("centre", "[1] Pick up the phone  [2] Leave it be.")
            cont = Elements.option(2)
            print(ch.Blank.blank(0))
            if cont == 1:
                break
            elif cont == 2:
                Elements.text("centre", "You ignore the call.")
                time.sleep(2)
                Elements.text("centre", "You bastard.")
                time.sleep(2)
                Elements.text("space", 1)
                if known == False:
                    Elements.text("right", "[YOU, Murmuring] Huh. If they call me back, they might be worth my time.")
                else:
                    Elements.text("right", "[YOU, Murmuring] Sorry Kita, I can't afford to talk to you right now.")
                time.sleep(5)
        Elements.loading(1, "", 0.75)
        print(ch.Blank.calling(0))








# Intro section

Elements.text("space", 2)
Elements.text("break", 0)
Elements.text("centre", "Welcome to the Bocchi the Rock escape room! By Matthew Kong")
Elements.text("centre", "It is recommended that you watch the anime before you proceed.")
Elements.text("centre", "Also, please expand your terminal window to fullscreen so that you can see everything.")
Elements.text("centre", "Press 1 to continue!")
Elements.text("break", 0)
Elements.text("space", 1)
cont = Elements.option(1)
Elements.loading(3, "Loading", 0.5)








# Room 1

print(ch.Blank.blank(0))
Elements.text("centre", "The year is 2016. You look around, and it's all black.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to open your eyes.")
cont = Elements.option(1)
print(ch.Blank.blank(0))
Elements.text("centre", "You open your eyes, and see a pink figure in front of you.")
time.sleep(4)
print(ch.Bocchi.normal(0))
time.sleep(1)
Elements.text("left", "[BOCCHI] Oh, uh, h-hey.")
time.sleep(2)
Elements.text("left", "[BOCCHI] Y-you've finally woken up, eh?")

time.sleep(2)
while True:
    # Loop that goes through the first dialogue option.
    print(ch.Bocchi.normal(0))
    Elements.text("centre", "RESPONSE:")
    Elements.text("centre", "[1] Who are you?")
    Elements.text("centre", "[2] Where am I?")
    # Note: I use the variable 'cont' throughout my code a lot.
    # This is just a temporary variable that stores the dialogue option you chose.
    # I reused the variable so that I wouldn't have to think of new names each time.
    # If the dialogue options conflict, I use cont2, cont3, ...

    cont = Elements.option(2)
    if cont == 1:
        print(ch.Bocchi.normal(0))
        Elements.text("right", "[YOU] Who the hell are you?")
        time.sleep(1)
        Elements.text("space", 1)
        Elements.text("left", "[BOCCHI] Ah, s-sorry, I'm Hitori Gotoh, but you can call me B-Bocchi.")
        Elements.text("left", "[BOCCHI] I'm a m-middle schooler that's t-trying to write some song lyrics.")
        time.sleep(2.5)
        Elements.text("space", 1)
        Elements.text("right", "[YOU] You play an instrument?")
        time.sleep(2)
        Elements.text("space", 1)
        Elements.text("left", "[BOCCHI] Yeah, I play the guitar.")
        time.sleep(1.5)
        Elements.text("left", "[BOCCHI] I've got this channel on OH!TUBE called guitarhero.")
        time.sleep(2)
        Elements.text("space", 1)
        Elements.text("right", "[YOU] Oh, I see.")
        Elements.text("centre", "Press 1 to continue.")
        cont2 = Elements.option(1)
    elif cont == 2:
        print(ch.Bocchi.normal(0))
        break

Elements.text("right", "[YOU] Where even am I right now?")
time.sleep(2)
Elements.text("space", 1)
Elements.text("left", "[BOCCHI] Ah, s-sorry, you're in my room.")
time.sleep(1.5)
Elements.text("left", "[BOCCHI] I've locked my door until I can t-think of some good song lyrics.")
time.sleep(2)
Elements.text("left", "[BOCCHI] A-and I, uh, need your help.")
time.sleep(3)
Elements.text("left", "[BOCCHI] I'm trying to make a band, you see.")
time.sleep(2)
Elements.text("left", "[BOCCHI] It's always been my dream to be a rockstar.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] Huh...? You know what, I'll help you. What do you need?")
time.sleep(3.5)

print(ch.Bocchi.happy(0))
time.sleep(2)
Elements.text("left", "[BOCCHI] T-thank you!")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

print(ch.Bocchi.normal(0))
Elements.text("left", "[BOCCHI] I have s-some lyrics right now, but they're not very good.")
time.sleep(1)
Elements.text("left", "[BOCCHI] They're missing some words, you know.")
time.sleep(1)
Elements.text("left", "[BOCCHI] Here's one line I'm trying to figure out right now:")
time.sleep(1)
Elements.text("left", "[BOCCHI] 'I've bought the ingredients for a ______ doll.'")
time.sleep(1)
Elements.text("left", "[BOCCHI] It'd be great if you could help me figure out a word to put there.")
time.sleep(1)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)
Elements.text("space", 1)
Elements.text("right", "[YOU] Sure.")
time.sleep(2)

while True:
    # Loops through first dialogue option
    print(ch.Rooms.room1(0))
    Elements.text("left", "[BOCCHI] Here's a floor plan of my room. You might find some inspiration with this.")
    time.sleep(2)
    Elements.text("space", 1)
    Elements.text("centre", "TRAVEL TO:")
    Elements.text("centre", "[1] BED  [2] DRAWER  [3] CLOSET")
    cont = Elements.option(3)
    while True:
        # Loops through first dialogue option's choices
        if cont == 1:
            Elements.loading(2, "You search the bed.", 0.5)
            print(ch.Blank.blank(0))
            Elements.text("right", "[YOU] Hmm, not very interesting.")
            time.sleep(2)
            Elements.text("right", "[YOU] A few clothes, a blanket, and...")
            time.sleep(1)
            Elements.text("right", "[YOU] oh ew, when was the last time this pillow was washed?")
            time.sleep(2)
            Elements.text("space", 1)
            Elements.text("centre", "TRAVEL TO:")
            Elements.text("centre", "[1] REPORT TO BOCCHI  [2] DRAWER  [3] CLOSET")
            cont2 = Elements.option(3)
            # Logic that determines if you're going to continue searching or not
            if cont2 == 1:
                break
            elif cont2 == 2:
                cont = 2
            elif cont2 == 3:
                cont = 3
        elif cont == 2:
            Elements.loading(2, "You rummage through the drawer.", 0.5)
            print(ch.Blank.blank(0))
            Elements.text("right", "[YOU] Hmmm... interesting.")
            time.sleep(2)
            Elements.text("right", "[YOU] A few socks, a guitar pick, and some coupon vouchers.")
            Elements.text("space", 1)
            Elements.text("centre", "TRAVEL TO:")
            Elements.text("centre", "[1] BED  [2] REPORT TO BOCCHI  [3] CLOSET")
            cont2 = Elements.option(3)
            if cont2 == 1:
                cont = 1
            elif cont2 == 2:
                break
            elif cont2 == 3:
                cont = 3
        elif cont == 3:
            Elements.loading(2, "You rummage through the closet.", 0.5)
            print(ch.Blank.blank(0))
            Elements.text("right", "[YOU] Hmm. There's alotta stuff here.")
            time.sleep(2)
            Elements.text("right", "[YOU] A laptop charger, a voodoo doll, and some school supplies.")
            Elements.text("space", 1)
            Elements.text("centre", "TRAVEL TO:")
            Elements.text("centre", "[1] BED  [2] DRAWER  [3] REPORT TO BOCCHI")
            cont2 = Elements.option(3)
            if cont2 == 1:
                cont = 1
            elif cont2 == 2:
                cont = 2
            elif cont2 == 3:
                break

    Elements.loading(1, "You walk back to Bocchi.", 0.5)
    while True:
        # loop through to check if answer is correct
        print(ch.Bocchi.normal(0))
        Elements.text("left", "[BOCCHI] Did you find something? R-remember, here are the lyrics:")
        time.sleep(2)
        Elements.text("left", "[BOCCHI] 'I've bought the ingredients for a ______ doll.'")
        time.sleep(2)
        Elements.text("space", 1)
        Elements.text("centre", "Type what you think fits...")
        
        answer = str(input("")).upper()

        print(ch.Bocchi.normal(0))
        Elements.text("right", "[YOU] Is it a " + answer + " doll?")
        time.sleep(1)
        Elements.text("left", "[BOCCHI] Hmm...")
        time.sleep(1)
        Elements.text("left", "[BOCCHI, whispering] 'I've bought the ingredients for a " + answer + " doll.'")
        time.sleep(3)
        if answer == "VOODOO":
            print(ch.Bocchi.happy(0))
            Elements.text("left", "[BOCCHI] W-wow, that sounds really good!")
            time.sleep(0.5)
            Elements.text("left", "[BOCCHI] Th-thank you so much!")
            break
        else:
            print(ch.Bocchi.normal(0))
            Elements.text("left", "[BOCCHI] Sorry, I d-don't, uh, think that's quite right.")
            Elements.text("space", 1)
            Elements.text("centre", "[1] Try again  [2] Search some more")
            cont = Elements.option(2)
            if cont == 1:
                continue
            elif cont == 2:
                break
    time.sleep(3)
    if answer == "VOODOO":
        break

Elements.loading(1, "You were then freed from the room.", 0.5)
time.sleep(1)
Elements.text("centre", "Bocchi would go on to finish the rest of the lyrics.")
time.sleep(4)
print(ch.Rooms.room1_lyrics(0))
time.sleep(5)
Elements.text("centre", "They were not very good.")
time.sleep(3)
Elements.text("centre", "And thus, after another year of struggle, she graduated middle school")
time.sleep(3)
Elements.text("centre", "It's safe to say that she never got to form a band.")
time.sleep(4)
Elements.text("centre", "That is, until her first year of high school.")
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue to room 2.")
cont = Elements.option(1)





# Room 2

print(ch.Blank.blank(0))
Elements.text("centre", "The year is 2018.")
time.sleep(3)
Elements.text("centre", "You haven't thought too deeply about the time you were kidnapped in 2016.")
time.sleep(3)
Elements.text("centre", "Not until recently, at least.")
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

print(ch.Blank.blank(0))
Elements.text("centre", "As you walk down Shimo-Kitazawa, you ponder.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("right", "[YOU] Why did that pink-haired girl kidnap me?")
time.sleep(3)
Elements.text("right", "[YOU] I wonder if she ended up forming a band....")
time.sleep(5)

Elements.loading(1, "You keep walking.", 1)
time.sleep(2)
Elements.text("right", "[YOU] Wait... is that you?")
time.sleep(1)
Elements.text("right", "[YOU] Bocchi, was it?")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to tap the girl on the shoulder.")
cont = Elements.option(1)

print(ch.Bocchi.normal(0))
Elements.text("left", "[BOCCHI] Ah! Uh, I uh...")
time.sleep(2)

print(ch.Blank.blank(0))
Elements.text("centre", "She falls onto the floor.")
time.sleep(3)

print(ch.Kita.normal(0))
Elements.text("left", "[KITA] Haha, sorry about that! Bocchi gets really nervous sometimes.")
time.sleep(3)
Elements.text("left", "[KITA] And... I think she's out cold.")
time.sleep(2)
Elements.text("left", "[KITA] Anyway, what's your name? ")
time.sleep(1)
Elements.text("space", 1)
Elements.text("centre", "Type your name in.")
your_name = str(input(""))

print(ch.Kita.normal(0))
Elements.text("left", "[KITA] Ooo, that's a cool name, " + your_name + "!")
time.sleep(3)
Elements.text("left", "[KITA] My name's Kita.")
time.sleep(2)
Elements.text("left", "[KITA] Could you help me out a bit?")
Elements.text("space", 1)
Elements.text("centre", "Press 1 to help out.")
cont = Elements.option(1)

print(ch.Kita.normal(0))
Elements.text("left", "[KITA] Awesome! Thank you so much, " + your_name)
time.sleep(3)
Elements.text("left", "[KITA] I need your help finding this one place, it's called Starry I think?")
time.sleep(4)
Elements.text("left", "[KITA] I don't know my way there, so Bocchi here was guiding me...")
time.sleep(4)
Elements.text("left", "[KITA] But she's, well, she's not available anymore.")
time.sleep(3)

while True:
    Elements.text("left", "[KITA] Could you help me find my way?")
    time.sleep(2)
    Elements.text("space", 1)
    Elements.text("centre", "[1] Sure  [2] I don't know where it is")
    cont = Elements.option(2)

    if cont == 1:
        print(ch.Kita.normal(0))
        Elements.text("left", "[KITA] Thank you so much!")
        time.sleep(2)
        break
    elif cont == 2:
        Elements.loading(1, "", 0.75)
        time.sleep(1)
        Elements.text("right", "[YOU] I... don't know what that is.")
        time.sleep(3)

        print(ch.Kita.normal(0))
        Elements.text("left", "[KITA] Oh... it's a club? For bands to play music?")
        time.sleep(3)
        Elements.text("space", 1)
        Elements.text("right", "[YOU] Yeah... I can't help you.")
        time.sleep(1.5)
        Elements.text("space", 1)
        Elements.text("left", "[KITA] Please " + your_name + "!!!")

print(ch.Kita.normal(0))
Elements.text("left", "[KITA] Luckily, I think Bocchi was showing me the directions on her phone.")
time.sleep(3)
Elements.text("left", "[KITA] You'll have to unlock her phone though, and I don't know the password.")
time.sleep(3)
Elements.text("left", "[KITA] I remember she showed me an alleyway where I could decrypt the password.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] What? That makes no sense. Almost like it was forced into this game.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("left", "[KITA] Just to fulfill the requirements of the assignment? Yup!")
time.sleep(2)
Elements.text("left", "[KITA] Anyways, follow me!")
time.sleep(1)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to follow.")
cont = Elements.option(1)

Elements.loading(2, "You follow Kita to the alleyway.", 0.5)
print(ch.Kita.normal(0))
Elements.text("left", "[KITA] So here's the alleywayyyy!! There's a few hints, but I can't figure it out.")
time.sleep(2.5)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to proceed.")
cont = Elements.option(1)

while True:
    print(ch.Rooms.room2(0))
    Elements.text("space", 1)
    Elements.text("centre", "TRAVEL TO:")
    Elements.text("centre", "[1] STICKY NOTE BOARD  [2] TRASH PILE  [3] GARBAGE CAN")
    cont = Elements.option(3)
    while True:
        if cont == 1:
            Elements.loading(2, "You glance at the sticky note board.", 0.5)
            Elements.text("space", 1)
            Elements.text("right", "[YOU] Hmm... this sticky note's interesting.")
            time.sleep(2)
            Elements.text("right", "[YOU] '(1) My 4 digit passcode is composed of two 2 digit codes.'")
            time.sleep(3)
            Elements.text("right", "[YOU] And also, '(2) is the first code, and (3) is the second.'")
            time.sleep(5)
            Elements.text("right", "[YOU] I wonder what that could mean.")
            time.sleep(1.5)
            Elements.text("centre", "TRAVEL TO:")
            Elements.text("centre", "[1] REPORT TO KITA  [2] TRASH PILE  [3] GARBAGE CAN")
            cont2 = Elements.option(3)
            if cont2 == 1:
                break
            elif cont2 == 2:
                cont = 2
            elif cont2 == 3:
                cont = 3
        elif cont == 2:
            Elements.loading(2, "You rummage through the trash pile. Disgusting behaviour.", 0.5)
            Elements.text("space", 1)
            Elements.text("right", "[YOU] This is all so disgusting. A bunch of rotten bananas, and...")
            Elements.text("right", "[YOU] A crumpled up piece of paper? I wonder what it says.")
            Elements.text("space", 1)
            Elements.text("centre", "Press 1 to uncrumple it.")
            cont3 = Elements.option(1)

            print(ch.Rooms.room2_clue1(0))
            Elements.text("right", "[YOU] I wonder what that could mean.")
            time.sleep(1.5)
            Elements.text("centre", "TRAVEL TO:")
            Elements.text("centre", "[1] STICKY NOTE BOARD  [2] REPORT TO KITA  [3] GARBAGE CAN")
            cont2 = Elements.option(3)
            if cont2 == 1:
                cont = 1
            elif cont2 == 2:
                break
            elif cont2 == 3:
                cont = 3
        elif cont == 3:
            Elements.loading(2, "You rummage through the garbage can. Disgusting behaviour.", 0.5)
            Elements.text("space", 1)
            Elements.text("right", "[YOU] Ah, what the hell. Food waste???")
            time.sleep(2)
            Elements.text("right", "[YOU] Who the hell throws out a perfectly good croissant?")
            time.sleep(2)
            Elements.text("space", 1)
            Elements.text("centre", "Press 1 to eat the mouldy croissant.")
            cont3 = Elements.option(1)

            print(ch.Blank.blank(0))
            Elements.text("right", "[YOU] That was digusting. What the fu-")
            time.sleep(2.5)
            Elements.text("space", 1)
            Elements.text("centre", "Out of the corner of your eye, you spot something.")
            time.sleep(2.5)
            Elements.text("space", 1)
            Elements.text("right", "[YOU] Is that a crumpled piece of paper in the garbage?")
            Elements.text("space", 1)
            Elements.text("centre", "Press 1 to take it out and uncrumple it.")
            cont3 = Elements.option(1)

            print(ch.Rooms.room2_clue2(0))
            Elements.text("right", "[YOU] I wonder what that could mean.")
            time.sleep(1.5)
            Elements.text("centre", "TRAVEL TO:")
            Elements.text("centre", "[1] STICKY NOTE BOARD  [2] TRASH PILE  [3] REPORT TO KITA")
            cont2 = Elements.option(3)
            if cont2 == 1:
                cont = 1
            elif cont2 == 2:
                cont = 2
            elif cont2 == 3:
                break

    Elements.loading(1, "You walk back to Kita", 0.5)

    while True:
        print(ch.Kita.normal(0))
        Elements.text("left", "[KITA] So, do you know what it is?")
        
        while True:
            try:
                Elements.text("space", 1)
                Elements.text("centre", "Type what you think the password is...")
                answer = int(input())
                if len(str(answer)) == 4:
                    break
                else:
                    Elements.text("space", 1)
                    Elements.text("centre", "Your answer should be 4 digits long.")
                    continue
            except:
                Elements.text("space", 1)
                Elements.text("centre", "Your answer should be an integer.")

        print(ch.Kita.normal(0))
        Elements.text("left", "[KITA] Hmm, let's try that.")

        # answer explanation:
        # Hitori Gotoh is Bocchi's full name. You need to do research to find this, or watch the anime/read the manga.
        # H = 8, G = 7
        # 2016 is when Bocchi kidnapped the player, so 2016-2000 = 16.
        if answer == 8716:
            break
        else:
            Elements.text("left", "[KITA] Ah, that's not the password unfortunately.")
            Elements.text("centre", "[1] Try again  [2] Search some more")
            cont = Elements.option(2)
            if cont == 1:
                continue
            elif cont == 2:
                break
    time.sleep(3)
    if answer == 8716:
        break

Elements.text("left", "[KITA] AHHHH It worked thank you so much " + your_name + "!!!")
time.sleep(2.5)
Elements.text("left", "[KITA] And it looks like she had her maps open at the right location!")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] Sure, no problem. Anytime!")
Elements.text("space", 1)
time.sleep(2.5)
Elements.text("left", "[KITA] Say, do you wanna come watch our band perform?")
time.sleep(1)
Elements.text("left", "[KITA] I don't really know my bandmates yet, so I'll have to just give you a call when we're ready.")
time.sleep(3.5)
# This story is so wacky, getting someone's number is definitely not this easy.
# Kita just has such massive Kita-aura that the story defies all logic
Elements.text("left", "[KITA] What's your number, " + your_name + "?")
time.sleep(2)
while True:
    try:
        Elements.text("centre", "Type your number as an integer.")
        # Note: I do not actually get your phone number from this, because there's no part of my code that calls home.
        # In other words, it's all offline.
        your_phone = int(input(""))
        if len(str(your_phone)) == 10:
            break
        else:
            Elements.text("space", 1)
            Elements.text("centre", "Please type your number in correctly.")
            continue
    except:
        Elements.text("space", 1)
        Elements.text("centre", "Please type your number in correctly.")

print(ch.Kita.normal(0))
Elements.text("left", "[KITA] Great! I'll call you when I've got things sorted out.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] Alright, cya!")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont3 = Elements.option(1)

print(ch.Blank.blank(0))
Elements.text("centre", "Even several months after your interaction with Kita, you eagerly awaited her call.")
time.sleep(3)
Elements.text("centre", "Something about her captivated you. And you couldn't quite put your finger on it.")
time.sleep(3)
Elements.text("centre", "Was it the long flowing red hair? Was it her below-average BMI?")
time.sleep(3)
Elements.text("centre", "Perhaps more captivating was why you were drawn to her.")
time.sleep(2)
# Definitely the KIT-AURA doing it's work here.
Elements.text("centre", "Why was a 28 year old attracted to this random high-schooler?")
time.sleep(3)
Elements.text("centre", "Regardless, she never got back to you.")
time.sleep(3)

print(ch.Blank.blank(0))
Elements.text("centre", "That is, until a few months later.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue to room 3.")
cont3 = Elements.option(1)





# Room 3

print(ch.Blank.blank(0))
Elements.text("centre", "It's a regular Japanese day. The sun is shining, the cicadas chirping. When suddenly...")
time.sleep(4)
Elements.pick_up_call(False)

Elements.text("left", "[MUFFLED VOICE] HIIII " + your_name + "!!!")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "You pause. The voice sounds familiar....")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to respond.")
cont = Elements.option(1)

print(ch.Blank.calling(0))
Elements.text("right", "[YOU] Hey, who is this?")
Elements.text("space", 1)
time.sleep(3)
Elements.text("left", "[KITA] It's Kita!!! How've you been??")
time.sleep(2.5)
Elements.text("space", 1)
Elements.text("centre", "Your heart skips a beat. She's finally called back.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("right", "[YOU] Oh, hi Kita! I've been good, how bout' you?")
time.sleep(4)

print(ch.Blank.calling(0))
Elements.text("left", "[KITA] Great!! We got our band together and we've been practicing.")
time.sleep(2.5)
Elements.text("left", "[KITA] We've actually got our first concert coming up soon!")
time.sleep(2.5)
Elements.text("left", "[KITA] Do you want to come?")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "Without even knowing anything about her band, you respond.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("right", "[YOU] S-sure! Of course, I'd love to see you play!")
time.sleep(4)
Elements.text("space", 1)
Elements.text("left", "[KITA] Great! Tickets are only ¥1500, and the concert is in two days.")
time.sleep(3)
Elements.text("left", "[KITA] You can just pay me in person later today at Shimo-Kitazawa.")
Elements.text("space", 1)
time.sleep(2.5)
Elements.text("centre", "Of course, she's calling to sell you something.")
time.sleep(2)
Elements.text("centre", "She wouldn't ACTUALLY call you for the sake of calling, would she?")
time.sleep(2)
Elements.text("centre", "Not when you're some random 28 year old basement dweller she found on the street.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

print(ch.Blank.calling(0))
Elements.text("right", "[YOU] Sure, what time?")
time.sleep(2.5)
Elements.text("left", "[KITA] Does 4PM by the train station work?")
time.sleep(2.5)
Elements.text("space", 1)
Elements.text("right", "[YOU] Yeah that works.")
time.sleep(2.3)
Elements.text("space", 1)
Elements.text("left", "[KITA] Great, I'll see you then!")
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

Elements.loading(1, "Some time passes.", 1)
print(ch.Blank.blank(0))
Elements.text("centre", "It's now 4 PM. You meet up with Kita at the train station.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

print(ch.Kita.normal(0))
Elements.text("left", "[KITA] Hi " + your_name + "!")
time.sleep(2.5)
Elements.text("left", "[KITA] Here's your ticket.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "She hands you your ticket.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to hand her the money.")
cont = Elements.option(1)

print(ch.Kita.happy(0))
Elements.text("centre", "You hand her ¥1500 out of your wallet.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("left", "[KITA] Thank you so much! I'll see you in two days!")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

Elements.loading(2, "2 days pass.", 1)
Elements.text("centre", "You walk towards the entrance of STARRY and see four girls at the entrance.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] Hey, uh, what's going on?")
time.sleep(3)

print(ch.Nijika.normal(0))
Elements.text("left", "[?] Oh hello! Are you here for our concert?")
time.sleep(2.5)
Elements.text("space", 1)
Elements.text("right", "[YOU] I'm here for a concert, yeah. Who're you?")
time.sleep(3)
Elements.text("space", 1)
Elements.text("left", "[NIJIKA] Oh sorry, I'm Nijika. I'm the drummer in the band that's performing today.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] Oh cool. You're with Kita and Bocchi?")
time.sleep(2.5)
Elements.text("space", 1)
Elements.text("left", "[NIJIKA] Yep! We've just got this little problem here.")
time.sleep(1)
Elements.text("left", "[NIJIKA] The manager gave us these keys to unlock the door, but she had to leave to go do something.")
time.sleep(3)
Elements.text("left", "[NIJIKA] Thing is, IDK which is the right one. There's about 50 of them, each labelled 1-50.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

print(ch.Nijika.normal(0))
Elements.text("centre", "She hands you the bundle of keys. There are indeed 50.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("left", "[NIJIKA] Sorry to put this on you, but we're performing in 30 minutes. Could you help us?")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to help out.")
cont = Elements.option(1)

print(ch.Nijika.happy(0))
Elements.text("right", "[YOU] Sure.")
time.sleep(1.5)
Elements.text("space", 1)
Elements.text("left", "[NIJIKA] Awesome! Thank you so much!")
time.sleep(2.5)
Elements.text("left", "There are a few clues hidden around here.")
time.sleep(2.5)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to explore the area.")
cont = Elements.option(1)

def ryo_check(ryo):
    Elements.text("space", 1)
    if ryo == "RYO":
        Elements.text("centre", "[1] TALK TO NIJIKA  [2] TALK TO RYO  [3] EXAMINE DOOR")
    else:
        Elements.text("centre", "[1] TALK TO NIJIKA  [2] TALK TO ?  [3] EXAMINE DOOR")
    return Elements.option(3)

# Ryo's name is unknown at first, so I set it equal to '?'.
# This gets changed if you ask her for her name.
# If you don't ask, her name remains unknown for the rest of the game.
# This is because Ryo is not best girl, and so the player doesn't care enough about her.
ryo = "?"

while True:
    print(ch.Rooms.room3(0))
    cont = ryo_check(ryo)

    while True:
        if cont == 1:
            Elements.loading(1, "You walk back to Nijika.", 0.5)
            print(ch.Nijika.normal(0))
            while True:
                Elements.text("space", 1)
                Elements.text("centre", "ASK ABOUT")
                Elements.text("centre", "[1] THE MANAGER  [2] THE BAND")
                cont2 = Elements.option(2)
                if cont2 == 1:
                    print(ch.Nijika.normal(0))
                    Elements.text("space", 1)
                    Elements.text("right", "[YOU] Hey Nijika, do you know anything about the manager?")
                    time.sleep(3)
                    Elements.text("space", 1)
                    Elements.text("left", "[NIJIKA] Yeah, she's my older sister.")
                    time.sleep(2.5)
                    while True:
                        Elements.text("space", 1)
                        Elements.text("centre", "[1] What's her number?  [2] Did she tell you anything about the key?")
                        cont3 = Elements.option(2)
                        if cont3 == 1:
                            Elements.loading(1, "Awkward silence...", 1)
                            print(ch.Nijika.normal(0))
                            time.sleep(1)
                            Elements.text("centre", "Nijika looks at you with disgust.")
                            time.sleep(1.5)
                            Elements.text("space", 1)
                            Elements.text("left", "[NIJIKA] What kind of question is that, weirdo.")
                        elif cont3 == 2:
                            Elements.loading(1, "Nijika thinks for a bit.", 1)
                            print(ch.Nijika.normal(0))
                            Elements.text("left", "[NIJIKA] Hmm... I think I remember her saying something about it.")
                            time.sleep(3)
                            Elements.text("left", "[NIJIKA] She said something about it being 'the length of the name'?")
                            time.sleep(2)
                            Elements.text("left", "[NIJIKA] Not too sure what that means....")
                            time.sleep(4)
                            break
                    break
                elif cont2 == 2:
                    print(ch.Nijika.normal(0))
                    Elements.text("right", "[YOU] So how's the band coming along?")
                    time.sleep(2.5)
                    Elements.text("space", 1)
                    Elements.text("left", "[NIJIKA] It's... okay. We're barely ready to play, but I think we have potential.")
                    time.sleep(3)
                    Elements.text("space", 1)
                    Elements.text("right", "[YOU] Ah, I see.")
                    time.sleep(3)
                
                
            Elements.text("space", 1)
            Elements.text("centre", "[1] TRY KEY  [2] TALK TO " + ryo + "  [3] EXAMINE DOOR")
            cont2 = Elements.option(3)
            if cont2 == 1:
                break
            elif cont2 == 2:
                cont = 2
            elif cont2 == 3:
                cont = 3

        elif cont == 2:
            Elements.loading(1, "You walk to " + ryo + ".", 0.5)
            print(ch.Ryo.normal(0))
            Elements.text("right", "[YOU] Hey, I have a couple questions to ask you.")
            time.sleep(3)
            Elements.text("left", "[" + ryo + "] Sure.")
            while True:
                Elements.text("space", 1)
                Elements.text("centre", "[1] What's your name?  [2] Know anything about the manager?")
                cont2 = Elements.option(2)
                if cont2 == 1:
                    print(ch.Ryo.normal(0))
                    Elements.text("right", "[YOU] By the way, what's your name?")
                    time.sleep(3)
                    Elements.text("space", 1)
                    if ryo == "?":
                        Elements.text("left", "[RYO] Ryo.")
                        ryo = "RYO"
                    else:
                        Elements.text("left", "[RYO] Didn't I already tell you?")
                elif cont2 == 2:
                    print(ch.Ryo.normal(0))
                    Elements.text("right", "[YOU] Do you know anything about the manager?")
                    time.sleep(3)
                    Elements.text("space", 1)
                    Elements.text("left", "[" + ryo + "] Yeah she sent me this weird message one time.")
                    Elements.text("left", "[" + ryo + "] 'key = len(name)'")
                    Elements.text("left", "[" + ryo + "] I don't know what it means.")
                    break

            Elements.text("space", 1)
            Elements.text("centre", "[1] TALK TO NIJIKA  [2] TRY KEY  [3] EXAMINE DOOR")
            cont2 = Elements.option(3)
            if cont2 == 1:
                cont = 1
            elif cont2 == 2:
                break
            elif cont2 == 3:
                cont = 3

        elif cont == 3:
            Elements.loading(1, "You walk to the door.", 0.5)
            print(ch.Rooms.room3_clue1(0))
            Elements.text("centre", "It reads 'Welcome to STARRY'")
            Elements.text("space", 1)
            time.sleep(2)
            Elements.text('right', "[YOU] So STARRY is the name, huh?")
            time.sleep(2)
            Elements.text("space", 1)
            Elements.text("centre", "[1] TALK TO NIJIKA  [2] TALK TO " + ryo + "  [3] TRY KEY")
            cont2 = Elements.option(3)
            if cont2 == 1:
                cont = 1
            elif cont2 == 2:
                cont = 2
            elif cont2 == 3:
                break
    while True:
        while True:
            print(ch.Blank.blank(0))
            Elements.text("centre", "Type which key (1-50) you think is correct.")
            time.sleep(2)
            try:
                answer = int(input(""))
                if 0 < answer <= 50:
                    break
                else:
                    Elements.text("centre", "Please enter a number between 1 and 50.")
                    time.sleep(2)
            except:
                Elements.text("centre", "Please enter an integer number.")
                time.sleep(2)
        Elements.loading(2, "You try key number " + str(answer) + "...", 0.5)
        print(ch.Blank.blank(0))
        if answer == 6:
            break
        else:
            Elements.text("centre", "That wasn't the right key.")
            time.sleep(2)
            Elements.text("centre", "[1] Try again.  [2] Go search for more clues.")
            cont = Elements.option(2)
            if cont == 1:
                continue
            elif cont == 2:
                break
    if answer == 6:
        break

Elements.text("centre", "The door opens.")
time.sleep(3)

print(ch.Nijika.happy(0))
Elements.text("left", "[NIJIKA] It worked! Thanks a bunch!")
time.sleep(2)
Elements.text("space", 1)
Elements.text("right", "[YOU] No problem, Nijika.")
Elements.text("space", 1)
Elements.text("centre", "Press 1 to enter STARRY.")
cont = Elements.option(1)

print(ch.Blank.blank(0))
Elements.text("centre", "You enter into Starry, and wait for the show to start.")
time.sleep(4)
Elements.loading(2, "The band plays.", 1)
print(ch.Blank.blank(0))
Elements.text("centre", "The band plays pretty well, for a band that's just started up.")
time.sleep(3)
Elements.text("centre", "You remark that they're a little bit rough around the edges...")
time.sleep(3)
Elements.text("centre", "...but they've got a lot of potential.")
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

print(ch.Blank.blank(0))
Elements.text("right", "[YOU] Bocchi's solo was kind of amazing, seemed to carry the whole show.")
time.sleep(4)
Elements.loading(2, "You leave the venue and wait a few months.", 1)
print(ch.Blank.blank(0))
Elements.text("centre", "And then you get another call.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue to room 4.")
cont = Elements.option(1)







# Room 4

Elements.pick_up_call(True)
# Kita here remembers your name after all this time because she's just that big of a boss.
Elements.text("left", "[KITA] Hey " + your_name + ", how's life been!?")
time.sleep(2.5)
Elements.text("space", 1)
Elements.text("right", "[YOU] It's alright, just got off work. How bout' you?")
time.sleep(2.5)
Elements.text("space", 1)
Elements.text("left", "[KITA] It's going amazing! My band and I have been practicing a lot!")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] Oh, I see. That's great news!")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "You pretend that it's your first time hearing about it.")
time.sleep(3)
Elements.text("centre", "You're lying through your teeth.")
time.sleep(2.5)
# ISSTAGRAM is not a typo btw, that's how it is in the show.
Elements.text("centre", "You've been stalking Kita's ISSTAGRAM for a while...")
time.sleep(2.5)
Elements.text("centre", "...so you know all about her Kessoku Band.")
time.sleep(4)

print(ch.Blank.calling(0))
Elements.text("left", "[KITA] Anyways, do you wanna come watch us play again? It'll be free!")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] For sure! I'd love to!")
time.sleep(2.5)
Elements.text("space", 1)
Elements.text("left", "[KITA] Great! It'll be at my school's culture festival on Wednesday.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] Awesome! I'll be sure to check it out.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

Elements.loading(1, "A few days pass. You're at the festival, and they're about to play.", 1)
print(ch.Blank.blank(0))
Elements.text("left", "[ANNOUNCER] Our next band is Kessoku Band!")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "As the curtains lift, the crowd cheers.")
time.sleep(3)
Elements.text("space", 1)

print(ch.Kita.normal(0))
Elements.text("left", "[KITA, on stage] We're Kessoku Band, and we mainly play outside of school.")
time.sleep(2.8)
Elements.text("left", "[KITA, on stage] We hope our performance helps make today more memorable for everyone.")
time.sleep(3)
Elements.text("left", "[KITA, on stage] And if you're interested, we hope you'll come to see us at our club!")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "The crowd cheers again.")
time.sleep(3)
Elements.text("left", "[KITA, on stage] Here comes our first song...")
time.sleep(4)

print(ch.Nijika.normal(0))
Elements.text("left", "[KITA, on stage] ...as Kessoku Band!")
time.sleep(1)
print(ch.Bocchi.normal(0))
Elements.text("left", "[KITA, on stage] ...as Kessoku Band!")
time.sleep(1)
print(ch.Ryo.normal(0))
Elements.text("left", "[KITA, on stage] ...as Kessoku Band!")
time.sleep(1)

print(ch.Blank.blank(0))
Elements.text("centre", "The band plays. But something feels off...")
time.sleep(2.5)
Elements.text("centre", "You glance at Bocchi. She's not playing anymore.")
time.sleep(4)

print(ch.Blank.exclaim(0))
Elements.text("right", "[YOU] One of the strings on her guitar is broken!")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "You make it your responsibility to make sure she can play.")
time.sleep(3)
Elements.text("centre", "Luckily, she has plot armour. You just have to activate it....")
time.sleep(3)
Elements.text("space", 1)
Elements.text("right", "[YOU] I need to give her a signal. She needs to do something!")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to look around for ideas.")
cont = Elements.option(1)

while True:
    print(ch.Blank.blank(0))
    Elements.text("right", "[YOU] I need to find something that she can use to mitigate her broken string.")
    time.sleep(3)
    Elements.text("space", 1)
    Elements.text("centre", "[1] Look right  [2] Look left  [3] Reach into pocket")
    cont = Elements.option(3)
    while True:
        print(ch.Blank.blank(0))
        if cont == 1:
            Elements.text("centre", "On your right, you see someone drinking water from a GLASS CUP.")
            time.sleep(3)
            Elements.text("space", 1)
            Elements.text("right", "[YOU] Hmmm, I wonder why 'glass cup' is in all-caps?")
            time.sleep(3)
            Elements.text("space", 1)
            Elements.text("centre", "Coincidentally, Bocchi has a glass cup right next to her on stage.")
            time.sleep(3)
            Elements.text("centre", "[1] I have an idea!  [2] Look left  [3] Reach into pocket")
            cont2 = Elements.option(3)
            if cont2 == 1:
                break
            elif cont2 == 2:
                cont = 2
            elif cont2 == 3:
                cont = 3
        elif cont == 2:
            Elements.text("centre", "On your left, you see someone chewing BUBBLE GUM.")
            time.sleep(3)
            Elements.text("space", 1)
            Elements.text("right", "[YOU] Hmmm, I wonder why 'bubble gum' is in all-caps?")
            time.sleep(3)
            Elements.text("space", 1)
            Elements.text("centre", "Bocchi could have bubble gum in her pocket.")
            time.sleep(3)
            Elements.text("centre", "[1] Look right  [2] I have an idea!  [3] Reach into pocket")
            cont2 = Elements.option(3)
            if cont2 == 1:
                cont = 1
            elif cont2 == 2:
                break
            elif cont2 == 3:
                cont = 3
        elif cont == 3:
            Elements.loading(1, "You rummage around in your pocket.", 0.5)
            print(ch.Blank.blank(0))
            Elements.text("centre", "You pull some KEYS out of your pocket.")
            time.sleep(3)
            Elements.text("space", 1)
            Elements.text("right", "[YOU] Hmmm, I wonder why 'keys' is in all-caps?")
            time.sleep(3)
            Elements.text("space", 1)
            Elements.text("centre", "Bocchi probably has keys on her.")
            time.sleep(3)
            Elements.text("centre", "[1] Look right  [2] Look left  [3] I have an idea!")
            cont2 = Elements.option(3)
            if cont2 == 1:
                cont = 1
            elif cont2 == 2:
                cont = 2
            elif cont2 == 3:
                break
    while True:
        print(ch.Blank.blank(0))
        Elements.text("centre", "You're pretty far back, but Bocchi will probably still hear you if you shout.")
        time.sleep(4)
        Elements.text("space", 1)
        Elements.text("right", "[YOU] I should shout something, maybe she'll hear it.")
        time.sleep(2.5)
        Elements.text("space", 1)
        Elements.text("centre", "What do you shout?")
        answer = str(input("")).upper()
        print(ch.Blank.exclaim(0))
        Elements.text("right", "[YOU, shouting] " + answer + "!")
        time.sleep(2)
        Elements.text("space", 1)
        Elements.text("centre", "People around you look at you funny.")
        time.sleep(2.5)
        if answer == "GLASS CUP":
            break
        else:
            Elements.text("centre", "Why did you say that...?")
            time.sleep(3)
            Elements.text("space", 1)
            if r(0,1) == 1:
                Elements.text("right", "[YOU] Hmm... maybe I should say something that she can slide across all her strings...")
            else:
                Elements.text("right", "[YOU] ...maybe something circular could work.")
            time.sleep(3)
            Elements.text("space", 1)
            Elements.text("centre", "[1] Shout something else  [2] Look for more clues")
            cont = Elements.option(2)
            if cont == 1:
                continue
            elif cont == 2:
                break
    if answer == "GLASS CUP":
        break

print(ch.Bocchi.happy(0))
Elements.text("centre", "Bocchi takes the glass cup right next to her, and slides it across all of her strings.")
time.sleep(3)
Elements.text("centre", "The sound of all of the strings reverberates through the cup together...")
time.sleep(2.8)
Elements.text("centre", "And create the sickest guitar improv you've ever seen.")
time.sleep(2.5)
Elements.text("centre", "The crowd cheers, and the show ends on a high note.")
time.sleep(2)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

print(ch.Blank.blank(0))
Elements.text("centre", "As the years pass, you follow Kessoku Band and all their shenanigans.")
time.sleep(3)
Elements.text("centre", "You watch them progress onto the world stage.")
time.sleep(3)
Elements.text("centre", "You watch them succeed.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "And as you're on your way to your dozenth Kessoku Band concert, you get another call.")
Elements.text("centre", "It's Kita.")
time.sleep(3)
Elements.text("space", 1)
Elements.text("centre", "Press 1 to continue.")
cont = Elements.option(1)

print(ch.Blank.ty_for_playing(0))
final_text = "Thank you for playing! I hopy you enjoyed!"
Elements.text("space", 1)
# Not using the Elements.text("centre") function here because the final frame is wider.
print(" " * int((181-len(final_text))/2) + final_text)
Elements.text("space", 2)