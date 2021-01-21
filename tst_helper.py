import requests
import json


def hex_string(input_string):
    """
    Возвращает HEX-STRING.

    :param str input_string: строка для преобразования в HEX
    :rtype: str
    :return: HEX-STRING
    """

    return ''.join([f'{ord(c):02X}' for c in input_string])


def hex_ip(input_string):
    _hex = hex_string(input_string)
    return '.'.join([str(int(_hex[n:n+2], 16)) for n in range(0,len(_hex),2)])


def mac_from_hexstring(input_data):
    result = input_data.copy()

    for key, value in input_data.items():
        if len(value) == 6:
            converted_value = hex_string(value).lower()
            result[key] = converted_value

    return result




def req_to_api(ip, func):
    url = f'http://192.168.81.130:7577/teleusl/{ip}/1/{func}'
    r = requests.get(url)
    data = json.loads(r.text)
    return(data)


if __name__ == '__main__':
    resp = req_to_api('10.100.2.91', 'walk_lldp')['response']['data']['ldpRemTable']
    print( mac_from_hexstring(resp) )



