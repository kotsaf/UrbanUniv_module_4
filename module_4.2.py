def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()
#inner_function()  - ошибка возникает из-за того, что внутрення функция находится в локальном пространстве