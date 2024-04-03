import addonHandler
import gui
import os.path
import sys
import wx

addon = addonHandler.getCodeAddon()
addonName = addon.name
addonDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "globalPlugins", addonName))
sys.path.append(addonDir)
from donate_dialog import requestDonations
sys.path.remove(sys.path[-1])

addonHandler.initTranslation()

def onInstall():
    for addon in addonHandler.getAvailableAddons():
        if addon.name == "instantTranslate" and not addon.isDisabled:
            result = gui.messageBox(
                # Translators: message asking the user wether instantTranslate whould be disabled or not
                _("instantTranslate has been detected on your NVDA installation. In order for instantTranslateCN to work without conflicts, instantTranslate must be disabled. Otherwise, instantTranslateCN will refuse to work. Would you like to disable instantTranslate now?"),
                # Translators: question title
                _("Running instantTranslate detected"),
                wx.YES_NO|wx.ICON_QUESTION, gui.mainFrame)
            if result == wx.YES:
                addon.enable(False)
#            return
    gui.mainFrame.prePopup()
    wx.CallAfter(requestDonations, gui.mainFrame)
    gui.mainFrame.postPopup()
