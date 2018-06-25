# reference: http://icrawler.readthedocs.io/en/latest/usage.html

from icrawler.builtin import GoogleImageCrawler
import os

dataset_base_dir = 'D:/Workspace/Dataset/fake_image_detection/task_2'
keyword_lists = ['snapchat face swap', 'MSQRD']

for keyword in keyword_lists:

    folder_path = dataset_base_dir + '/' + keyword
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(folder_path + ' is created!')
    else:
        pass

    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': folder_path})

    keyword_comma = keyword.replace(' ', ',')
    google_crawler.crawl(keyword=keyword, max_num=10000)

    print('Crawling ' + keyword + ' is done')


# ()()
# ('')HAANJU.YOO
