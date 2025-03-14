@echo off
setlocal enabledelayedexpansion

chcp 1251

:: Путь к файлу .pgpass
set pgpassFile=.pgpass

:: Чтение строки из файла .pgpass
set /p password=<%pgpassFile%

:: Компоненты строки подключения
set user=postgres
set host=localhost
set port=5432
set dbname=warriors_db

:: Формирование строки подключения
set connectionString=postgresql://postgres:%password%@%host%:%port%/%dbname%

:: Выполнение команды psql с подставленной строкой подключения
psql !connectionString!

endlocal
