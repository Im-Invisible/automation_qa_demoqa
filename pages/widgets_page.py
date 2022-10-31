from selenium.common import TimeoutException
from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_HEADING_ONE,
                          'content': self.locators.SECTION_CONTENT_ONE},
                     'second':
                         {'title': self.locators.SECTION_HEADING_TWO,
                          'content': self.locators.SECTION_CONTENT_TWO},
                     'third':
                         {'title': self.locators.SECTION_HEADING_THREE,
                          'content': self.locators.SECTION_CONTENT_THREE},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]
