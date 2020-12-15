#! /bin/bash

#Just in case I run this in a different directory
cd ~/projects/udemy/100-days-of-python

# Gets the last touched numeric file in the directory
# (This could be subject to failure if I modify a previous folder)
last=$(ls -t | egrep '[0-9]{2}' | cut -d$'\n' -f1)

next=$(($last+1))

# Create a new branch
git checkout -b $next

# Make the directory for the day, copy yesterday's README into it
mkdir $next
cp $last/README.md $next/

cd $next

# Pad the number by one to reflect counting from 1
pad=$(($next+1))

# Update the README to say the correct day
sed -i "s/$next/$pad/g" README.md

return 
