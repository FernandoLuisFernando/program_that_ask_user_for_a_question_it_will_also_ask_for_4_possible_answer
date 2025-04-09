with open("questions.txt", "w") as file:
    for questions in range (1, 4):
        print(f"\n--- Question {questions} ---")
queston = input("Enter option a: ")
queston = input("Enter option b: ")
queston = input("Enter option c: ")
queston = input("Enter option d: ")

correct_answer = ""
while correct_answer not in ["a", "b", "c", "d"]:
    correct_answer = input ("Enter the correct answer (a/b/c/d): ").lower()
    if correct_answer not in ["a", "b", "c", "d"]:
        print("Please enter a valid choice (a, b ,c , or d).")