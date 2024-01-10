# How to clone this repo and work in local/remote machines

Developed By: Indranil Pal <br>
Linkdin Profile:  

## Step 1: Pre-Requisite -
1. Install below softwares -
	1. install python 3
	2. install vscode
	3. install gitbash


## Step 2: Clone the code from repo -
1. Open gitbash and execute below commands:
	```shell
	cd D:\\pythonProject\\thedatafestai_repo
	git clone https://github.com/TheDataFestAI/learn_flask.git
	cd learn_flask
	code .
	```

## Step 3: Create and Activate Python Virtual Environment
1. Open terminal from vscode and execute below commands:
	```shell
	pip install virtualenv
	python -m virtualenv .venv

	# windows
	.venv\\Scripts\\activate
	python.exe -m pip install --upgrade pip

	# linux
	# source ./venv/bin/activate
	```
2. Install the required python packages:
	```shell
	pip install -r .\requirements.txt
	```



## Step n: Follow below commands as per the errors/issues -
1. If you can't execute bash script file from vscode terminal:
	```shell
	Set-ExecutionPolicy Unrestricted -Scope Process
	get-ExecutionPolicy
	```
2. When you have un-authorize access error from github 
	```shell
	git remote -v

	# git remote set-url origin https://<TOKEN>@github.com/<USERNAME>/<REPOSITORYNAME>.git
	git remote set-url origin https://<TOKEN>@github.com/TheDataFestAI/learn_flask.git
	```