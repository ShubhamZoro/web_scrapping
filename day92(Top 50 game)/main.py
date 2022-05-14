import requests
from bs4 import BeautifulSoup
import csv
link_="https://store.steampowered.com/search/?term=top+games"
response=requests.get(url=link_,
                      headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                               'Accept-Language': 'en-US,en;q=0.9',
                               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
                               ,}
                      )
soup = BeautifulSoup(response.content, "html.parser")
results=soup.find(id="search_resultsRows")

prices=results.find_all(class_='col search_price_discount_combined responsive_secondrow')
# reviews=results.find_all("span",{"class":"search_review_summary"})
titles=results.find_all(class_='title')

title_list=[]
for title in titles:
    title_list.append(title.get_text())
# print(title_list)
price_list=[]
for price in prices:
    print(len(price.get_text()))
    if len(price.get_text())==5:
        price_list.append(str("not found"))
    else:
        price_list.append(price.get_text().replace("\r\n","").replace("\n\n\n","").strip().split("₹")[-1])
print(price_list)

links=results.find_all("a",{"class":"search_result_row ds_collapse_flag"})
links_list=[]

# review_list=[]
# for review in reviews:
#     review_list.append(review.get('data-tooltip-html').replace("<br>",", "))
# print(len(review_list))
# print(review_list)

for link in links:
    links_list.append(link.get('href'))
# print(links_list)
game_list=[]
for i in range(len(links_list)):
    dict={"name":title_list[i],"Url":links_list[i],"Price(in Rs)":price_list[i]
              }
    game_list.append(dict)



field_name=['name','Url','Price(in Rs)']
with open('Top50 Game.csv', 'w',encoding='UTF-8', newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_name)
    writer.writeheader()
    writer.writerows(game_list)