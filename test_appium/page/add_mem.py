from test_appium.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self,name,phone):
        '''添加成员成功'''
        self._params['{name}'] = name
        self._params['{phone}'] = phone
        self.steps('../page/add_mem.yaml')
        return True