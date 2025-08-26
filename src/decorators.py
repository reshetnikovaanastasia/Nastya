from datetime import datetime


def log(filename=None):
    """Автоматически логирует начало и конец выполнения функции, а также ее результаты или
    возникшие ошибки.Принимает необязательный аргумент filename, который определяет,
    куда будут записываться логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль.
    Логирование включает:
    Имя функции и результат выполнения при успешной операции.
    Имя функции, тип возникшей ошибки и входные параметры,
    если выполнение функции привело к ошибке."""

    def log_decorator(function):
        def wrapper(*args, **kwargs):
            try:
                time_start = f'{function.__name__} start-{datetime.now()}'
                result = function(*args, **kwargs)
                time_stop = f'{function.__name__} stop-{datetime.now()}'
                result_message = f'{function.__name__} ok'
                if filename is None:
                    print(f'{time_start}\n{time_stop}\n{result_message}')
                else:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{time_start}\n{time_stop}\n{result_message}\n')
            except Exception as e:
                time_stop = f'{function.__name__} stop-{datetime.now()}'
                result_message = f'{function.__name__} error: {type(e).__name__}.Inputs: {args}, {kwargs}'
                if filename is None:
                    print(f'{time_start}\n{time_stop}\n{result_message}')
                else:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{time_start}\n{time_stop}\n{result_message}\n')

        return wrapper

    return log_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
