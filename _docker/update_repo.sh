#!/usr/bin/env bash


SCRIPTDIR=$(cd $(dirname $BASH_SOURCE[0]) && pwd)
PROJ_HOME=$(cd $(dirname $SCRIPTDIR) && pwd)
cd $PROJ_HOME

git pull
./_docker/dscripts/run.sh -i
cp /dv/30eventfetcher/output/registration.md $PROJ_HOME/
git add ./registration.md
git commit -m generated
git push