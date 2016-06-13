#!/usr/bin/env python3

import socket
import re
from collections import namedtuple

HDDTEMP_HOST = 'localhost'
HDDTEMP_PORT = 7634
HDDTEMP_DIR = 'hddtemp/'  # Dir in KSysGuard sensors tree
HDDTEMP_RE = re.compile(r'\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|')

Sensor = namedtuple('Sensor', ['dev', 'dev_name', 'value', 'sign', 'type'])


def get_sensors():
    with socket.create_connection((HDDTEMP_HOST, HDDTEMP_PORT)) as sock:
        sock_file = sock.makefile()
        response = sock_file.read()
        sock_file.close()
    return parse(response)


def parse(string):
    return {
        HDDTEMP_DIR + data[0].replace('/', '_'): Sensor(*data, type='integer')
        for data in HDDTEMP_RE.findall(string)
    }  # {'path': ('dev', 'dev_name', 'value', 'sign', 'type'), ... }


def main():
    print('ksysguardd 4')
    print('ksysguardd> ', end='')

    while True:
        command = input()
        sensors = get_sensors()

        if command == 'quit':
            break
        elif command == 'monitors':
            for path, sensor in sensors.items():
                print('%s\t%s' % (path, sensor.type))
        elif command in sensors:
            print(sensors[command].value)
        elif command.endswith('?') and command[:-1] in sensors:
            sensor = sensors[command[:-1]]
            print('{s.dev} {s.dev_name}\t0\t0\t°{s.sign}'.format(s=sensor))
        else:
            print('UNKNOWN COMMAND')

        print('ksysguardd> ', end='')

if __name__ == '__main__':
    main()