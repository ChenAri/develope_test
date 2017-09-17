# -*- coding: utf-8 -*- 
#!/usr/bin/env python
__author__ = "scott.huang"
__version__ = "0.0.1"


###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import os
import cv2
from threading import Thread
import wx.lib.agw.rulerctrl as RC
import wx
import wx.xrc
import vlc
import subprocess
import wx.lib.agw.rulerctrl as rc
from const import *
from API_manager import *
from Calculate_FV import *
from singleton import *
from button_event import *
from ConfigParser import ConfigParser 
###########################################################################
## Class panel_view
###########################################################################

class panel_view ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 960,960 ), style = wx.TAB_TRAVERSAL )
        
    def __del__( self ):
        pass
    

###########################################################################
## Class panel_status
###########################################################################

class panel_status ( wx.Panel ):
    
    def __init__( self, parent, panel_view ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 320,960 ), style = wx.TAB_TRAVERSAL )
        config = ConfigParser()
        config.optionxform = str
        config.read('TestFocus.ini')
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"IP address 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
        self.m_txtIP1 = wx.TextCtrl( self, wx.ID_ANY, config.get('ip', 'ip1'), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_txtIP1, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"IP address 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.m_txtIP2 = wx.TextCtrl( self, wx.ID_ANY, config.get('ip', 'ip2'), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_txtIP2, 0, wx.ALL, 5 )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Login ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.m_txtUser = wx.TextCtrl( self, wx.ID_ANY, u"administrator", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_txtUser, 0, wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Password :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        gSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.m_txtPwd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_txtPwd, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Cut Number :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        gSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self.m_txtCut = wx.TextCtrl( self, wx.ID_ANY, config.get('cut', 'number'), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_txtCut, 0, wx.ALL, 5 ) 

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Cut X % :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        gSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self.m_txtCutX = wx.TextCtrl( self, wx.ID_ANY, config.get('cut', 'xPercent'), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_txtCutX, 0, wx.ALL, 5 ) 
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Cut Y % :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        gSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
        
        self.m_txtCutY = wx.TextCtrl( self, wx.ID_ANY, config.get('cut', 'yPercent'), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_txtCutY, 0, wx.ALL, 5 ) 
        
        bSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )
        
        gSizer2 = wx.GridSizer( 0, 3, 0, 0 )
        
        self.m_stxt_area1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_area1.Wrap( -1 )
        gSizer2.Add( self.m_stxt_area1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_stxt_score1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_score1.Wrap( -1 )
        gSizer2.Add( self.m_stxt_score1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_bmpStatus1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), 0 )
        gSizer2.Add( self.m_bmpStatus1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_stxt_area2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_area2.Wrap( -1 )
        gSizer2.Add( self.m_stxt_area2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_stxt_score2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_score2.Wrap( -1 )
        gSizer2.Add( self.m_stxt_score2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_bmpStatus2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), 0 )
        gSizer2.Add( self.m_bmpStatus2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_stxt_area3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_area3.Wrap( -1 )
        gSizer2.Add( self.m_stxt_area3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_stxt_score3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_score3.Wrap( -1 )
        gSizer2.Add( self.m_stxt_score3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_bmpStatus3 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), 0 )
        gSizer2.Add( self.m_bmpStatus3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_stxt_area4 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_area4.Wrap( -1 )
        gSizer2.Add( self.m_stxt_area4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_stxt_score4 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_score4.Wrap( -1 )
        gSizer2.Add( self.m_stxt_score4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_bmpStatus4 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), 0 )
        gSizer2.Add( self.m_bmpStatus4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_stxt_area5 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_area5.Wrap( -1 )
        gSizer2.Add( self.m_stxt_area5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_stxt_score5 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_score5.Wrap( -1 )
        gSizer2.Add( self.m_stxt_score5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_bmpStatus5 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), 0 )
        gSizer2.Add( self.m_bmpStatus5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
      
        self.m_stxt_area0 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_area0.Wrap( -1 )
        gSizer2.Add( self.m_stxt_area0, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_stxt_score0 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stxt_score0.Wrap( -1 )
        gSizer2.Add( self.m_stxt_score0, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_bmpStatus0 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), 0 )
        gSizer2.Add( self.m_bmpStatus0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        
        bSizer1.Add( gSizer2, 0, wx.EXPAND, 5 )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

    
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_btnIP1 = wx.Button( self, wx.ID_ANY, u"Channel 1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_btnIP1, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_btnIP2 = wx.Button( self, wx.ID_ANY, u"Channel 2", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_btnIP2, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_btnReset = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_btnReset, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_btnLockFV = wx.Button( self, wx.ID_ANY, u"Lock MAX FV", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_btnLockFV, 1, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )
        
        self.m_btnDisconn = wx.Button( self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.Size( 290,-1 ), 0 )
        bSizer2.Add( self.m_btnDisconn, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_btnUpload = wx.Button( self, wx.ID_ANY, u"Upload BurnIn tool", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_btnUpload, 0, wx.ALL|wx.EXPAND, 5 )
        
        # self.m_btnSaveFV = wx.Button( self, wx.ID_ANY, u"Save FV", wx.DefaultPosition, wx.DefaultSize, 0 )
        # bSizer2.Add( self.m_btnSaveFV, 0, wx.ALL|wx.EXPAND, 5 )

        # self.m_btnLoadFV = wx.Button( self, wx.ID_ANY, u"Load FV", wx.DefaultPosition, wx.DefaultSize, 0 )
        # bSizer2.Add( self.m_btnLoadFV, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnSetIni = wx.Button( self, wx.ID_ANY, u"Set ini", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_btnSetIni, 0, wx.ALL|wx.EXPAND, 5 )
        button_ini = config.get('button', 'set_ini')
        if str(button_ini) == '0':
            self.m_btnSetIni.Enable(False)
        self.m_btnShowImg = wx.Button( self, wx.ID_ANY, u"Show image", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_btnShowImg, 0, wx.ALL|wx.EXPAND, 5 )
      
        self.m_drawLineImg = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), 0 )
        bSizer2.Add( self.m_drawLineImg, 0, wx.ALL, 5 )
        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )        
        self.SetSizer( bSizer1 )
        self.Layout()
    

        self.__init_iamge()
        self.__init_UI()
        self.panel_view = panel_view
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.singleton = Singleton.get_instance()
        self.btn_evt = Button_event(tuple([self.m_btnIP1, self.m_btnIP2, self.m_btnReset, self.m_btnDisconn]))

        self.m_btnIP1.Bind( wx.EVT_LEFT_DOWN, self.evt_connect1 )
        self.m_btnIP2.Bind( wx.EVT_LEFT_DOWN, self.evt_connect2 )
        self.m_btnDisconn.Bind( wx.EVT_LEFT_DOWN, self.evt_disconnect )
        self.m_btnReset.Bind( wx.EVT_LEFT_DOWN, self.evt_reset)
        self.m_btnLockFV.Bind( wx.EVT_LEFT_DOWN, self.evt_lock_fv)
        self.m_btnUpload.Bind(wx.EVT_LEFT_DOWN, self.evt_upload_burnin)
        #self.m_btnSaveFV.Bind(wx.EVT_LEFT_DOWN, self.evt_save_fv)
        #self.m_btnLoadFV.Bind(wx.EVT_LEFT_DOWN, self.evt_load_fv)
        self.m_btnSetIni.Bind(wx.EVT_LEFT_DOWN, self.__evt_set_ini)
        self.m_btnShowImg.Bind(wx.EVT_LEFT_DOWN, self.__evt_show_image)
    def __del__( self ):
        pass

    # =================EVENT=====================

    def __evt_show_image(self, evt):
        config = ConfigParser()
        config.optionxform = str
        config.read('TestFocus.ini')
        image_file = config.get('file','cut_image')
        imgFile = cv2.imread(image_file)
        cv2.imshow('cut_image', imgFile)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def evt_connect1(self, evt):
        self.ip = self.m_txtIP1.GetValue()
        self.singleton = Singleton.get_instance()
        self.singleton.cut_number = int(self.m_txtCut.GetValue())
        self.singleton.cut_x_percent = int(self.m_txtCutX.GetValue())
        self.singleton.cut_y_percent = int(self.m_txtCutY.GetValue())
        self.__start_test()
        
    def evt_connect2(self, evt):
        self.ip = self.m_txtIP2.GetValue()
        self.singleton = Singleton.get_instance()
        self.singleton.cut_number = int(self.m_txtCut.GetValue())
        self.singleton.cut_x_percent = int(self.m_txtCutX.GetValue())
        self.singleton.cut_y_percent = int(self.m_txtCutY.GetValue())
        self.__start_test()
        
    def evt_disconnect(self, evt):
        wx.CallAfter(self.__set_color, self.m_btnUpload, "White")
        self.player.stop()

        self.singleton.stop = True
        self.btn_evt.stop_fv()
        self.__init_UI()

    def evt_reset(self, evt):
        print self.player.video_take_snapshot(0, 'snapshot.tmp.png', 0, 0)

        self.__clear_score()
        self.__clear_singleton()
        self.__init_status_img()

    def evt_lock_fv(self, evt):
        self.singleton.stop_fv = True

    def __start_test(self):    

        self.__set_mjpg(self.ip)
        wx.CallAfter(self.__connect, self.ip)
        Thread(target=self.__calculateFV, args=(self.ip,)).start()

    def evt_save_fv(self, evt):
        print self.singleton.model_type
        print self.singleton.fv
        f = open('%s.txt'%self.singleton.model_type,'a')
        for x in self.singleton.fv:
            f.write(str(x))
            f.write('\t')
        f.write('\n')
        f.close()

    def evt_load_fv(self, evt):
        with open('%s.txt'%self.singleton.model_type, 'r') as f:
            data = f.read()
            fv = [x.replace('\n', '') for x in data.split('\t')]
        f.close()        
        
        min_fv = [1000000000]*6
        for i, data in enumerate(fv):
            if not data: break
            if min_fv[i%6] > float(data)*0.9:
                min_fv[i%6] = float(data)*0.9
        print min_fv
        self.singleton.load_sample = True
        self.singleton.sample = min_fv

    def evt_upload_burnin(self, evt):

        # verify upload status
        result = self.__verify_burnin()
        if result:
            wx.CallAfter(self.__set_color, self.m_btnUpload, "Green")
        else:
            wx.CallAfter(self.__set_color, self.m_btnUpload, "Red")

    def __evt_set_ini(self, evt):
        print "test"
        singleton = Singleton.get_instance()
        singleton.cut_x_percent = int(self.m_txtCutX.GetValue())
        singleton.cut_y_percent = int(self.m_txtCutY.GetValue())
        singleton.cut_number = int(self.m_txtCut.GetValue())
        print singleton.cut_y_percent
        config = ConfigParser()
        config.optionxform = str
        config.read('TestFocus.ini')
        config.set('cut', 'number', self.m_txtCut.GetValue())
        config.set('ip', 'ip1', self.m_txtIP1.GetValue())
        config.set('ip', 'ip2', self.m_txtIP2.GetValue())
    
        config.set('golden_sample', 'sample1', singleton.fv[1])
        config.set('golden_sample', 'sample2', singleton.fv[2])
        config.set('golden_sample', 'sample3', singleton.fv[3])
        config.set('golden_sample', 'sample4', singleton.fv[4])
        config.set('golden_sample', 'sample5', singleton.fv[5])
        config.set('golden_sample', 'sample0', singleton.fv[0])
        config.set('cut', 'xPercent', self.m_txtCutX.GetValue())
        config.set('cut', 'yPercent', self.m_txtCutY.GetValue())

        with open('TestFocus.ini', 'w') as configfile:
            config.write(configfile)

    def __set_color(self, ctrlItem, color):
        ctrlItem.SetBackgroundColour(color)

    def __set_mjpg(self, ip):
        url = 'http://%s%s'%(self.ip, '/cgi/test_video.cgi')
        headers = {'content-type': 'text/html'}
        response = requests.get(url, headers=headers, timeout=5)

        print response
        print response.text

    def __conn_test(self, ip):
        return True

    def __connect(self, ip):
        self.__clear_singleton()
        self.btn_evt.start_fv()
        if not self.__conn_test(ip): 
            #TODO show msg and return
            return

        # url = "rtsp://administrator:@172.19.16.88/defaultPrimary?streamType=u"
        url = "rtsp://%s:%s@%s/defaultPrimary?streamType=u"%(self.m_txtUser.GetValue(), self.m_txtPwd.GetValue(), ip)
        # rtsp://172.19.1.215:8900/live
        url = 'rtsp://%s:8900/live'%ip
        print url
        self.Media = self.Instance.media_new(url)
        self.player.set_media(self.Media)
        self.player.set_hwnd(self.panel_view.GetHandle())
        self.player.play()
        # self.singleton.stop = False
    
    def __calculateFV(self, ip):

        fv = Calculate_FV(ip, host=self.m_txtUser.GetValue(), pwd=self.m_txtPwd.GetValue())
        # fv = Calculate_FV("172.19.16.88", realm=self.parameters["serialNumber"])
        ctrlFV = [getattr(self, "m_stxt_score%d"%i) for i in range(6)]
        ctrlImg = [getattr(self, "m_bmpStatus%d"%i) for i in range(6)]
        #ctrlDrawImg = getattr(self, "m_drawLineImg")

        fv.run(ctrlFV, ctrlImg)
        
    def __init_UI(self):
        for i in range(6):
            control = getattr(self, "m_stxt_area%d"%i)
            control.SetLabel(UI_INIT["m_stxt_area%d"%i].decode('utf-8').encode('cp950'))
        self.__clear_score()
        self.__init_status_img()
        # self.__init_show_img()

    def __clear_score(self):
        for i in range(6):
            control = getattr(self, "m_stxt_score%d"%i)
            control.SetLabel("0")

    def __init_status_img(self):
        for i in range(6):
            control = getattr(self, "m_bmpStatus%d"%i)
            control.SetBitmap(wx.BitmapFromImage(self.img_fail))

    def __init_show_img(self):
        control = getattr(self, "m_drawLineImg")
        control.SetBitmap(wx.BitmapFromImage(self.img_draw_line))

    def __init_iamge(self):
        self.img_pass = wx.Image("img/ok.png", wx.BITMAP_TYPE_ANY)
        self.img_fail = wx.Image("img/fail.png", wx.BITMAP_TYPE_ANY)
        self.img_warning = wx.Image("img/warning.png", wx.BITMAP_TYPE_ANY)
        #self.img_draw_line = wx.Image("img/ok.png", wx.BITMAP_TYPE_ANY)

    def __clear_singleton(self):
        self.singleton.max_fv = [0]*6
        self.singleton.fv = [0]*6
        self.singleton.stop = False
        self.singleton.stop_fv = False
        self.singleton.update_img = False
        # print self.singleton.max_fv
        # print self.singleton.fv

###########################################################################
## Class dlg_FV_lite
###########################################################################

class dlg_FV_lite ( wx.Frame ):
    
    def __init__( self ):
        wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = u"Focus Assistant Lite", pos = wx.DefaultPosition, size = wx.Size( 1280,995 ), style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX  )#
        

        panel = wx.Panel(self, -1, size=(1280,995))
        config = ConfigParser()
        config.optionxform = str
        config.read('TestFocus.ini')
        singleton = Singleton.get_instance()
       

        self.ruler1 = RC.RulerCtrl(panel, -1, orient=wx.HORIZONTAL, style=wx.SUNKEN_BORDER)
        self.ruler2 = RC.RulerCtrl(panel, -1, orient=wx.VERTICAL, style=wx.SUNKEN_BORDER)
        self.ruler2.SetRange(-2.55,10.0)
        bigmainsizer = wx.BoxSizer(wx.VERTICAL)
        mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        leftsizer = wx.BoxSizer(wx.VERTICAL)
        bottomleftsizer = wx.BoxSizer(wx.HORIZONTAL)
        topsizer = wx.BoxSizer(wx.HORIZONTAL )


        leftsizer.Add((20, 20), 0, wx.ADJUST_MINSIZE, 0)
        topsizer.Add((39, 0), 0, wx.ADJUST_MINSIZE, 0)
        topsizer.Add(self.ruler1, 1, wx.EXPAND, 0)
        topsizer.Add((270, 0), 0, wx.ADJUST_MINSIZE, 0)
        leftsizer.Add(topsizer, 0, wx.EXPAND, 0)

        bottomleftsizer.Add((10, 0))
        bottomleftsizer.Add(self.ruler2, 0, wx.EXPAND, 0)
        
        self.panel_view = panel_view(panel)
        panel2 = panel_status(panel, self.panel_view)
        bottomleftsizer.Add(self.panel_view)
        m_staticline1 = wx.StaticLine( panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        bottomleftsizer.Add( m_staticline1, 0, wx.EXPAND |wx.ALL, 2 )
        bottomleftsizer.Add(panel2)

        leftsizer.Add(bottomleftsizer, 1, wx.EXPAND, 0)
        mainsizer.Add(leftsizer, 3, wx.EXPAND, 0)
        panel.SetSizer(mainsizer)

    def __del__( self ):
        pass




if __name__ == "__main__":
    app = wx.App(False)
    frame = dlg_FV_lite()
    frame.Show()
    app.MainLoop()

    print os.system("taskkill /f /im python.exe")