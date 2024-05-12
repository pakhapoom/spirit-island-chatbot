from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


XPATH = "xpath"


class Scraper:
    def __init__(
        self, 
        wait_duration: int = 5,
    ) -> None:
        self._init_webdriver()
        self._init_waitdriver(wait_duration)

    def scrape(
        self, 
        url: str,
        target_xpath: str,
    ) -> WebElement:
        self.driver.get(url)
        self.scroll_down()
        self.activate_wait_driver(target_xpath)
        element = self.get_element_by_xpath(target_xpath)
        return element

    def _init_webdriver(self) -> None:
        service = webdriver.ChromeService(
            executable_path=ChromeDriverManager().install()
        )
        self.driver = webdriver.Chrome(service=service)

    def _init_waitdriver(
        self,
        wait_duration: int = 5,
    ) -> None:
        self.wait_driver = WebDriverWait(self.driver, wait_duration)

    def activate_wait_driver(
        self,
        target_xpath: str,
    ) -> None:
        self.wait_driver.until(
            EC.visibility_of_element_located((
                By.XPATH, target_xpath,
            ))
        )

    def get_element_by_xpath(
        self,
        target_xpath: str,
    ) -> WebElement:
        element = self.driver.find_element(
            By.XPATH,
            target_xpath,
        )
        return element

    def scroll_down(
        self,
        y: str | float = "document.body.scrollHeight",
    ) -> None:
        self.driver.execute_script(
            f"window.scrollTo(0, {y});"
        )

    def terminate(self) -> None:
        self.driver.close()
