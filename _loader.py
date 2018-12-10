import os
import pathlib
import re
import sys

import requests


base, = sys.argv[1:]
path = pathlib.Path(base).with_suffix(".txt")

year, n = map(int, re.findall(r'\d+', base))
url = f"https://adventofcode.com/{year}/day/{n}/input"
response = requests.get(url, cookies={"session": os.environ["SESSION"]})
response.raise_for_status()

path.write_bytes(response.content)
