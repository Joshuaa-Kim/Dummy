print("This edit was made in main branch")

print("These edits are made from newedits, check it out bro!")
print("Praise the Lord Almighty regardless of situation, even when things get tough walk with Him and he will make your paths straight")


#i wrote this in newedits lol

# couple of things to note: 
# The edits made in the main branch carry over to the edits in the branches below it
# make sure to create a new branch underneath the main one by first creating a branch called main and then using git branch [branch name]
# always make sure to git add and commit with -m "" because for some reason you always need a message along with the commit
# Recall that commits are always checkpoints and saves made to your changes
# lastly, in order to merge the changes made in a branch into them main branch, first checkout main and then merge the branch you made the 
#edits in. If there are ever conflicts, you will be given the option to pick what you want to keep and what you want to leave out. 

# one more thing to note is that since you merged newedits into main, newedits have none of the changes that main has. It doesn't even have 
#the file you created when you were in the main branch. In order to essentially make the two branches identical, checkout newedits and then
#merge main

# Today is a new day where I have a Dummy respository in github, now it is time to see if I can send it up there

# More changes lol

# By using git config user.email, it still thinks this file is attached to jkim2224@usc.edu even though I changed the global. Strange
# But to have separate emails for each repository do: git config user.email "joshuakimtwin2004@gmail.com"
# To confirm global address: git config --global user.email 
# But this is still not working, so do git remote set-url origin git://someserver/chirag/myproject.git to change the origin 
# repository git is pulling from

# When branches have diverged, use: git rebase origin/main
# Here are some more edits:

# BRO IT WORKED: how to fix: you need to proper remote set-url origin (to set up the path), proper email, username (my best guess is for linearity and sycning), 
# and incase there are divergent branches rebase them. But before to pull contents of the remote repository and then push it up

# The dummy directory in this file is the clone of the remote repository 