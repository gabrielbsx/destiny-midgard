#-*- coding: utf-8 -*-
import ctypes

class PacketHeader(ctypes.Structure):
    _fields_ = [
        ('Size', ctypes.c_ushort),
        ('Key', ctypes.c_ubyte),
        ('CheckSum', ctypes.c_ubyte),
        ('PacketId', ctypes.c_ushort),
        ('ClientId', ctypes.c_ushort),
        ('TimeStamp', ctypes.c_uint),
    ]
    
'''struct PacketHeader
{
	unsigned short Size;
	unsigned char Key;
	unsigned char CheckSum;
	unsigned short PacketId;
	unsigned short ClientId;
	unsigned int TimeStamp;
};'''