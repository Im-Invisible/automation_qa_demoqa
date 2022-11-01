import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage
from generator.generator import generated_color


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first': {'title': self.locators.SECTION_HEADING_ONE,
                               'content': self.locators.SECTION_CONTENT_ONE},
                     'second': {'title': self.locators.SECTION_HEADING_TWO,
                                'content': self.locators.SECTION_CONTENT_TWO},
                     'third': {'title': self.locators.SECTION_HEADING_THREE,
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


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multiple(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multiple = self.element_is_clickable(self.locators.MULTIPLE_INPUT)
            input_multiple.send_keys(color)
            input_multiple.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multiple(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTIPLE_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.DELETE_MULTIPLE_VALUE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTIPLE_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multiple(self):
        color_list = self.elements_are_present(self.locators.MULTIPLE_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text
