# Тестовое задание

## Инструкция к подготовке

Перед началом работы необходимо убедиться в том, что на компьютере установлено следующее ПО:
- `PostgreSQL` версии `10.17-2` или выше
- `Python` версии `3.7.9` или выше
- `PIP` версии `21.2.2` или выше
- Библиотеки для `Python`, указанные в файле `itmegastar/tools/requirements.txt` 

## Инструкция к инициализации

Перед началом работы, пользователь должен создать ПОЛЬЗОВАТЕЛЯ и БД для проекта. Пользователь должен обладать необходимыми для работы БД с проектом правами:
- Создание БД
- Удаление БД
- Изменение БД
- и тд.

Можно делегировать пользователю такие права вручную, либо назначить пользователя суперпользователем.

В файле настроек БД (`/itmegastar/itmegastar/.env`) необходимо указать:
- Имя БД (`DB_NAME`)
- Пользователя БД (`DB_USER`)
- Пароль (`DB_PASSWORD`)
- Хост (`DB_HOST`)
- Порт (`DB_PORT`)

### Cheat sheet с запросами

- Создание БД `CREATE DATABASE <dbname>;`
- Создание пользователя `CREATE USER <user> WITH ENCRYPTED PASSWORD <password>;`
- Назначение всех прав управления БД пользователю `GRANT ALL PRIVILEGES ON DATABASE <dbname> TO <user>;`
- Назначение пользователя суперпользователем `ALTER USER <user> WITH SUPERUSER;`

## Инструкция к запуску сервиса

В файле настроек сервиса (`/itmegastar/tools/.server`) необходимо (можно оставить значения по умолчанию) указать:
- Хост (`HOST`)
- Порт (`PORT`)

В папке `/itmegastart/tools/` расположены инструменты для ускоренного взаимодействия с сервисом:
- `create_env` - сценарий для создания виртуального окружения с использованием библиотек из `itmegastar/tools/requirements.txt` 
- `create_superuser` - сценарий создания суперпользователя. Указание эл. почты необязательно
- `init_data` - инициализация данных в БД из фикстуры, указанной в `/itmegastar/itmegastar/settings.py` в значении `TEST_TASK_FIXTURE` в разделе `Fixtures`
- `runserver` - запуск сервера с параметрами, указанными в `/itmegastar/tools/.server`
- `test` - запуск тестов

## Ресурсы

### Административная панель

Адрес - `<host>:<port>/admin/`
Для входа необходимы имя и пароль суперпользователя

### API 

Адрес - `<host>:<port>/api/`

#### Список писателей и их книг

Адрес - `<host>:<port>/api/writers/`

#### Информация о конкретном писателе и о его книгах

Адрес - `<host>:<port>/api/writers/<id>`