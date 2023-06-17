# Парсер документации PEP-8

[![Praktikum](https://yastatic.net/q/logoaas/v2/%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81.svg?circle=black&color=000&first=white)](https://practicum.yandex.ru/profile/backend-developer/) [![Praktikum](https://yastatic.net/q/logoaas/v2/%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D1%83%D0%BC.svg?color=000)](https://practicum.yandex.ru/profile/backend-developer/)

## Описание проекта
Парсерс работает асинхронно. Он открывает ссылки на документацию со страницы https://peps.python.org/ и считывает со страницы каждого документа название и статус. 

## Использованные технологии
- Scrapy==2.5.1

## Инструкции по запуску
Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd scrapy_parser_pep/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить парсер:
```
scrapy crawl pep
```
Результаты работы парсера сохранятся в папке results

## Требования к версии Python
Работает на Python 3.7.0

## Автор
- Павел Вервейн | [hive937](https://github.com/hive937)
