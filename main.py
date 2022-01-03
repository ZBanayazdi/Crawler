from Models.SiteConfig import SiteConfig
from NewsCrawler.NewsCrawler import NewsCrawler
from Downloader import Downloader

farsnews = SiteConfig().set_base_url("https://www.farsnews.ir/")

farsnews.set_news_box_selector('.top-middle-news.news-list')
farsnews.set_news_item_selector('ul>li')
farsnews.set_news_title_selector("h3>a")
farsnews.set_news_link_selector("")
farsnews.set_news_sub_title_selector("h4>a")
farsnews.set_news_thumbnail_selector("img.lazyimage")

farsnews.set_news_body_selector('.news-box')
farsnews.set_news_lead_selector("h1+p")
farsnews.set_news_image_selector('figure>img')
farsnews.set_news_other_images_selector('p>img')
farsnews.set_news_videos_selector('video>source')
farsnews.set_news_tags_selector('.tags>a')
farsnews.set_news_content_selector('.nt-body')

newsCrawler = NewsCrawler(farsnews)
newsData = newsCrawler.crawler()

downloader = Downloader(newsData)
downloader.download()
