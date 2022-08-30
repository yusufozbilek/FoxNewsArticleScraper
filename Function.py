from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

class FoxNewsScraper:
    def __init__(self):
        op = webdriver.ChromeOptions()
        #op.add_argument('headless')
        self.driver = webdriver.Chrome(options=op)
        self.url = "https://www.foxnews.com/"
        self.driver.get(self.url)
        self.site = self.driver.find_element(By.CLASS_NAME,"main-content")
        self.editedSpotlightList = []
        self.contentarticleList = []
        self.exculusiveclipList = []
        self.SearchList = []
    def ScrapMainPageNews(self):
        self.MainPageContents = self.site.find_element(By.CLASS_NAME, "main.main-primary.js-river")
        self.TopSpotlight = self.site.find_element(By.TAG_NAME, "article")
        self.TopSpotlightTitle = self.TopSpotlight.find_element(By.CLASS_NAME,"title")
        self.TopSpotlightLink = self.TopSpotlightTitle.find_element(By.TAG_NAME, "a").get_attribute("href")
        self.TopSpotlightTitle = self.TopSpotlightTitle.find_element(By.TAG_NAME, "a").text
        
        self.driver.get(self.url)
        self.site = self.driver.find_element(By.CLASS_NAME,"main-content")
        self.MainPageContents = self.site.find_element(By.CLASS_NAME, "main.main-primary.js-river")
        self.spotlightDiv = self.site.find_elements(By.CLASS_NAME,"collection.collection-spotlight")[1]
        self.spotlightList = self.spotlightDiv.find_elements(By.TAG_NAME, "article")
        
        
        for sub in self.spotlightList:
            Title = sub.find_element(By.CLASS_NAME, "title").text
            Link = sub.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, "a").get_attribute("href")
            self.editedSpotlightList.append([Title,Link])
        
        self.driver.get(self.url)
        self.site = self.driver.find_element(By.CLASS_NAME,"main-content")
        self.MainPageContents = self.site.find_element(By.CLASS_NAME, "main.main-primary.js-river")
        self.spotlightDiv = self.site.find_element(By.CLASS_NAME,"main.main-secondary")
        self.spotlightList = self.spotlightDiv.find_elements(By.TAG_NAME, "article")
        for sub in self.spotlightList:
            Category = sub.find_element(By.CLASS_NAME, "eyebrow").text
            Title = sub.find_element(By.CLASS_NAME, "title").text
            Link = sub.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, "a").get_attribute("href")
            self.contentarticleList.append([Category, Title, Link])
        return ([self.TopSpotlightTitle,self.TopSpotlightLink],self.editedSpotlightList,self.contentarticleList)
    def ScrapExculusiveClipText(self):
        self.driver.get(self.url)
        self.ExculusiveClips = self.site.find_element(By.XPATH, "//main/div/div/div[4]/aside/div/div/div[3]/section/div").find_elements(By.TAG_NAME, "article")
        for sub in self.ExculusiveClips:
            Program = sub.find_element(By.CLASS_NAME, "eyebrow").text
            Title = sub.find_element(By.CLASS_NAME, "title").text
            Link = sub.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, "a").get_attribute("href")
            self.exculusiveclipList.append([Program,Title,Link])
        return self.exculusiveclipList
    def ScrapBySection(self):
        pass
    def ScrapBySearch(self,Keyword):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH,"/html/body/div[2]/header/div[2]/div/div[1]/nav/ul/li[13]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/header/div[4]/div[1]/div/div/form/fieldset/input[1]").send_keys(Keyword)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/header/div[4]/div[1]/div/div/form/fieldset/input[2]").click()
        self.driver.get(self.driver.current_url)
        try:
            while True:
                self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/div[3]/div[2]").find_element(By.TAG_NAME, "a").click()
        except:
            print("page loaded")
            
        while int(self.driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[1]/div/div[1]/div[1]/span[1]").text) != 100:
            pass
        self.Articles = self.driver.find_element(By.CLASS_NAME,"collection.collection-search.active").find_elements(By.TAG_NAME, "article")
        for sub in self.Articles:              
            Category = sub.find_element(By.CLASS_NAME, "eyebrow").text
            Link = sub.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, "a").get_attribute("href")
            Title = sub.find_element(By.CLASS_NAME, "title").text
            Image = sub.find_element(By.TAG_NAME,"picture").find_element(By.TAG_NAME,"img").get_attribute("src")
            self.SearchList.append([Category,Link,Title,Image])
            
        return self.SearchList
    
    def ScrapByCatetgory(self):
        pass
    def SaveArticles(self):
        pass
    def GetArticleCount(self):
        pass
