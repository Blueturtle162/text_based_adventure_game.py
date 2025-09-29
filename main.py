#AK,EB,YS,JS 6th Text based adventure game

#Eva Briggs background story, begining and ending.
print("This story begins in a small village in Hyrule where a young boy plays unaware of the evil that would soon arise. This boy is named Link, little does he know he is a descendant of the legendary hero who in the past had protected Hyrule from the evils of Ganandorf and defeated him, but it was prophesied that one day Ganadorf would come back and a hero would rise and defeat him.")
print("Years later the prophecy became true and the evil Lord Ganondorf returned and stole Princess Zelda, now someone must rise to save her, perhaps the descendant of the hero? Link does his chores on the farm not knowing what has just occurred, a messenger comes and tells the town to flee, links father tells him that he is descendant of the great hero and gives him the choice to flee with them or take his grandfather's sword and save the princess.")
print("What will you do?")


choice = input("Will you take the sword? or will you flee")
while True:
    if choice == ("Yes"):
         print("You grab the sword and continue your journey ")  
         break
    elif choice ("No"):
        ("You flee with the town and Lord Ganandorf takes over Hyrule")
        break
    else:
        print("You need to tell your father Yes or No!")\

#Juliette Santacruz, forest part of storyline     
print("You arrive in The Lost Woods, the first part of the triforce buried deep in the woods. To obtain this piece, you will need to light torches to find you way and find a key to enter throough the gates.")
print("First, you need to find the torch to light your way.")
looking = input("Where will you look, in the bushes, or  inside the great oak tree?:\n").strip().lower()
while True:
    if looking == ("bushes"):
        print("You look in the bushes only to find a couple of berries, which you put in your bag, you then head over to look in the great oak tree finding the torch!")
        break
    elif looking == ("great oak tree"):
        print("you search inside the Great Oak Tree, finding the torch! congrats. Your next mission is to find the gates leading to the triforce")
        break
    else:
        print("Sorry that is not an option, Please type either, 'great oak tree' or 'bushes'")

print("You have collected both berries, (Yu)r ")

print("You have the torch to light your path, you need to find the Gates of Secrets leading to the triforce.")
print("You light your torch, and see the fire flickering left but you also see a trail of rocks leading foward.")
choice = input("Will you follow the rocks and go foward, or will you follow the torch and go left? (Type foward or type left)")
if choice == ("left"):
    print("You  go left, following the torch... after 1 hour of long walking, you end up the gates but it is gaurded by an evil elf!")

#Annalise Kinsey, 2nd part lake region.
def invalid_input():
    print("I'm sorry that is not a valid input try again.")
def user_input(choice):
    return choice.stirp().lower
print ("You arrive at lake Hylia. The second piece of the triforce visble at the bottom of the lake. To obtain it you will need to dive down to the bottom of the lake and find the key to the ornate chest it is hidden in.")
print ("The lake is hundreds of feet deep and you will need scuba gear to reach the bottom. You glance around and notice a dark cave but you slaos can see a waterfall that leads up to a higher plateu over looking the lake")
cave_choice = user_input(input(print("Will you go inside the cave or climb the waterfall? Type left for the cave and right for the waterfall")))
if cave_choice == ("right"):
    print ("You make your way toward the sheer rock face with water cascading down. You slowly begin to make you way up the slick black rocks. Several hours later you finally arrive at the top of the waterfall")
elif cave_choice == ("left"):
    print("You plunge into the dark cave and through the light coming from the opening you can see that the cave drops off into a cliff. You back  out of the cave and make you way towards the waterfall instead. You make your way up to the top of the waterfall and at the top")
else:
    invalid_input
print ("you can see a river streaching for miles srrounded by a medow filled with wild flowers. As you glance around you see a sign that saying that there is a town a little less than a mile away. You still need to find the key to the tresure so you begin to look around.") 
print ("After hours of looking you finally stumble upon a door that leads down into the earth. You open the door and decend into the darkness beyond. After stumbling down some stairs in the darkness you come upon a room with a lit torch. You aproch a wall and notice a riddle writen upon it.")
print ("The riddle reads: I am tall when I am yound and I am short when I am old what am I?")
riddle_answer = user_input(input(print("What does the riddle mean?")))

while True:
    if riddle_answer == ("candle") or ("a candle"):
        print("Congradulations you solved the riddle.")
        break
    else:
        print("You enter your answer to the riddle and nothing happens. You should try again.")

print ("The wall the riddle was written on begins to shake and move to the left. It reveals a room with a chest in the center. You open the chest and discover an small sliver key. You pocket the key and then exit the room. You make your way back up the stairs and exit into the medow")
print ("You still need to find scuba gear to get to the bottom of the lake. You rember seeing a sign about a town nearby and you amek your way down a dirt path that appears to lead to the nearest town. After walking for 20 minutes you stumble upon a small town with quiant little shops all lining a bussling town sqaure.")
print ("You examine all the shops and notice that one procliams that it sells the best quality suba gear. You make your way over to the shop and the owner greets you with a smile. On the course of your journey you have not eraned enough money to bu the scuba gear bu the owner of the shop informs you that if you can solve her riddle she will give you the gear for free.")
print ("The shop keeper gives you a piece of paper. The paper reads I have a bed but never sleep I have a mouth but never speak what am I?")
river_answer = user_input(input(print("What is the answer to the riddle")))
while True:
    if river_answer == ("river") or ("a river"):
        print("The shop keeper smilies and gives you the scuba gear.")
        break
    else:
        print ("The shop keeper shakes her head and tells you to try again.")

print ("You leave the town behind am make your way back to the top of the waterfall. You climb back down the rocks and make your way to Hylia lake. You put on you scuba gear and dive down to the bottom of the lake. You pull out the silver key and use it to unlock the chest located at the bottom of the lake.")
print ("A glow spills out of the chest and you can see a small golden triangle. You grab the triangle and obtain the second part of the triforce. You surface from the bottom of the lake. You take off all of you scuba gear and start on a path that should take you to the base of death mountain.")

#Yaretzi Sanchez, the volcano, part 3 

print("Congrats you have made it to the base of Death mountain!")
print("you have already have gotten the first two pieces of the triforce. Now you will need the last piece.")
print(" However you will need armor in order to make it up death mountain, where the last piece of the triforce is guared by a Hinox. Plus you will need water and food for the trip there.")
print("you see a small light coming from inside a little hut looking house on your right, and to your left you see a very faint path")
choice_DM = input(print("would you like to go to the right, small hut or left down the path?\n ")).strip().lower()
if choice_DM==("left"):
    print("you go down the faint path. it had lots of pretty colorful flowers and in one of the rose bushes you see something. You find a bottle with a  key and a small old map leading to somewhere inside.")
else:
    print("you make your way to the small hut. you find a chest full of food, and bott" )

print("after you walk down the path and collect the key and map you make your way following the map you fnd a hi")    

   
#Eva Briggs ending

print("Now that you have acquired all 3 pieces of the Triforce you can go to Hyrule Castle, defeat Ganondorf, and save Princess Zelda.)"??????""

print("It takes you the next few days to get the castle but you made it and Ganondorf is there waiting for you.”)
 
print("You walk into the castle and Ganondorf is there sitting on the king's throne. Ganondorf approaches and says: Finally the hero has come to try and defeat me, I have waited for you, and now I will destroy you.”) 
