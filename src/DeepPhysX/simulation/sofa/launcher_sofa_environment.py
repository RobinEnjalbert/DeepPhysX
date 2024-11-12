from os import sep
from os.path import dirname
from sys import argv, path

from DeepPhysX.simulation.sofa.sofa_environment import SofaEnvironment as Environment
from DeepPhysX.simulation.multiprocess.tcpip_client import TcpIpClient

if __name__ == '__main__':

    # Check script call
    if len(argv) != 7:
        print(f"Usage: python3 {argv[0]} <file_path> <environment_class> <ip_address> <port> <instance_id> "
              f"<max_instance_count> <visu_db>")
        exit(1)

    # Import environment_class
    path.append(dirname(argv[1]))
    module_name = argv[1].split(sep)[-1][:-3]
    exec(f"from {module_name} import {argv[2]} as Environment")

    # Create, init and run Tcp-Ip environment
    client = TcpIpClient(environment=Environment,
                         ip_address=argv[3],
                         port=int(argv[4]),
                         instance_id=int(argv[5]),
                         instance_nb=int(argv[6]))
    client.initialize()
    client.launch()

    # Client is closed at this point
    print(f"[launcherSofaEnvironment] Shutting down client {argv[3]}")
