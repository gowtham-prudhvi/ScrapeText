import json
import sys
# import urllib2
import requests
from langdetect import detect
from langdetect import detect_langs
from bs4 import BeautifulSoup
from bs4 import NavigableString
import time

json_file_list = sys.argv[1]


def end_node(tag):
    if tag.name not in ["div", "p", "li"]:
        return False
    if isinstance(tag,NavigableString): #if str return
        return False
    if not tag.text: #if no text return false
        return False
    elif len(tag.find_all(text=False)) > 0: #no other tags inside other than text
        return False
    return True #if valid it reaches here

all_links = set()
with open(json_file_list) as fp:
    for line in fp:
        total_count = 0
        outlink_count = 0
        te_count = 0
        print(line.strip())
        with open(line.strip()) as jsonfp:
            for json_line in jsonfp:
                total_count += 1
                # print(total_count, outlink_count)
                # if total_count < 3:
                #     continue
                curr_dict = json.loads(json_line.strip())
                # print(curr_dict)
                # quit()
                if len(curr_dict['outlinks']) != 0:
                    # print(len(curr_dict['outlinks']))
                    outlink_count += 1
                    all_links.update(curr_dict['outlinks'])
                    # page = requests.get(curr_dict['outlinks'][0])
                    # time.sleep(1)
                    # print(page)
                    # soup = BeautifulSoup(page.content, 'html.parser')
                    # # print(soup.prettify())
                    # # print(curr_dict['outlinks'][0])
                    
                    # content = soup.find_all(end_node)
                    # print(content[3]) #all end nodes matching our criteria
                    # quit()
                    # print(detect_langs(curr_dict['content']))
                    # quit()
                    # try:
                    #     if 'te' in detect_langs(curr_dict['content']):
                    #         te_count += 1
                    # except:
                    #     print(total_count, outlink_count, te_count)
                    #     # pass
                    # print(detect_langs(curr_dict['content']))
                    # print(curr_dict['content'], curr_dict['outlinks'])
        # print(total_count, outlink_count, te_count)
        # quit()
        # break


for link in all_links:
    print(link)

# print(len(all_links))