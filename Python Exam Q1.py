def grade_input_program():
    grades = []
    print("Enter grades between 0-100")
    print("Enter minimum 10 valid grades")
    print("Enter -999 to finish")

    while True:
        user_input = input("Enter grade:")
        try:
            grade = float(user_input)
        except ValueError:
            print("Invalid input")
            continue

        if grade == -999:
            if len(grades) < 10:
                print(f"Please enter 10 grades. (Currently have: {len(grades)})")
                continue
            else:
                break

        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Grade must be between 0 and 100")

    if grades:
        class_average = sum(grades) / len(grades)
        max_grade = max(grades)
        valid_count = len(grades)

        print(f"Number of Valid Grades: {valid_count}")
        print(f"Class Average: {class_average:.2f}")
        print(f"Highest Grade: {max_grade}")


grade_input_program()