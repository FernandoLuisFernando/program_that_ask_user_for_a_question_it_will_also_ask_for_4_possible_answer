with open("questions.txt", "w") as file:
    for quests in range (1, 4):
        print(f"\n--- Question {quests} ---")
        question = input("Enter the question: ")

        option_a = input("Enter option a: ")
        option_b = input("Enter option b: ")
        option_c = input("Enter option c: ")
        option_d = input("Enter option d: ")

        correct_answer = ""
        while correct_answer not in ["a", "b", "c", "d"]:
            correct_answer = input ("Enter the correct answer (a/b/c/d): ").lower()
            if correct_answer not in ["a", "b", "c", "d"]:
                print("Please enter a valid choice (a, b ,c , or d).")

        file.write(f"Question {quests}: {question}\n")
        file.write(f"a) {option_a}\n")
        file.write(f"b) {option_b}\n")
        file.write(f"c) {option_c}\n")
        file.write(f"d) {option_d}\n")
        file.write(f"Correct Answer: {correct_answer}\n")
        file.write("---\n")

print("\nAll questions have been saved to 'questions.txt'.")

