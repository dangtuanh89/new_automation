import json
import os

class ConfigReader: #Tạo class ConfigReader để quản lý việc đọc cấu hình
    # Biến class (class variable) để lưu trữ dữ liệu config, khởi tạo là None 
    # Dấu _ ở đầu biến thể hiện đây là biến private (nội bộ)
    _config = None 
    
    @staticmethod # Decorator cho phép gọi method mà không cần tạo instance của class
    def load_config(): # Method để tải cấu hình từ file JSON
        if ConfigReader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'testsetting.json')
            with open(config_path, 'r') as file: #Mở file JSON với context manager (with)
                ConfigReader._config = json.load(file) #json.load(file): Đọc và parse nội dung JSON thành Python dictionary, lưu vào biến class _config
        return ConfigReader._config #Trả về dữ liệu config đã được load
    
    @staticmethod
    def get_base_url():
        return ConfigReader.load_config()['base_url']
    
    @staticmethod
    def get_username():
        return ConfigReader.load_config()['credentials']['username']
    
    @staticmethod
    def get_password():
        return ConfigReader.load_config()['credentials']['password']