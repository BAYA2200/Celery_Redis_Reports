
Этот проект представляет собой сайт в котором можно писать отчет и отправлять его по почте
Отправлять отчеты могут только авторизованные пользователи


# Настройте свою виртуальную среду для Windows

```bash
python -m venv env 
.\env\Scripts\activate 
cd app
pip install -r requirements.txt 
```
# Если вы используете Linux или macOS, вы вместо этого запустите

```bash
python3 -m venv env 
source ./env/bin/activate
cd app
pip install -r requirements.txt
```

# Создаем и запускаем контейнер(У вас должен быть Docker установлен)

```bash
docker-compose up -d --build
```

# Затем переходим на следующий путь введя его в браузере




