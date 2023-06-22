import png
import requests
import json

## https://docs.python-requests.org/en/latest/user/advanced/#session-objects
## https://stackoverflow.com/a/45684352/4493036
## https://absarcs.info/how-to/call-pixiv-api-curl/
def get_img_from_url(url, referer=None):
    with requests.Session() as s:
        if referer:
            s.headers.update({'referer': referer})
        req = s.get(url, stream=True)

    return req.raw


def main():
    url = 'https://i.pximg.net/img-original/img/2023/06/23/03/30/09/109257097_p0.png'
    with open('referers.json', 'r') as ref_file:
        referers = json.load(ref_file)
        
    f = get_img_from_url(url, referer=referers['pixiv'])
    r = png.Reader(file=f)
    cs = r.chunks()

    chunk_dict = dict(cs)
    # print(chunk_dict.keys())
    # print(chunk_dict[b'iTXt'])


if __name__=='__main__':
    main()