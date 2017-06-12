# shodanminer
Simple Miner for known shodan scanner ip addresses. Intended to be used as a miner in PaloAtloNetworks Minemeld to create a block list.
Creates feed of IPv4 addresses that will periodically update and withdraw the known scanner ip addresses listed at:
http://wiki.ipfire.org/en/configuration/firewall/blockshodan

To use in your MineMeld configuration, refer to the MineMeld documentation:
Minemeld Quick Tour: https://live.paloaltonetworks.com/t5/MineMeld-Articles/Quick-tour-of-MineMeld-default-config/ta-p/72042
Creating Minemeld Node: https://www.paloaltonetworks.com/documentation/autofocus/autofocus/autofocus_admin_guide/autofocus-apps/minemeld/create-a-minemeld-node#id85e88ccc-eb74-478c-b374-51d526cb69d8
