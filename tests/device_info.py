import os


def get_android_device_model():
    android_device_model = os.popen('adb shell getprop ro.product.model').read()
    return android_device_model


def get_android_os_version():
    android_os_version = os.popen('adb shell getprop ro.build.version.release').read()
    return android_os_version
