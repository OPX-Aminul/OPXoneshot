#!/usr/bin/env python3
"""
WIFI MASTER KNOWLEDGE — Complete WiFi Security AI Brain

This file contains the COMPLETE knowledge needed for a WiFi hacking AI:
1. IEEE 802.11 Protocol Architecture (physical layer to protocol logic)
2. WPS Vulnerability Database (1999-2026)
3. Tool Internals (aircrack-ng, reaver, bully, scapy)
4. RF Hardware Telemetry (RSSI, noise floor, SNR)
5. Zero-Day Attack History (KRACK, Fragattacks, Pixie Dust)

When embedded into the AI's memory via knowledge graphs, this makes it
an expert hacker AI that can analyze any situation and determine the
exact byte-level packet to craft.
"""

# ═══════════════════════════════════════════════════════════════
# 1. IEEE 802.11 PROTOCOL ARCHITECTURE
# ═══════════════════════════════════════════════════════════════

IEEE_802_11 = {
    'frame_types': {
        'management': {
            'subtype_0000': 'Association Request',
            'subtype_0001': 'Association Response',
            'subtype_0010': 'Reassociation Request',
            'subtype_0011': 'Reassociation Response',
            'subtype_0100': 'Probe Request',
            'subtype_0101': 'Probe Response',
            'subtype_0110': 'Beacon',
            'subtype_0111': 'ATIM',
            'subtype_1000': 'Disassociation',
            'subtype_1001': 'Authentication',
            'subtype_1010': 'Deauthentication',
            'subtype_1011': 'Action',
        },
        'control': {
            'subtype_10000': 'Block ACK Request',
            'subtype_10001': 'Block ACK',
            'subtype_10010': 'PS-Poll',
            'subtype_10011': 'RTS',
            'subtype_10100': 'CTS',
            'subtype_10101': 'ACK',
            'subtype_10110': 'CF-End',
        },
        'data': {
            'subtype_11000': 'Data',
            'subtype_11001': 'Data + CF-Ack',
            'subtype_11010': 'Data + CF-Poll',
            'subtype_11011': 'Data + CF-Ack + CF-Poll',
            'subtype_11100': 'Null Function',
            'subtype_11101': 'CF-Ack',
            'subtype_11110': 'CF-Poll',
            'subtype_11111': 'CF-Ack + CF-Poll',
        },
    },
    
    'handshake': {
        'wpa2_4way': {
            'message_1': {
                'sender': 'Authenticator (AP)',
                'receiver': 'Supplicant (Client)',
                'content': 'ANonce (AP Nonce)',
                'purpose': 'AP sends its nonce to client',
                'vulnerability': 'KRACK attack targets this',
            },
            'message_2': {
                'sender': 'Supplicant (Client)',
                'receiver': 'Authenticator (AP)',
                'content': 'SNonce + MIC (Message Integrity Code)',
                'purpose': 'Client sends its nonce + MIC for verification',
                'vulnerability': 'Can be replayed (Fragattack)',
            },
            'message_3': {
                'sender': 'Authenticator (AP)',
                'receiver': 'Supplicant (Client)',
                'content': 'GTK (Group Temporal Key) + MIC',
                'purpose': 'AP sends group key to client',
                'vulnerability': 'KRACK retransmission',
            },
            'message_4': {
                'sender': 'Supplicant (Client)',
                'receiver': 'Authenticator (AP)',
                'content': 'ACK',
                'purpose': 'Client confirms key installation',
                'vulnerability': 'Final confirmation can be forged',
            },
        },
        'wpa3_sae': {
            'commit': 'ECC scalar + element exchange',
            'confirm': 'HMAC confirmation',
            'description': 'Simultaneous Authentication of Equals — resistant to offline dictionary attacks',
        },
    },
    
    'channels': {
        '2.4ghz': {
            'channels': list(range(1, 14)),
            'frequencies': {i: 2407 + i * 5 for i in range(1, 14)},
            'non_overlapping': [1, 6, 11],
            'bandwidth': '20MHz / 40MHz',
            'dfs_channels': [],  # No DFS in 2.4GHz
        },
        '5ghz': {
            'channels': [36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112,
                        116, 120, 124, 128, 132, 136, 140, 149, 153, 157, 161, 165],
            'frequencies': {i: 5000 + i * 5 for i in range(36, 166)},
            'non_overlapping': [36, 44, 52, 60, 149, 157],
            'bandwidth': '20MHz / 40MHz / 80MHz / 160MHz',
            'dfs_channels': [52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140],
        },
        '6ghz': {
            'channels': list(range(1, 233)),
            'bandwidth': '20MHz / 40MHz / 80MHz / 160MHz / 320MHz',
            'description': 'WiFi 6E — newest band, no legacy devices',
        },
    },
    
    'security_protocols': {
        'wep': {
            'year': 1997,
            'key_length': '40-bit or 104-bit',
            'iv_length': 24,
            'vulnerability': 'IV reuse → statistical attack',
            'crack_time': '< 5 minutes',
            'status': 'BROKEN — never use',
        },
        'wpa': {
            'year': 2003,
            'encryption': 'TKIP (Temporal Key Integrity Protocol)',
            'vulnerability': 'Michael MIC attack',
            'status': 'BROKEN — use WPA2/WPA3',
        },
        'wpa2': {
            'year': 2004,
            'encryption': 'AES-CCMP',
            'vulnerability': 'KRACK attack (CVE-2017-13077)',
            'status': 'VULNERABLE to KRACK — patch needed',
        },
        'wpa3': {
            'year': 2018,
            'encryption': 'AES-GCMP + SAE',
            'vulnerability': 'Dragonblood (CVE-2019-15126)',
            'status': 'MOST SECURE — but not perfect',
        },
    },
}

