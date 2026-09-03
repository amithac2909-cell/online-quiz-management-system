import json
import os

FILE_NAME = "quizzes.txt"


def load_quizzes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    else:
        return {}


def save_quizzes(quizzes):
    with open(FILE_NAME, 'w') as f:
        json.dump(quizzes, f)


def add_quiz(quizzes):
    quiz_name = input("Enter quiz name: ")
    if quiz_name in quizzes:
        print("Quiz already exists!")
    else:
        quizzes[quiz_name] = []
        save_quizzes(quizzes)
        print(f"Quiz '{quiz_name}' created successfully!")


def add_question(quizzes):
    quiz_name = input("Enter quiz name to add questions: ")
    if quiz_name not in quizzes:
        print("Quiz not found!")
        return

    question = input("Enter question: ")
    a = input("Option A: ")
    b = input("Option B: ")
    c = input("Option C: ")
    d = input("Option D: ")
    correct = input("Enter correct option (A/B/C/D): ").upper()

    quizzes[quiz_name].append({
        "question": question,
        "options": {"A": a, "B": b, "C": c, "D": d},
        "answer": correct
    })
    save_quizzes(quizzes)
    print("Question added successfully!")


def view_quizzes(quizzes):
    if not quizzes:
        print("No quizzes available.")
    else:
        print("\nAvailable Quizzes:")
        for name, questions in quizzes.items():
            print(f"- {name} ({len(questions)} questions)")


def take_quiz(quizzes):
    quiz_name = input("Enter quiz name to take: ")
    if quiz_name not in quizzes:
        print("Quiz not found!")
        return

    questions = quizzes[quiz_name]
    if not questions:
        print("No questions in this quiz yet!")
        return

    score = 0
    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['question']}")
        for key, value in q['options'].items():
            print(f"{key}) {value}")
        ans = input("Your answer (A/B/C/D): ").upper()
        if ans == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}")

    print(f"\nYou scored {score}/{len(questions)} points!")


def admin_menu(quizzes):
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. Add Quiz")
        print("2. Add Question")
        print("3. View Quizzes")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            add_quiz(quizzes)
        elif choice == '2':
            add_question(quizzes)
        elif choice == '3':
            view_quizzes(quizzes)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")


def student_menu(quizzes):
    while True:
        print("\n=== STUDENT MENU ===")
        print("1. View Quizzes")
        print("2. Take Quiz")
        print("3. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            view_quizzes(quizzes)
        elif choice == '2':
            take_quiz(quizzes)
        elif choice == '3':
            break
        else:
            print("Invalid choice!")


def main():
    quizzes = load_quizzes()

    while True:
        print("\n=== QUIZ MANAGEMENT SYSTEM ===")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            user = input("Enter admin username: ")
            pwd = input("Enter admin password: ")
            if user == "admin" and pwd == "admin":
                admin_menu(quizzes)
            else:
                print("Invalid admin credentials!")

        elif choice == '2':
            student_menu(quizzes)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
