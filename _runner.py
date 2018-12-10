import json
import pathlib
import sys


base, = sys.argv[1:]
year, question = base.split('/')
path = pathlib.Path(year, question).with_suffix('.txt')

script = __import__(year + '.' + question).__dict__[question]
script.main(path.read_text()[:-1], True)
script.main(path.read_text()[:-1], False)

for k, v in json.loads(pathlib.Path('sols.json').read_text()).items():
    if base in k:
        print(v)
