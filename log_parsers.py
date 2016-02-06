from re import findall


class SSHDLogParser:

    def __init__(self):
        pass

    def retrieve_ip_addresses_from_log(self, path):
        #add path checks
        ip_addresses = []

        fp = open(path, 'r')
        log_text = fp.read()

        ip_addresses.append(findall("(?:sshd\[[0-9]+\]:.+authentication failure.+)(?<=rhost=)(\S+)", log_text))

        return [ip for ip_matches in ip_addresses for ip in ip_matches]


