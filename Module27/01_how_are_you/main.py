import functools
import random

class RandomAnecdot:
    def __init__(self):
        self.sbornic = [
            "Если бы программисты были врачами, им бы говорили «У меня болит нога», а они отвечали «Ну не знаю,"
            " у меня такая же нога, а ничего не болит»" , "Из комбинации лени и логики получаются программисты" ,
            "Работа программиста и шамана имеет много общего — оба бормочут непонятные слова, совершают"
            " непонятные действия и не могут объяснить, как оно работает"]
    def get_random_anecdot(self):
        if not self.sbornic:
            return None
        return random.choice(self.sbornic)

def how_are_you(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        random_element = random_anecdot_instance.get_random_anecdot()
        answer = input("Хочешь анекдот?")
        if answer == "да":
            print(f"{random_element}.")
        else:
            print(f"А я все равно расскажу! {random_element}.")
        return func(*args, **kwargs)

    return wrapper


@how_are_you
def test():
    print('<И не благодари>')
random_anecdot_instance = RandomAnecdot()
test()

