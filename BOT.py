import pandas as pd

# Load benign dataset
benign_df = pd.read_csv('2.benign.csv')

# Load attack datasets
mirai_scan_df = pd.read_csv('2.mirai.scan.csv')
mirai_ack_df = pd.read_csv('2.mirai.ack.csv')
mirai_syn_df = pd.read_csv('2.mirai.syn.csv')
mirai_udp_df = pd.read_csv('2.mirai.udp.csv')
mirai_udpplain_df = pd.read_csv('2.mirai.udpplain.csv')

mirai_attack_df = pd.concat([mirai_scan_df, mirai_ack_df, mirai_syn_df, mirai_udp_df, mirai_udpplain_df], axis=0)

# Label benign data
benign_df['class'] = 0

# Label attack data
mirai_attack_df['class'] = 1

combined_df = pd.concat([benign_df, mirai_attack_df], axis=0)
