students = {
    65322: [
        {'Student Info': ["Johan", "George", 21, "Male"]},
        {'Results': [95, 90, 85, 80, 75, 70]}
    ],

    95685: [
        {'Student Info': ["John", "Doe", 20, "Male"]},
        {'Results': [65, 90, 20, 85, 65, 80]}
    ]
}

print(students.keys())


while True:

    option = int(input('''1. View Student INformation
2. Add new Information
3. Exit
Enter your option: '''))

    if option == 1:
        studentID = int(input("Enter the studentID: "))

        print("First Name:", students[studentID][0]['Student Info'][0])
        print("Last Name:", students[studentID][0]['Student Info'][1])
        print("Age:", students[studentID][0]['Student Info'][2])
        print("Gender:", students[studentID][0]['Student Info'][3])

        print()

        print("English:", students[studentID][1]['Results'][0])
        print("Science:", students[studentID][1]['Results'][1])
        print("Maths:", students[studentID][1]['Results'][2])
        print("Social Studies:", students[studentID][1]['Results'][3])
        print("Physics:", students[studentID][1]['Results'][4])
        print("Chemistry:", students[studentID][1]['Results'][5])
    elif option == 2:

        studentID = int(input("Enter the studentID: "))

        f_name = input("Enter the students first name: ")
        l_name = input("Enter the students last name: ")
        new_age = int(input("Enter the student's age: "))
        new_gender = input("Enter the student's gender: ")

        score_english = int(input("Enter the student's english score': "))
        score_science = int(input("Enter the student's science score': "))
        score_maths = int(input("Enter the student's maths score': "))
        score_socialstudies = int(
            input("Enter the student's social studies score': "))
        score_physics = int(input("Enter the student's physics score': "))
        score_chemistry = int(input("Enter the student's chemistry score': "))

        students.update({
            studentID: [
                {'Student Info': [f_name, l_name, new_age, new_gender]},
                {'Results': [score_english, score_science, score_maths,
                             score_socialstudies, score_physics, score_chemistry]}
            ]
        }
        )

    elif option == 3:
        print("Thank you for using the program")
        break

    else:
        print("Invalid Input")

# while studentID != students.keys():
#     studentID = int(input("Invalid Student ID, PLease try again: "))

#     if studentID in students.keys():
#         break
