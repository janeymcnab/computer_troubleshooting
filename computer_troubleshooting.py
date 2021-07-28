# PseudoCode
# START
# PRINT "Turn Computer On"

# INPUT "Did it boot up? "
# IF boot_up == "no"
#   INPUT "Is it plugged in? "
# IF plugged_in == "no"
#   PRINT "Plug it in"
# INPUT "Did this fix the problem? "
#   IF problem_solve == "no"
#       print "The computer is broken."
# ELSE  
#       PRINT "Login with password."
# 
# 
# ELSE 
#       PRINT "Login with password."

# responses = "yes" "no"

print("************************************")
print("* COMPUTER TROUBLESHOOTING PROGRAM *")
print("************************************")

print("Turn Computer On")

boot_up = input("Did it boot up? (yes/no):  ")
if boot_up == "no":
    plugged_in = input("Is it plugged in? (yes/no): ")
    if plugged_in == "no":
        print("Plug it in")
        problem_solve = input("Did this fix the problem? (yes/no): ")
        if problem_solve == "no":
            print("The computer is broken.")
        else: 
            print("Login with password.")
    else:
        print("The computer is broken.")
else:
    print("Login with password.")


#refactoring above code to be more effiecient:

comp_working = False
print("Turn your computer on.")

boot_up = input("Did it boot up? (yes/no) ")
if boot_up == "yes":
    comp_working = True
else:
    plugged_in = input("Is it plugged in? (yes/no) ")
    if plugged_in == "no":
        print("Plug it in")
        solution = input("Did this fix the problem? (yes/no) ")
        if solution == "yes":
            comp_working = True       


if comp_working == True:
    print("Login with password.")
else:
    print("Your computer is broken.")



