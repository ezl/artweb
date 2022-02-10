from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from sms2url.models import Url
import logging

class google():

    def search(msg_id, url):

        # Init web driver
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

        # Send http request
        driver.get("https://www.google.com/searchbyimage?image_url=" + url)

        # Set variables
        position = 1
        message = ""

        # Go through tags
        tags = driver.find_elements(By.CLASS_NAME, 'yuRUbf')
        for tag in tags:
            parts = tag.text.split("\n")
            if len(parts) < 2:
                continue
            elif str(parts[0]).strip().startswith("http"):
                continue

            # Add url
            u = Url(
                message_id = msg_id,
                position = position,
                title = parts[0],
                url = parts[1]
            )
            u.save()

            ## Update variables
            position = position + 1
            message = message + "\n\nTitle: " + parts[0] + "\nURL: " + parts[1]

        # Return
        return message


