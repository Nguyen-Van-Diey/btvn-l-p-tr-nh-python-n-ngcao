import requests
import xml.etree.ElementTree as ET
import csv


url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"


response = requests.get(url)


if response.status_code == 200:
    with open("rss.xml", "wb") as f:
        f.write(response.content)
    print("✅ Đã tải và lưu file RSS thành công: rss.xml")
else:
    print("❌ Không thể tải RSS Feed. Mã lỗi:", response.status_code)
    exit()


tree = ET.parse("rss.xml")
root = tree.getroot()

items = root.findall(".//item")

news_list = []  

for item in items:
    title = item.findtext("title")
    link = item.findtext("link")
    description = item.findtext("description")
    pubDate = item.findtext("pubDate")

    news = {
        "Title": title,
        "Link": link,
        "Description": description,
        "Published": pubDate
    }
    news_list.append(news)

with open("news.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Title", "Link", "Description", "Published"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(news_list)

print(f"✅ Đã lưu {len(news_list)} tin tức vào file news.csv")
