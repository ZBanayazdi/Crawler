from Models.NewsItem import NewsItem
from Models.SiteConfig import SiteConfig
import helpers


#
# def crawl(soup, selectors, counter):
#     for each in soup:
#         if selectors[counter]:
#             selected_part = soup_selector(each, selectors[counter])
#
#             counter += 1
#             if counter < len(selectors):
#                 crawl(selected_part, selectors[counter], counter)
#                 news_item = NewsItem()
#                 if len(selected_part):
#                     print(selected_part[0])


class NewsCrawler:

    def __init__(self, site_config: SiteConfig, **kwargs):
        self.news_items = []
        self.site_config = site_config

    def main_page_info_extractor(self, item):
        news_item = NewsItem()
        if self.site_config.get_news_title_selector():
            title = item.select(self.site_config.get_news_title_selector())
            if len(title):
                news_item.title = title[0].text
        if self.site_config.get_news_link_selector():
            link = item.select(self.site_config.get_news_link_selector())
            if len(link):
                news_item.url = self.site_config.get_base_url() + link[0].get('href')
        else:
            if self.site_config.get_news_title_selector():
                link = item.select(self.site_config.get_news_title_selector())
                if len(link):
                    news_item.url = self.site_config.get_base_url() + link[0].get('href')
        if self.site_config.get_news_sub_title_selector():
            sub_title = item.select(self.site_config.get_news_sub_title_selector())
            if len(sub_title):
                news_item.sub_title = sub_title[0].text
        if self.site_config.get_news_thumbnail_selector():
            img = item.select(self.site_config.get_news_thumbnail_selector())
            if len(img):
                news_item.thumbnail = img[0].get('src')

        return news_item

    def news_info_extractor(self, news_item):
        news_dom = helpers.crawl_request(news_item.url)
        news_body = news_dom.select(self.site_config.get_news_body_selector())

        for body in news_body:
            lead = body.select(self.site_config.get_news_lead_selector())
            news_item.lead = lead[0].text

            image = body.select(self.site_config.get_news_image_selector())
            print(image)
            if image[0].get('src')!='':
                news_item.image = image[0].get('src')

            other_images = body.select(self.site_config.get_news_other_images_selector())
            for img in other_images:
                news_item.other_images.append(img.get('src'))

            videos = body.select(self.site_config.get_news_videos_selector())
            for video in videos:
                news_item.videos.append(video.get('src'))

            tags = body.select(self.site_config.get_news_tags_selector())
            for tag in tags:
                temp_tags = tag.get('href')
                news_item.tags.append(temp_tags.split('/')[2])

            content = body.select(self.site_config.get_news_content_selector())
            news_item.content = content[0].text

        return news_item

    def crawler(self):

        main_dom = helpers.crawl_request(self.site_config.get_base_url())
        news_box = main_dom.select(self.site_config.get_news_box_selector())

        for box in news_box:
            news = box.select(self.site_config.get_news_item_selector())
            for item in news:
                news_item = self.main_page_info_extractor(item)
                news_item = self.news_info_extractor(news_item)

                # add to array
                self.news_items.append(news_item)

        self.__get_all_news_body(self.news_items)
        return self.news_items

    def __get_all_news_body(self, news_items):
        pass
