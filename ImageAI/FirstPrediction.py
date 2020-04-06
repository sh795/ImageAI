from PIL import Image

import cloudsight

auth = cloudsight.SimpleAuth('gqPvkvZfv_mAwMO3Kaa9Zw')

api = cloudsight.API(auth)

for x in range(5):
    string = str(x)
    im = Image.open(string + '.jpg')
    im.thumbnail((600, 600))
    im.save(string + 'cloudsight.jpg')
    with open(string + '.jpg', 'rb') as f:
        response = api.image_request(f, string + 'cloudsight.jpg', {'image_request[locale]': 'en-US',})
        status = api.wait(response['token'], timeout=30)

    print(status['name'])