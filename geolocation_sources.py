import subprocess
from re import findall
from iso3166 import countries, countries_by_alpha3

class IPGeolocationSource:

    def __init__(self):
        self.description = "Sample description"
        self.countries = countries_by_alpha3.keys()
        self.ip_geolocation_report_template = {c: 0 for c in self.countries}

    def generate_ip_geolocation_report(self, ip_list):

        report = self.ip_geolocation_report_template

        for ip in ip_list:
            country = countries.get(self.geolocate_ip(ip)).alpha3
            report[country] = report.get(country) + 1

        return report

    def geolocate_ip(self, ip):

        pass


class GeoIPLookup(IPGeolocationSource):


    def __init__(self):
        super(GeoIPLookup, self).__init__()

        # can verify credentials here e.g. for login sources

        pass

    def geolocate_ip(self, ip):
        output = subprocess.check_output(["geoiplookup", ip],
                                         stderr=subprocess.STDOUT).decode("UTF-8")

        return findall("(?<=: )(\w{2})(?=,)", output)[0]
















































