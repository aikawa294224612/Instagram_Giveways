# Instagram_Giveways
為了justreadwithme_抽獎，自己寫一個簡單抽獎 (臨時要抽獎，ig更新了，所以不走爬蟲)

![Imgur](https://i.imgur.com/1w7CIoo.jpg)

### txt內容
抓取instagram貼文中留言的區塊:
```
<ul class="XQXOT    pXf-y ">
	<ul class="Mr508 ">...</ul>
	<ul class="Mr508 ">...</ul>
	....
</ul>
```

### Config

```
num = 2  # 要抽出的人數
except_id = ['justreadwithme_', 'wishlotus']  #要排除的結果
cant_repeat = True  #是否可重複抽獎(True=不可重複抽)
```

### Output:

- 總參加人數
- 不參加抽獎者
- 總抽獎人數
- 全部參加者
- 得獎者

