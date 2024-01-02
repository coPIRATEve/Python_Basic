import json

def compare_json(json_old, json_new, diff_list):
    result = {}

    for key in json_old:
        if key in diff_list and json_old[key] != json_new[key]:
            result[key] = {
                "old_value": json_old[key],
                "new_value": json_new[key]
            }
            print(f"Difference in {key}: {json_old[key]} -> {json_new[key]}")

    return result

diff_list = ["services", "staff", "datetime"]

with open('json_old.json', 'r') as f_old:
    data_old = json.load(f_old)

with open('json_new.json', 'r') as f_new:
    data_new = json.load(f_new)

result = compare_json(data_old, data_new, diff_list)

print(result)

with open('result.json', 'w') as f_result:
    json.dump(result, f_result, ensure_ascii=False, indent=2)
