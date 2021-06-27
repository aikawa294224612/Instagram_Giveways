import re
import random

attendee = []
num = 2  # 要抽出的人數
except_id = ['justreadwithme_', 'wishlotus']  #要排除的結果
cant_repeat = True  #是否可重複抽獎(True=不可重複抽)


def get_html():
    f = open('ig.txt', 'r', encoding='utf-8')
    html = f.read()
    f.close()
    return html


def catch_tag(html):
    tag = r'<a class="sqdOP yWX7d     _8A5w5   ZIAjV " href="/[a-zA-Z0-9./_]+/"'
    tag_list = re.findall(tag, html)
    return tag_list


def cut_tags(tag):
    # tag = tag.replace('<a class="_2dbep qNELH kIKUG" href="/', '')
    tag = tag.replace('<a class="sqdOP yWX7d     _8A5w5   ZIAjV " href="/', '')
    name = tag.replace('/"', '')
    return name

# 清除重複的
def clear_repeat(lst):
    clear_list = list(set(lst))
    return clear_list


html = get_html()
tag_list = catch_tag(html)

print("全部參加者:")
index = 1
for tag in tag_list:
    name = cut_tags(tag)
    if name not in except_id:
        print('(', index, ')', name)
        attendee.append(name)
        index += 1

if cant_repeat:
    attendee = clear_repeat(attendee)

total = len(tag_list)-1
total_except = len(except_id)-1
total_giveway = total - total_except
print('總參加人數:', total)
print('不參加抽獎者:', total_except)
print('總抽獎人數:', total_giveway)
print("恭喜🎉✨得獎者是:")
print(random.sample(attendee, num))
