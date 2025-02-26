# Проект курсовой работы №4 курса SkyPro

## Описание:

Курсовая работа №4

Бэкенд по работе с рассылками


## Функционал:
Данная программа позволяет делать рассылки пользователям.   
    
Разработан функционал:

* модели юзера, получателя, сообщения, рассылки, попытки рассылки
* админка + модератор;
* определены права доступа к функционалу по иерархии;
* рассылка через консоль (send_letter);
* юзеры регистрируются с подтверждением email;
* серверное и клиентское кэширование на 10 секунд.


## Тестирование:

Для самостоятельного тестирования используйте модули тестирования находящиеся в пакете tests.

## Установка:

1. Клонируйте репозиторий:
```
git clone github.com/BazilioSan/CP4.git
```
2. Установите зависимости:
```
pip install poetry
poetry update
```
## Использование:

заполните .env файл по примеру .env.sample
python manage.py runserver

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:


Этот проект лицензирован по [лицензии MIT](LICENSE).