include .env
export

# always default to running the last problem modified
export last=$(shell ls -lt y*/*.py | head -n 1 | grep -oE 'y..../p..')

main: venv $(last).txt
	venv/bin/python -u _runner.py $(last)

sols:
	venv/bin/python -u _benchmark.py

$(last).txt:
	venv/bin/python -u _loader.py $(last)

venv: requirements.txt
	pypy3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
	touch requirements.txt venv

flake:
	venv/bin/flake8
