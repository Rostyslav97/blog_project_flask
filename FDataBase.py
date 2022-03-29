import math
import sqlite3
from time import time


class FDataBase:
    def __init__(self, db): 
        self.__db = db 
        self.__cur = db.cursor() 


    def getMenu(self): 
        sql = '''SELECT * FROM mainmenu'''
        try: 
            self.__cur.execute(sql)
            res = self.__cur.fetchall() 
            if res: return res 
        except:
            print("Mistake while reading from DB")
        return [] 


    def addPost(self, title, text): 
        try: 
            tm = math.floor(time()) 
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm)) 
            self.__db.commit() 
        except sqlite3.Error as e:
            print("Mistake while adding post to DB "+str(e))
            return False
        
        return True


    def getPost(self, postId):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE id = {postId} LIMIT 1") 
            res = self.__cur.fetchone() # берем один пост
            if res: # если res не равняется None
                return res 
        except sqlite3.Error as e:
            print("Mistake while getting post from DB " +str(e))
        
        return (False, False)

    
    def getPostsAnonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text FROM posts ORDER BY time DESC") # выбираем все записи с таблицы posts начиная от самой новой
            res = self.__cur.fetchall() # получаем все записи в виде словаря
            if res: return res
        except sqlite3.Error as e:
            print("Mistake while getting post from DB "+str(e))

        return []