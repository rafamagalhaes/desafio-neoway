import boto3
from netmiko import ConnectHandler

def list_servers():
    ec2 = boto3.resource('ec2', region_name='us-east-1')
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
    print(ip)
    device = {
        'device_type': 'linux',
        'host': ip,
        'username': 'ubuntu',
        'use_keys': True,
        'key_file': '../key-pair/aws_key',
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