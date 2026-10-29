# Name: Whitney Martinez
# Description: Assignment 7 - Student Grade Calculator

def calculate_grade(score):
    """Determine the letter grade based on the numerical score."""

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    print("Student Grade Calculator")
    print("------------------------")

    student_name = input("Enter the student's name: ")
    score = float(input("Enter the student's numerical grade (0-100): "))

    if score < 0 or score > 100:
        print("Invalid grade. Please enter a score between 0 and 100.")
    else:
        letter_grade = calculate_grade(score)

        print("\nGrade Report")
        print("------------------------")
        print(f"Student: {student_name}")
        print(f"Numerical Grade: {score:.1f}")
        print(f"Letter Grade: {letter_grade}")


if __name__ == "__main__":
    main()