@echo off

:: Root folder creation
mkdir fastapi_project
cd fastapi_project

:: Create root-level files
type nul > .env
echo # FastAPI Project > README.md
type nul > requirements.txt
echo @echo off > Create_Folders.bat

:: Create app folder structure
mkdir app
cd app
type nul > main.py

:: Create app subdirectories
mkdir api
mkdir models
mkdir schemas
mkdir services
mkdir tests
mkdir utils

:: Create API subdirectories
cd api
mkdir v1
mkdir v2
mkdir core
cd ..

:: Back to root
cd ..

:: Create migrations folder
mkdir migrations

:: Done
echo Folder structure created successfully!
pause
