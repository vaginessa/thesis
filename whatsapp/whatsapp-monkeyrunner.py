#!/usr/bin/python
# -*- coding: ascii -*-

# import monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

# connect to the currently running device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
print("waiting for the connection..")
MonkeyRunner.sleep(10)
easy_device = EasyMonkeyDevice(device)

print "launching app..."

# set a variable with the package's internal name
package = 'com.whatsapp'

# set a variable with the name of an Activity in the package
activity = '.Main'

# set the name of the component to start
runComponent = package + '/' + activity

# run the component
device.startActivity(component=runComponent)

# wait for a few seconds
MonkeyRunner.sleep(5)

# click on a FAB button to start a new conversation.
easy_device.touch(By.id('id/fab'), MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)

# navigate down and click on the first available contact to start a conversation.
device.press("DPAD_DOWN", MonkeyDevice.DOWN_AND_UP)
device.press("DPAD_DOWN", MonkeyDevice.DOWN_AND_UP)
device.press("DPAD_DOWN", MonkeyDevice.DOWN_AND_UP)
device.press("DPAD_DOWN", MonkeyDevice.DOWN_AND_UP)
device.press("DPAD_CENTER", MonkeyDevice.DOWN_AND_UP)

MonkeyRunner.sleep(5)

easy_device.touch(By.id('id/entry'), MonkeyDevice.DOWN_AND_UP)
device.type('test')
MonkeyRunner.sleep(5)
easy_device.touch(By.id('id/send'), MonkeyDevice.DOWN_AND_UP)

MonkeyRunner.sleep(5)

# close the app
device.shell('am force-stop com.whatsapp')

