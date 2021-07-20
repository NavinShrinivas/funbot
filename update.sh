#!/bin/bash 

git remote update > /dev/null

if [ "$(git rev-parse HEAD)" = "$(git rev-parse @{u})" ];
then
    return "0"//no need of update
else
    return "1"
fi