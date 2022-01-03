from typing import Any


class NewsItem:
    def __init__(self, **kwargs):
        self.url = kwargs.get('url', "")
        self.title = kwargs.get('title', "")
        self.sub_title = kwargs.get('sub_title', "")
        self.lead = kwargs.get('lead', "")
        self.thumbnail = kwargs.get('thumbnail', "")
        self.image = kwargs.get('image', "")
        self.other_images = kwargs.get('other_images', [])
        self.body = kwargs.get('body', "")
        self.videos = kwargs.get('videos', [])
        self.tags = kwargs.get('tags', [])
        self.content = kwargs.get('content', "")
        self.images_local_address = kwargs.get('address', [])
