# Это серверная часть проекта
Возможно, всё переменится и бэкенд будет на C# - кто знает, кто знает...

## Установка
- Установите [`python`](https://www.python.org/downloads/) версии хотя бы `3.9`
- Склонируйте репозиторий:\
`git clone git@github.com:AndrusovN/E-Grade-Book.git`
- Зайдите в папку `backend`\
`cd E-Grade-Book/backend`
- Создайте виртуальную среду python
    - Windows:
    ```
    pip install virtualenv
    python -m venv venv
    venv\Scripts\activate 
    ```
    
    - Linux:

    ```
    sudo apt-get install python-pip -y
    pip3 install virtualenv
    python3 -v venv venv
    . venv/bin/activate
    ```
- Установите нужные зависимости
`pip install -r requirements.txt`
- Заполните файл `.env` --- в нём должны быть заполнены все поля, которые есть в `example.env`
- Запустите тесты:
    - Windows: `python main_test.py`
    - Linux: `python3 main_test.py`
- Запустите проект:
    - Windows: `python main.py`
    - Linux: `python3 main.py`
