""" Command line interface for Sector Alarm MyPages """

from __future__ import print_function
import argparse
import json
import sectoralarm

COMMAND_SET = 'set'
COMMAND_TEMPERATURE = 'temperature'
COMMAND_ETHERNET = 'ethernet'
COMMAND_EVENTLOG = 'eventlog'
COMMAND_ARMSTATE = 'armstate'
COMMAND_LOCK_DEVICES = 'lock_devices'
COMMAND_LOCK = 'lock'


def print_result(overview, *names):
    """ Print the result of a Sector Alarm request """
    if names:
        for name in names:
            toprint = overview
            for part in name.split('/'):
                toprint = toprint[part]
            print(json.dumps(toprint, indent=4, separators=(',', ': ')))
    else:
        print(json.dumps(overview, indent=4, separators=(',', ': ')))


# pylint: disable=too-many-locals,too-many-statements
def main():
    """ Start Sector Alarm command line """
    parser = argparse.ArgumentParser(
        description='Read or change status of sector alarm devices')
    parser.add_argument(
        'username',
        help='MyPages username')
    parser.add_argument(
        'password',
        help='MyPages password')
    parser.add_argument(
        'panel',
        help='Panel Id')

    commandsparser = parser.add_subparsers(
        help='commands',
        dest='command')

    # armstate command
    commandsparser.add_parser(
        COMMAND_ARMSTATE,
        help='Get arm state')

    # ethernet status
    commandsparser.add_parser(
        COMMAND_ETHERNET,
        help='Get ethernet status')

    # doorlock status
    commandsparser.add_parser(
        COMMAND_LOCK,
        help='Get lock status')

    commandsparser.add_parser(
        COMMAND_LOCK_DEVICES,
        help='Get lock devices')

    # Set command
    set_parser = commandsparser.add_parser(
        COMMAND_SET,
        help='Set status of a device')
    set_device = set_parser.add_subparsers(
        help='device',
        dest='device')

    # Set alarm
    set_alarm = set_device.add_parser(
        'alarm',
        help='set alarm status')
    set_alarm.add_argument(
        'code',
        help='alarm code')
    set_alarm.add_argument(
        'new_status',
        choices=[
            'ARMED_HOME',
            'ARMED_AWAY',
            'DISARMED'],
        help='new status')

    # Set lock
    set_lock = set_device.add_parser(
        'lock',
        help='set lock status')
    set_lock.add_argument(
        'code',
        help='alarm code')
    set_lock.add_argument(
        'serial_number',
        help='serial number')
    set_lock.add_argument(
        'new_status',
        choices=[
            'lock',
            'unlock'],
        help='new status')

    # Get temperatures
    temperature = commandsparser.add_parser(
        COMMAND_TEMPERATURE,
        help='Get temperatures')
    temperature.add_argument(
        '-d', '--device_label',
        default=None,
        help='device label')

    # Event log command
    eventlog_parser = commandsparser.add_parser(
        COMMAND_EVENTLOG,
        help='Get event log')
    eventlog_parser.add_argument(
        '-o', '--offset',
        type=int,
        default=0,
        help='Page offset')

    args = parser.parse_args()
    session = sectoralarm.Session(args.username, args.password, args.panel)
    try:
        if args.command == COMMAND_ARMSTATE:
            print_result(session.get_arm_state())
        if args.command == COMMAND_TEMPERATURE:
            print_result(session.get_temperature(args.device_label))
        if args.command == COMMAND_ETHERNET:
            print_result(session.get_ethernet_status())
        if args.command == COMMAND_LOCK_DEVICES:
            print_result(session.get_lock_devices())
        if args.command == COMMAND_LOCK:
            print_result(session.get_lock_status())
        if args.command == COMMAND_EVENTLOG:
            print_result(
                session.get_history(
                    offset=args.offset))
        if args.command == COMMAND_SET:
            if args.device == 'alarm':
                print_result(session.set_arm_state(
                    args.code,
                    args.new_status))
            if args.device == 'lock':
                print_result(session.set_lock_state(
                    args.code,
                    args.serial_number,
                    args.new_status))
    except sectoralarm.session.ResponseError as ex:
        print(ex.text)


# pylint: disable=C0103
if __name__ == "__main__":
    main()
