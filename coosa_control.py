from os import makedirs

import socket as sk
from appdirs import user_config_dir
from argparse import ArgumentParser
from ast import literal_eval
from os.path import isfile, join, dirname


def main():
    parser = ArgumentParser(description='Lights control script for coosa smart plugs')
    parser.add_argument('command', nargs='?', choices=['on', 'off'])
    parser.add_argument('-i', '--ip-address', help='IP address of device')
    parser.add_argument('-s', '--save-params', action='store_true', help='Save params as default')
    parser.add_argument('-e', '--enable-data', help='File with data to send to enable plug')
    parser.add_argument('-d', '--disable-data', help='File with data to send to disable plug')
    args = parser.parse_args()

    params_file = join(user_config_dir('coosa-control'), 'params.dat')
    if isfile(params_file):
        with open(params_file) as f:
            params = literal_eval(f.read())
    else:
        params = {}

    params = {k: v or params.get(k) for k, v in vars(args).items()}

    address = params['ip_address']
    enable = params['enable_data']
    disable = params['disable_data']

    if not enable or not disable or not address:
        parser.error('Specify --ip-address, --enabled-data, and --disable-data, or save params first.')
        raise SystemExit(1)

    if not args.command and not args.save_params:
        parser.error('Specify a command or use --save-params')

    if isinstance(enable, str):
        with open(enable, 'rb') as f:
            enable = params['enable_data'] = f.read()

    if isinstance(disable, str):
        with open(disable, 'rb') as f:
            disable = params['disable_data'] = f.read()

    if args.command:
        sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((address, 6668))
        sock.sendall(enable if args.command == 'on' else disable)

    if args.save_params:
        makedirs(dirname(params_file), exist_ok=True)
        with open(params_file, 'w') as f:
            f.write(str(params))


if __name__ == '__main__':
    main()
