import sys
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

MAX_HANDLE_ATTEMPTS = 1000  # Set how many users you want to scrape
MINIMUM_FOLLOWER_COUNT = 5  # Min number of followers user needs to have for scraper to check

IG_USERNAME = 'yourUsername' # Enter your IG username
IG_PASSWORD = 'yourPassword' # Enter your IG password

def get_tags():
    tags = []
    with open('./tags', 'r') as f:
        for line in f:
            tags.append(line.strip())

    return tags


def get_userProfiles():
    userProfiles = []
    with open('./userProfiles', 'r') as f:
        for line in f:
            d = {
                'handle': line.split(',')[0].strip(),
                'name': line.split(',')[1].strip()
            }
            userProfiles.append(d)

    return userProfiles


def save_userProfile(handle, name):
    userProfiles = get_userProfiles()
    name = name.replace(',', ' ')  # Remove commas
    name = name.encode('ascii', 'ignore').decode('ascii').strip()  # Remove any special characters
    if any(handle == userProfile['handle'] for userProfile in userProfiles):
        print('  -> Already saved this profile before [{}]'.format(handle))
        return

    with open('./userProfiles', 'a') as f:
        f.write('{},{}\n'.format(handle, name))

    print('  -> Saved <{}, {}>'.format(handle, name))


def parse_follower_count(text):
    text = text.replace(' followers', '')
    text = text.replace(',', '')
    text = text.replace('.', '')

    if 'k' in text:
        text = int(text.replace('k', '')) * 100
    else:
        text = int(text)

    return text


def scrape():
    try:
        tags = get_tags()
        handle_attempts = 0

        options = Options()
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'pathToYourChromeDriver')

        # Login to your IG account
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        username = driver.find_element_by_xpath("//input[@name='username']").send_keys(IG_USERNAME)
        time.sleep(1)
        password = driver.find_element_by_xpath("//input[@name='password']").send_keys(IG_PASSWORD)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)

        # Scrape by hashtags
        for tag in tags:
            print('Scraping by hashtag "{}"'.format(tag))
            posts = []
            driver.get('https://www.instagram.com/explore/tags/{}/'.format(tag))

            elems = driver.find_elements_by_xpath("//a[@href]")
            for elem in elems:
                if '/p/' in elem.get_attribute("href"):
                    posts.append(elem.get_attribute("href"))

            print('Found {} posts'.format(len(posts)))

            for post in posts:
                try:
                    name = ''
                    handle_attempts += 1
                    driver.get(post)
                    elems = driver.find_elements_by_xpath("//a[@title]")
                    handle = elems[0].get_attribute("title")

                    print('Inspecting handle {}'.format(handle))
                    driver.get('https://www.instagram.com/{}/'.format(handle))

                    # Scrape name
                    try:
                        elems = driver.find_elements_by_xpath("//h1")
                        name = elems[1].text
                    except Exception:
                        print('Name not found.')

                    # Scrape follower count
                    try:
                        elems = driver.find_elements_by_partial_link_text('followers')
                        if parse_follower_count(elems[0].text) < MINIMUM_FOLLOWER_COUNT:
                            print('  -> Not enough followers [{}]'.format(elems[0].text))
                            continue
                    except Exception:
                        print('No follower count found.')

                    save_userProfile(handle, name)

                    if handle_attempts > MAX_HANDLE_ATTEMPTS:
                        sys.exit('Max attempts reached')

                    time.sleep(random.choice(range(1, 5)))
                except Exception as e:
                    print(e)


    except Exception as e:
        print(e)
    finally:
        driver.quit()


if __name__ == '__main__':
    scrape()