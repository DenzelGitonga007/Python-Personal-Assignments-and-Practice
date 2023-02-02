# Capture cat 1 and 2, and main exams marks,
# compute the total(out of 100) and assign grade
print("... Enter the marks of the student(s) ...")
cat_one = int(input("Enter CAT 1 marks: "))
if cat_one > 15: #CAT 1 marks cannot be more than 15
    cat_one = print(input("CAT 1 marks cannot be more than 15, please enter a valid score: "))
cat_two = int(input("Enter CAT 2 marks: "))
if cat_two > 15: #CAT 2 marks cannot be more than 15
    cat_two = print(input("CAT 2 marks cannot be more than 15, please enter a valid score: "))
main_exam = int(input("Enter the main exam marks: "))
if main_exam > 70:
    main_exam = print(input("Main exam marks cannot be more than 79, please enter a valid score: "))
# Compute the marks
cat_results = cat_one + cat_two
print("The CAT results are: {}".format(cat_results))
#The total result
exam_results = cat_results + main_exam
print("The students scored {} for the whole exam".format(exam_results))
#Assigning grades
if exam_results >= 70:
    print("That's an A, first class honors")
elif exam_results >= 60:
    print("That's a B, second-class upper division")
elif exam_results >= 50:
    print("That's a C, second-class lower division")
elif exam_results >= 40:
    print("That's a D, pass")
else:
    print("That's an E, supplementary")
print("...End of program...")

