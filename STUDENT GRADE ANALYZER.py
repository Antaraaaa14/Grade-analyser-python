# Student Grade Analyzer

print("===== STUDENT GRADE ANALYZER =====")

# Number of subjects
n = int(input("Enter number of subjects: "))

subjects = []
marks = []

# Taking input
for i in range(n):
    subject = input(f"Enter subject {i+1} name: ")
    mark = float(input(f"Enter marks for {subject}: "))
    
    subjects.append(subject)
    marks.append(mark)

# Calculations
total = sum(marks)
percentage = total / n

# Grade Calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Highest & Lowest scoring subjects
max_mark = max(marks)
min_mark = min(marks)

highest_subject = subjects[marks.index(max_mark)]
lowest_subject = subjects[marks.index(min_mark)]

# Output
print("\n===== RESULT SUMMARY =====")
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Highest Scoring Subject:", highest_subject, "-", max_mark)
print("Lowest Scoring Subject:", lowest_subject, "-", min_mark)

if grade == "Fail":
    print("Status: ❌ FAIL")
else:
    print("Status: ✅ PASS")

print("===================================")