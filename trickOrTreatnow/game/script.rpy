# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gojo = Character("your sensei (gojo satoru)")
define nobara = Character("Nobara Kugisaki")
define choso = Character("Choso (drunk)")
define all3 = Character("(everyone in the group)")
define todo = Character("Aoi Todo")
define yuji = Character("Itadori Yuji")
define mahito = Character("Mahito")
define megumi = Character("Megumi Fushiguro")
define context_prompter = Character("")

image ghost = "ghost.png"

transform ghost1:
    zoom 0.2
    xalign 0.0 yalign 0.2
    linear 0.2 xalign 0.8 yalign 0.3
    linear 0.2 xalign 0.1 yalign 0.7
    linear 0.2 xalign 0.7 yalign 0.5
    linear 0.2 xalign 0.2 yalign 0.1
    linear 0.2 xalign 0.6 yalign 0.4
    alpha 0.0
transform ghost2:
    zoom 0.25
    xalign 0.2 yalign 0.1
    linear 0.2 xalign 0.9 yalign 0.2
    linear 0.2 xalign 0.3 yalign 0.6
    linear 0.2 xalign 0.8 yalign 0.4
    linear 0.2 xalign 0.1 yalign 0.3
    linear 0.2 xalign 0.5 yalign 0.5
    alpha 0.0
transform ghost3:
    zoom 0.3
    xalign 0.1 yalign 0.8
    linear 0.2 xalign 0.6 yalign 0.1
    linear 0.2 xalign 0.2 yalign 0.7
    linear 0.2 xalign 0.7 yalign 0.2
    linear 0.2 xalign 0.3 yalign 0.5
    linear 0.2 xalign 0.8 yalign 0.8
    alpha 0.0
transform ghost4:
    zoom 0.22
    xalign 0.3 yalign 0.3
    linear 0.2 xalign 0.7 yalign 0.1
    linear 0.2 xalign 0.1 yalign 0.5
    linear 0.2 xalign 0.8 yalign 0.8
    linear 0.2 xalign 0.2 yalign 0.2
    linear 0.2 xalign 0.6 yalign 0.6
    alpha 0.0
transform ghost5:
    zoom 0.28
    xalign 0.4 yalign 0.6
    linear 0.2 xalign 0.1 yalign 0.1
    linear 0.2 xalign 0.7 yalign 0.5
    linear 0.2 xalign 0.3 yalign 0.8
    linear 0.2 xalign 0.8 yalign 0.2
    linear 0.2 xalign 0.5 yalign 0.3
    alpha 0.0
transform ghost6:
    zoom 0.2
    xalign 0.5 yalign 0.2
    linear 0.2 xalign 0.9 yalign 0.7
    linear 0.2 xalign 0.2 yalign 0.3
    linear 0.2 xalign 0.8 yalign 0.5
    linear 0.2 xalign 0.1 yalign 0.1
    linear 0.2 xalign 0.6 yalign 0.4
    alpha 0.0
transform ghost7:
    zoom 0.3
    xalign 0.6 yalign 0.1
    linear 0.2 xalign 0.2 yalign 0.6
    linear 0.2 xalign 0.7 yalign 0.2
    linear 0.2 xalign 0.1 yalign 0.8
    linear 0.2 xalign 0.8 yalign 0.3
    linear 0.2 xalign 0.3 yalign 0.5
    alpha 0.0
transform ghost8:
    zoom 0.25
    xalign 0.7 yalign 0.5
    linear 0.2 xalign 0.1 yalign 0.2
    linear 0.2 xalign 0.8 yalign 0.6
    linear 0.2 xalign 0.3 yalign 0.1
    linear 0.2 xalign 0.9 yalign 0.7
    linear 0.2 xalign 0.5 yalign 0.4
    alpha 0.0
transform ghost9:
    zoom 0.2
    xalign 0.8 yalign 0.3
    linear 0.2 xalign 0.3 yalign 0.7
    linear 0.2 xalign 0.6 yalign 0.1
    linear 0.2 xalign 0.2 yalign 0.5
    linear 0.2 xalign 0.7 yalign 0.2
    linear 0.2 xalign 0.4 yalign 0.6
    alpha 0.0
