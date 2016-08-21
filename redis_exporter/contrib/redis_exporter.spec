%define debug_package %{nil}

Name:		redis-exporter
Version:	0.0.1
Release:	1%{?dist}
Summary:	Prometheus exporter for redis metrics.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/reedwade/redis_exporter
Source0:	https://github.com/reedwade/redis_exporter/fake/redis_exporter-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
Requires:       daemonize
AutoReqProv:	No

%description

Prometheus exporter for redis metrics.

%prep
%setup -q -n redis_exporter-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/var/log/prometheus/
mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/etc/init.d
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
install -m 755 redis_exporter-%{version}.linux-amd64/redis_exporter $RPM_BUILD_ROOT/usr/bin/redis_exporter
install -m 755 contrib/redis_exporter.init $RPM_BUILD_ROOT/etc/init.d/redis_exporter
install -m 644 contrib/redis_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/redis_exporter

%clean

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -s /sbin/nologin \
    -d $RPM_BUILD_ROOT/var/lib/prometheus/ -c "prometheus Daemons" prometheus
exit 0

%post
chgrp prometheus /var/run/prometheus
chmod 774 /var/run/prometheus
chown prometheus:prometheus /var/log/prometheus
chmod 744 /var/log/prometheus

%files
%defattr(-,root,root,-)
/usr/bin/redis_exporter
/etc/init.d/redis_exporter
%config(noreplace) /etc/sysconfig/redis_exporter
/var/run/prometheus
/var/log/prometheus
