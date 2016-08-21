%define debug_package %{nil}

Name:		rabbitmq-exporter
Version:	0.0.1
Release:	1%{?dist}
Summary:	Prometheus exporter for RabbitMQ metrics.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/reedwade/rabbitmq_exporter
Source0:	https://github.com/reedwade/rabbitmq_exporter/fake/rabbitmq_exporter-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
Requires:       daemonize
AutoReqProv:	No

%description

Prometheus exporter for RabbitMQ metrics.

%prep
%setup -q -n rabbitmq_exporter-%{version}.linux-amd64

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
install -m 755 rabbitmq_exporter-%{version}.linux-amd64/rabbitmq_exporter $RPM_BUILD_ROOT/usr/bin/rabbitmq_exporter
install -m 755 contrib/rabbitmq_exporter.init $RPM_BUILD_ROOT/etc/init.d/rabbitmq_exporter
install -m 644 contrib/rabbitmq_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/rabbitmq_exporter
install -m 644 rabbitmq_exporter-%{version}.linux-amd64/rabbitmq_exporter.json $RPM_BUILD_ROOT/etc/prometheus/rabbitmq_exporter.json

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
/usr/bin/rabbitmq_exporter
/etc/init.d/rabbitmq_exporter
/etc/prometheus/rabbitmq_exporter.json
%config(noreplace) /etc/sysconfig/rabbitmq_exporter
/var/run/prometheus
/var/log/prometheus
