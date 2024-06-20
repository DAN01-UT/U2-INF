import json
import os
import requests
import meraki
API_KEY = '6bec40cf957de430a6f1f2baf056b99a4fac9ea0'
dashboard = meraki.DashboardAPI(API_KEY)

def formar_json():

    dic_data = {
        'switches': [
            {"model": 'CAT3750',
            "model": 'CAT3760'}
        ],
        'routers': {'name': 'CSR100V',
                    'vendor': 'cisco',
                    'type': 'hardware'
                    }
    }
    data = {
        'servers': [
            {
                'name': 'vboxserver-01',
                'operative-system': 'Linux CentOS Stream 9',
                'services': ['dhcp', 'http']
            },
            {
                'name': 'vboxserver-02',
                'operative-system': 'Linux CentOS Stream 9',
                'services': ['dns', 'dhcp']
            }
        ],
        'AP': {
            'name': 'TL-SF1008D',
            'vendor': 'TP-Link',
            'type': 'hardware'
        },
        'clients': {
            'name': 'David-Lenovo',
            'vendor': 'Lenovo'
        }
    }
    
    print(json.dumps(data, indent=2))
    with open("./data/infraestructura.json", 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

def get_api_ips():

    response = requests.get('http://ip-api.com/json/24.48.0.1')
    data = response.json()
    print(json.dumps(data, indent=2))
    with open("./data/server_info.json", 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

def get_inf_base():
    response =requests.get('http://ip-api.com/json/24.48.0.1?fields=28949')
    data = response.json()
    print(json.dumps(data, indent=2))
    with open("./data/basic_info.json", 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

def get_ip_info():
    response =requests.get('http://ip-api.com/json/24.48.0.1?fields=22233085')
    data = response.json()
    print(json.dumps(data, indent=2))
    with open("./data/ip_info.json", 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

def get_Devnet():
    dashboard = meraki.DashboardAPI('6bec40cf957de430a6f1f2baf056b99a4fac9ea0')
    response = dashboard.organizations.json()
    print(json.dumps(response, indent=2))
    with open("./data/meraki_Api.json", 'w') as file:
        json.dump(response, file, indent=4, sort_keys=True)
        








if __name__ == '__main__':
    formar_json()
    get_api_ips()
    get_inf_base()
    get_ip_info()
    get_Devnet


#En base a la infraestructura ya creada, agregar todos los elementos de red que ya se tienen en formato .json