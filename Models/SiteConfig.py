class SiteConfig:
    def __init__(self, **kwargs):
        self.settings = kwargs.get('settings', {})

    def get_settings(self):
        return self.settings

    def __get_setting(self, key):
        return self.settings.get(key)

    def __add_setting(self, name, value):
        self.settings[name] = value

    def set_settings(self, settings):
        self.settings = settings
        return self

    def set_base_url(self, base_url):
        self.__add_setting('base_url', base_url)
        return self

    def set_news_box_selector(self, selector):
        self.__add_setting('news_box_selector', selector)
        return self

    def set_news_item_selector(self, selector):
        self.__add_setting('news_item_selector', selector)
        return self

    def set_news_title_selector(self, selector):
        self.__add_setting('news_title_selector', selector)
        return self

    def set_news_sub_title_selector(self, selector):
        self.__add_setting('news_sub_title_selector', selector)
        return self

    def set_news_link_selector(self, selector):
        self.__add_setting('news_link_selector', selector)
        return self

    def set_news_lead_selector(self, selector):
        self.__add_setting('news_lead_selector', selector)
        return self

    def set_news_thumbnail_selector(self, selector):
        return self.__add_setting('news_thumbnail_selector', selector)

    def set_news_image_selector(self, selector):
        self.__add_setting('news_image_selector', selector)
        return self

    def set_news_other_images_selector(self, selector):
        self.__add_setting('news_other_images_selector', selector)
        return self

    def set_news_body_selector(self, selector):
        self.__add_setting('news_body_selector', selector)
        return self

    def set_news_videos_selector(self, selector):
        self.__add_setting('news_videos_selector', selector)
        return self

    def set_news_tags_selector(self, selector):
        self.__add_setting('news_tags_selector', selector)
        return self

    def set_news_content_selector(self, selector):
        self.__add_setting('news_content_selector', selector)
        return self

    # getters
    def get_base_url(self):
        return self.__get_setting('base_url')

    def get_news_box_selector(self):
        return self.__get_setting('news_box_selector')

    def get_news_item_selector(self):
        return self.__get_setting('news_item_selector')

    def get_news_title_selector(self):
        return self.__get_setting('news_title_selector')

    def get_news_sub_title_selector(self):
        return self.__get_setting('news_sub_title_selector')

    def get_news_link_selector(self):
        return self.__get_setting('news_link_selector')

    def get_news_lead_selector(self):
        return self.__get_setting('news_lead_selector')

    def get_news_thumbnail_selector(self):
        return self.__get_setting('news_thumbnail_selector')

    def get_news_image_selector(self):
        return self.__get_setting('news_image_selector')

    def get_news_other_images_selector(self):
        return self.__get_setting('news_other_images_selector')

    def get_news_body_selector(self):
        return self.__get_setting('news_body_selector')

    def get_news_videos_selector(self):
        return self.__get_setting('news_videos_selector')

    def get_news_tags_selector(self):
        return self.__get_setting('news_tags_selector')

    def get_news_content_selector(self):
        return self.__get_setting('news_content_selector')

    # def get_news_images_local_address(self):
    #     return self.__get_setting('news_images_local_address')