transform ghost10:
    zoom 0.3
    xalign 0.9 yalign 0.6
    linear 0.2 xalign 0.2 yalign 0.1
    linear 0.2 xalign 0.8 yalign 0.5
    linear 0.2 xalign 0.1 yalign 0.8
    linear 0.2 xalign 0.7 yalign 0.3
    linear 0.2 xalign 0.5 yalign 0.2
    alpha 0.0

screen ghost_attack:
    add "ghost" at ghost1
    add "ghost" at ghost2
    add "ghost" at ghost3
    add "ghost" at ghost4
    add "ghost" at ghost5
    add "ghost" at ghost6
    add "ghost" at ghost7
    add "ghost" at ghost8
    add "ghost" at ghost9
    add "ghost" at ghost10

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene your_local_cursed_school

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    transform half_size:
        zoom 0.5

    show gojo at half_size

    # These display lines of dialogue.

    gojo "HEY MY LITTLE YOUNG ADVENTURER."
    gojo "Look. I'm not going to sentence you to prison or anything. This isn't lore accurate."
    gojo "the gameplay will have a bit of jumpscares, but nothing too crazy."
    gojo "and this game contains spoiler for Jujutsu Kaisen season 2 (Shibuya Incident arc)"
    gojo "the story goes as follows..."

    jump context

label context:

    scene black
    hide gojo

    context_prompter "on a black scary night of the 31st october..."
    context_prompter "you, and your high-school friends decide to go trick or treating."

    show yuji_blkwht with Dissolve(.5):
        xalign 0.0
        yalign -0.2

    show megumi_blkwht with Dissolve(.5):
        xalign 1.0
        yalign 1.0

    show nobara_blkwht with Dissolve(.5): 
        xalign 0.50
        yalign 1.0

    context_prompter "the choices you make this night may change your life... and such forever."
    jump maingame

