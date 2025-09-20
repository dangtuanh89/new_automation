from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage

class VacancyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.add_vacancy = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']")
        self.vacancy_name = (By.XPATH, "//label[text()='Vacancy Name']/following::input[1]")
        self.select_job_box = (By.XPATH, "//label[text()='Job Title']/following::div[contains(@class,'oxd-select-wrapper')][1]")
        self.select_hiring_manager_dropbox = (By.XPATH, "//label[text()='Job Title']/following::div[contains(@class,'oxd-select-wrapper')][3]")
        self.job_title = (By.XPATH, "//div[@class='oxd-select-wrapper']//span[text()='Automaton Tester']")
        self.decription = (By.XPATH, "//textarea[@placeholder='Type description here']")
        self.hiring_manager_input_box = (By.XPATH, "//input[@placeholder='Type for hints...']")
        
        self.current_login_user = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
        self.number_of_positions = (By.XPATH, "//label[text()='Number of Positions']/following::input[1]")
        self.save_button = (By.XPATH, "//button[text()=' Save ']")
        self.edit_vacancy = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']")
        self.active_switch = (By.XPATH, "//p[text()='Active']/following::span[contains(@class,'oxd-switch-input')][1]")
        self.active_input = (By.XPATH, "//p[text()='Active']/following::input[1]")
        self.publish_switch = (By.XPATH, "//p[text()='Publish in RSS Feed and Web Page']/following::span[contains(@class,'oxd-switch-input')][1]")
        self.publish_input = (By.XPATH, "//p[text()='Publish in RSS Feed and Web Page']/following::input[1]")
        self.search_btn = (By.XPATH, "//button[text()=' Search ']")
        self.record_found = (By.XPATH, "//span[text()='No Records Found']")

        self.actual_vacancy_name_path = (By.XPATH, "//div[@class = 'oxd-table-body']//div[@role = 'row'][1]//div[@role = 'cell'][2]")
        self.actual_job_title = self.actual_hiring_manager_path = (By.XPATH, "//div[@class = 'oxd-table-body']//div[@role = 'row'][1]//div[@role = 'cell'][2]")
        self.actual_hiring_manager_path = (By.XPATH, "//div[@class = 'oxd-table-body']//div[@role = 'row'][1]//div[@role = 'cell'][4]")
        self.logout_text = (By.XPATH, "//a[text () = 'Logout']")
    
    def confirm_navigate_to_vacancy_page(self):
        add_btn = self.get_element(self.add_btn)
        return add_btn.is_displayed()

    def click_add_btn(self):
        self.get_element(self.add_btn).click()
        add_vacancy = self.get_element(self.add_vacancy)
        return add_vacancy.is_displayed()

    def input_vacancy_data(self, vacancy_name_value, description_value, number_of_positions_value):
        self.get_element(self.vacancy_name).send_keys(vacancy_name_value)
        self.get_element(self.select_job_box).click()
        job_title_element = self.get_element(self.job_title)
        #arguments[0]: là đối số đầu tiên truyền vào JavaScript từ Python. Trong trường hợp này chính là job_title_element
        #.scrollIntoView(): là một hàm DOM chuẩn của JavaScript, giúp cuộn trình duyệt để đưa phần tử vào vùng hiển thị (viewport).
        #vì các tùy chọn nằm trong span không thể click trực tiếp được nên cần dùng java script execute_script để click
        self.driver.execute_script("arguments[0].scrollIntoView();", job_title_element) 
        job_title_element.click()

        self.get_element(self.decription).send_keys(description_value)

        current_login_user_name = self.get_element(self.current_login_user).text
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_element(self.hiring_manager_input_box))
        actions.click()
        actions.send_keys(current_login_user_name)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        self.get_element(self.number_of_positions).send_keys(number_of_positions_value)

    def set_active(self, expected = False):
        if self.get_element(self.active_input).is_selected() != expected:
            self.js_click(self.active_switch)

    def set_publish(self, expected = True):
        if self.get_element(self.publish_input).is_selected() != expected:
            self.js_click(self.publish_switch)

    def is_active_selected(self):
        return self.get_element(self.active_input).is_selected()
       
    def is_publish_selected(self):
        return self.get_element(self.publish_input).is_selected()
        

    def click_save_btn(self):
        self.get_element(self.save_button).click()

    def confirm_navigate_to_edit_page(self):
        edit_vacancy = self.get_element(self.edit_vacancy)
        return edit_vacancy.is_displayed() 
    
    def search_job(self):
        self.get_element(self.select_job_box).click()
        self.js_click(self.job_title)

        self.get_element(self.select_hiring_manager_dropbox).click()
        hiring_manager_option = (By.XPATH, f"//span[text()='{self.get_element(self.current_login_user).text}']")
        self.js_click(hiring_manager_option)

    def click_search(self):
        self.get_element(self.search_btn).click()
    
    def verify_records_found(self):
        try:
            rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
            if len(rows) >0:
                print(f'Có {len(rows)} dòng kết quả được tìm thấy')
                return True
            else:
                print('No Records Found')
                return False
        except Exception as e:
            print(f'Lỗi khi kiểm tra kết quả tìm kiếm: {e}')
            return False

    def log_out(self):
        self.get_element(self.current_login_user).click()
        self.get_element(self.logout_text).click()

    def confirm_logout(self):
        self.username = (By.XPATH, "//input[@name='username']")
        return self.get_element(self.username).is_displayed()
        
        
    '''
    def verify_data(self, expected_vacancy, expected_job_title):
        try:
            actual_vacancy = self.get_element(self.actual_vacancy_name_path).text
            actual_job_title = self.get_element(self.actual_job_title).text
            actual_hiring_manager = self.get_element(self.actual_hiring_manager_path).text
            current_login_user_name = self.get_element(self.current_login_user)

            assert expected_vacancy == actual_vacancy, f'Vacancy name does not match. Expected: {expected_vacancy}, Found: {actual_vacancy}'
            assert expected_job_title == actual_job_title, f'Job title does not match. Expected: {expected_job_title}, Found: {actual_job_title}'
            assert current_login_user_name == actual_hiring_manager, f'Hirring manager does not match. Expected: {current_login_user_name}, Found: {actual_hiring_manager}'
            print("Search results verified successfully!")
            return True

        except Exception as e:
            print(f"Error verifying search results: {e}")
            return False
    '''







    




