import requests
import re
import subprocess
import pkg_resources


def ensure_packages():
    required_packages = ['requests']
    for package in required_packages:
        try:
            dist = pkg_resources.get_distribution(package)
            print(f"{dist.key} ({dist.version}) is installed")
        except pkg_resources.DistributionNotFound:
            print(f"{package} is NOT installed")
            subprocess.call(['pip', 'install', package])


def open_url_with_requests(url, proxy):
    proxy_parts = proxy.split(':')
    proxy_ip = proxy_parts[0]
    proxy_port = proxy_parts[1]
    proxy_username = proxy_parts[2]
    proxy_password = proxy_parts[3]

    proxies = {
        'http': f'http://{proxy_username}:{proxy_password}@{proxy_ip}:{proxy_port}',
        'https': f'http://{proxy_username}:{proxy_password}@{proxy_ip}:{proxy_port}',
    }

    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        views_value = re.search(r'<span class="tgme_widget_message_views">(\d+)</span>', response.text)
        views_value = views_value.group(1) if views_value else 'N/A'
        print(f"Current views: {views_value} using proxy: {proxy}")
    except Exception as e:
        print(f"Failed to access the URL using proxy: {proxy}. Error: {e}")


def main():
    ensure_packages()

    proxies = [
        "2.56.119.93:5074:ioztoppc:bc8ih4h3zl96",
        "185.199.229.156:7492:ioztoppc:bc8ih4h3zl96",
        "185.199.228.220:7300:ioztoppc:bc8ih4h3zl96",
        "185.199.231.45:8382:ioztoppc:bc8ih4h3zl96",
        "188.74.210.207:6286:ioztoppc:bc8ih4h3zl96",
        "188.74.183.10:8279:ioztoppc:bc8ih4h3zl96",
        "188.74.210.21:6100:ioztoppc:bc8ih4h3zl96",
        "45.155.68.129:8133:ioztoppc:bc8ih4h3zl96",
        "154.95.36.199:6893:ioztoppc:bc8ih4h3zl96",
        "45.94.47.66:8110:ioztoppc:bc8ih4h3zl96",
    ]

    url = "https://t.me/TechCraftersHub/5242"

    for proxy in proxies:
        open_url_with_requests(url, proxy)


if __name__ == "__main__":
    main()