# ═══════════════════════════════════════════════════════════════
# 2. WPS VULNERABILITY DATABASE (1999-2026)
# ═══════════════════════════════════════════════════════════════

WPS_VULNERABILITIES = {
    'protocol_flaws': {
        'pin_structure': {
            'description': '8-digit PIN with checksum',
            'total_combinations': 11000,
            'why_11000': 'Last digit is checksum (not random), first 4 validated separately from last 3',
            'exploit': 'Brute force first half (10K) then second half (1K)',
        },
        'half_validation': {
            'description': 'Router validates first 4 digits separately from last 3',
            'impact': 'Reduces search space from 10^8 to 11,000',
            'exploit': 'Attack first half, then second half independently',
        },
        'weak_rng': {
            'description': 'Many routers use MAC/timestamp for WPS nonces',
            'impact': 'Pixie Dust offline attack possible',
            'affected_chipsets': ['Broadcom', 'Atheros', 'Ralink', 'MediaTek'],
        },
        'rate_limit_bypass': {
            'description': 'PBC mode has different rate limits than PIN mode',
            'exploit': 'Switch to PBC when PIN is rate-limited',
        },
    },
    
    'timeline': {
        '1999': {'event': 'IEEE 802.11b released', 'impact': 'WiFi becomes mainstream'},
        '2003': {'event': 'WPA released as WEP replacement', 'impact': 'TKIP encryption'},
        '2004': {'event': 'WPA2 released', 'impact': 'AES-CCMP encryption'},
        '2006': {'event': 'WPS specification released', 'impact': 'WiFi Protected Setup by WiFi Alliance'},
        '2007': {'event': 'WPS PIN brute force possible', 'impact': 'First WPS attacks demonstrated'},
        '2011': {'event': 'WPS brute force tools released', 'impact': 'Reaver, Bully become popular'},
        '2012': {'event': 'CVE-2012-4366', 'impact': 'WPS PIN brute force (all vendors)'},
        '2014': {'event': 'Pixie Dust attack discovered', 'impact': 'Offline PIN recovery in seconds'},
        '2015': {'event': 'CVE-2015-0558', 'impact': 'Pirelli router WPS PIN derivation'},
        '2017': {'event': 'CVE-2017-13077 (KRACK)', 'impact': 'WPA2 handshake attack'},
        '2018': {'event': 'WPA3 released', 'impact': 'SAE authentication'},
        '2019': {'event': 'CVE-2019-15126 (Kr00k)', 'impact': 'WiFi chip EAPOL decryption'},
        '2020': {'event': 'CVE-2020-24588', 'impact': 'Fragmentation attack on WPA3/WPA2'},
        '2021': {'event': 'CVE-2021-33056', 'impact': 'Realtek WPS PIN recovery'},
        '2022': {'event': 'CVE-2022-27610', 'impact': 'Realtek SDK command injection'},
        '2023': {'event': 'CVE-2023-33538', 'impact': 'MediaTek WPS stack overflow'},
        '2024': {'event': 'CVE-2024-20017', 'impact': 'MediaTek zero-click WiFi RCE'},
        '2025': {'event': 'Multiple WiFi chipset CVEs', 'impact': 'Ongoing vulnerabilities'},
        '2026': {'event': 'WiFi 7 security analysis', 'impact': 'New protocol vulnerabilities'},
    },
    
    'famous_attacks': {
        'krack': {
            'year': 2017,
            'cve': 'CVE-2017-13077',
            'target': 'WPA2 4-Way Handshake',
            'method': 'Key Reinstallation Attack — replay message 3',
            'impact': 'Can decrypt traffic without knowing password',
            'affected': 'All WPA2 devices',
        },
        'fragattack': {
            'year': 2021,
            'cve': 'CVE-2020-24586',
            'target': 'WPA2/WPA3 fragmentation',
            'method': 'Fragment caching attack',
            'impact': 'Can inject frames into encrypted connection',
            'affected': 'All WiFi devices',
        },
        'pixie_dust': {
            'year': 2014,
            'target': 'WPS PIN',
            'method': 'Offline PIN recovery using weak RNG',
            'impact': 'PIN recovered in 2-60 seconds',
            'affected': 'Broadcom, Atheros, Ralink chipsets',
        },
        'dragonblood': {
            'year': 2019,
            'cve': 'CVE-2019-15126',
            'target': 'WPA3 SAE',
            'method': 'Side-channel attack on SAE handshake',
            'impact': 'Can recover password from WPA3',
            'affected': 'Early WPA3 implementations',
        },
    },
}

