import requests
from bs4 import BeautifulSoup



def check_ip():
    ip = requests.get('https://api.ipify.org').text
    return ip

def find_proxies_list(print_list="no"):
    url = "https://free-proxy-list.net/"
    proxy_list = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    list = soup.find("table",{"class": "table table-striped table-bordered"})
    table = list.find('tbody')
    proxy_rows = table.find_all('tr')[1:]

    for row in proxy_rows:
        columns = row.find_all('td')
        ip_address = columns[0].text
        port = columns[1].text
        proxy_list.append(f'{ip_address} : {port}')
        if print_list == "yes":
            print(f'IP Address: {ip_address}\tPort: {port}')

    return proxy_list

def find_working_proxies(proxylist ,howmanyproxies = 3):  
    working_proxies = []
    counter = 0
    rightproxies = 0
    for p in range(len(proxylist)):
        counter += 1
        # Define the proxy server URL and port
        l = proxylist[p].split(":")
        proxy_ip_ = l[0] 
        proxy_port_ = l[1]
        proxy_ip = proxy_ip_.rstrip().lstrip() #formating
        proxy_port = proxy_port_.rstrip().lstrip() #formating
        
        # Define the proxy settings
        proxies = {
            'http': f'http://{proxy_ip}:{proxy_port}',
            'https': f'http://{proxy_ip}:{proxy_port}',
        }

        try:
            # Make the request through the proxy
            ip = requests.get('https://api.ipify.org', proxies=proxies).text
        except:
            print(str(counter)+".Don´t like this one: "+ proxy_ip+":"+proxy_port)
            continue
        if ip == proxy_ip:
            print(str(counter)+". "+proxy_ip+":"+proxy_port+ " is working")
            howmanyproxies+=1
            working_proxies.append(proxy_ip+":"+proxy_port)

        if rightproxies == howmanyproxies:
            break
    print("The working proxies:")
    print(working_proxies)
        
    return working_proxies        

def find_one_proxy():
    url = "https://free-proxy-list.net/"
    proxy_list = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    list = soup.find("table",{"class": "table table-striped table-bordered"})
    table = list.find('tbody')
    proxy_rows = table.find_all('tr')[1:]

    for row in proxy_rows:
        columns = row.find_all('td')
        ip_address = columns[0].text
        port = columns[1].text
        proxy_list.append(f'{ip_address} : {port}')

            
    working_proxy = ""
    counter = 0
    rightproxies = 0
    for p in range(len(proxy_list)):
        counter += 1
        # Define the proxy server URL and port
        l = proxy_list[p].split(":")
        proxy_ip_ = l[0] 
        proxy_port_ = l[1]
        proxy_ip = proxy_ip_.rstrip().lstrip() #formating
        proxy_port = proxy_port_.rstrip().lstrip() #formating
        
        # Define the proxy settings
        proxies = {
            'http': f'http://{proxy_ip}:{proxy_port}',
            'https': f'http://{proxy_ip}:{proxy_port}',
        }

        try:
            # Make the request through the proxy
            ip = requests.get('https://api.ipify.org', proxies=proxies).text
        except:
            print(str(counter)+".Don´t like this one: "+ proxy_ip+":"+proxy_port)
            continue
        if ip == proxy_ip:
            print(str(counter)+". "+proxy_ip+":"+proxy_port+ " is working")
            return proxy_ip,proxy_port

        
    