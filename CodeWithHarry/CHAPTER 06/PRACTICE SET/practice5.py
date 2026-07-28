#WAP to calculate the grade of a student from his marks from the following scheme.
#90-100 => A
#80-90 => B
#70-80 => C
#60-70 => D
#50-60 => E
#<50 => F

sub1 = float(input("Enter the marks of subject 1:"))
sub2 = float(input("Enter the marks of subject 2:"))
sub3 = float(input("Enter the marks of subject 3:"))
sub4 = float(input("Enter the marks of subject 4:"))

percentage = ((sub1 + sub2 + sub3 + sub4)/400) * 100

print(f"\nTotal Percentage: {percentage:.2f}%")

if(percentage >= 90 and percentage <= 100 ):
    print("Your Grade is A!\nExcellent performance!\nKeep up the outstanding work.")

elif(percentage >= 80 and percentage <= 90 ):
    print("Your Grade is B!\nVery good!\nGreat job, but there's still room to excel.")

elif(percentage >= 70 and percentage <= 80 ):
    print("Your Grade is C!\nGood effort!\nSolid performance, keep practicing.")

elif(percentage >= 60 and percentage <= 70 ):
    print("Your Grade is D!\nFair.\nYou passed, but you need to focus more on key areas.")

elif(percentage >= 50 and percentage <= 60 ):
    print("Your Grade is E!\nNeeds Improvement.\nYou are close to failing, work harder.")

else:
    print("Your Grade is F!\nFail.\nAdditional support and study required to improve.")