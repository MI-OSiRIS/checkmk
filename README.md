# checkmk
This repository contains the RPM spec files and source tarballs used to build check-mk-agent-plugins and check-mk-server-checks packages used by OSiRIS.  

The RPMS include hardware specific checks and service specific checks relevant to our project.  
- ceph service checks on pool status and pool usage
- Dell idrac snmp hardware information 
- Dell Openmanage hardware information
- Other miscellaneous checks of interest.  Please review the .spec files in the rpm directory of this repo.  

The checks are part of the agent-plugins or server-checks RPM depending on where they need to be run.  Client checks gather information on the client and then have a corresponding server-side interpreter script.  Sometimes these client checks are actually SNMP queries whose result is interpreted into a service state by the server side script (such as queries of Dell idrac cards or other remote access controllers).  

We do not maintain any of these checks.  They can be built as part of the official Check_mk distribution and we package them to easily distribute to our clients and servers.  With the SPEC files and tarballs included in this repo one can replicate the packages we use.  

Full catalogue of check_mk plugins is on their site:
https://mathias-kettner.de/checkmk_check_catalogue.html

