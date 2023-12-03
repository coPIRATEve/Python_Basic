class App:
    routes = {}
    @classmethod
    def callback(cls, path):
        def wrapper(callback_func):
            cls.routes[path] = callback_func
            return callback_func
        return wrapper
    def get(self, path):
        return self.routes.get(path)

app = App()

@app.callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
