# Info here http://www.soda-pro.com/help/cams-services/cams-radiation-service/automatic-access

import requests


def download(lat, lon, start_date, end_date, email):
    url = (
        f"http://www.soda-is.com/service/wps?"  # alternative: pro.soda-is.com
        f"Service=WPS&"
        f"Request=Execute&"
        f"Identifier=get_cams_radiation&"
        f"version=1.0.0&"
        f"DataInputs="
        f"latitude={lat};"
        f"longitude={lon};"
        f"altitude=-999;"
        f"date_begin={start_date};"
        f"date_end={end_date};"
        f"time_ref=UT;"
        f"summarization=PT01M;"
        f"verbose=true;"
        f"username={email.replace('@','%2540')}&"
        f"RawDataOutput=irradiation"
    )
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f"{lat}_{lon}_{start_date}_{end_date}.csv", 'wb') as f:
            f.write(resp.content)
    else:
        print(resp.status_code)


download(44.083, 5.059, "2017-01-01", "2017-01-05", "YourEmail@mail.com")