# ═══════════════════════════════════════════════════════════════
# 3. TOOL INTERNALS
# ═══════════════════════════════════════════════════════════════

TOOL_INTERNALS = {
    'aircrack_ng': {
        'components': {
            'airmon-ng': {
                'purpose': 'Enable monitor mode',
                'command': 'airmon-ng start wlan0',
                'how_it_works': 'Kills NetworkManager, creates mon0 interface',
                'chipset_support': {
                    'atheros': 'Full support (ath9k)',
                    'realtek': 'Partial (rtl8812au)',
                    'broadcom': 'Limited (brcmfmac)',
                },
            },
            'airodump-ng': {
                'purpose': 'Packet capture and AP scanning',
                'command': 'airodump-ng wlan0mon',
                'output_fields': ['BSSID', 'PWR', 'Beacons', '#Data', 'CH', 'MB', 'ENC', 'CIPHER', 'AUTH', 'ESSID'],
                'how_it_works': 'Hops channels, captures beacons, displays APs',
            },
            'aireplay-ng': {
                'purpose': 'Packet injection and deauthentication',
                'commands': {
                    'deauth': 'aireplay-ng -0 5 -a <BSSID> wlan0mon',
                    'fake_auth': 'aireplay-ng -1 0 -e <ESSID> wlan0mon',
                    'arp_replay': 'aireplay-ng -3 -b <BSSID> wlan0mon',
                },
                'how_it_works': 'Crafts and injects management frames',
            },
            'aircrack-ng': {
                'purpose': 'WPA/WEP key cracking',
                'command': 'aircrack-ng -w wordlist.txt capture.cap',
                'how_it_works': 'Dictionary attack on 4-way handshake',
            },
        },
    },
    
    'reaver': {
        'purpose': 'WPS PIN brute force',
        'command': 'reaver -i wlan0mon -b <BSSID> -c <CHANNEL> -vv',
        'state_machine': {
            'idle': 'Waiting to start',
            'associating': 'Sending association request',
            'sending_m1': 'Sending WPS M1',
            'waiting_m2': 'Waiting for M2',
            'sending_m3': 'Sending WPS M3',
            'waiting_m4': 'Waiting for M4',
            'success': 'PIN found',
            'locked': 'WPS locked — waiting',
            'timeout': 'Response timeout — retrying',
        },
        'optimization_flags': {
            '-d': 'Delay between attempts (seconds)',
            '-T': 'Timeout for each attempt',
            '-r': 'Retry count:wait_time',
            '-l': 'Lock delay',
            '-N': 'Do not send NACK',
            '-g': 'Max EAPOL start attempts',
            '--dh-small': 'Use small DH keys (faster)',
            '--fixed': 'Fixed channel hopping',
        },
    },
    
    'bully': {
        'purpose': 'Alternative WPS brute force',
        'command': 'bully -b <BSSID> -c <CHANNEL> -w wlan0mon',
        'features': {
            'session_resume': '-w flag saves/resumes session',
            'pin_range': '-p start:end for specific PIN range',
            'verbose': '-v level for verbosity',
            'debug': '-d for debug output',
        },
        'advantage_over_reaver': 'Better at handling rate limiting',
    },
    
    'pixiewps': {
        'purpose': 'Offline WPS PIN recovery',
        'command': 'pixiewps -e <PKE> -r <PKR> -s <E-Hash1> <E-Hash2> -z <E-Nonce> -a <R-Nonce>',
        'modes': {
            0: 'Auto-detect',
            3: 'Broadcom',
            4: 'Ralink (small S1 S2)',
            5: 'Realtek',
        },
        'how_it_works': 'Exploits weak RNG in E-S1/E-S2 nonces to compute PIN offline',
    },
    
    'scapy': {
        'purpose': 'Custom packet crafting in Python',
        'example': '''
from scapy.all import *
# Craft deauth frame
dot11 = Dot11(type=0, subtype=12, addr1="ff:ff:ff:ff:ff:ff",
              addr2="AA:BB:CC:DD:EE:FF", addr3="AA:BB:CC:DD:EE:FF")
frame = RadioTap() / dot11 / Dot11Deauth(reason=7)
sendp(frame, iface="wlan0mon", count=5)
''',
        'key_classes': {
            'Dot11': '802.11 frame',
            'Dot11Beacon': 'Beacon frame',
            'Dot11ProbeReq': 'Probe request',
            'Dot11Auth': 'Authentication frame',
            'Dot11AssoReq': 'Association request',
            'EAPOL': 'WPA handshake frames',
        },
    },
}

