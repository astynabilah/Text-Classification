from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import io

browser = webdriver.Chrome(executable_path='D:\chromedriver\chromedriver.exe') #for opening chrome
wait = WebDriverWait(browser, 10) #waiting time
browser.set_window_size(1280, 800) #chrome's window size
html_source = ''
for j in range(1,13): #since there's12 pages
    url = "https://reviews.femaledaily.com/products/blush-76/blush/pixy/blush-on?cat=&cat_id=0&age_range=&skin_type=&skin_tone=&skin_undertone=&hair_texture=&hair_type=&order=newest&page="+str(j)
    browser.get(url) #accessing site url

    elems = browser.find_elements_by_class_name('read-more') #finding all "read more..." texts

    for i in range(0,len(elems)):
        if len(elems) > 0 and elems[i].is_displayed():
            elems[i].click() #expanding all long review by clicking all "read more..." 
    html_source = browser.page_source #storing source code of current page along with previous source code
    with io.open("html_source.txt", "a", encoding="utf-8") as f:
        f.write(html_source)
    f = open("D:/Tel-U/6 Semester 6/Natural Language Processing/task 4/html_source.txt","a")
    f.write(html_source)
    f.close()
browser.close() #closing

