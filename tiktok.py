from TikTokApi import TikTokApi as tiktok
import json       # exporting data

# # Get cookie data
verifyFP = ''

# Instance setup
api = tiktok.get_instance(custom_verify=verifyFP, use_test_endpoints=True)

# Get data by hashtag
trending = api.by_hashtag('python')
print(trending)

