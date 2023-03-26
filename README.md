# Get-IP-from-location

This project is for generating random IP addresses from certain location (coutry) based on MaxMind CSV databases

Easy to change for cities. 

## Using

1. Just download script
2. Download MaxMind CSV databases from their website or another way
3. Use script

```
ipgetter = IPFaker()
# OR
ipgetter = IPFaker(blocksFile="GeoLite2-Country-Blocks-IPv4.csv",locationFile="GeoLite2-Country-Locations-en.csv")

print(ipgetter.getip())
print(ipgetter.getip(country='US')) # ISO code, can see in Locations file
print(ipgetter.getiplist(country='IT', count=14))

```

Very simple, return is String or List
