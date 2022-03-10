from crawl.init_driver import initDriver
from utils.utils import writeFile, readFile
from selenium.webdriver.common.keys import Keys

driver = initDriver()


def crawl_url(url_channel, name_channel):
    driver.get(url_channel)
    i = 0
    while True:
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        i += 1
        if i == 100:
            break
    lst_url = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for url in lst_url:
        writeFile(f'data/data_url/{name_channel}.txt', url.get_attribute('href'))


if __name__ == '__main__':
    dict_channel = {
        'anhtu': 'https://www.youtube.com/c/MCAnhT%C3%BA/videos',
        'batien': 'https://www.youtube.com/c/B%C3%A1Ti%E1%BA%BFnVlog/videos',
        'nguyenhuy': 'https://www.youtube.com/channel/UClNgiM5phXLHyI3FREPIpZA/videos',
        'thanhmai': 'https://www.youtube.com/channel/UCPy7wx2x-OUL4YkaWbYRyIg/videos',
        'thuyhatruyen': 'https://www.youtube.com/c/Th%C3%BAyH%C3%A0Truy%E1%BB%87nAudioTH/videos',
        'truyendinhsoan': 'https://www.youtube.com/c/Truy%E1%BB%87n%C4%90%C3%ACnhSo%E1%BA%A1n/videos'
    }
    for k, v in dict_channel.items():
        crawl_url(v, k)
