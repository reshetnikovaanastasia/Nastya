from src.decorators import log


@log()
def my_function(x, y):
    return x + y


def test_log_capsys(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert ("my_function start" in captured.out and "my_function stop" in captured.out
            and "my_function ok" in captured.out)


@log()
def my_function_error(x, y):
    raise ValueError("Страшная ошибка")


def test_log_capsys_error(capsys):
    my_function_error(1, 2)
    captured = capsys.readouterr()
    assert ("my_function_error start" in captured.out and "my_function_error stop" in captured.out
            and "my_function_error error: Страшная ошибка. Inputs: (1, 2), {}" in captured.out)
