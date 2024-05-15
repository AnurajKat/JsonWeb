#!/bin/bash

SOURCE=${BASH_SOURCE[0]}
while [ -h "$SOURCE" ]; do
  DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
  SOURCE=$(readlink "$SOURCE")
  [[ $SOURCE != /* ]] && SOURCE=$DIR/$SOURCE
done
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
# source ${DIR}/.env
set -x
cd $DIR
source ${DIR}/.env

if [[ "$DEBUG_ENABLED" == "true" ]]; then
    echo "Debug mode is enabled."
    APP_CMD="dev"
else
    APP_CMD="run" 
fi
echo $DEBUG_ENABLED
echo $JSON_APP_OWNER
echo $APP_BASE_URL
echo $APP_DATA_LOCATION
echo $APP_DATA_SRC

nohup fastapi $APP_CMD src/app.py 