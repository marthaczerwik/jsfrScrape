import urllib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.fakepersongenerator.com/Index/generate')
with open('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/testUsers.txt', 'w') as newFile:
    newFile.close()
with open('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/testUsers.txt', 'a') as testUsers:

    for x in range(0, 5):
        sleep(2)
        fullName = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div[1]/p/b').text
        firstName = str(fullName).split(" ")[0]
        lastName = str(fullName).split(" ")[-1]
        emailAddress = str(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/input').get_attribute('value'))
        username = str(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[9]/div[2]/p').text).split("\n")[0]
        password = str(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[9]/div[4]/p').text)
        bday = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div[2]/p[3]/b[1]').text
        day = str(bday).split("/")[1]
        month = str(bday).split("/")[0]
        year = str(bday).split("/")[-1]
        birthday = (year + "-" + month + "-" + day)
        address = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div[2]/p[5]/b').text
        city = str(address).split(",")[0]
        provOrState = str(address).split(",")[1]
        country = str(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[11]/div[14]/input').get_attribute('value'))
        gender = str(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div[2]/p[1]/b').text)
        photo = ('justfriends_images/profilepic' + str(x) + '.png')

        with open('C:/ECLIPSE-WORKSPACE/JustFriends/WebContent/images/profilepic' + str(x) + '.png', 'wb') as file:
            file.write(driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/div[3]/div[1]/div/div[1]/div/img').screenshot_as_png)

        testData = str('\n' + firstName + '\t' + lastName + '\t' + emailAddress + '\t' + username + '\t' + password + '\t' + birthday + '\t' +
                        city + '\t' + provOrState + '\t' + country + '\t' + gender + '\t' + photo + '\t')
        testUsers.write(testData)


        driver.find_element_by_xpath('//*[@id="generate"]').click()

    #remove empty line at the end of the txt file
    lines = testData.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]

    testData = ""
    for line in non_empty_lines:
        testData += line + "\n"

    driver.close()

