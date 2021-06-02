# Linked List  Unit Test

A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers

## Test Plan
Find the Test plan [here](https://docs.google.com/spreadsheets/d/1lG5JL3pCyihY7gLyZKe47XCz_79oH6WgKX34gMOFuZY/edit?usp=sharing)

## Requirements
Download and install

[Python3](https://www.python.org/downloads/)  

[Pip](https://pypi.org/project/pip/) 

[virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

## Instructions

clone the Project

```bash
git clone https://github.com/zhbdripon/linked-list-test-demo.git
```

go to project directory 

```bash
cd linked-list-test-demo
```

create virtual environment and activate it

```bash
virtualenv .venv
source .venv/bin/activate
```

run unit-test

```bash
python -m unittest discover -s tests/ -p *_test.py -v
```
