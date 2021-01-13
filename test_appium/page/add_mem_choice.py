
from test_appium.page.add_mem import AddMember
from test_appium.page.base_page import BasePage


class AddMemberChoice(BasePage):

    def manual_add_member(self):
        '''点击手动添加成员'''
        self.steps('../page/addmc_goto_addmem.yaml')
        return AddMember(self._driver)
