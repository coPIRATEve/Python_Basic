import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

data_old = load_json('json_old.json')
data_new = load_json('json_new.json')

diff_list = ["services", "staff", "datetime"]
result = {}

for key in diff_list:
    if key in data_old and key in data_new and data_old[key] != data_new[key]:
        result[key] = data_new[key]

print(result)

with open('result.json', 'w', encoding='utf-8') as result_file:
    json.dump(result, result_file, ensure_ascii=False, indent=2)
