@echo off
echo Создание виртуального окружения...

REM Проверяем наличие Python
python --version 2>NUL
if errorlevel 1 (
    echo Python не установлен. Пожалуйста, установите Python
    exit /b 1
)

REM Создаем виртуальное окружение, если его нет
if not exist "venv" (
    echo Создаем виртуальное окружение...
    python -m venv venv
) else (
    echo Виртуальное окружение уже существует
)

REM Активируем виртуальное окружение
echo Активируем виртуальное окружение...
call venv\Scripts\activate.bat

REM Обновляем pip до последней версии
echo Обновляем pip...
python -m pip install --upgrade pip

REM Устанавливаем зависимости из requirements.txt
if exist "requirements.txt" (
    echo Устанавливаем зависимости из requirements.txt...
    pip install -r requirements.txt
) else (
    echo Файл requirements.txt не найден
    exit /b 1
)

echo Настройка завершена успешно!
echo Для активации окружения используйте команду: venv\Scripts\activate.bat 