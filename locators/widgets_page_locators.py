from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_HEADING_ONE = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_CONTENT_ONE = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_HEADING_TWO = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_CONTENT_TWO = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_HEADING_THREE = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_CONTENT_THREE = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTIPLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTIPLE_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    DELETE_MULTIPLE_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
