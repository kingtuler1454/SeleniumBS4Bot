
def klicker(id_bank, pass_value):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="side-menu"]/div/div[2]/a[4]/img'))).click()  # клик на мои зявки

    time.sleep(1)
    status_trade = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div[1]/div/span')))

    if status_trade.text != 'Торговля активирована':  # activation a trade
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div[1]/div/label/span').click()
    k = 1
    request = ''
    while request != 'Создать новую заявку':
        try:
            request = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div[3]/div[' + str(
                k) + ']').get_attribute('span')
            k += 1
        except:
            request = 'Создать новую заявку'
            k = k - 2
    l_max = 1
    while l_max <= k:
        type_zav = driver.find_element(By.XPATH,
                                       '//*[@id="root"]/div[1]/main/div[2]/div[3]/div[' + str(l) + ']/div[3]/div/span')
        if type_zav.text == 'Продажа':
            bank_end_name = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div[3]/div[' + str(
                l) + ']/div[5]/div/span/div/span')
            if bank_end_name.text == BANK:
                element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div[3]/div[' + str(
                    l) + ']/div[4]/div/div/span')
                a = element.text
                element.click()
                znach_ster = ''

                for symbol in a:
                    if symbol != ' ' and symbol != 'R' and symbol != 'U' and symbol != 'B':
                        znach_ster = znach_ster + symbol
                element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div[3]/div[' + str(
                    l) + ']/div[4]/div/input')
                element.click()
                for h in range(0, len(znach_ster)):
                    element.send_keys(Keys.BACK_SPACE)
                element.send_keys(pass_value)
                driver.find_element(By.XPATH,
                                    '//*[@id="root"]/div[1]/main/div[2]/div[3]/div[' + str(l) + ']/div[5]/div').click()
                time.sleep(3)
                l_max = k + 1
        l_max += 1