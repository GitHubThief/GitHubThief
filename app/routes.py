import os
from app import app
from flask import render_template, request, redirect
from app.models import model


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'IA'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://MrHypeman:tWHNmGVrmDVacOuA@cluster0-7hbc1.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)
# INDEX

@app.route('/')
@app.route('/index')

def index():
    # image = "https://gamepedia.cursecdn.com/mtgsalvation_gamepedia/thumb/c/c8/Naya.jpg/500px-Naya.jpg?version=dbaf25f9461408c012cd52820e904800"
    return render_template('index.html',)



@app.route('/results', methods = ["get", "post"])
def results():
    collection = mongo.db.events
    user_info = dict(request.form)
    try:
        white = user_info["color1"]
    except:
        print("color1")
    try:
        blue = user_info["color2"]
    except:
        print("color2")
    try:
        black = user_info["color3"]
    except:
        print("color3")
    try:
        red = user_info["color4"]
    except:
        print("color4")
    try:
        green = user_info["color5"]
    except:
        print("color5")
    rating = user_info["rating"]
    print(rating)
    print(user_info)


    if rating == "1":
        message2 = """The rating you chose for yourself is for someone close to a begginer player. The recomendation is to
        keep the deck simple, and to not focus to much on the interaction between cards."""

    elif rating == "2":
        message2 = """The rating you chose for yourself is for someone close to a begginer player. The recomendation is to
        keep the deck simple, and to not focus to much on the interaction between cards."""

    elif rating == "3":
        message2 = """The rating you chose for yourself is for someone close to a begginer player. The recomendation is to
        keep the deck simple, and to not focus to much on the interaction between cards."""

    elif rating == "4":
        message2 = """The rating you chose for yourself is for someone who is an intermediate to seasoned player of magic. By this time you
        should known the game pretty well and be playing decks that are fairly complex. The recomendation is to start focusing on
        the inner workings of a deck. Build combos that complement it and find cards that work together for the purpose of your deck."""

    elif rating == "5":
        message2 = """The rating you chose for yourself is for someone who is an intermediate to seasoned player of magic. By this time you
        should known the game pretty well and be playing decks that are fairly complex. The recomendation is to start focusing on
        the inner workings of a deck. Build combos that complement it and find cards that work together for the purpose of your deck."""

    elif rating == "6":
        message2 = """The rating you chose for yourself is for someone who is an intermediate to seasoned player of magic. By this time you
        should known the game pretty well and be playing decks that are fairly complex. The recomendation is to start focusing on
        the inner workings of a deck. Build combos that complement it and find cards that work together for the purpose of your deck."""

    elif rating == "7":
        message2 = """The rating you chose for yourself is for someone who is an intermediate to seasoned player of magic. By this time you
        should known the game pretty well and be playing decks that are fairly complex. The recomendation is to start focusing on
        the inner workings of a deck. Build combos that complement it and find cards that work together for the purpose of your deck."""

    elif rating == "8":
        message2 = """The rating you chose for yourself is for someone who is an intermediate to seasoned player of magic. By this time you
        should known the game pretty well and be playing decks that are fairly complex. The recomendation is to start focusing on
        the inner workings of a deck. Build combos that complement it and find cards that work together for the purpose of your deck."""

    elif rating == "9":
        message2 = """The rating you chose for yourself is for someone who has been playing magic for years and is an expert at playing. The
        recomendation is to maybe find a new color to play and master it as well, or play with the other color combinations."""

    elif rating == "10":
        message2 = """The rating you chose for yourself is for someone who has been playing magic for years and is an expert at playing. The
        recomendation is to maybe find a new color to play and master it as well, or play with the other color combinations."""


    try:
        if white:
            message = """White in Magic will regularly be regarded as the support color in the game,
            however it still has a lot to offer. White is asscociated with life gain and being able to
            destroy almost anything on the board. In addition those in white tend to have/want a longer game,
            Since white spells become worse to deal with the longer they stick around"""
            image = model.magic_dictionary[0]["image"]
    except:
         print()
    try:
        if blue:
            message = """Blue is the control color of Magic, It doesn't really want to do anything
            specific except prohibit the opponent from playing effectivly through different means. Blue
            is also able to keep up with the other colors by drawing lots of cards."""
            image = model.magic_dictionary[1]["image"]
    except:
         print()
    try:
        if black:
            message = """Black by itself is the most strategic of the five colors. In addition to being
            able to get rid of any creature, Black decks tend to use the graveyard for resourcees and take
            advantage of things dying across the board."""
            image = model.magic_dictionary[2]["image"]
    except:
         print()
    try:
        if red:
            message = """Red in Magic is called the color of emotion. Red likes to deal lots of damage fast or swarm
            the board with small creatures. In addition most combos in red are either damage or combat based. """
            image = model.magic_dictionary[3]["image"]
    except:
         print()
    try:
        if green:
            message = """Green isnt known for being very diverse when it comes to play style. What Green does in Magic
            is make a lot of mana or play big creatures. However eventhough green isnt very diverse onits own, it combos
            very well with the other colors """
            image = model.magic_dictionary[4]["image"]
    except:
         print()
    try:
        if white and blue:
            message = """White and blue are classic control colors in Magic. Known to the Magic fanbase as Azorius, it combines
            the ability to draw cards from blue, and being able to inhibit creatures from acting granted by white. Also from Blue
            Azorius has a lot of powerful flying creatures which can be protected by the white aspect."""
            image = model.magic_dictionary[5]["image"]
    except:
         print()
    try:
        if red and white:
            message = """Red and White are the Boros colors. Armed with powrful flying creatures and high damage spells Boros
            wants to attack and attack fast. If it is unable to play early than it brings out some of the most powerful creatures
            in the game and protect them until the oppennet loses."""
            image = model.magic_dictionary[6]["image"]
    except:
         print()
    try:
        if black and blue:
            message = """Black and Blue are the Dimir colors, they are noted as a color pair suited for control magic. This is due
            to Blue being able to draw cards and black being able to remove almsot any creature that appears on the board."""
            image = model.magic_dictionary[7]["image"]
    except:
         print()
    try:
        if green and black:
            message = """Green and Black are the Color Combination called Golgari. It is simple to explain and hard to execute in game.
            Golgarri aims to get creatures and cards into the graveyardand them get them back onto the battlefield, in general it takes
            advatage of cards in your or an opponents graveyard."""
            image = model.magic_dictionary[8]["image"]
    except:
         print()
    try:
        if green and red:
            message = """Green and red are the Gruul colors. They are fast and aim to beat the opponent quickly. The red side is able
            to play creatures fast and the green side can make them stronger. If it goes to the late game Then these color can overwhelm
            with big creatures that cant be stopped."""
            image = model.magic_dictionary[9]["image"]
    except:
         print()
    try:
        if red and blue:
            message = """A combination of colors that is reconsided among fans, red and blue are knwon as Izzet. Red and blue are seen together
            often as they work off of eachother very well. While red can deal damage quickly blue can draw more cards to deal more damage
            or counter the oppenents spells altogehter. Izzet also has a lot of affinity with the card type artifact."""
            image = model.magic_dictionary[10]["image"]
    except:
         print()
    try:
        if red and blue:
            message = """A combination of colors that is reconsided among fans, red and blue are knwon as Izzet. Red and blue are seen together
            often as they work off of eachother very well. While red can deal damage quickly blue can draw more cards to deal more damage
            or counter the oppenents spells altogehter. Izzet also has a lot of affinity with the card type artifact."""
            image = model.magic_dictionary[10]["image"]
    except:
         print()
    try:
        if red and blue:
            message = """A combination of colors that is reconsided among fans, red and blue are knwon as Izzet. Red and blue are seen together
            often as they work off of eachother very well. While red can deal damage quickly blue can draw more cards to deal more damage
            or counter the oppenents spells altogehter. Izzet also has a lot of affinity with the card type artifact."""
            image = model.magic_dictionary[10]["image"]
    except:
         print()
    try:
        if black and white:
            message = """The colors of Black and white ae called Orzhov, and like Izzet the two colors that make it up work very well together.
            Black and white are common to be seen together and very well play of the colors strengths. Black is able to expend life and creatures
             to get more cards, while white is bale to gain that life back and return the orginal creatures to the battlefield."""
            image = model.magic_dictionary[11]["image"]
    except:
         print()
    try:
        if red and black:
            message = """Black and red are called Rakdos and are staple agro colors. Rakdos aims to deal damage fast and as much as possible.
            This can be in many ways, ranging from creatures to spells that damage out of nowhere, all the while the black side of the color
            combination can get rid of any opposing creatures and even deal more damage."""
            image = model.magic_dictionary[12]["image"]
    except:
         print()
    try:
        if green and white:
            message = """Green and white are the Selesnya colors and are strong and durable. Slesnya aims to be teh last one standing in a battle
             of strength. The green side makes creatures that are large, and the white half protects them until the time is right. The Selesnya
             colors also care about more of your own creatures on the battlefield, as shown in some of the key mechanics of the colors."""
            image = model.magic_dictionary[13]["image"]
    except:
         print()
    try:
        if green and blue:
            message = """Green blue is Simic, a powerful color combination that can win easily when left unchecked. The Simic colors differnt to
            most color combination more so becomes its own color and not use the strengths of each color within it. Simic tends to alter your
            creatures on the battlefield to make them more powerfull"""
            image = model.magic_dictionary[14]["image"]
    except:
         print()
    try:
        if white and green and black:
            message = """White green and black are the tri-color combination known as Abzan. Most decks that use theese colors revolve around the
            graveyard in some way. This could be either getting creatures in and out of the graveyard to benefit your deck, or to make it easier to
            play big creatures with more cards in the graveyard."""
            image = model.magic_dictionary[15]["image"]
    except:
         print()
    try:
        if white and green and blue:
            message = """White green and blue are the tri-color combination known as Bant. The Bant colors care about creatures and how they interact
            with the board. This could even be your opponents creatures. A deck with the Bant colors could either support its own creatures, or even
            steal the opponents for its own benefit."""
            image = model.magic_dictionary[16]["image"]
    except:
         print()
    try:
        if white and black and blue:
            message = """White balck and blue are the tri-color combination known as Esper. Esper is an intersting group of colors becuase they want to
            take advantage of any creature or any card anywhere. The Esper colors are able to manipulate and steal cards from any zone of the game, the library,
            the battlefield, the graveyard, and even your opponents hand."""
            image = model.magic_dictionary[17]["image"]
    except:
         print()
    try:
        if red and black and blue:
            message = """Red black and Blue are the tri-color combiation kown as Grixis. Grixis is the combination for three color control. It aims to take away
            all of its oppenents resources so they are powerless to do anything. This can be done in a few ways, the most common and famous is Grixs' abilitiy to
            make its opponents discard cards."""
            image = model.magic_dictionary[18]["image"]
    except:
         print()
    try:
        if red and white and blue:
            message = """Red white and blue are teh tri-color combination known as Jeskai. The Jeskai colors work very well together and are very good and destroying
            everything in its path. These colors are also very good at building defenses and drawing cards. Blue draws cards while red and white defend and fortify
            your board."""
            image = model.magic_dictionary[19]["image"]
    except:
         print()
    try:
        if red and green and black:
            message = """Red green and black are the tri-color combination known as Jund. Jund is a group of colors focused on creatures and damage. The jund colors
            want to first make a lot of creatures and then either attack with them, or sacrifice them to deal more damage to the opponent. Later those creatures
            can come back and repeat the cycle thanks to Jund having black in it's colors."""
            image = model.magic_dictionary[20]["image"]
    except:
         print()
    try:
        if red and black and white:
            message = """red black and white are the tri-color combination known as Mardu. Mardu wants to play fast and cast giant creatures as soon as possible. Mardu
            relies on the speed of red and the removal of the combined black and white, This allows it to play fast with nothing in its way. In addition, the black in Mardu
            will often take advantage of dying creatures and the graveyard."""
            image = model.magic_dictionary[21]["image"]
    except:
         print()
    try:
        if red and green and white:
            message = """Red green and white are the tri-color combination known as Naya. These three colors aim to Cast big spells and hold nothing back in the process. With
            the green side Naya plays big creatures and uses red and some green to play them faster than normal. The white side then assists to either make the creatures bigger,
            make more big creatures, or remove any threats on the opponents board."""
            image = model.magic_dictionary[22]["image"]
    except:
         print()
    try:
        if green and blue and black:
            message = """Green blue and black are the tri-color combination known as Sultai. Sultain is the crad draw from green and blue with the added bonus of black's graveyard
            recurssion. Sultai aims to play spells to draw cards and limit the resources of its opponents. Then when decided by the play it grabs huge creatures from graveyards
            and plays all of them."""
            image = model.magic_dictionary[23]["image"]
    except:
         print()
    try:
        if red and green and blue:
            message = """Red green and blue are the tri-color combination known as Temur. Temur wants to play really big creatures and often. Temur uses the speed of red and the massive
            creatures from green to get an early presence on the board. Then it can use the blue side to make sure all of it's board stays intact and continues to cast big spells. """
            image = model.magic_dictionary[24]["image"]
    except:
         print()
    try:
        if red and blue and black and green:
            message = """Glint-Eye or Glint is the comniantion of all five colors except white. Glint acts like a five color deck being able to do almost anything realting to the board,
            however it lacks some of the support and life gain without the white aspect."""
            image = model.magic_dictionary[25]["image"]
    except:
         print()
    try:
        if red and white and black and green:
             message = """Dune-Brood or Dune is the comniantion of all five colors except blue. Dune acts like a five color deck being able to do almost anything realting to the board,
             however it lacks some of the control and card draw without the blue aspect ."""
             image = model.magic_dictionary[26]["image"]
    except:
        print()
    try:
        if red and blue and white and green:
            message = """Ink-Treader or Ink is the comniantion of all five colors except black. Ink acts like a five color deck being able to do almost anything realting to the board,
            however it lacks some of the removal and graveyard manipulation without the black aspect."""
            image = model.magic_dictionary[27]["image"]
    except:
        print()
    try:
        if black and blue and white and green:
            message = """Witch-Maw or Witch is the comniantion of all five colors except red. Witch acts like a five color deck being able to do almost anything realting to the board,
            however it lacks some of the speed and direct damage without the red aspect."""
            image = model.magic_dictionary[28]["image"]
    except:
        print()
    try:
        if red and blue and white and black:
            message = """Yore-Tiller or Yore is the comniantion of all five colors except green. Ink acts like a five color deck being able to do almost anything realting to the board,
            however it lacks some of the big ramp and pump spells without the green aspect."""
            image = model.magic_dictionary[29]["image"]
    except:
        print()
    try:
        if white and blue and black and red and green:
            message = """When all five colors are in a single deck it is referred to as either five color, or sometimes it is called Domain. Decks that have all five colors are easily
            the most versitile of all color combination; this is due to the fact that having all five colors present in one deck allows acces to all of the individual colors mechanics.
            However, having all five colors is also the hardest to manage, this is becuase when there are more colors in a deck it becomes less and less likely that a player will be able
            draw the correct cards to play all five colors. """
            image = model.magic_dictionary[30]["image"]
    except:
        print()

    return render_template('results.html',message = message, image = image, message2 = message2)