label maingame:

    scene maingame_night

    hide yuji_blkwht
    hide megumi_blkwht
    hide nobara_blkwht

    menu:
        "Go trick or treating...":
            jump trick_yes
        
        "I'd rather not.":
            jump trick_no

    label trick_yes:
        $ menu_flag = True

        show nobara_blkwht with Dissolve(.5):
            xalign 0.05
            yalign 1.0

        nobara "I knew you'd be up for that! It'll be fun, cmon!"
        jump trick_next

    label trick_no:
        $ menu_flag = True

        show nobara_blkwht with Dissolve(.5):
            xalign 0.05
            yalign 1.0

        nobara "What are you? A scaredy cat? C'mon. Let's go!! What's the worst that can happen anyway??"
        jump trick_next

    label trick_next:

        hide nobara_blkwht

        scene house1 with Dissolve(.5)
        context_prompter "You arrive at the first house. You walk up to the door."

        show nobara_blkwht with Dissolve(.5):
            xalign 0.5
            yalign 1.0

        show yuji_blkwht with Dissolve(.5):
            xalign 0.0
            yalign -0.2
        
        show megumi_blkwht with Dissolve(.5):
            xalign 1.0
            yalign 1.0

        menu:
            "Knock on the door":
                context_prompter "You knock on the door."

                show choso_blkwht at half_size with Dissolve(.5):
                    xalign 0.75
                    yalign 0.685

                choso "what."
                all3 "TRICK OR TREAT!!"
                choso "i'm tired dude. just take this candy and go away."
                choso "i can't even focus on my eyes."

                hide choso_blkwht with Dissolve(.2)

                context_prompter "Choso gives you a bit of candy. Some of them are already eaten cause he can't see, but it's not all that bad."
                context_prompter "You thank him and move on."

                jump afterchoso

            "Run away":
                context_prompter "You all 3 run away. You shouldn't do this often.. candy's not gonna come magically!"
                jump afterchoso

    label afterchoso:
        hide megumi_blkwht
        hide yuji_blkwht
        hide nobara_blkwht
        scene house2 with Dissolve(.5)
        context_prompter "You arrive at the second house. What will you do?"

        show nobara_blkwht with Dissolve(.5):
            xalign 0.5
            yalign 1.0

        show yuji_blkwht with Dissolve(.5):
            xalign 0.0
            yalign -0.2

        show megumi_blkwht with Dissolve(.5):
            xalign 1.0
            yalign 1.0

        menu:
            "Knock on the door":
                context_prompter "You knock on the door."
                show todo at half_size with Dissolve(.5):
                    xalign 0.75
                    yalign 0.54

                todo "IS THAT MY BESTO FRIENDO YUJI ITADORIDO?????"
                yuji "dang. didn't know you were in that house. that's crazy."
                all3 "TRICK OR TREAT??????????????????"

                todo "since yuji's here, i'll give treat. i'll give you a lot too."

                show white_flash with Dissolve(.2):
                    Solid("#FFFFFF")
                with Pause(0.005)
                hide white_flash with Dissolve(.2)

                image snow = SnowBlossom("candy.png", count=100)
                show snow

                todo "there."

                yuji "hey bro chill out on the candy cmon we get the idea."
                todo "my fault."
                hide snow with Dissolve(.5)
                all3 "thanks todo you're the best!!"
                hide todo with Dissolve(0.5)
                context_prompter "you then move on to the next house, happy of having this many candy now thanks to todo."
                jump afterh2
            
            "Run away":
                context_prompter "You all 3 run away. I really think you should stop and you should start trick or treating next time... just saying."
                jump afterh2

    label afterh2:
        hide nobara_blkwht
        hide yuji_blkwht
        hide megumi_blkwht
        scene house3 with Dissolve(.5)
        context_prompter "You arrive at the last house, the third. What will you do now..?"

        show nobara_blkwht with Dissolve(.5):
            xalign 0.5
            yalign 1.0

        show yuji_blkwht with Dissolve(.5):
            xalign 0.0
            yalign -0.2

        show megumi_blkwht with Dissolve(.5):
            xalign 1.0
            yalign 1.0  

        menu:
            "Knock on the door":
                label h3knock:
                context_prompter "You knock on the door..."
                show mahito at half_size with Dissolve(.5):
                    xalign 0.75
                    yalign 0.78
                mahito "Let me guess."
                all3 "TRICK OR TREAT!!!!!!!!!!"
                mahito "C'mon guys. You've passed age for this. Whataver."
                context_prompter "Mahito gives all 3 of you treats, hardly smiling..."

                mahito "By the way, wanna hear a joke?"
                menu:
                    "Hear the joke":
                        mahito "Great! Why does Nobara look like a skull?"
                        label h3joke:
                        megumi "she dosen't you dumb fat pig."
                        mahito "Are you sure?"
                        yuji "I mean yeah. She's in front of us."
                        mahito "look again!"
                        hide nobara_blkwht
                        play sound "killsfx.mp3"
                        show nobara_dead with Dissolve(.5)
                        mahito "hahaha."
                        megumi "yo what the fuck"
                        yuji "what the fuck did you do???"
                        mahito "wasn't my joke funny?"
                        menu:
                            "no, that shit isn't funny man":
                                mahito "how do you dare say that? all right then."
                                label badjoke:
                                    play sound "killsfx.mp3"

                                    show screen ghost_attack
                                    play sound "hahahahah.mp3"
                                    $ renpy.pause(1, hard=True)
                                    hide screen ghost_attack

                                    show screen ghost_attack
                                    $ renpy.pause(1, hard=True)
                                    hide screen ghost_attack

                                    show screen ghost_attack
                                    play sound "hahahahah.mp3"
                                    $ renpy.pause(1, hard=True)
                                    hide screen ghost_attack

                                    mahito "these ghosts r going crazy but heh u lost nobara now"
                                    mahito "don't worry tho. you're next, megumi and yuji!"
                                    jump death

                            "yeah that's funny":
                                mahito "stop lying. i know you're so mad, yuji."
                                jump badjoke
                    
                    "No thanks.":
                        mahito "I don't care. you'll hear it anyway."
                        mahito "Why does Nobara look like a skull?"
                        jump h3joke
            
            "Run away (you really shouldn't)":
                context_prompter "Mahito heard you arrive..."
                mahito "Hey hey hey. Where are you all going. Come back here. Go ahead."
                jump h3knock

    label death:
        play sound "killsfx.mp3"
        hide nobara_dead
        hide yuji_blkwht
        hide mahito
        play sound "killsfx.mp3"
        hide megumi_blkwht

        scene black
        show blood with Dissolve(.5):
            xalign 0.5
            yalign 0.0
        context_prompter "unfortunately, mahito killed nobara.. aswell as yuji and megumi."
        context_prompter "you all died. mahito is now having a fest eating those treats you catched."
        context_prompter "don't forget to check the github repo and to give good stars!! :)"
        return
