#BE-1-init-application
Програма на запит на голову сторінку повертає:
{
    "status_code": 200,
    "detail" : "ok",
    "result" : "working"
}
А по запиту /health повертає:
{"status" : "Ok"}

## Запуск додатку

1. Встановіть залежності, які вказані в файлі `requirements.txt`:
    ```shell
    pip install -r requirements.txt
2. Впевниться, що у ває є файл '.env' який містить змінні, для додатку.
    За потреби можете створити файл '.env' на основі файла '.env.sample'
3. Запустіть додаток за допомогою команди:
   ```shell
   uvicorn main:app
    Або ж просто запустіть основний файл 'main.py'
4. Після успішного запуска ваш додаток буде доступний за указаним портом та хостом. Ви мали вказати їх в файлі '.env'
 Тому відкрийте браузер та перейдіть за адресою 
    http://ваш хост:ваш порт

