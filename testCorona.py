import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree as Et



@pytest.fixture(params=["chrome","Edge"],scope="function")
def get_browser(request):

    if request.param == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    if request.param == "Edge":
        driver = webdriver.Edge()

    # driver.get("https://he.wikipedia.org/wiki/%D7%9E%D7%92%D7%A4%D7%AA_%D7%94%D7%A7%D7%95%D7%A8%D7%95%D7%A0%D7%94_%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C")
    yield driver
    driver.quit()

def test_url(get_browser):

    driver = get_browser
    driver.get("https://www.wikipedia.org/")
    root = Et.parse('C:\portland\\Corona\config_corona_ex').getroot()
    title = root.find("title").text
    print(title + "eeeeeeeeeeeeeee")
    assert (driver.title == title)


def test_title(get_browser):
    driver = get_browser
    driver.get("https://www.wikipedia.org/")
    root = Et.parse('C:\portland\\Corona\config_corona_ex').getroot()
    url = root.find("url").text
    url2 = driver.current_url
    driver.close()
    assert (url2 == url)

def test_data(get_browser):
    driver = get_browser
    driver.get(
        "https://he.wikipedia.org/wiki/%D7%9E%D7%92%D7%A4%D7%AA_%D7%94%D7%A7%D7%95%D7%A8%D7%95%D7%A0%D7%94_%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C")
    driver.implicitly_wait(10)
    num1 = \
    driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[7]/td/small[1]').text.split(" ")[
        3]
    driver.get("https://datadashboard.health.gov.il/COVID-19/general")
    driver.implicitly_wait(10)
    num2 = driver.find_element_by_xpath(
        '/html/body/ngx-app/ngx-pages/nb-layout/div[1]/div/div/div/div/nb-layout-column/ngx-general/section[1]/div/ngx-tile-wrapper[2]/ngx-doughnut-pie-statistic/nb-card/ngx-small-statistics-info/div/div[1]/h4').text
    assert (num1 == num2)

