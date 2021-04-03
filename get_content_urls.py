import requests
import random
import multiprocessing as mp

with open("just_the_outlinks.txt") as fp:
    text = fp.read()
file_list = text.splitlines()
# random.shuffle(file_list)
# print(file_list[:10])
print("Shuffled")
# i = 0
file_list = file_list[:10]


def get_content(curr_url):
    print(curr_url)
    # try:
    page = requests.get(curr_url)
    #     return 1
    # except:
    #     return 0




# for curr_url in file_list:
#     print(curr_url)
#     try:
#         page = requests.get(curr_url)
#     except:
#         pass
#     i += 1
#     if i > 1000:
#         break
# print(i)
pool = mp.Pool(processes=1)
print("Pool created")
print(file_list)
pool.map(get_content, file_list)
# print(results)