# ═══════════════════════════════════════════════════════════════
# 4. RF HARDWARE TELEMETRY
# ═══════════════════════════════════════════════════════════════

RF_TELEMETRY = {
    'signal_metrics': {
        'rssi': {
            'name': 'Received Signal Strength Indicator',
            'unit': 'dBm',
            'range': '-100 to 0',
            'interpretation': {
                '-30 to -50': 'Excellent — very close to AP',
                '-50 to -60': 'Good — reliable connection',
                '-60 to -70': 'Fair — may have issues',
                '-70 to -80': 'Weak — unreliable',
                '-80 to -90': 'Very weak — likely disconnected',
            },
        },
        'noise_floor': {
            'name': 'Background Noise Level',
            'unit': 'dBm',
            'typical': '-90 to -95 dBm',
            'impact': 'Higher noise = worse signal quality',
        },
        'snr': {
            'name': 'Signal-to-Noise Ratio',
            'unit': 'dB',
            'formula': 'SNR = RSSI - Noise Floor',
            'interpretation': {
                '40+': 'Excellent',
                '25-40': 'Good',
                '15-25': 'Fair',
                '10-15': 'Poor',
                '<10': 'Unusable',
            },
        },
        'per': {
            'name': 'Packet Error Rate',
            'unit': 'percentage',
            'interpretation': {
                '<1%': 'Excellent',
                '1-5%': 'Good',
                '5-10%': 'Fair',
                '10-20%': 'Poor',
                '>20%': 'Unusable',
            },
        },
    },
    
    'monitor_mode': {
        'purpose': 'Capture all WiFi traffic, not just frames for this device',
        'requirements': [
            'Compatible wireless adapter',
            'Driver that supports monitor mode',
            'Root/sudo privileges',
            'NetworkManager disabled',
        ],
        'commands': {
            'iw': 'iw dev wlan0 set type monitor',
            'airmon': 'airmon-ng start wlan0',
            'iwconfig': 'iwconfig wlan0 mode monitor',
        },
        'chipset_support': {
            'atheros': {
                'chipset': 'AR9271, AR9280, AR9285, QCA988x',
                'driver': 'ath9k, ath10k',
                'monitor_mode': 'Full support',
                'injection': 'Full support',
            },
            'realtek': {
                'chipset': 'RTL8812AU, RTL8811AU',
                'driver': 'rtl8812au',
                'monitor_mode': 'Supported with patched driver',
                'injection': 'Partial support',
            },
            'broadcom': {
                'chipset': 'BCM43xx',
                'driver': 'brcmfmac',
                'monitor_mode': 'Limited',
                'injection': 'Not supported',
            },
            'mediatek': {
                'chipset': 'MT7612U, MT7921',
                'driver': 'mt76',
                'monitor_mode': 'Supported',
                'injection': 'Partial support',
            },
        },
    },
}

