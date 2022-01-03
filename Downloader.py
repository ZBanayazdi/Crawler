import urllib


class Downloader:
    def __init__(self, news_data):
        self.news_data = news_data
        self.image_name_assigner = 1
        self.thumbnail_name_assigner = 1
        self.other_images_name_assigner = 1
        self.video_name_assigner = 1

    def info_getter(self, url, name):
        urllib.request.urlretrieve(url, name)

    def name_maker(self, directory, prop, name_assigner, url):
        name = directory + "/" + prop + "/" + str(name_assigner) + "." + str(url.split('.')[-1])
        return name

    def download(self):
        for item in self.news_data:
            name = self.name_maker("img", 'thumbnail', self.thumbnail_name_assigner, item.thumbnail)
            self.info_getter(item.thumbnail, name)
            self.thumbnail_name_assigner += 1

            name = self.name_maker("img", 'image', self.image_name_assigner, item.image)
            self.info_getter(item.image, name)
            self.image_name_assigner += 1

            for img in item.other_images:
                name = self.name_maker("img", 'other_images', self.other_images_name_assigner, img)
                self.info_getter(img, name)
                self.other_images_name_assigner += 1

            for video in item.videos:
                name = self.name_maker("video", 'videos', self.video_name_assigner, video)
                self.info_getter(video, name)
                self.video_name_assigner += 1
