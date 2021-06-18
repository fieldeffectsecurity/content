import json
import io
import sys

def util_load_json(path):
    with io.open(path, mode='r', encoding='utf-8') as f:
        return json.loads(f.read())

if __name__ == '__main__':
    f_name = sys.argv[1]

    sample = util_load_json(f_name)

    s = f''
    for key in sample[0].keys():
        s += f'''assert '{key}' in r[0]\n'''

    print(s)
