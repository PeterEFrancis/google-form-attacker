import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

print('\n\n  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n________ GOOGLE FORM ATTACKER ________\n\n')

# open log.txt and get total
f = open('log.txt')
total = int(f.readlines()[0])
f.close()

print('Loaded previous attacks. \n\n')

# set number of attacks and URL
attacks = int(input("Input the number of submissions you would like to attempt: "))
goal = attacks + total
attempt = 0
base = input('Input the base URL: ')
if base[0:30] != 'https://docs.google.com/forms/':
    print('\nNot a valid URL.')
    base = input('Input the base URL: ')

form = base + '/viewform'
response = base + '/formResponse'

# Open the driver and webpage
browser = webdriver.Safari()
# wait = WebDriverWait(browser, 10)

# Display that attacks have started and which have happened
print(f"\n \n Attacks have started. \n \n")

time.sleep(1)

while total < goal:
    try:
        browser.get(form)

        # Click the right selection
        browser.find_elements_by_class_name('quantumWizTogglePaperradioOffRadio')[0].click()

        # Click the submit
        browser.find_element_by_class_name('quantumWizButtonPaperbuttonFlat').click()

        # wait for redirect
        # time.sleep(1)
        # wait.until(EC.url_to_be(response))

        # Click 'submit another'
        # browser.find_elements_by_tag_name('a')[0].click()

        # wait for redirect
        # wait.until(EC.url_to_be(form))



        # increment, feedback, and write to log
        # total += 1
        # print(f'Completed: {total} ({attempt+1}/{attacks})', end="\r")
        #
        # # update log.txt
        # with open('log.txt', 'w') as f:
        #     f.write(str(total))
        # f.close()
        # attempt += 1
    except selenium.common.exceptions.TimeoutException:
        browser.close()
        # Open the driver and webpage
        browser = webdriver.Safari()
        browser.get(form)
        wait = WebDriverWait(browser, 10)




print(f'\n\n {attacks} Attacks have finished successfully!')

browser.close()
