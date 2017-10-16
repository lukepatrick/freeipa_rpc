## Basic FreeIPA JSON-RPC client

This was built with the [OpenStack-Helm](https://github.com/openstack/openstack-helm) project
in mind. When setting up OpenStack on Kubernetes a path way in is with Ingress. 
Using FreeIPA as a DNS provider, bulk add the desired Ingress DNS settings to FreeIPA.


A few use examples:

Clone the repository, cd to the directory

    $ pip install -r requirements.txt

Then run the example app to bulk add/del OpenStack DNS entries.


    $ {operation add/del} {user initials} {ipaddress - if add}
    $ python spoc_os_helm_dns.py add lp 1.2.3.4
    
    
    
For your own app, clone the repository and install the ipa_rpc package with PIP
Use the path to the _repo/setup.py_

    pip install -e /freeipa_rpc/ipa_rpc