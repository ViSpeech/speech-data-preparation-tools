from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def initDriver():
    # CHROMEDRIVER_PATH = './chrome'
    WINDOW_SIZE = "860,540"
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--no-sandbox')
    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                        'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                        'notifications': 2, 'auto_select_certificate': 2,
                                                        'fullscreen': 2,
                                                        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                        'media_stream_mic': 2, 'media_stream_camera': 2,
                                                        'protocol_handlers': 2,
                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                        'metro_switch_to_desktop': 2,
                                                        'protected_media_identifier': 2, 'app_banner': 2,
                                                        'site_engagement': 2,
                                                        'durable_storage': 2}}
    # chrome_options.add_experimental_option('prefs', prefs)

    # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
    #                           options=chrome_options
    #                           )
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    return driver