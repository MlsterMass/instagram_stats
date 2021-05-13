from modules.InstagramER import InstagramER

headers = {
 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
 "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
}

accounts = [
 "https://www.instagram.com/adventurer.me/",
 "https://www.instagram.com/grime.shop/",
 "https://www.instagram.com/stasy_deg/",

]
# Создаём объект анализатора
inst_er = InstagramER(headers=headers)
# Получаем ER заданнх аккаунтов
for account in accounts:
     er_of_account = inst_er.get(account)
     print(f"Account: {account}, ER: {er_of_account}")
