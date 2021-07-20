#!/bin/bash 

git remote update

dryrunret='git pull --dry-run'
if ['$dryrunret'=="Already up-to-date."]
    echo "upto date"
else
    echo "need to update"
fi