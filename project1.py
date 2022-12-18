# File: Project1.py
# Student: Preston Cook
# UT EID: plc886
# Course Name: CS303E
# 
# Date: 12/16/2022
# Description of Program: Basic Grade Calculator

def main():

    user_selection = input("Enter the student's name (or 'stop'): ")
    print()

    while user_selection != 'stop':
        hw_avg = computeHomeworkAvg()
        project_avg = computeProjectAvg()
        exam_avg = computeExamAvg()

        course_avg = computeStudentGradeReport(hw_avg, project_avg, exam_avg)
        printGradeReport(user_selection, hw_avg, project_avg, exam_avg, course_avg)

        user_selection = input("Enter the student's name (or 'stop'): ")
        print()

    print('Thanks for using the grade calculator! Goodbye.')

def computeHomeworkAvg():
    print('HOMEWORKS: ')
    total = 0
    for i in range(1, 4):
        grade = int(input(f'  Enter HW{i} grade: '))
        while grade not in range(0, 11):
            print("  Grade must be in range [0..10]. Try again.")
            grade = int(input(f'  Enter HW{i} grade: '))
        total += grade
    
    print()
    return total * 10 / 3
        

def computeProjectAvg():
    print('PROJECTS: ')
    total = 0
    for i in range(1, 3):
        grade = int(input(f'  Enter Pr{i} grade: '))
        while grade not in range(0, 101):
            print("  Grade must be in range [0..100]. Try again.")
            grade = int(input(f'  Enter Pr{i} grade: '))
        total += grade
    
    print()
    return total / 2

def computeExamAvg():
    print('EXAMS: ')
    total = 0
    for i in range(1, 3):
        grade = int(input(f'  Enter Ex{i} grade: '))
        while grade not in range(0, 101):
            print("  Grade must be in range [0..100]. Try again.")
            grade = int(input(f'  Enter Ex{i} grade: '))
        total += grade
    
    print()
    return total / 2

def avgToLetterGrade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    return 'F'

def computeStudentGradeReport(hw_avg, project_avg, exam_avg):
    return (hw_avg * 0.3) + (project_avg * 0.3) + (exam_avg * 0.4)

def printGradeReport(name, hw_avg, project_avg, exam_avg, course_avg):
    print(f"Grade report for: {name}")
    print(f"  Homework average (30% of grade): {hw_avg:.2f}")
    print(f"  Project average (30% of grade): {project_avg:.2f}")
    print(f"  Exam average (40% of grade): {exam_avg:.2f}")
    print(f"  Student course average: {course_avg:.2f}")
    print(f"  Course grade (CS303E: Fall, 2022): {avgToLetterGrade(course_avg)}")
    print()

if __name__ == '__main__':
    main()