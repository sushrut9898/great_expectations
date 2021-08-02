import os
import requests
from requests.auth import HTTPBasicAuth
import sys

access_token = "OTU2ODg1NzQ3NzI3OudQj1L7tvmPgGUQ20nsa/nMDMex"


def expectations_check():
    val = sys.argv[1]
    path = os.getcwd()
    path = path + "\\great_expectations\\expectations"
    name = val
    in_file = name.replace('.', '/')
    led_name = in_file.split('/')[0]
    db_name = in_file.split('/')[1]
    table_name = in_file.split('/')[2]
    local_search = name.replace('.', '\\')
    file_path = path + '\\' + local_search + '.json'
    url = 'https://msstash.morningstar.com/projects/DL/repos/dl-data-qc/browse/great_expectations/expectations/' + in_file + '.json' + '?raw'
    response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
    if response.status_code == 200:
        # print(response.text)
        exp_folder = os.path.join(path + '\\' + led_name)
        db_folder = os.path.join(path + '\\' + led_name + '\\' + db_name)
        if not os.path.isdir(exp_folder):
            os.makedirs(exp_folder)
        elif not os.path.isdir(db_folder):
            os.makedirs(exp_folder + '\\' + db_name)
        file_name = '{}.json'.format(table_name)
        with open(path + '\\' + led_name + '\\' + db_name + '\\' + file_name, 'w') as f:
            f.write(response.text)
            print("file created locally:", name)
        with open(file_path, 'r') as f:
            data = f.read()
            # print(data)
    else:
        with open(file_path, 'r') as f:
            data = f.read()
            # print(data)


if __name__ == "__main__":
    expectations_check()