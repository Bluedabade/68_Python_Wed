score = int(input('Enter a test score:'))
while (score < 0 or score > 100):
    print("Invalid score. Please input a score between 0 and 100.")
    score = int(input('Enter a test score:'))
print(f"Your score is:{score:.2f}")