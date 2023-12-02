class PermissionError(Exception):
    pass

def check_permission(required_permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_permissions = ['admin']

            if required_permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")

        return wrapper
    return decorator


user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')

delete_site()
try:
    add_comment()
except PermissionError as e:
    print(e)

