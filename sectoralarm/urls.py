"""
Sector Alarm urls.
"""

# pylint: disable=missing-docstring
BASE_URL = 'https://panelapi.sectoralarm.net/MobileAppWS.svc'


def status(username, password, panel):
    return (
        '{base_url}/PanelStatus?username={username}&password={password}'
        '&panel={panel}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel)


def history(username, password, panel):
    return (
        '{base_url}/Logs?username={username}&password={password}'
        '&panel={panel}&includeannex=true').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel)


def login(username, password, deviceId, deviceName, language, version, token):
    return (
        '{base_url}/LogOn?username={username}&password={password}'
        '&deviceId={deviceId}&deviceName={deviceName}&language={language}'
        '&appVersion={version}&pushToken={token}&pushService=GCM').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        deviceId=deviceId,
        deviceName=deviceName,
        language=language,
        version=version,
        token=token)


def disarm(username, password, panel, code):
    return (
        '{base_url}/disarm?username={username}&password={password}'
        '&panel={panel}&disarmCode={code}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel,
        code=code)


def arm(username, password, panel, code):
    return (
        '{base_url}/arm?username={username}&password={password}'
        '&panel={panel}&armCode={code}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel,
        code=code)


def partialarm(username, password, panel, code):
    return (
        '{base_url}/partialarm?username={username}&password={password}'
        '&panel={panel}&armCode={code}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel,
        code=code)


def disarm_and_unlock(username, password, panel, code):
    return (
        '{base_url}/ArmAndLock?username={username}&password={password}'
        '&panel={panel}&disarmCode={code}&armType=DisarmAndUnlock').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel,
        code=code)


def logout(username):
    return ('{base_url}/Logout?username={username}').format(
        base_url=BASE_URL,
        username=username)


def get_smartplugs(username, password, panel):
    return (
        '{base_url}/GetSmartPlugStatus?username={username}'
        '&password={password}&panel={panel}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel)


def get_doorlock_devices(username, password, panel):
    return (
        '{base_url}/GetDoorlockDevices?username={username}'
        '&password={password}&panelId={panel}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel)


def get_doorlock_status(username, password, panel):
    return (
        '{base_url}/GetDoorlockStatus?username={username}'
        '&password={password}&panelId={panel}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel)


def lock_doorlock(username, password, panel, serialNo, code):
    return (
        '{base_url}/lockDoorlock?username={username}'
        '&password={password}&panelId={panel}'
        '&serial={serialNo}&userCode={code}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel,
        serialNo=serialNo,
        code=code)


def unlock_doorlock(username, password, panel, serialNo, code):
    return (
        '{base_url}/unlockDoorlock?username={username}'
        '&password={password}&panelId={panel}'
        '&serial={serialNo}&userCode={code}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel,
        serialNo=serialNo,
        code=code)


def get_temperature(username, password, panel):
    return (
        '{base_url}/GetTemperatureComponents?username={username}'
        '&password={password}&panel={panel}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel)


def get_ethernet_status(username, password, panel):
    return (
        '{base_url}/GetEthernetStatus?username={username}'
        '&password={password}&panel={panel}').format(
        base_url=BASE_URL,
        username=username,
        password=password,
        panel=panel)
