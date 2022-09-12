import klicker


def sbor_inf(id_bank, max_random_value, first_circle,nick_btc):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="side-menu"]/div/div[2]/a[3]/img'))).click()  # click on  купить/продать

    direction_html = '//*[@id="root"]/div[1]/main/div[2]/div[2]/div/div[3]/div[2]'  # on anyway direction to buttons

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, direction_html+'/div[1]/div'))).click()  # click on button list
    if first_circle == false:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, direction_html+'/div[1]/div/div/span[1]'))).click()  # click on button base
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@id="root"]/div[1]/main/div[2]/div[2]/div/div[3]/div[2]/div[1]/div'))).click()# list banks

    first_circle = false
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
        direction_html+'/div[2]/div[' + str(id_bank) + ']'))).click()  # click on  button of bank
    time.sleep(2)
    mark_users = []  #

    for i in range(1, 9):  # search a green mark users
        mark_users.append((driver.find_element(By.XPATH,
            '//*[@id="root"]/div[1]/main/div[2]/div[3]/div/div/div[3]/table/tbody/tr[' +
                str(i) + ']/td[1]/div/div[4]').get_attribute("title")))

    baza = driver.find_elements_by_css_selector(
        'td.MuiTableCell-root.MuiTableCell-body.MuiTableCell-paddingNone')  # search elements
    player = []
    value_user = []
    max_balance = []
    i = 0
    for elements in baza:  # sorted elements
        if i % 5 == 0:  # each 5th element is name player
            name = ''
            for k in range(5):
                name = name + elements.text[k]
            player.append(name)
        if i % 5 == 2:  # through one element is value user
            k = 0
            value = ''
            while elements.text[i] != 'R' and elements.text[i] != ',':
                if elements.text[i] != ' ':
                    value = value + elements.text[i]
                k += 1
            value_user.append(value)
        if i % 5 == 3:  # through two element is max balance user
            k = 0
            max_balance = ''
            while elements.text[k] != 'д':
                k += 1
            k += 2
            while elements.text[k] != 'R':
                if elements.text[k] != ' ':
                    max_balance = max_balance + elements.text[k]
                k += 1
            max_balance.append(max_balance)
    i += 1

    our_position = 10  # make our position a bottom
    for element in player:
        if element == nick_btc:
            our_position = player_result.index(nick_btc)

    n = 0
    check_fora = 0  # for search a concurent 0- concurent is not found
    while n < our_position:
        if mark_users[n] == "Верифицированный":
            if int(max_balance[n]) > 10000:
                pass_value = value_user[n]
                n = our_position
                check_fora = 1
        n += 1
    del mark_users, max_balance, value_user, player
    if check_fora == 0:
        print("Мы лидеры")
    else:
        pass_value = int(pass_value) - randint(0, int(max_random_value))
        klicker.klicker(id_bank, pass_value)
