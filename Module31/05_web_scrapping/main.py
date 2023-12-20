import requests
import re
def get_h3_headings(url):
    response = requests.get(url)
    if response.status_code == 200:
        pattern = re.compile(r'<h3.*?>(.*?)<\/h3>', re.DOTALL)
        headings = pattern.findall(response.text)

        return headings
    else:
        print(f"Ошибка при получении страницы. Код ошибки: {response.status_code}")
        return None
url = 'https://www.example.com'
headings = get_h3_headings(url)
if headings:
    print(headings)
