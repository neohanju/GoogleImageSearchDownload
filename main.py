# reference: http://icrawler.readthedocs.io/en/latest/usage.html

from icrawler.builtin import GoogleImageCrawler
import os

dataset_base_dir = 'D:/Workspace/Dataset/HJ_Rain'
keyword_lists = ['cloudy street', 'dull weather',
                 'outdoor scene', 'bus stop',
                 'city traffic',
                 'pedestrians', 'town',
                 'village', 'flood',
                 'american football scene', 'baseball play']

for keyword in keyword_lists:

    folder_path = dataset_base_dir + '/' + keyword
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(folder_path + ' is created!')
    else:
        continue

    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': folder_path})

    keyword_comma = keyword.replace(' ', ',')
    google_crawler.crawl(keyword=keyword, max_num=1000,
                         date_min=None, date_max=None,
                         min_size=(200, 200), max_size=None)

    print('Crawling ' + keyword + ' is done')


# ()()
# ('')HAANJU.YOO
