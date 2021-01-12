#!/bin/bash

LOCAL_REPO="/home/bitseat/visualizer/"
USERNAME="yenat"
PASSWORD="103671cbfb177cfeef70d220a62a915cb375d80a"
REMOTE_REPO="github.com/yenat/visualizer.git"
EMAIL="yenatshif@gmail.com"

cd $LOCAL_REPO


echo "-------ADD COMMENTS-------" 
git add *
echo "-------COMMIT COMMENTS-------" 
git commit -m "Auto-commit"
echo "-------PUSH COMMENTS-------" 

git push -u https://yenat:103671cbfb177cfeef70d220a62a915cb375d80a@$REMOTE_REPO master 

