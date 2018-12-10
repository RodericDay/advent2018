import json
import pathlib
import sys


base, = sys.argv[1:]
year, question = base.split('/')
path = pathlib.Path(year, question).with_suffix('.txt')

script = __import__(year + '.' + question).__dict__[question]
script.main(path.read_text().rstrip('\n'), True)
script.main(path.read_text().rstrip('\n'), False)

for k, v in json.loads(pathlib.Path('sols.json').read_text()).items():
    if base in k:
        print(v)
