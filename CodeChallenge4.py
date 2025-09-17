print("Welcome to the Anime/Manga/Manhwa/Manhua Recommendator!")
genre = input("What genre would you like to read/watch? (action / horror / romance): ")

if genre == "action":
    print("You've selected action.")
    length = input("How long do you want it? (short, medium, long): ")
    if length == "short":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of action titles before the 2000s")
            print("Ninja Scroll\nAkira\nCrying Freeman\nFist of the North Star: Movie\nDevilman OVA")
        else:
            print("Here's the list of action titles after the 2000s")
            print("Fullmetal Alchemist: Brotherhood\nKill la Kill\nSamurai Champloo\nClaymore\nNoragami")

    elif length == "medium":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of action titles before the 2000s")
            print("Slayers\nRecord of Lodoss War\nMagic Knight Rayearth\nBlue Seed\nTrigun")
        else:
            print("Here's the list of action titles after the 2000s")
            print("Bleach\nFate/Stay Night\nSword Art Online\nNoragami Aragoto\nKabaneri of the Iron Fortress")

    elif length == "long":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of action titles before the 2000s")
            print("Dragon Ball\nYu Yu Hakusho\nSlam Dunk\nCity Hunter\nRanma ½")
        else:
            print("Here's the list of action titles after the 2000s")
            print("Naruto Shippuden\nOne Piece\nFairy Tail\nMy Hero Academia\nBleach: Thousand-Year Blood War")
    else:
        print("That is not a valid length.")

elif genre == "romance":
    print("You've selected romance.")
    length = input("How long do you want it? (short, medium, long): ")
    if length == "short":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of romance titles before the 2000s")
            print("Kare Kano\nHis and Her Circumstances\nMaison Ikkoku\nBoys Be...\nMarmalade Boy")
        else:
            print("Here's the list of romance titles after the 2000s")
            print("Toradora!\nClannad\nYour Lie in April\nLovely★Complex\nGolden Time")

    elif length == "medium":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of romance titles before the 2000s")
            print("Kimagure Orange Road\nVideo Girl Ai\nDNA²\nFushigi Yuugi\nSailor Moon R")
        else:
            print("Here's the list of romance titles after the 2000s")
            print("Nana\nSkip Beat!\nHoney and Clover\nKimi ni Todoke\nAo Haru Ride")

    elif length == "long":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of romance titles before the 2000s")
            print("Boys Over Flowers\nTouch\nItazura na Kiss\nGlass Mask\nHana yori Dango")
        else:
            print("Here's the list of romance titles after the 2000s")
            print("Fruits Basket (2019)\nKaichou wa Maid-sama!\nAkagami no Shirayuki-hime\nMy Little Monster\nSnow White with the Red Hair")
    else:
        print("That is not a valid length.")

elif genre == "horror":
    print("You've selected horror.")
    length = input("How long do you want it? (short, medium, long): ")
    if length == "short":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of horror titles before the 2000s")
            print("Vampire Hunter D\nDevilman: The Birth\nMermaid Forest\nWicked City\nPerfect Blue")
        else:
            print("Here's the list of horror titles after the 2000s")
            print("Corpse Party\nShiki\nHellsing Ultimate\nAnother\nElfen Lied")

    elif length == "medium":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of horror titles before the 2000s")
            print("Demon City Shinjuku\n3x3 Eyes\nPet Shop of Horrors\nDarkside Blues\nBio Hunter")
        else:
            print("Here's the list of horror titles after the 2000s")
            print("Paranoia Agent\nBlood+ \nAjin: Demi-Human\nThe Future Diary (Mirai Nikki)\nErased")
        
    elif length == "long":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of horror titles before the 2000s")
            print("Devilman Lady\nGuyver: Bio-Boosted Armor\nVampire Princess Miyu\nBoogiepop Phantom\nDemon Lord Dante")
        else:
            print("Here's the list of horror titles after the 2000s")
            print("Tokyo Ghoul\nAttack on Titan\nD.Gray-man\nThe Promised Neverland\nJujutsu Kaisen")
    else:
        print("That is not a valid length.")

else:
    print("Invalid genre.")
