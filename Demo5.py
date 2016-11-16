
import requests

url = 'http://www.photophoto.cn/'
# respond = requests.get(url='http://img36.photophoto.cn/20150902/0017030052685519_s.jpg', stream=True)
# print(respond.iter_lines(chunk_size=1024,delimiter=))
imgUrl = 'http://img36.photophoto.cn/20150902/0017030052685519_s.jpg'


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
    downloadImageFile('http://img36.photophoto.cn/20150902/0017030052685519_s.jpg')