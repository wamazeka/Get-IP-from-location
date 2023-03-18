import csv
import random
import ipaddress


class IPFaker:

    def __init__(self,
                 blocksfile="GeoLite2-Country-Blocks-IPv4.csv",
                 locationfile="GeoLite2-Country-Locations-en.csv"):

        self.countriesIPblocks = {}
        self.id2code = {}

        with open(locationfile, "r") as f:
            reader = csv.DictReader(f)
            next(reader)
            for row in reader:
                self.id2code[row["geoname_id"]] = row["country_iso_code"]
                self.countriesIPblocks[row["country_iso_code"]] = []

        with open(blocksfile, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.countriesIPblocks[self.id2code[row['geoname_id']]].append(row["network"])
                except:
                    pass

    def getip(self, country="ANY"):
        if country == "ANY":
            country = random.choice(list(self.countriesIPblocks.keys()))

        mask = ipaddress.IPv4Network(random.choice(self.countriesIPblocks[country]))

        network = int(mask.network_address)
        broadcast = int(mask.broadcast_address)

        if mask.prefixlen > 30:
            randid = random.randint(network, broadcast)
        else:
            randid = random.randint(network + 1, broadcast - 1)

        ip = mask._address_class(randid)

        return str(ip)

    def getiplist(self, country="ANY", count=10):
        list = []
        for i in range(count):
            list.append(str(self.getip(country)))
        return list


if __name__ == '__main__':
    ipgetter = IPFaker()

    print(ipgetter.getip())
    print(ipgetter.getip(country='US'))
    print(ipgetter.getiplist(country='IT', count=9000))
