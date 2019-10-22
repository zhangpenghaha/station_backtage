from selenium import webdriver


class InitDriver():
    # 定义类属性保存驱动对象
    # 定义标记,判断是否需要退出驱动对象
    _driver = None

    # 定义标记,判断是否需要退出驱动对象
    _auto_quit = True

    # 获取浏览器驱动对象  类方法
    @classmethod
    def get_driver( cls ):
        # 判断_driver中是否存有驱动,如果没有实例化一个保存在_driver中
        # 返回_driver中的驱动对象
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(20)
            # cls._driver.get("http://192.168.2.63:8082/#/rule")
        return cls._driver



    # 退出浏览器驱动对象 类方法
    @classmethod
    def quit_driver(cls):
        # 如果_driver属性中有驱动对象,退出驱动对象-重置为None
        if cls._auto_quit and cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
    # 手动设置自动退出
    @classmethod
    def set_auto_quit(cls, auto_quit):
        cls._auto_quit = auto_quit
