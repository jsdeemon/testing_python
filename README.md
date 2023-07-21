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