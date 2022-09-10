import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
from colorama import init
base_url = "https://www.imdb.com/chart/top/"
base_html = requests.get(base_url)
soup = BeautifulSoup(base_html.text,"lxml")
class find_top_250_movies():
    def find_movie(placement):
        all_names=soup.find_all("td",class_="titleColumn")
        soup2 = BeautifulSoup(str(all_names[placement-1]),"lxml")
        damn_name = soup2.find_all("a")
        for real_name in damn_name[0]:
            return real_name
    def find_most_imdb_points(placement):
        all_points = soup.find_all("td",class_='ratingColumn imdbRating')
        soup2 = BeautifulSoup(str(all_points[placement-1]),"lxml")
        point = soup2.find_all("strong")
        for real_point in point[0]:
            return real_point
    def find_most_imdb_points_long(placement):
        all_points = soup.find_all("td",class_='ratingColumn imdbRating')
        soup2 = BeautifulSoup(str(all_points[placement-1]),"lxml")
        point = soup2.find_all("strong")
        return point[0]["title"]



class find_specific_movie():
    def find_subject_of_the_top_250_movies(placement):
        all_names=soup.find_all("td",class_="titleColumn")
        soup2 = BeautifulSoup(str(all_names[placement-1]),"lxml")
        damn_name = soup2.find_all("a")
        link = str(damn_name[0]["href"])
        new_base_url = f"https://www.imdb.com{link}"
        new_base_html  = requests.get(new_base_url)
        soup3 = BeautifulSoup(new_base_html.text,"lxml")
        subject =soup3.find_all("span",class_="sc-16ede01-2 gXUyNh")
        for main_subject in subject[0]:
            return main_subject

        #




        
        
        





        
            
        



