# Program on Types of Lists in Grading: Grades and Passing Grades

# Categorization
List_of_Grades = []
Passed_Grades = []

# Processing Input Calculation
for n in range(5):
    Student_Grade_List = int(input("Please input the grade of an individual student: "))
    if Student_Grade_List >= 0 and Student_Grade_List <= 100:
        List_of_Grades.append(Student_Grade_List)
        
        if Student_Grade_List >= 75:
            Passed_Grades.append(Student_Grade_List)
    else:
        print("Invalid Grade Input.")
        break

# Execution of Calculations
Summation_of_Grades = List_of_Grades[0] + List_of_Grades[1] + List_of_Grades[2] + List_of_Grades[3] + List_of_Grades[4]
Average_of_Grades = Summation_of_Grades / 5
Passed_Students = len(Passed_Grades)
Average_of_Passing = Passed_Students / 5
Percentage_Passing_Grades = str(Average_of_Passing * 100)

# Printing of Final Results
print("Inputted Grades: ", List_of_Grades)
print("Average of Grades: ", Average_of_Grades)
print("Passing Percentage: {}%".format(Percentage_Passing_Grades))
print("Passed Students: ", Passed_Students)