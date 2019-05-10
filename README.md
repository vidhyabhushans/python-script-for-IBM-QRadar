# python-script-for-IBM-QRadar

Python Script for Custom action in IBM QRadar SIEM.

Before adding in custom action you need to install all modules in IBM QRadar(consol) from cli

pip install netmiko
pip install os
pip install sys
pip install python-ldap

If the custom action taking to much time to execute or the custom action give you time out erroe you need to extend your custom action default timout from QRadar

  extend a custom action default timeout:
1. Using SSH, log in to the QRadar Console as the root user. 
2. To make a backup of the file, type: cp /opt/qradar/conf/nva.conf /root/nva.conf.bak
3. To edit the file, type: vim /opt/qradar/conf/nva.conf (or use the RHEL editor you are most familiar with)
4. Edit the follwing line: CUSTOM_ACTION_TIMEOUT= and change the value from 15 to 30 as a test. I don't know how long these looksup are actually taking, so start with a doubling of the timeframe and see if the lookup completes.
5. Press :wq to save the change using vim.
6. Make the same edit for /store/configservices/staging/globalconfig/nva.conf 
7. Log in to the QRadar user interface.
8. Click the Admin tab.
9. Click the Deploy Changes button.
