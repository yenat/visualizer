#!/bin/bash

LOCAL_REPO="/home/bitseat/visualizer"
USERNAME="yenatshif@gmail.com"
PASSWORD="103671cbfb177cfeef70d220a62a915cb375d80a"
REMOTE_REPO="github.com/yenat/visualizer.git"
EMAIL="yenatshif@gmail.com"

cd $LOCAL_REPO


add_commit_push()
{
    echo "-------ADD COMMENTS-------" 
    git add cia_new_tensor.tsv cia_new_metadata.tsv 
    echo "-------COMMIT COMMENTS-------" 
    git commit -m "Auto-commit"
    echo "-------PUSH COMMENTS-------" 

    sudo git push -u https://yenat:103671cbfb177cfeef70d220a62a915cb375d80a@$REMOTE_REPO master 



    if [[ $? != 0 ]]; then

        echo "push failed"
        exit 1
    fi
    echo "success!"
}

add_commit_push

