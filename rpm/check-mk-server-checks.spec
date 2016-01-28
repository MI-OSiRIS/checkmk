Summary: Server checks for check-mk used by OSiRIS project
Name: check-mk-server-checks
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: System/Monitoring
URL:  http://mathias-kettner.de/check_mk.html
Source0:  check-mk-server-checks.tgz 
BuildArch: noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# The 'source' directory we install to.  Post-install copies from there into sites.
%define _checksinst /omd/check-mk-server-checks
%define _checksdir local/share/check_mk/checks
%define _sites /omd/sites

###   /omd/sites/$(omdsites)/local/share/check_mk/checks/$(omdchecks)"

%description
CheckMK is a system monitoring tool.  This RPM packages server-side check scripts used in the OSiRIS project.  
It will install them to %{_checksinst} and copy to %{_checksdir} under each site in %{_sites}

%prep
%setup -n check-mk-server-checks

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_checksinst}

install * $RPM_BUILD_ROOT%{_checksinst}

%pre

%post 

for site in `ls %{_sites}` 
do
if [ -d %{_sites}/${site}/%{_checksdir} ]
then
echo "Copying checks into site at %{_sites}/${site}/%{_checksdir}" 
/bin/cp -f %{_checksinst}/* %{_sites}/${site}/%{_checksdir}
fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files

%defattr(755,root,root,-)
%{_checksinst}/ceph                     
%{_checksinst}/dell_idrac_cooling     
%{_checksinst}/dell_idrac_sysinfo    
%{_checksinst}/dell_omsa_coolingdevice  
%{_checksinst}/dell_omsa_temp700
%{_checksinst}/cephpools                
%{_checksinst}/dell_idrac_disks       
%{_checksinst}/dell_idrac_vdisk      
%{_checksinst}/dell_omsa_fan            
%{_checksinst}/dell_omsa_vdisk
%{_checksinst}/dell_idrac_fan         
%{_checksinst}/dell_idrac_voltage    
%{_checksinst}/dell_omsa_memory         
%{_checksinst}/pvs
%{_checksinst}/check_nfs                
%{_checksinst}/dell_idrac_memory      
%{_checksinst}/dell_omsa_amperage    
%{_checksinst}/dell_omsa_pdisk         
%{_checksinst}/dell_idrac_amperage      
%{_checksinst}/dell_idrac_processors  
%{_checksinst}/dell_omsa_battery     
%{_checksinst}/dell_omsa_powersupply    
%{_checksinst}/sslcertificates
%{_checksinst}/dell_idrac_battery       
%{_checksinst}/dell_idrac_sensors     
%{_checksinst}/dell_omsa_controller  
%{_checksinst}/dell_omsa_sysinfo        
%{_checksinst}/vgs

%changelog
* Thu Jan 28 2016 Ben Meekhof <bmeekhof@umich.edu> - 1.0
- Created

