import re
import random

attendee = []
num = 2  # 要抽出的人數
exceptid = 'justreadwithme_' #要排出的結果
cant_repeat = True  #是否可重複抽獎(True=不可重複抽)

def get_html():
    f = open('ig.txt', 'r', encoding='utf-8')
    html = f.read()
    f.close()
    return html


def catch_tag(html):
    regex_tag = r'<a class="_2dbep qNELH kIKUG" href="/[a-zA-Z0-9./_]+"'
    tag_list = re.findall(regex_tag, html)
    return tag_list


def clear_repeat(lst):
    clear_list = list(set(lst))
    return clear_list


html = get_html()
tag_list = catch_tag(html)

print('總參加人數:',len(tag_list)-1)
print("全部參加者:")
index = 1
for tag in tag_list:
    tag = tag.replace('<a class="_2dbep qNELH kIKUG" href="/', '')
    name = tag.replace('/"', '')
    if name != except_id:
        print('(', index, ')', name)
        attendee.append(name)
        index += 1

if cant_repeat:
    attendee = clear_repeat(attendee)

print('')
print("恭喜🎉✨得獎者是:")
print(random.sample(attendee, num))