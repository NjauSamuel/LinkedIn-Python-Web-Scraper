# Import libraries and packages for the project 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By

print('- Finish importing packages')

# Task 1: Login to Linkedin

# Task 1.1: Open Chrome and Access Linkedin login site
driver = webdriver.Chrome()
sleep(3)
url = 'https://www.linkedin.com/login'
driver.get(url)
print('- Finish initializing a driver')
sleep(5)

# Task 1.2: Import username and password
credential = open('credentials.txt')
line = credential.readlines()
username = line[0]
password = line[1]
print('- Finish importing the login credentials')
sleep(2)

# Task 1.2: Key in login credentials
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(username)
print('- Finished keying in email')
sleep(3)

password_field = driver.find_element(By.NAME, 'session_password')
password_field.send_keys(password)
print('- Finish keying in password')
sleep(2)

# Task 1.2: Click the Login button // No longer needed Linked in automatically logs in.
# signin_field = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
# signin_field.click()
# sleep(3)

print('- Finish Task 1: Login to Linkedin')

sleep(10)
# Task 2: Search for the profile we want to crawl
# Task 2.1: Locate the search bar element
search_field = driver.find_element(By.XPATH, '//input[contains(@class, "search-global-typeahead__input")]')

# Task 2.2: Input the search query to the search bar
search_query = input('What profile do you want to scrape? ')
search_field.send_keys(search_query)

# Task 2.3: Search
search_field.send_keys(Keys.RETURN)

print('- Finish Task 2: Search for profiles')


# Task 3: Scrape the URLs of the profiles
# Task 3.1: Write a function to extract the URLs of one page
def GetURL():
    page_source = BeautifulSoup(driver.page_source, features="lxml")
    profiles = page_source.find_all('a', class_='app-aware-link')  # ('a', class_ = 'search-result__result-link
    # ember-view')
    all_profile_URL = []
    for profile in profiles:
        # profile_ID = profile.get('href')
        # profile_URL = "https://www.linkedin.com" + profile_ID
        profile_URL = profile.get('href')
        if profile_URL not in all_profile_URL:
            all_profile_URL.append(profile_URL)
    return all_profile_URL


# Task 3.2: Navigate through many page, and extract the profile URLs of each page
input_page = int(input('How many pages you want to scrape: '))
URLs_all_page = []
for page in range(input_page):
    URLs_one_page = GetURL()
    sleep(2)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # scroll to the end of the page
    sleep(3)

    # Check if the next button is available and enabled
    try:
        next_button = driver.find_element(By.CLASS_NAME, "artdeco-pagination__button--next")
        if "disabled" in next_button.get_attribute("class"):
            print("No more pages to navigate. Exiting loop.")
            break  # Exit loop if "Next" button is disabled
        driver.execute_script("arguments[0].click();", next_button)
    except Exception as e:
        print(f"Could not find next button: {e}")
        break  # Exit loop if "Next" button is not found or if an error occurs

    URLs_all_page = URLs_all_page + URLs_one_page
    sleep(2)


print('- Finish Task 3: Scrape the URLs')
# Task: Scrape the data of 1 LinkedIn profile, and write only the URLs to a .txt file
with open('output.txt', 'w', newline='') as file_output:
    for linkedin_URL in URLs_all_page:
        driver.get(linkedin_URL)
        print('- Accessing profile: ', linkedin_URL)
        sleep(3)
        page_source = BeautifulSoup(driver.page_source, "html.parser")
        info_div = page_source.find('div', {'class': 'flex-1 mr5'})
        try:
            # Only save the profile URL to the txt file
            file_output.write(linkedin_URL + '\n')
            print(f'--- URL saved: {linkedin_URL}')
        except:
            pass

print('Mission Completed!')
