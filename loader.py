import os
import sys
import pathlib

year, n = sys.argv[1:]
path = pathlib.Path().resolve().joinpath(f"y{year}/p{n:0>2}.txt")
if not path.exists():
    import requests
    url = f"https://adventofcode.com/{year}/day/{n}/input"
    cookies = {"session": os.environ["SESSION"]}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    path.with_suffix(".txt").write_bytes(response.content)
if not path.with_suffix(".py").exists():
    path.with_suffix(".py").touch()
module, question = path.with_suffix('').parts[-2:]
module = __import__('.'.join([module, question])).__dict__[question]
module.main(path.read_text()[:-1], True)
module.main(path.read_text()[:-1], False)
