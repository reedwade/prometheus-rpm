VERSION=0.0.1
# modify contrib/rabbitmq_exporter.spec if you change the version
#
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild/SOURCES"
	# cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/rabbitmq_exporter/releases/download/$(VERSION)/rabbitmq_exporter-$(VERSION).linux-amd64.tar.gz -O rabbitmq_exporter-$(VERSION).linux-amd64.tar.gz
	cp  code/rabbitmq_exporter-$(VERSION).linux-amd64.tar.gz "$(PWD)/rpmbuild/SOURCES"
	cd "$(PWD)/rpmbuild/SOURCES" && mkdir "rabbitmq_exporter-$(VERSION).linux-amd64" && tar xzvf rabbitmq_exporter-$(VERSION).linux-amd64.tar.gz -C "rabbitmq_exporter-$(VERSION).linux-amd64"
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/rabbitmq_exporter-$(VERSION).linux-amd64"
	#cp -Rv rabbitmq_exporter-0.0.1.linux-amd64 "$(PWD)/rpmbuild/SOURCES/rabbitmq_exporter-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz rabbitmq_exporter-$(VERSION).linux-amd64.tar.gz rabbitmq_exporter-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/rabbitmq_exporter.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-rabbitmq-exporter -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/rabbitmq_exporter/rpmbuild/RPMS/x86_64/rabbitmq-exporter-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)
clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-rabbitmq-exporter-$(VERSION)"
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-rabbitmq-exporter-$(VERSION).linux-amd64.tar.gz"

clean-all:
	rm -rf "$(PWD)/rpmbuild"
