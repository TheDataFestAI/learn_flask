# How to clone this repo and work in local/remote machines

Developed By: Indranil Pal <br>
Linkdin Profile:  

## Step 1: Pre-Requisite -
1. Install below softwares -
	1. install python 3
	2. install vscode
	3. install gitbash


## Step 2: Setup the Local directory and Clone the code and install the dependencies 
1. Open gitbash and execute below commands.
	```shell
	cd D:\\pythonProject\\thedatafestai_repo
	git clone https://github.com/TheDataFestAI/learn_flask.git
	cd learn_flask
	code .
	```
2. Python Virtual Environment
	```shell
	pip install virtualenv
	python -m virtualenv .venv

	# windows
	.venv\\Scripts\\activate
	python.exe -m pip install --upgrade pip
	pip install -r .\requirements.txt

	# linux
	# source ./venv/bin/activate
	```


## Step n:
1. Daily commands
	```shell
	cd learn_flask
	Set-ExecutionPolicy Unrestricted -Scope Process
	get-ExecutionPolicy
	.venv\\Scripts\\activate
	```