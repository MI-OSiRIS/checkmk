Summary: Client plugins for check-mk used by OSiRIS project
Name: check-mk-agent-plugins
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: System/Monitoring
URL:  http://mathias-kettner.de/check_mk.html
Source0:  check-mk-agent-plugins.tgz 
BuildArch: noarch
Requires: check-mk-agent

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# define the plugin directory for install
%define _plugindir /usr/lib/check_mk_agent/plugins/

%description
CheckMK is a system monitoring tool.  This RPM packages client check plugins used in the OSiRIS project.

%prep
%setup -n check-mk-agent-plugins

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_plugindir}

install * $RPM_BUILD_ROOT%{_plugindir}

%pre

%post 

%clean
rm -rf $RPM_BUILD_ROOT

%files

%defattr(755,root,root,-)
%{_plugindir}/apache_status  
%{_plugindir}/lnx_quota      
%{_plugindir}/mk_inventory.linux  
%{_plugindir}/mk_mysql       
%{_plugindir}/mk_oracle_crs  
%{_plugindir}/nfsexports    
%{_plugindir}/smart
%{_plugindir}/ceph           
%{_plugindir}/lvm            
%{_plugindir}/mk_logins           
%{_plugindir}/mk_oracle      
%{_plugindir}/mk_postgres    
%{_plugindir}/nginx_status  
%{_plugindir}/sslcertificates
%{_plugindir}/dnsclient      
%{_plugindir}/mailman_lists  
%{_plugindir}/mk_logwatch         
%{_plugindir}/mk_oracle_asm  
%{_plugindir}/netstat.linux  

%changelog
* Thu Jan 28 2016 Ben Meekhof <bmeekhof@umich.edu> - 1.0
- Created

