import io
import scapy.all as scapy
from Security import Decrypt
from Packets import Login

def process_packet(packet):
    if packet.haslayer(scapy.Raw) and packet.haslayer(scapy.IP):
        _packet = Decrypt.decrypt(packet.getlayer(scapy.Raw).load)
        AccountLogin = Login.MSG_AccountLogin()
        io.BytesIO(scapy.raw(_packet)).readinto(AccountLogin)
        
        print(hex(AccountLogin.PacketHeader.PacketId))
        
        print(AccountLogin.AccountPassword)
        
if __name__ == '__main__':
    scapy.sniff(iface='Ethernet', store=False, filter='tcp and port 8281', prn=process_packet)