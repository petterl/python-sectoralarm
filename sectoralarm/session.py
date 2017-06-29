'''
Sector Alarm session, using Sector Alarm app api
'''

import json
import requests
from datetime import datetime
from . import urls


def _validate_response(response):
    """ Verify that response is OK """
    if response.status_code == 200:
        return
    raise ResponseError(response.status_code, response.text)


def fix_date_short(date_string):
    '''
    Convert the short date to ISO.
    '''
    try:
        result = datetime.strptime(date_string, '%m/%d %H:%M')
        result = result.replace(datetime.now().year)
    except ValueError:
        if date_string[:5] == 'Today':
            return fix_date_short(
                datetime.now().strftime('%m/%d') + date_string[5:])
        if date_string[:9] == 'Yesterday':
            return fix_date_short(
                datetime.now().strftime('%m/%d') + date_string[9:])

    return result.isoformat()


class Error(Exception):
    ''' Sector Alarm session error '''
    pass


class RequestError(Error):
    ''' Wrapped requests.exceptions.RequestException '''
    pass


class LoginError(Error):
    ''' Login failed '''
    pass


class ResponseError(Error):
    ''' Unexcpected response '''
    def __init__(self, status_code, text):
        super(ResponseError, self).__init__(
            'Invalid response'
            ', status code: {0} - Data: {1}'.format(
                status_code,
                text))
        self.status_code = status_code
        self.text = json.loads(text)


class Session(object):
    """ Sector Alarm app session

    Args:
        username (str): Username used to login to Sector Alarm app
        password (str): Password used to login to Sector Alarm app

    """

    def __init__(self, username, password, panel):
        self._username = username
        self._password = password
        self._panel = panel

    def get_arm_state(self):
        """ Get arm state """
        response = None
        try:
            response = requests.get(
                urls.status(self._username, self._password, self._panel))
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        res = json.loads(response.text)
        res['timeex'] = fix_date_short(res['timeex'])
        return res

    def get_temperature(self, device_label=None):
        """ Get temperatures """
        response = None
        try:
            response = requests.get(urls.get_temperature(
                self._username, self._password, self._panel))
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        res = json.loads(response.text)
        if device_label is not None:
            res['temperatureComponentList'] = [
                i for i in res['temperatureComponentList']
                if i['serialNo'] == device_label]
        return res

    def get_ethernet_status(self):
        """ Get ethernet state """
        response = None
        try:
            response = requests.get(urls.get_ethernet_status(
                self._username,
                self._password,
                self._panel))
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        res = json.loads(response.text)
        return res

    def get_lock_devices(self):
        """ Get lock devices """
        response = None
        try:
            response = requests.get(urls.get_doorlock_devices(
                self._username,
                self._password,
                self._panel))
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        res = json.loads(response.text)
        return res

    def get_lock_status(self):
        """ Get lock state """
        response = None
        try:
            response = requests.get(urls.get_doorlock_status(
                self._username,
                self._password,
                self._panel))
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        res = json.loads(response.text)
        return res

    def set_arm_state(self, code, state):
        """ Set alarm state

        Args:
            code (str): Personal alarm code (four or six digits)
            state (str): 'ARMED_HOME', 'ARMED_AWAY' or 'DISARMED'
        """
        response = None
        try:
            response = requests.put(
                urls.set_armstate(self._giid),
                headers={
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Content-Type': 'application/json',
                    'Cookie': 'vid={}'.format(self._vid)},
                data=json.dumps({"code": str(code), "state": state}))
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        return json.loads(response.text)

    def get_history(self, offset=0):
        """ Get recent events
        """
        response = None
        try:
            response = requests.get(
                urls.history(self._username, self._password, self._panel),
                params={
                    "startIndex": int(offset)})
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        res = json.loads(response.text)
        for row in res['logs']:
            row['time'] = fix_date_short(row['time'])
        return res

    def get_lock_state(self):
        """ Get current lock status """
        response = None
        try:
            response = requests.get(
                urls.get_lockstate(self._giid),
                headers={
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Cookie': 'vid={}'.format(self._vid)})
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        return json.loads(response.text)

    def set_lock_state(self, code, device_label, state):
        """ Lock or unlock

        Args:
            code (str): Lock code
            device_label (str): device label of lock
            state (str): 'lock' or 'unlock'
        """
        response = None
        try:
            response = requests.put(
                urls.set_lockstate(self._giid, device_label, state),
                headers={
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Content-Type': 'application/json',
                    'Cookie': 'vid={}'.format(self._vid)},
                data=json.dumps({"code": str(code)}))
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        return json.loads(response.text)

    def get_lock_config(self, device_label):
        """ Get lock configuration

        Args:
            device_label (str): device label of lock
        """
        response = None
        try:
            response = requests.get(
                urls.lockconfig(self._giid, device_label),
                headers={
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Cookie': 'vid={}'.format(self._vid)})
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
        return json.loads(response.text)

    def logout(self):
        """ Logout and remove vid """
        response = None
        try:
            response = requests.delete(
                urls.login(),
                headers={
                    'Cookie': 'vid={}'.format(self._vid)})
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)
        _validate_response(response)
