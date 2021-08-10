import pprint
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


def get_phone_info(number:str) -> dict:
    result = {}
    mynumber = phonenumbers.parse(number)
    result['number'] = number
    result['location'] = geocoder.description_for_number(mynumber, "de")
    provider = phonenumbers.parse(number)
    result['provider'] = carrier.name_for_number(provider, 'de')
    return result


phone_info = get_phone_info('+491738014345')
print(phone_info)

