import json


def get_request_ip(request) -> str:
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_ip_info(ip) -> dict:
    import requests
    try:
        resp = requests.get(f"https://ipinfo.io/{ip}/geo/")
        return resp.json()
    except:
        return {}

