#!/usr/bin/env python
import ldap
import sys

#ACCOUNTDISABLE = 2
#NORMAL_ACCOUNT = 512
#un = Administrator

te = sys.argv[1]
def testdisable():

    Unametest = ("cn=%s,cn=Users,dc=security-hq-labtwo,dc=net" % te)
#    dn="cn=%s,cn=Users,dc=security-hq-labtwo,dc=net" % (Unametest)
#    ad_u = {}
#    ad_u = l.search_s(Unametest,ldap.SCOPE_SUBTREE)
#    print ad_u
    mod_acct = [(ldap.MOD_REPLACE, 'userAccountControl', '66050')]
    l.modify_s(Unametest, mod_acct)

l = ldap.initialize('ldap://2.2.2.146')
username = "cn=test,cn=Users,dc=labtwo,dc=net"
password = "************"
try:
    l.protocol_version = ldap.VERSION3
    l.set_option(ldap.OPT_NETWORK_TIMEOUT, 10.0)
    l.simple_bind_s(username, password)
    valid = True
#    print l.simple_bind_s(username, password)
#    result = l.search_s(username,ldap.SCOPE_SUBTREE)
#    print type(result)


    testdisable()
    l.unbind_s()

except ldap.LDAPError, error:
    print error
