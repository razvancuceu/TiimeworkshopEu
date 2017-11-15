#!/bin/sh

TARGET_DIR='/Users/rhoerbe/temp/var/www/wwwTiimeworkshopEu/html/'

git remote update
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})
BASE=$(git merge-base @ @{u})
if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
elif [ $LOCAL = $BASE ]; then
  git pull
  jekyll build --destination $TARGET_DIR
fi
