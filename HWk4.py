 HOMEWORK WEEK 4
(handout for students)


TASK 1 (Git and GitHub)

Question 1
Complete definitions for key Git & GitHub terminology
GIT WORKFLOW FUNDAMENTALS
·        Working Directory: This is the directory that holds the current files being worked on. It acts as a temporary repository till the next commit is made. A working directory is a folder created to store all your project files which can contain any type of file. A working directory can function without a Git directory.
·        Staging Area: This allows us to control which changes we commit to our repository. This makes it easier to keep the commit small per logical change.
WORKING DIRECTORY STATES:
·        Staged: This is when a modified file has been marked in its current version to be saved to the database in the next commit statement.
·        Modified: When changes are made to a working file, but these changes are not yet committed to the database
·        Committed: changes made to a working file, is saved and stored to the database
GIT COMMANDS:
·        Git add: This is the command to add files to the staging area. (When the ‘git add’ command is run on a file, it will add the changes to that file to the staging area. If the file was previously untracked, then it will be staged to start tracking that file.)
·        Git commit: (After some changes have been added to the staging area, you can change your staging area to a commit with the ‘git commit’ command. Running ‘git commit’ will no arguments will commit the contents of the staging area in a new commit. When ‘git commit’ is run, it will take you to an editor to create a commit message. The editor will be loaded with the output from ‘git status’, which will provide a summary of what is being committed.)
·        Git push: This pushes changes made on the local repo to the master repo, thus making the most recent commits available on the remote server, and also updates ethe remote-tracking branches.


balance = 100

userInput = None
print('Welcome to your Piggy Bank!')
pin = 1234
balance = 100
log_in = int (input ('Enter your 4 digit pin '))
try:
    if log_in == pin:
        print ('PIN Accepted')
except ValueError:
            print('Invalid pin')
