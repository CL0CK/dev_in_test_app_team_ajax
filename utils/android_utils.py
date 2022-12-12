import subprocess


def get_device_udid():
    cmd = "adb devices"
    returned_output = subprocess.check_output(cmd)
    return returned_output.decode("utf-8").splitlines()[1].split('\t')[0]


def android_get_desired_capabilities():
    return {
        'autoLaunch': False,
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_device_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
