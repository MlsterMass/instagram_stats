import requests
import json

class InstagramER:
     def __init__(self, headers=None, proxy=None, cookies=None):
    # Инициализируем заголовки
        self.__headers = headers
        # Инициализируем прокси
        self.__proxy = proxy
        # Инициализируем куки
        self.__cookies = cookies
     def __get_user_info(self, url):
        # Получаем данные пользователя, в т.ч. посты
        user_info = requests.get(url, headers=self.__headers, proxies=self.__proxy, params={"__a": 1})
        # Если сервер ответил
        if user_info.status_code == 200:
        # Получаем JSON-ответ
            json_info = user_info.text
        # Десертализуем JSON в словарь
        return json.loads(json_info)
     def __get_count_of_subscribers(self, user_info):
        # Из словаря с данными возвращаем
        return user_info["graphql"]["user"]["edge_followed_by"]["count"]
     def __get_summary_likes_and_comments(self, user_info):
        # Счётчик комментариев
        count_of_comments = 0
        # Счётчик лайков
        count_of_likes = 0
        # Со скольки постов собираем статистику
        count_of_posts = len(user_info["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"])
        # Обходим в цикле все посты
        for key in user_info["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
            # Суммируем количество комментариев поста к общему счётчику
            count_of_comments += key["node"]["edge_media_to_comment"]["count"]
            # Суммируем количество лайков поста к общему счётчику
            count_of_likes += key["node"]["edge_liked_by"]["count"]
            # Суммируем среднее количество лайков и среднее количество комментариев у одного поста
        return (count_of_comments / count_of_posts) + (count_of_likes / count_of_posts)
     def get(self, url):
        # Получаем информацию о пользователей
        user_info = self.__get_user_info(url)
        # Получаем количество подписчиков
        count_of_subscribers = self.__get_count_of_subscribers(user_info)
        # Получаем суммарное количество лайков и репостов у одного поста (в среднем)
        summary_likes_and_comments = self.__get_summary_likes_and_comments(user_info)
        # Определяем ER
        return summary_likes_and_comments / count_of_subscribers * 100