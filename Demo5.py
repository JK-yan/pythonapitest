import re

import requests

url = 'http://www.photophoto.cn/'
# respond = requests.get(url='http://img36.photophoto.cn/20150902/0017030052685519_s.jpg', stream=True)
# print(respond.iter_lines(chunk_size=1024,delimiter=))
imgUrl = 'http://clouds.onlinesjtu.com/mooc/2016_3/computer/856/31.mp4'


def downloadImageFile(imgUrl):
    """下载资源"""
    local_filename = imgUrl.split('/')[-1]
    print("Download Image File=", local_filename)
    r = requests.get(imgUrl, stream=True)  # here we need to set stream = True parameter
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename


if __name__ == '__main__':
    downloadImageFile('ftp://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5MjE5LmR5ZHl0dC5uZXQ6ODE5Ni9bJUU5JTk4JUIzJUU1JTg1JTg5JUU3JTk0JUI1JUU1JUJEJUIxd3d3LnlnZHk4LmNvbV0uJUU1JTg2JTlCJUU3JTgxJUFCJUU4JUI0JUE5LkJELjcyMHAuJUU0JUI4JUFEJUU4JThCJUIxJUU1JThGJThDJUU1JUFEJTk3JUU1JUI5JTk1LnJtdmJaWg==')

    # res = requests.get(
    #     url='http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%BB%C6%BD%F0%CA%A5%D2%C2&fr=ala&ori_query=%E9%BB%84%E9%87%91%E5%9C%A3%E8%A1%A3&ala=0&alatpl=sp&pos=0')
    # # print(res.text)
    # html=res.text
    # r = re.compile(r'http:\/\/.+?\.jpg')
    # # print(html)
    # imglist = r.findall(html)
    # print(imglist)
    # for imgUrl in imglist:
    #     downloadImageFile(imgUrl=imgUrl)
    # for imglist in res.iter_lines():
    #     imglist = r.findall(imglist)
    #     for imgUrl in imglist:
    #         downloadImageFile(imgUrl=imgUrl)