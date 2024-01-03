import json

with open('json_old.json') as json_file1:
    json1_dict = json.load(json_file1)

with open('json_new.json') as json_file2:
    json2_dict = json.load(json_file2)

diff_list = ["services", "staff", "datetime"]

result = {}
for key in diff_list:
    if json1_dict['data'][key] != json2_dict['data'][key]:
        result[key] = {
            'old_value': json1_dict['data'][key],
            'new_value': json2_dict['data'][key]
        }

print(result)

with open('result.json', 'w') as outfile:
    json.dump(result, outfile)