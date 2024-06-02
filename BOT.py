import pandas as pd

# Load benign dataset
benign_df = pd.read_csv('2.benign.csv')

# Load attack datasets
mirai_scan_df = pd.read_csv('2.mirai.scan.csv')
mirai_ack_df = pd.read_csv('2.mirai.ack.csv')
mirai_syn_df = pd.read_csv('2.mirai.syn.csv')
mirai_udp_df = pd.read_csv('2.mirai.udp.csv')
mirai_udpplain_df = pd.read_csv('2.mirai.udpplain.csv')

