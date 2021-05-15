#-*- coding: utf-8 -*-
import ctypes
from .Header import PacketHeader

class MSG_AccountLogin(ctypes.Structure):
    _fields_ = [
        ('PacketHeader', PacketHeader),
        ('AccountPassword', ctypes.c_char * 12),
        ('AccountName', ctypes.c_char * 16),
        ('Zero', ctypes.c_char * 52),
        ('ClientVersion', ctypes.c_int),
        ('DBNeedSave', ctypes.c_int),
        ('AdapterName', ctypes.c_int * 4),
    ]
    
'''struct MSG_AccountLogin
{
	PacketHeader Header;
	char AccountPassword[12];
	char AccountName[16];
	char Zero[52];
	int  ClientVersion;
	int  DBNeedSave;
	int AdapterName[4];
};'''