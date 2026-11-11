import time
import requests
from bs4 import BeautifulSoup

# 1. 練習サイトのURLを指定
url = "http://quotes.toscrape.com/"

# 2. Webページを取得
response = requests.get(url)

# サーバーに負荷をかけないよう、リクエスト後は小休止を入れる習慣をつける
time.sleep(1)

# 3. HTMLを解析する準備
soup = BeautifulSoup(response.text, "html.parser")

# 4. 名言が格納されているブロック（class="quote" の divタグ）をすべて取得
quotes = soup.find_all("div", class_="quote")

# 5. 各ブロックからテキストと著者名を抽出して出力
for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    print(f"「{text}」 - {author}\n")