https://www.youtube.com/watch?v=UzkuOACmBpA 

https://github.com/LambdaTest/Pylenium-pytest-tutorial 


### Install Python and Poetry
```bash
$ python3 --version 

$ pip3 install poetry
$ sudo apt install python3-poetry 
$ sudo poetry --version
``` 

### Install VSCode with extensions

Python extension -from Microsoft 
Pylance extension - from Microsoft 

Create project directory 
Initialize it with Poetry 

poetry init 
include pylenium, autopep8 and flake8 

install packages 
 - automatically creates Virtual Environment 

 Iside the project folder:
 ```bash
 $ sudo poetry init 
 ```
yes
pyleniumio  
0 

for development packages say yes
autopep8 
flake8   - for linting 

Then, when pyproject.toml file will be generated, install dependencies:
```bash
$ sudo poetry install
```

### Configure VSCode 
- Select interpreter 
- Create tests folder (with __init__.py)
- configure tests 

```bash 
$ sudo poetry env info
```
copy Path link 
open in VSCode View -> Command Pallette 

Type:
Python: select interpreter  

then copy Path and +Enter interpreter path 


in command pallete type: 
Python: Configure tests 
select Pytest 
select directory - tests 



To initialize Pylenium with poetry 
```bash
$ sudo poetry run pylenium init 
```

```bash
$ sudo poetry run python script_filenae.py
```


### Ui tests with Pylenium and Pytest 
lambdatest.github.io/sample-todo-app 

scenarios to cover:
- check first item in the list 
- check many items 
- check all items 
- add a new item
- remove an item  

### Run tests in Parallel
pytest-xdist-plugin 

- running tests in parallel greatly reduces execution of time which is crutial to Ci/CD 

Parralel design - Pitfalls:
- tests should not share data or state 
- tests should not be dependant on each other 

RIGHT WAY:
- each test has it`s own instance of a driver 
- tests are independent of each other 
- tests manage their own data and state 
- tests should be modular 

Pylenium is parallel-first 
- the py fixture gives a river to each test 

To run test in pytest
```bash
$ sudo pytest tests/test_todo.py 
```
To run in parallel with number of threads 2:
```bash
$ sudo pytest tests/test_todo.py -n 2
```

```bash
$ sudo poetry run pytest tests/test_todo.py
``` 


## RUN WITH DOCKER 
https://docs.pylenium.io/guides/run-tests-in-containers 

create docker-compose.yml 

https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md

https://phoenixnap.com/kb/docker-permission-denied 
here do the following to use docker without sudo:
```bash
$ sudo groupadd -f docker
$ sudo usermod -aG docker $USER 
$ newgrp docker 
$ groups
``` 
there should be a docker shown in terminal

run 
```bash
$ docker compose up
```
or
```bash
$ docker compose up -d
```
stop
```bash 
$ docker compose down
```

run in terminal:
```bash
$ pytest tests/test_todo.py -n 2 --remote_url="http://localhost:4444/wd/hub"
``` 

To scale nodes:
```bash
$ docker-compose up -d --scale chrome=5
```
This will spin up the Grid with 5 chrome Nodes!