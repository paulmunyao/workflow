CircleCI setup in a Django Web Application
This is a CircleCI tutorial on how to set up a workflow in a django web application

Getting started
Create a circleci folder inside the project directory.Afterwards create a yaml file.The yaml file is usually inside the circleci folder.Inside the yaml file is where you write your orbs or automation.An example of a script test would be writing test to perform unit testing i your code or automatic deployment

```
- run:
          name: install dependencies
          command: pip install -r requirements.txt
```
This is an example of a workflow of how one can install dependencies using circleci