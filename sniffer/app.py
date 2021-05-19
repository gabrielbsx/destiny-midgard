import io
import scapy.all as scapy
from Security import Decrypt
from Packets import Login

def process_packet(packet):
    bkpPacket = packet
    if packet.haslayer(scapy.Raw) and packet.haslayer(scapy.IP):
        _packet = Decrypt.decrypt(packet.getlayer(scapy.Raw).load)
        AccountLogin = Login.MSG_AccountLogin()
        io.BytesIO(scapy.raw(_packet)).readinto(AccountLogin)
        
        if AccountLogin.PacketHeader.PacketId == 0x20d:
            print('Login: {0}\nSenha: {1}'.format(AccountLogin.AccountName.decode('latin1'), AccountLogin.AccountPassword.decode('latin1')))
            
        else:
            print('Pacote: {0}'.format(hex(AccountLogin.PacketHeader.PacketId)))
            #print(list(bkpPacket))
        
if __name__ == '__main__':
    scapy.sniff(iface='Ethernet', store=False, filter='tcp and port 8281', prn=process_packet)