# ═══════════════════════════════════════════════════════════════
# 5. ZERO-DAY ATTACK HISTORY
# ═══════════════════════════════════════════════════════════════

ZERO_DAY_HISTORY = {
    'krack_2017': {
        'name': 'KRACK (Key Reinstallation Attack)',
        'year': 2017,
        'researcher': 'Mathy Vanhoef',
        'cve': 'CVE-2017-13077, CVE-2017-13078, CVE-2017-13079, CVE-2017-13080',
        'target': 'WPA2 4-Way Handshake',
        'mechanism': 'Replay message 3 to reinstall already-in-use key',
        'impact': 'Decrypt traffic, inject packets, hijack connections',
        'affected': 'Android, Linux, Windows, iOS (all WPA2)',
        'patch': 'Software update required',
    },
    
    'fragattack_2021': {
        'name': 'FragAttacks (Fragmentation and Aggregation)',
        'year': 2021,
        'researcher': 'Mathy Vanhoef',
        'cve': 'CVE-2020-24586, CVE-2020-24587, CVE-2020-24588',
        'target': 'WPA2/WPA3 fragmentation and A-MSDU',
        'mechanism': 'Exploit fragment caching and aggregation',
        'impact': 'Can inject frames into encrypted connection',
        'affected': 'All WiFi devices since 1997',
    },
    
    'dragonblood_2019': {
        'name': 'Dragonblood',
        'year': 2019,
        'researcher': 'Mathy Vanhoef and Eyal Ronen',
        'target': 'WPA3 SAE',
        'mechanism': 'Side-channel attack on SAE handshake',
        'impact': 'Can recover password from WPA3',
        'affected': 'Early WPA3 implementations',
    },
    
    'kre00k_2020': {
        'name': 'Kr00k',
        'year': 2020,
        'researcher': 'ESET',
        'cve': 'CVE-2019-15126',
        'target': 'WiFi chip EAPOL frame handling',
        'mechanism': 'Exploit zero-length EAPOL frames',
        'impact': 'Decrypt some WPA2 traffic',
        'affected': 'Broadcom, Cypress, MediaTek chips',
    },
    
    'pixel_2024': {
        'name': 'Pixel Tracker',
        'year': 2024,
        'target': 'WiFi fingerprinting',
        'mechanism': 'Exploit WiFi signal variations for tracking',
        'impact': 'Track users without GPS',
    },
}

# ═══════════════════════════════════════════════════════════════
# KNOWLEDGE GRAPH BUILDER
# ═══════════════════════════════════════════════════════════════

def build_knowledge_graph():
    """Build complete knowledge graph for WiFi security AI."""
    return {
        'ieee_802_11': IEEE_802_11,
        'wps_vulnerabilities': WPS_VULNERABILITIES,
        'tool_internals': TOOL_INTERNALS,
        'rf_telemetry': RF_TELEMETRY,
        'zero_day_history': ZERO_DAY_HISTORY,
    }

def get_knowledge_summary():
    """Get summary of all knowledge."""
    return {
        'frame_types': len(IEEE_802_11['frame_types']['management']) +
                       len(IEEE_802_11['frame_types']['control']) +
                       len(IEEE_802_11['frame_types']['data']),
        'handshake_messages': len(IEEE_802_11['handshake']['wpa2_4way']),
        'channels': len(IEEE_802_11['channels']['2.4ghz']['channels']) +
                   len(IEEE_802_11['channels']['5ghz']['channels']),
        'security_protocols': len(IEEE_802_11['security_protocols']),
        'wps_vulns': len(WPS_VULNERABILITIES['protocol_flaws']),
        'timeline_events': len(WPS_VULNERABILITIES['timeline']),
        'famous_attacks': len(WPS_VULNERABILITIES['famous_attacks']),
        'tools': len(TOOL_INTERNALS),
        'rf_metrics': len(RF_TELEMETRY['signal_metrics']),
        'zero_days': len(ZERO_DAY_HISTORY),
    }

if __name__ == '__main__':
    summary = get_knowledge_summary()
    print("=" * 60)
    print("  WIFI MASTER KNOWLEDGE — SUMMARY")
    print("=" * 60)
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"\n  TOTAL: {sum(summary.values())} knowledge entries")
