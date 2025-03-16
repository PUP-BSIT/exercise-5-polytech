#PolyTech Quiz
print(" ------------------------------[POLYTECH QUIZ]-------------------------------\n\n")
print("1. (Kalelle Mae B. Victorio) The Boötes Void is referred to as 'The Great Nothing' because: \n")
choice_a = "\ta.) left over void from the Big Bang where no matter could form"
choice_b = "\tb.) It contains almost no galaxies or stars and is mostly empty space"
choice_c = "\tc.) It is a massive black hole that absorbs all surrounding light and matter"
choice_d = "\td.) It is a region of space where time does not exist"

score = 0

print(choice_a)
print(choice_b)
print(choice_c)
print(choice_d)

answer = input("\nEnter your answer: ").lower()

if answer == "b":
    print("Correct! The Boötes Void is a huge area of space that contains almost no galaxies or stars.")
    print(f"Your score is {score + 1}")
    score += 1
else:
    print("Incorrect! The correct answer  is b.")
    print(f"Your score is {score}")

print("\n\n----------------------------------------------------------------------------\n\n")
print("(Niones, Zyra Joy O.) What is the life maximum life span of cats?\n")
choice_a = "a.) 5-8 years"
choice_b = "b.) 9 years"
choice_c = "c.) 10- 15 years"
choice_d = "d.) 22-30 years "

print(choice_a)
print(choice_b)
print(choice_c)
print(choice_d)

answer = input("Enter your answer:").lower()

if answer == "c":
    print("Correcrt! The life span of cats is 10-15 years.")
    print(f"Your score is {score + 1}") 
    score +=1
else: 
    print("Incorrent! The correct answer is c.")
    print(f"Your score is {score}")

print("\n\n----------------------------------------------------------------------------\n\n")
print("(Niones, Zyra Joy O.) What creature has blue blood due to copper instead of iron?\n")
choice_a = "a.) Lobster"
choice_b = "b.) Octopus"
choice_c = "c.) Horsehoe Crab"
choice_d = "d.) Scorpion "

print(choice_a)
print(choice_b)
print(choice_c)
print(choice_d)

answer = input("Enter your answer:").lower()

if answer == "c":
    print("Correcrt! The Horseshoe Crab has blue blood due to copper instead of iron.")
    print(f"Your score is {score + 1}") 
    score +=1
else:
    print("Incorrect! The answer is c.")
    print("f(your score is {score}")

print("\n\n----------------------------------------------------------------------------\n\n")
print("Add Questions")
print("\n\n----------------------------------------------------------------------------\n\n")
print("Add Questions")
print("\n\n----------------------------------------------------------------------------\n\n")

total_score = score

if total_score >= 3  and total_score <= 5:
    print(f"You have passed the quiz!, your final score is {total_score}.")
else:
    print(f"You have failed the quiz, your final score is {total_score}. Better luck next time!.")

