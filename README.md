#BE-3-init-application
Програма на запит на голову сторінку повертає:
{
    "status_code": 200,
    "detail" : "ok",
    "result" : "working"
}

## Запуск додатку

1. Встановіть залежності, які вказані в файлі `requirements.txt`:
    ```shell
    pip install -r requirements.txt
2. Створіть файл Dockerfile з таким змістом:
    ```shell
    FROM python:3.9

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    EXPOSE 8000

    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
    ```
    Зміст можете змінювати. В залежності від вашого хоста, порта та робочої директорії

2. Створіть файл docker-compose.yml з таким змістом:
    ```shell
    version: '3'
        services:
            core_api:
                build: .
                container_name:  "mcontainer"
                ports:
                  - "8000:8080"

                volumes:
                  - /app
                  - /tests
            test_runner:
              build:
                context: .
              command: pytest tests/test_main.py
              volumes:
                - ./tests:/app/tests
              depends_on:
                - core_api
    ```
    У файлі `docker-compose.yml` ми використовуємо версію 3 для Docker Compose та описуємо сервіси з назвами `app` та `test_runner`. Ми вказуємо `build: .`, щоб використовувати поточну директорію як контекст для побудови образу. 

3. Відкрийте термінал та перейдіть до кореневої папки вашого проекту.
4. Виконайте наступну команду, щоб запустити ваше FastAPI додаток в Docker:
    ```shell
    docker-compose up
    ```
    Ця команда побудує образ та контейнер для вашого додатку, запустить його та перенаправить порти.
    Також запустить тести.
    Ви побачите вивід, що додаток запущено і доступний за адресою http://localhost:8080.
5. Щоб зупинити додаток та контейнер, виконайте команду:
    ```shell
    docker-compose stop
    ```
    Це зупинить додаток та контейнер.
