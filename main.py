#PolyTech Quiz
score = 0

print("\n------------------------------[POLYTECH QUIZ]-------------------------------\n\n")
print("1. (Kalelle Mae B. Victorio): The Boötes Void is referred to as 'The Great Nothing' because: \n")
choice_a = "\ta.) left over void from the Big Bang where no matter could form"
choice_b = "\tb.) It contains almost no galaxies or stars and is mostly empty space"
choice_c = "\tc.) It is a massive black hole that absorbs all surrounding light and matter"
choice_d = "\td.) It is a region of space where time does not exist"



print(choice_a)
print(choice_b)
print(choice_c)
print(choice_d)

answer = input("\nEnter your answer: ").lower()

if answer == "b":
    print("Correct! The Boötes Void is a huge area of space that contains almost no galaxies or stars.")
    score += 1
else:
    print("Incorrect! The correct answer  is b.")
    

print("\n\n----------------------------------------------------------------------------\n\n")
print("2. (Kalelle Mae B. Victorio): Which of the following best describes the Nazi concept of 'Lebensraum'?\n")
choice_a = "\ta.) A military stategy for defending German borders"
choice_b = "\tb.) To restrict the rights of jewish people"
choice_c = "\tc.) The idea that Germany needed to expand its territory"
choice_d = "\td.) A propaganda strategy to manipulate public opinion"

print(choice_a)
print(choice_b)
print(choice_c)
print(choice_d)

answer = input("\nEnter your answer:").lower()

if answer == "c":
    print("Correct! 'Lebensraum' refers to the idea that Germany needed to expand its territory.")
    score += 1
else:
    print("Incorrect! The correct answer is c.")
   
print("\n\n----------------------------------------------------------------------------\n\n")
print("3. (Zyra Joy O. Niones): What is the life maximum life span of cats?\n")
choice_a = "\ta.) 5-8 years"
choice_b = "\tb.) 9 years"
choice_c = "\tc.) 10- 15 years"
choice_d = "\td.) 22-30 years "

print(choice_a)
print(choice_b)
print(choice_c)
print(choice_d)

answer = input("\nEnter your answer:").lower()

if answer == "c":
    print("Correct! The life span of cats is 10-15 years.")
    score += 1
else:
    print("Incorrect! The correct answer is c.")
   

print("\n\n----------------------------------------------------------------------------\n\n")
print("4. (Zyra Joy O. Niones): What creature has blue blood due to copper instead of iron?\n")
choice_a = "\ta.) Lobster"
choice_b = "\tb.) Octopus"
choice_c = "\tc.) Horsehoe Crab"
choice_d = "\td.) Scorpion "

print(choice_a)
print(choice_b)
print(choice_c)
print(choice_d)

answer = input("\nEnter your answer:").lower()

if answer == "c":
    print("Correct! The Horseshoe Crab has blue blood due to copper instead of iron.")
    score += 1
else:
    print("Incorrect! The answer is c.")
    

print("\n\n----------------------------------------------------------------------------\n\n")
print("5. (Annie Rose S. Raquem): Which social media platform introduced the 'Stories' feature first?\n")
choice_a = "\ta.) Snapchat"
choice_b = "\tb.) Instagram"
choice_c = "\tc.) Facebook"
choice_d = "\td.) TikTok"

print(choice_a)
print(choice_b)
print(choice_c)
print(choice_d)

answer = input("\nEnter your answer:").lower()

if answer == "a":
    print("Correct! Snapchat was the first platform to introduce 'Stories' in 2013, which was later adopted by others.")
    score += 1
else:
    print("Incorrect! The correct answer is a.")
    

print("\n\n----------------------------------------------------------------------------\n\n")
print("6. (Annie Rose S. Raquem): Which social media platform is known for the 'Like' button with a thumbs-up icon?\n")
choice_a = "\ta.) Twitter"
choice_b = "\tb.) Instagram"
choice_c = "\tc.) Facebook"
choice_d = "\td.) TikTok"

print(choice_a)
print(choice_b)
print(choice_c)
print(choice_d)

answer = input("\nEnter your answer:").lower()

if answer == "c":
    print("Correct! Facebook introduced the 'Like' button in 2009, represented by a thumbs-up icon.")
    score +=1
else:
    print("Incorrect! The correct answer is c.")
   

print("\n\n----------------------------------------------------------------------------\n\n")
print("Add Questions")
print("\n\n----------------------------------------------------------------------------\n\n")
print("Add Questions")
print("\n\n----------------------------------------------------------------------------\n\n")

total_score = score

if total_score >= 5 and total_score <= 10:
    print(f"\nYou have passed the quiz!, your final score is {total_score}.\n")
else:
    print(f"\nYou have failed the quiz, your final score is {total_score}. Better luck next time!.\n")

