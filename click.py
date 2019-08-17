import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


import time

print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('\n\n                    ________ GOOGLE FORM ATTACKER ________\n\n')

# open log.txt and get total
f = open('log.txt')
total = int(f.readlines()[0])
f.close()

print(f'Loaded {total} previous attacks. \n\n')

# set number of attacks and URL
attacks = int(input("Input the number of submissions you would like to attempt: \n >>> "))
goal = attacks + total
attempt = 0
URL = input('\nInput the form URL: \n >>> ')
while URL[0:30] != 'https://docs.google.com/forms/':
    print('Not a valid URL.')
    URL = input('Input the form URL: \n >>> ')

print('\n\nLoading the Web Driver...\n\n')

# Open the web driver
driver = webdriver.Safari()

# Display that attacks have started
print(f"Attacks have started.\n\n")

while total < goal:
    # open the form
    driver.get(URL)

    # wait for element to load
    # try:
    #     element_present = EC.presence_of_element_located((By.CLASS_NAME, 'quantumWizTogglePaperradioOffRadio'))
    #     WebDriverWait(driver, 10).until(element_present)
    # except selenium.common.exceptions.TimeoutException:
    #     continue
    time.sleep(1)

    # Click the first selection
    driver.find_elements_by_class_name('quantumWizTogglePaperradioOffRadio')[0].click()

    # wait for element to load
    # try:
    #     element_present = EC.presence_of_element_located((By.CLASS_NAME, 'quantumWizButtonPaperbuttonFlat'))
    #     WebDriverWait(driver, 10).until(element_present)
    # except selenium.common.exceptions.TimeoutException:
    #     continue
    time.sleep(1)

    # Click the submit
    driver.find_element_by_class_name('quantumWizButtonPaperbuttonFlat').click()

    # increment, feedback, and write to log
    total += 1
    print(f'Completed: {total} ({attempt+1}/{attacks})', end="\r")

    # update log.txt
    with open('log.txt', 'w') as f:
        f.write(str(total))
    f.close()
    attempt += 1


print(f'\n\n{attacks} Attacks have finished successfully!')

driver.close()
