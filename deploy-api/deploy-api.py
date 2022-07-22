import boto3
import argparse
from netmiko import ConnectHandler
import os

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Please which server do you want install Zabbix Agent. If do you want to install in all servers, type "all" in --ip'
    )
    parser.add_argument("-a", dest="access_key",
                help="AWS Access Key",
                required=True, type=str)
    parser.add_argument("-k", dest="secret_key", 
                help="AWS Secret Access Key",
                required=True, type=str)

    args = parser.parse_args()

    return args

def list_servers():
    args = parse_arguments()
    ec2 = boto3.resource('ec2', aws_access_key_id=args.access_key, aws_secret_access_key=args.secret_key, region_name='us-east-1')
    running_instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']
    }])
    for instance in running_instances:
        for tags in instance.tags:
            if tags["Key"] == 'Name':
                instancename = tags["Value"]
        if "neoway_ec2" in instancename:
            app = instance.public_ip_address

    return app

def install_app():
    ip = list_servers()
    device = {
        'device_type': 'linux',
        'host': ip,
        'username': 'ubuntu',
        'use_keys': True,
        'key_file': 'aws_key',
        "read_timeout_override": 90,
        }
    with ConnectHandler(**device) as net_connect:
        download_docker = "curl -fsSL https://get.docker.com -o get-docker.sh"
        install_docker = "sudo bash get-docker.sh"
        net_connect.send_command(download_docker)
        net_connect.send_command(install_docker)
        installapp = "sudo docker run --name neoway-app -p 5000:5000 -d rafapmagalhaes/neoway:latest"
        net_connect.send_command(installapp)

def main():
    install_app()

if __name__ == '__main__':
    main()