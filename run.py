from sys import argv
from log_parsers import SSHDLogParser
from geolocation_sources import GeoIPLookup
import plot

if __name__ == "__main__":

    path = argv[1]

    parser = SSHDLogParser()
    ip_addresses = parser.retrieve_ip_addresses_from_log(path)

    g = GeoIPLookup()
    data = g.generate_ip_geolocation_report(ip_addresses)

    plot.plot_chloropleth(data)

    print("done")







