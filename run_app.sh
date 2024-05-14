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
source .env

if [[ "$DEBUG_ENABLED" == "true" ]]; then
    APP_CMD="dev"
else
    APP_CMP="run" 
fi

LOG_FILE="${DIR}/logs/fastapi_$(date +"%d.%m.%Y").log"

fastapi $APP_CMD src/app.py