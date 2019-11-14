from argparse import Action
#####加了隐式的等待后sleep（）可以去掉，以下用########注释掉了sleep（）
import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_input(driver):
    driver.get("http://ui.yansl.com/#/input")
    #xpath定位到输入框
    input = driver.find_element_by_xpath("//input[@name='t1']")
    # 清空
    input.clear()
    # 输入

    input.send_keys("我是谁？我在哪？我该干嘛？")
    ##########
    sleep(2)


from time import sleep

def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)

    slider = driver.find_element_by_xpath("//label[text()='竖向选择']/../div/div/div/div/div")
    sleep(2)
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider,0,-200).perform()
    sleep(2)

def test_radio(driver):
    driver.get("http://ui.yansl.com/#/radio")
    ##########

    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")

    # 点击
    radio.click()
    ##########


def test_select(driver):
    driver.get("http://ui.yansl.com/#/select")
    ##########

    select = driver.find_element_by_xpath("//*[@id='form']/form/div[3]/div/div/div[2]/input")
    select.click()

    ##########
    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions = ActionChains(driver)
    actions.move_to_element(option).perform()

    ##########
    option.click()
##########


def test_time(driver):
    driver.get("http://ui.yansl.com/#/dateTime")

    t1 = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[1]/div/div/input")
    # 清空
    t1.clear()
    # 输入
    t1.send_keys("14:18:00")
    ##########


def test_file(driver):
    driver.get("http://ui.yansl.com/#/upload")
    file = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")
    ##########
    # 清空
    file.clear()
    file.send_keys("C:\\Users\\000\\Desktop\\tup\\QQ图片20191113144447.jpg")
    ##########

def test_file2(driver):
    driver.get("http://ui.yansl.com/#/upload")
    ##########

    file = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button/span")

    file.click()
    ##########
    autoit.win_wait("打开", 10)
    ##########
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "C:\\Users\\000\\Desktop\\tup\\QQ图片20191113144447.jpg")
    ##########
    autoit.control_click("打开", "Button1")
##########

def test_alert(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    ##########

    button = driver.find_element_by_xpath("/html/body/table/tbody/tr[6]/td[2]/input")
    button.click()
    ##########
    alert = driver.switch_to.alert
    alert.send_keys("fsjdfhldsf")
    alert.accept()
##########



def test_windows(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    ##########

    dang_dang = driver.find_element_by_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    ##########
    jd = driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    ##########
    dn = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    ##########

# 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
 # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)
 ##########
        if driver.title.__contains__("京东"):
            break

#嵌套切换
def test_iframe(driver):
    driver.get("http://192.168.1.128:8082/xuepl1/frame/main.html")
    ##########
#进入当前的iframe模块
    frame = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
#切换模块 frame
    driver.switch_to.frame(frame)
    ##########
#点击京东的文字按钮
    driver.find_element_by_partial_link_text('京东').click()
    ##########
# 退出当前frame
    driver.switch_to.parent_frame()

# 回到初始页面
    iframe = driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
    driver.switch_to_frame(iframe)
    ##########

#选定输入框
    inpu = driver.find_element_by_xpath('//*[@id="key"]')
    inpu.clear()
#输入文字电脑
    inpu.send_keys("电脑")
##########
