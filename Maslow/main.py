from Networks import GetNetworks
from Organizations import GetOrganizations
import sys
import asyncio
import core
import argparse
from Devices import GetDevices
from Devices import PutDevicesTag
def main():
        
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--api_key', help='API key', required=True)
    parser.add_argument('-ao', '--allorg', help='Get All Organizations')
    parser.add_argument('-o', '--organization', help='Organization name or ID')
    parser.add_argument('-n', '--network', help='Get Organization networks')
    parser.add_argument('-d', '--device', help='Get devices for serial number')
    parser.add_argument('-ad', '--adevices', help='Get all devices for all organizations')
    parser.add_argument('-p', '--put', help='Put configuration to device by name of organization')
    parser = parser.parse_args()
    
    if parser.api_key and parser.organization:
        organization = parser.organization
        api_key = parser.api_key
        Organizaciones = GetOrganizations.Organization(api_key)
        Organizaciones.Find_OrganizationsByName(organization)
    if parser.api_key and parser.network:
        api_key = parser.api_key
        network = parser.network
        Networks = GetNetworks.Network(api_key)
        Networks.getNetworksByOrganizationName(network)
    if parser.api_key and parser.allorg:
        api_key = parser.api_key
        allorg = parser.allorg
        Organizations = GetOrganizations.Organization(api_key)
        Organizations.AllOrganizations(allorg)
       
    '''Methods  for devices file''' 
    if parser.api_key and parser.device:
        api_key = parser.api_key
        serial = parser.device
        device = GetDevices.Devices(api_key)
        device.getDevicesBySerialnumber(serial)
    elif parser.api_key and parser.adevices:
        api_key = parser.api_key
        alldevice = parser.adevices
        device = GetDevices.Devices(api_key)
        asyncio.run(device.getDevices(alldevice))
   
        
if __name__ == "__main__":
        try:
           core.Core.banner_maslow()
           main()    
        except KeyboardInterrupt:
            sys.exit()