# Instagram_Giveways
為了justreadwithme_抽獎，自己寫一個簡單抽獎

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
exceptid = 'justreadwithme_' #要排出的結果
cant_repeat = True  #是否可重複抽獎(True=不可重複抽)
```

### Output:

- 總參加人數
- 全部參加者
- 得獎者

