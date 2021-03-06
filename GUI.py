#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.7 (standalone edition) on Fri Jan 10 22:16:02 2014
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.statusbar = self.CreateStatusBar(5, wx.ST_SIZEGRIP)
        self.SplitterWindow = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER | wx.SP_LIVE_UPDATE)
        self.window_1_pane_1 = wx.ScrolledWindow(self.SplitterWindow, wx.ID_ANY, style=wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnlSettingBar = wx.Panel(self.window_1_pane_1, wx.ID_ANY)
        self.btnHideBar = wx.Button(self.pnlSettingBar, wx.ID_ANY, "Hide")
        self.btnEnumPorts = wx.Button(self.pnlSettingBar, wx.ID_ANY, "EnumPorts")
        self.label_1 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Port")
        self.cmbPort = wx.ComboBox(self.pnlSettingBar, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.label_2 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Baud Rate")
        self.cmbBaudRate = wx.ComboBox(self.pnlSettingBar, wx.ID_ANY, choices=["300", "600", "1200", "1800", "2400", "4800", "9600", "19200", "38400", "57600", "115200", "230400", "460800", "500000", "576000", "921600", "1000000", "1152000", "1500000", "2000000", "2500000", "3000000", "3500000", "4000000"], style=wx.CB_DROPDOWN)
        self.label_3 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Data Bits")
        self.choiceDataBits = wx.Choice(self.pnlSettingBar, wx.ID_ANY, choices=["5", "6", "7", "8"])
        self.label_4 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Parity")
        self.choiceParity = wx.Choice(self.pnlSettingBar, wx.ID_ANY, choices=["None", "Even", "Odd", "Mark", "Space"])
        self.label_5 = wx.StaticText(self.pnlSettingBar, wx.ID_ANY, "Stop Bits")
        self.choiceStopBits = wx.Choice(self.pnlSettingBar, wx.ID_ANY, choices=["1", "1.5", "2"])
        self.chkboxrtscts = wx.CheckBox(self.pnlSettingBar, wx.ID_ANY, "RTS/CTS")
        self.chkboxxonxoff = wx.CheckBox(self.pnlSettingBar, wx.ID_ANY, "Xon/Xoff")
        self.sizer_6_staticbox = wx.StaticBox(self.pnlSettingBar, wx.ID_ANY, "HandShake")
        self.btnOpen = wx.Button(self.pnlSettingBar, wx.ID_ANY, "Open")
        self.btnClear = wx.Button(self.pnlSettingBar, wx.ID_ANY, "Clear Screen")
        self.window_1_pane_2 = wx.Panel(self.SplitterWindow, wx.ID_ANY)
        self.pnlData = wx.Panel(self.window_1_pane_2, wx.ID_ANY)
        self.txtctlMain = wx.TextCtrl(self.pnlData, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_RICH | wx.TE_RICH2 | wx.TE_AUTO_URL | wx.TE_LINEWRAP | wx.TE_WORDWRAP | wx.NO_BORDER)
        self.pnlTransmitHex = wx.Panel(self.pnlData, wx.ID_ANY, style=wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.label_6 = wx.StaticText(self.pnlTransmitHex, wx.ID_ANY, "Transmit Hex")
        self.btnTransmitHex = wx.Button(self.pnlTransmitHex, wx.ID_ANY, "Transmit")
        self.txtctlHex = wx.TextCtrl(self.pnlTransmitHex, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_RICH | wx.TE_RICH2 | wx.TE_LINEWRAP | wx.TE_WORDWRAP | wx.NO_BORDER)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("MyTerm")
        self.SetSize((752, 610))
        self.statusbar.SetStatusWidths([-28, -10, -10, 55, 105])
        # statusbar fields
        statusbar_fields = ["", "Rx:0", "Tx:0", "Rx:Ascii", "Local echo:Off"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)
        self.cmbBaudRate.SetSelection(7)
        self.choiceDataBits.SetSelection(3)
        self.choiceParity.SetSelection(0)
        self.choiceStopBits.SetSelection(0)
        self.btnOpen.SetMinSize((-1, 30))
        self.btnClear.SetMinSize((-1, 30))
        self.pnlSettingBar.SetMinSize((158, -1))
        self.window_1_pane_1.SetScrollRate(1, 1)
        self.txtctlMain.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        self.pnlTransmitHex.SetMinSize((454, 160))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_6_staticbox.Lower()
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(6, 2, 0, 0)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.btnHideBar, 1, wx.ALL | wx.EXPAND, 1)
        sizer_4.Add(self.btnEnumPorts, 1, wx.ALL | wx.EXPAND, 1)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.cmbPort, 0, wx.ALL | wx.EXPAND, 1)
        grid_sizer_1.Add(self.label_2, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.cmbBaudRate, 0, wx.ALL | wx.EXPAND, 1)
        grid_sizer_1.Add(self.label_3, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.choiceDataBits, 0, wx.ALL | wx.EXPAND, 1)
        grid_sizer_1.Add(self.label_4, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.choiceParity, 0, wx.ALL | wx.EXPAND, 1)
        grid_sizer_1.Add(self.label_5, 0, wx.ALL, 1)
        grid_sizer_1.Add(self.choiceStopBits, 0, wx.ALL | wx.EXPAND, 1)
        sizer_3.Add(grid_sizer_1, 0, wx.ALL | wx.EXPAND, 1)
        sizer_6.Add(self.chkboxrtscts, 1, wx.ALL | wx.EXPAND, 1)
        sizer_6.Add(self.chkboxxonxoff, 1, wx.ALL | wx.EXPAND, 1)
        sizer_3.Add(sizer_6, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 2)
        sizer_3.Add(self.btnOpen, 0, wx.ALL | wx.EXPAND, 5)
        sizer_3.Add(self.btnClear, 0, wx.ALL | wx.EXPAND, 5)
        self.pnlSettingBar.SetSizer(sizer_3)
        sizer_2.Add(self.pnlSettingBar, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetSizer(sizer_2)
        sizer_7.Add(self.txtctlMain, 1, wx.EXPAND, 0)
        sizer_9.Add(self.label_6, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_9.Add((20, 20), 1, 0, 0)
        sizer_9.Add(self.btnTransmitHex, 0, wx.ALL, 2)
        sizer_9.Add((10, 20), 0, 0, 0)
        sizer_8.Add(sizer_9, 0, wx.EXPAND, 0)
        sizer_8.Add(self.txtctlHex, 1, wx.EXPAND, 0)
        self.pnlTransmitHex.SetSizer(sizer_8)
        sizer_7.Add(self.pnlTransmitHex, 0, wx.EXPAND, 0)
        self.pnlData.SetSizer(sizer_7)
        sizer_5.Add(self.pnlData, 1, wx.EXPAND, 0)
        self.window_1_pane_2.SetSizer(sizer_5)
        self.SplitterWindow.SplitVertically(self.window_1_pane_1, self.window_1_pane_2, 271)
        sizer_1.Add(self.SplitterWindow, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

# end of class MyFrame
class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        mainFrame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(mainFrame)
        mainFrame.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()