from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
import calendar

# Встановлюємо поточну дату та час
now = datetime.now()
weekday = calendar.day_name[now.weekday()]
hour = now.hour

# Перевіряємо, чи будній день та чи ми відповідаємо годині запуску
if weekday in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] and hour in range(9, 18):
    # Запускаємо браузер та відкриваємо сторінку hurma
    driver = webdriver.Chrome()
    driver.get("https://m2eteam.hurma.work/")

    # Логінимось на сайті

    email_input = driver.find_element(By.CLASS_NAME, 'login-form_login')
    email_input.send_keys("d.borodaikevych@m2e.team")

    password_input = driver.find_element(By.CLASS_NAME, 'login-form_password')
    password_input.send_keys("9mOL1ank")

    submit_button = driver.find_element(By.CLASS_NAME, 'login-form__signIn')
    submit_button.click()
    
    #максимізуємо розмір вікна браузера
    driver.maximize_window()

    # Чекаємо 10 секунд на завантаження сторінки
    time.sleep(10)

    # Клікаємо на кнопку "Старт"
    #start_button = driver.find_element_by_id("start")
    #start_button.click()

    # Чекаємо 9 годин
    #time.sleep(9*60*60)

    # Клікаємо на кнопку "Стоп" header-stop-button js__timetracking_stop
    stop_button = driver.find_element(By.CLASS_NAME, 'js__timetracking_stop')
    stop_button.click()
    time.sleep(10)
    # Закриваємо браузер
    #driver.quit()
