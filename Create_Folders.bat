@echo off

:: FastAPI Project Folders Creation Script

:: Main Project Folder
mkdir fastapi_project

:: Navigating to fastapi_project directory
cd fastapi_project

:: Creating app folder and subfolders
mkdir app
cd app
mkdir core
mkdir api
mkdir models
mkdir schemas
mkdir services
cd ..

:: Creating subfolders inside api folder for versioning
cd app\api
mkdir v1
mkdir v2
cd ..

:: Creating tests folder
mkdir tests

:: Other files
echo .env file will be created manually.
echo requirements.txt file will be created manually.
echo README.md file will be created manually.
echo Dockerfile will be created manually.

:: Done message
echo Folder structure created successfully!

:: Pause the batch file to see the output
pause
