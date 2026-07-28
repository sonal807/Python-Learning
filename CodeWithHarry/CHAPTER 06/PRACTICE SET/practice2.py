#WAP to find out whether a student has passed or failed if it requires a total of 40% and atleast 33% in each subject to pass.
#assume 3 subjects and take marks as an input from the user

sub1 = float(input("Enter the marks of subject 1:"))
sub2 = float(input("Enter the marks of subject 2:"))
sub3 = float(input("Enter the marks of subject 3:"))

total_percentage = ((sub1 + sub2 + sub3)/300) * 100

print(f"\nTotal Percentage: {total_percentage:.2f}%")

if (total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("Congratulations!\nYou have passed.")
else:
    print("Sorry! You have got failed.\nTry again next time.")