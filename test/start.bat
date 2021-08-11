@echo off
if $1=="new" python get_expectaion_json.py $1 && great_expectation suite edit quarantine.business_stg__titanic_stg.tickets_stg
python get_expectaion_json.py $1 && great_expectation suite edit $1