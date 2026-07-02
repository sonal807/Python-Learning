#you are given alist of subjects for students.
#Assume one classroom is required for 1 subject.
#how many classrooms are needed by all students.
#"python", "java", "C++", "python", "javascript",
#"java", "python", "java", "C++", "C"
subjects = {"python", "java", "C++", "python", "javascript",
            "java", "python", "java", "C++", "C"
 }
print(subjects)
total_classrooms = len(subjects)
print("Total classrooms needed:", total_classrooms)