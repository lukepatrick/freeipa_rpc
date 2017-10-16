import ipa_rpc
import sys


# A Records
#
# 1.2.3.4     horizon.os.foo.org
# 1.2.3.4     neutron.os.foo.org
# 1.2.3.4     keystone.os.foo.org
# 1.2.3.4     nova.os.foo.org
# 1.2.3.4     metadata.os.foo.org
# 1.2.3.4     glance.os.foo.org


class helm_dns(object):

    HORIZON = 'horizon'
    KEYSTONE = 'keystone'
    GLANCE = 'glance'
    NEUTRON = 'neutron'
    NOVA = 'nova'
    METADATA = 'metadata'

    DNS_ZONE = ''

    OSDNS = [HORIZON, KEYSTONE, GLANCE, NEUTRON, NOVA, METADATA]

    IPA_SERVER = ''

    USERNAME=""
    PASSWORD=""



    def __init__(self):
        self.myipa = ipa_rpc.ipa(self.IPA_SERVER)
        self.myipa.login(user=self.USERNAME, password=self.PASSWORD)


    def add_dns_for_user(self, user_init, ip_address):

        if not user_init or not ip_address:
            raise Exception("user initials and ip_address must be specified")
        if not self.myipa.is_valid_ipv4_address(address=ip_address):
            raise Exception("ip_address is not valid")

        for app in self.OSDNS:
            a_record_name = "{}.{}".format(app, user_init.lower())

            response = self.myipa.dnsrecord_add(dns_zone=self.DNS_ZONE, record_name=a_record_name,
                                                ip_address=ip_address)

            error = response.get('error')
            if error:
                print a_record_name
                print error

            print "{}.{} added".format(a_record_name, self.DNS_ZONE)

        print "add_dns_for_user for {} and {} success!".format(user_init, ip_address)

    def del_dns_for_user(self, user_init):

        if not user_init:
            raise Exception("user initials must be specified")

        for app in self.OSDNS:
            a_record_name = "{}.{}".format(app, user_init.lower())

            response = self.myipa.dnsrecord_del(dns_zone=self.DNS_ZONE, record_name=a_record_name)

            error = response.get('error')
            if error:
                print a_record_name
                print error

            print "{}.{} deleted".format(a_record_name,self.DNS_ZONE)

        print "del_dns_for_user for {} success!".format(user_init)


def main(argv):
    if argv is None:
        argv = sys.argv
    os_dns = helm_dns()

    if argv[0].lower() == 'add':
        os_dns.add_dns_for_user(user_init=argv[1], ip_address=argv[2])
    elif argv[0].lower() == 'del':
        os_dns.del_dns_for_user(user_init=argv[1])
    else:
        print "nop"


if __name__ == "__main__":
    if sys.argv[1:]:
        main(sys.argv[1:])
    else:
        print "Inputs expected in order: " \
              "{operation add/del} {user initials} {ipaddress - if add}\n " \
              "Example: \n python spoc_os_helm_dns.py add lp 1.2.3.4"

