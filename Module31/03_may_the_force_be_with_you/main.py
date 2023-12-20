import requests
import json


def get_millennium_falcon_info():
    falcon_url = "https://swapi.dev/api/starships/10/"

    response = requests.get(falcon_url)

    if response.status_code == 200:
        falcon_info = response.json()
        pilots_info = []
        for pilot_url in falcon_info['pilots']:
            pilot_response = requests.get(pilot_url)
            if pilot_response.status_code == 200:
                pilot_info = pilot_response.json()
                homeworld_response = requests.get(pilot_info['homeworld'])
                if homeworld_response.status_code == 200:
                    homeworld_info = homeworld_response.json()
                    pilot_info['homeworld_info'] = homeworld_info
                pilots_info.append(pilot_info)
        result = {
            'название': falcon_info['name'],
            'максимальная скорость': falcon_info['max_atmosphering_speed'],
            'класс': falcon_info['starship_class'],
            'список пилотов': pilots_info
        }

        return result
    else:
        print(f"Ошибка при запросе к API. Код ответа: {response.status_code}")
        return None


def main():
    millennium_falcon_info = get_millennium_falcon_info()

    if millennium_falcon_info:
        print("Информация о Millennium Falcon:")
        print(json.dumps(millennium_falcon_info, indent=2, ensure_ascii=False))

        with open('millennium_falcon_info.json', 'w', encoding='utf-8') as file:
            json.dump(millennium_falcon_info, file, indent=2, ensure_ascii=False)
        print("Информация записана в файл millennium_falcon_info.json")


if __name__ == "__main__":
    main()

