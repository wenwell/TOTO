from time import sleep

from selenium import webdriver
#打开浏览器
driver=webdriver.Chrome('../chormdriver_78//chromedriver.exe')

sleep(1)
#调整浏览器窗口大小
driver.maximize_window()
sleep(1)
#打开网址
driver.get("http://www.baidu.com")
sleep(1)
driver.get("http://www.jd.com")
sleep(1)


#后退
driver.back()
sleep(1)
#前进
driver.forward()
sleep(1)
#刷新
driver.refresh()
sleep(1)


#关闭浏览器，而不退出driver
#driver.close()

#关闭浏览器，并退出driver
driver.quit()