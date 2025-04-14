from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.dida365.com/signin")

# 输入用户名和密码
username_input = driver.find_element(By.ID, "emailOrPhone")
password_input = driver.find_element(By.ID, "password")
username_input.send_keys("851284850@qq.com")
password_input.send_keys("200810chen")
# password_input.send_keys(Keys.RETURN)
sign_button = driver.find_element(By.CLASS_NAME,"button__3eXSs ")
sign_button.click();

time.sleep(3)  # 等待登录完成

print(sign_button)
# 添加任务
# add_task_button = driver.find_element(By.CLASS_NAME, "add-task-button")
# add_task_button.click()
# task_input = driver.find_element(By.CLASS_NAME, "task-input")
# task_input.send_keys("新任务")
# task_input.send_keys(Keys.RETURN)

# time.sleep(2)
driver.quit()
