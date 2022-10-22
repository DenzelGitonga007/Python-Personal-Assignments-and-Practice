# Capture cat 1 and 2, and main exams marks,
# compute the total(out of 100) and assign grade
print("... Enter the marks of the student(s) ...")
cat_one = int(input("Enter CAT 1 marks: "))
if cat_one > 15: #CAT 1 marks cannot be more than 15
    cat_one = print(input("CAT 1 marks cannot be more than 30, please enter a valid score: ".format(cat_one)))
cat_two = int(input("Enter CAT 2 marks: "))
if cat_two > 15: #CAT 2 marks cannot be more than 15
    cat_two = print(input("CAT 2 marks cannot be more than 30, please enter a valid score: ".format(cat_one)))
main_exam = int(input("Enter the main exam marks: "))
# Compute the marks
cat_results = cat_one + cat_two
if cat_results > 30:
    cat_results = print("CAT results cannot be more than 30, please enter valid CAT results: ")
print("The CAT results are: {}".format(cat_results))
#The total result
exam_results = cat_results + main_exam
print("The students scored {} for the whole exam".format(exam_results))

