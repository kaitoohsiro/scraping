import requests

from bs4 import BeautifulSoup

# 検索ページurl
page_url = 'https://images.search.yahoo.com/search/images;_ylt=Awr9F69HSERhEb0ABQCJzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRhY3RuA2NsawRjc3JjcHZpZANNcGdGVURFd0xqTGJzaGhQWHA2b01RQUFNVE16TGdBQUFBQW42OVAwBGZyA3NmcARmcjIDc2EtZ3AEZ3ByaWQDTXNDbDU1M2hRVkM1S2N5b2NqN0E4QQRuX3N1Z2cDMTAEb3JpZ2luA2ltYWdlcy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzM2BHF1ZXJ5AyVFNiU5NiU4RSVFOCU5NyVBNCVFOSVBMyU5QiVFOSVCMyVBNQR0X3N0bXADMTYzMTg2NTI2OA--?p=%E6%96%8E%E8%97%A4%E9%A3%9B%E9%B3%A5&fr=sfp&fr2=sb-top-images.search&ei=UTF-8&x=wrt'

r = requests.get(page_url)
soup = BeautifulSoup(r.text)

# find.allは検索結果に対して欲しいものだけを選択する
# soup.find_all("img", attrs={"alt": "「齋藤飛鳥」の画像検索結果"})
# soup.find_all("img")


img_tags = soup.find_all("img")


img_urls = []

count = 0
for img_tag in img_tags:
  url = img_tag.get("src")
  if url != None:
    count += 1
    img_urls.append(url)

# print(img_urls)  # ダウンロードする写真データのurl
# print(count)  # データ数のカウント



# ダウンロード関数
def download_image(url, file_path):
  r = requests.get(url, stream=True)

  if r.status_code == 200:
    with open(file_path, "wb") as f:
      f.write(r.content)


# ダウンロード先ファイルの参照(google drive用)
from google.colab import drive
drive.mount('./gdrive')

import os
google_drive_save_dir = "./gdrive/My Drive/研究/本研究/colab/スクレイピング /テスト3" # ダウンロード先の指定

for index, url in enumerate(img_urls):
  file_name = "{}.jpg".format(index)

  print(file_name)
  image_path = os.path.join(google_drive_save_dir, file_name)
  print(image_path)

  download_image(url=url, file_path=image_path)