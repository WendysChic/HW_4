#  HOMEWORK WEEK 4
# (handout for students)
#
#
# TASK 1 (Git and GitHub)

# Question 1
# Complete definitions for key Git & GitHub terminology
# GIT WORKFLOW FUNDAMENTALS
# Working Directory: This is the directory that holds the current files being worked on. It acts as a temporary repository till the next commit is made. A working directory is a folder created to store all your project files which can contain any type of file. A working directory can function without a Git directory.
# Staging Area: This allows us to control which changes we commit to our repository. This makes it easier to keep the commit small per logical change.
# Local Repo (head):  These are git repositories residing on the local PC of the user. It has a working directory. The actual work on whichever active project is done on the local repo pending when the changes are committed to the remote repo.
# Remote repo (master): This resides in a shared server accessible to a group of users via the internet or a local area network. It does not have a working directory. They are used mainly as a resource to share and exchange code between developers
# WORKING DIRECTORY STATES:
# Staged: This is when a modified file has been marked in its current version to be saved to the database in the next commit statement.
# Modified: When changes are made to a working file, but these changes are not yet committed to the database
# Committed: changes made to a working file, is saved and stored to the database
# GIT COMMANDS:
# Git add: This is the command to add files to the staging area. (When the ‘git add’ command is run on a file, it will add the changes to that file to the staging area. If the file was previously untracked, then it will be staged to start tracking that file.)
# Git commit: (After some changes have been added to the staging area, you can change your staging area to a commit with the ‘git commit’ command. Running ‘git commit’ will no arguments will commit the contents of the staging area in a new commit. When ‘git commit’ is run, it will take you to an editor to create a commit message. The editor will be loaded with the output from ‘git status’, which will provide a summary of what is being committed.)
# Git push: This pushes changes made on the local repo to the master repo, thus making the most recent commits available on the remote server, and also updates ethe remote-tracking branches.
# Git fetch: This retrieves commits, files and refs from a remote repository onto a local repo. It does not do any files transfers, more like checking to see if there are any changes available on the remote repo
# Git merge: It combines sequences of commits into one unified history of commit. Two methods are the fast forward and three-way. Commits can be auto merged unless there are conflicting changes in both commit sequences.
# Git pull: Used to fetch and download content from a remote repo onto your local repo and updates the content on the local repo to match the file downloaded


# ATM Program
def check_pin(atm_pin):
    if atm_pin == '2021':
        return True
    else:
        return False


def login():
    check = 0
    while check < 3:
        pin = input('Kindly enter your pin: ')
        if check_pin(pin):
            print('Print correct')
            return True
        else:
            print('Invalid pin')
            check += 1
    print('Account have been blocked')
    return False


def menu():
    balance = 100
    print("****************************")
    print("*****SELECT AN OPTION*******")
    print("****************************")
    print(" \n1 - View Balance\n 2 - Withdraw\n 3 - Exit Program")
    choice = int(input("\nEnter your selection: "))

    # This is to view account balance
    if choice == 1:
        print("Account Balance: $" + str(balance))

    elif choice == 2:
        amount = float(input("\nEnter amount to withdraw: "))

        if amount < balance:
            balance -= amount
            print("\nTransaction was successful. Updated Balance: $" + str(balance) + "")
        else:
            print("\nInsufficient amount. The transaction was terminated")

    elif choice == 3:
        print("Transaction is now complete.")
        print("Thank you for banking with us")
        exit()
    else:
        print("nInvalid code selected. Operation terminated")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to your Piggy Bank!")
    if login():
        # you will need to make this one yourself!
        menu()
    print("Exiting Program")