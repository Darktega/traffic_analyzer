import socket
import struct
import textwrap
import ethernet
import ipv4
import icmpv4
import ipv6
import icmpv6
import arp
import tcp
import udp

def main():
	op = input('¿Iniciar ciclo de captura? (S/N)')
	
	if (op == 'S'):
		conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

		while (op == 'S'):
			rawData, addr = conn.recvfrom(65535)
			eth = ethernet.Ethernet(rawData)
			print ('Ethernet Frame:')	
			print(eth.getInfo())

			if (getattr(eth, 'type') == 8):
				'Is IPv4'
				ipv4Packet = ipv4.IPv4( getattr(eth, 'ethPayload') )
				print ('IPv4 Datagram:')
				print (ipv4Packet.getInfo())

				if (getattr(ipv4Packet, 'protocol') == 1):
					'Is ICMPv4'
					icmpv4Packet = icmpv4.ICMPv4( getattr(ipv4Packet, 'ipv4Payload') )
					print('ICMPv4 Packet:')
					print(icmpv4Packet.getInfo())

				elif (getattr(ipv4Packet, 'protocol') == 6):
					'Is TCP'
					tcpSegment = tcp.TCP( getattr(ipv4Packet, 'ipv4Payload') )
					print ('TCP Segment:')
					print (tcpSegment.getInfo())

				elif (getattr(ipv4Packet, 'protocol') == 17):
					'Is UDP'
					udpSegment = udp.UDP( getattr(ipv4Packet, 'ipv4Payload') )
					print ('UDP Segment:')
					print (udpSegment.getInfo())

			elif (getattr(eth, 'type') == 1544):
				'Is ARP'
				arpPacket = arp.ARP( getattr(eth, 'ethPayload') )
				print ('ARP Message:')
				print (arpPacket.getInfo())

			elif (getattr(eth, 'type') == 56710):
				'Is IPv6'
				ipv6Packet = ipv6.IPv6( getattr(eth, 'ethPayload') )
				print('IPv6 Packet:')
				print(ipv6Packet.getInfo())

				if (getattr(ipv6Packet, 'nextHeader') == 58):
					'Is ICMPv6'
					icmpv6Packet = icmpv6.ICMPv6( getattr(ipv6Packet, 'ipv6Payload') )
					print('ICMPv6 Packet:')
					print(icmpv6Packet.getInfo())

				elif (getattr(ipv6Packet, 'nextHeader') == 6):
					'Is TCP'
					tcpSegment = tcp.TCP( getattr(ipv6Packet, 'ipv6Payload') )
					print ('TCP Segment:')
					print (tcpSegment.getInfo())

				elif (getattr(ipv6Packet, 'nextHeader') == 17):
					'Is UDP'
					udpSegment = udp.UDP( getattr(ipv6Packet, 'ipv6Payload') )
					print ('UDP Segment:')
					print (udpSegment.getInfo())

main()