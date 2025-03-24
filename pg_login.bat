@echo off
setlocal enabledelayedexpansion

chcp 1251

:: Чтение строки подключения к БД (DB_ADMIN) из файла (.env)
for /f "tokens=1,2 delims==" %%a in (.env) do (
    :: if "%%a"=="DB_TEST" set connectionString="%%b"
    if "%%a"=="DB_ADMIN" set connectionString="%%b"
)

:: Выполнение команды psql с подставленной строкой подключения
psql !connectionString!

endlocal
