# Grace Meredith
# CS333 Final Project
# 2 May 2023

### This project was my hw1 assignment in Fall 2022 Design Patterns re-written in python.

## Technology Used: 

- 1. Git/Github for Source Control
- 2. Github Actions for Automated Jobs
- 3. Python Unittest Library for Unit/Integration Tests
- 4. Coverage.py for Coverage Report
- 5. Amazon EC2 for Deployment.

## Pipeline: 

- 1. Publish New Feature Branch -> 
- 2. Commit Changes -> 
- 3. Create Pull Request -> 
- 4. Build & Test jobs run w/ Github Actions (build.yml) -> 
- 5. Merge Pull Request into Main Branch once all Tests Pass -> 
- 6. Deployment job runs w/ Github Action (deploy.yml) -> 
- 7. Changes are deployed to Amazon EC2 instance

## Coverage Report






![img](/screenshot.png)
## To view more recent coverage report

- 1. go to Actions ->
- 2. latest job that ran "test-coverage-report" on feature branch -> 
- 3. Display Coverage Report
