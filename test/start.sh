#!/bin/sh

name="$1"

if [[ $1 == "new" ]]
then
  python get_expectaion_json.py quarantine.business_stg__titanic_stg.tickets_stg
  great_expectations suite edit  quarantine.business_stg__titanic_stg.tickets_stg
else
  echo "using second method"
  python get_expectaion_json.py $1
  great_expectations suite edit  $1
fi
