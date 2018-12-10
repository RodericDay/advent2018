import functools
import json
import multiprocessing
import os
import pathlib
import re

import requests


def web(path):
    try:
        year, n = map(int, re.findall(r'\d+', str(path)))
        url = f"https://adventofcode.com/{year}/day/{n}"
        resp = requests.get(url, cookies={"session": os.environ["SESSION"]})
        resp.raise_for_status()
        text = resp.text

        found = re.findall(r'Your puzzle answer was <code>(.+?)</code>', text)
        return {f"y{year}/p{n:0>2}.{p}": ans for p, ans in enumerate(found, 1)}
    except Exception as e:
        print(e)
        return {}


paths = pathlib.Path().rglob("y*/p*.py")
dix = multiprocessing.Pool().map(web, paths)
d = functools.reduce(lambda a, b: {**a, **b}, dix, {})
with open("sols.json", "w") as fp:
    json.dump(d, fp, indent=2)
