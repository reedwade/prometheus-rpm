VERSION=0.0.1
# modify contrib/redis_exporter.spec if you change the version
#
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild/SOURCES"
	# cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/redis_exporter/releases/download/$(VERSION)/redis_exporter-$(VERSION).linux-amd64.tar.gz -O redis_exporter-$(VERSION).linux-amd64.tar.gz
	cp  code/redis_exporter-$(VERSION).linux-amd64.tar.gz "$(PWD)/rpmbuild/SOURCES"
	cd "$(PWD)/rpmbuild/SOURCES" && mkdir "redis_exporter-$(VERSION).linux-amd64" && tar xzvf redis_exporter-$(VERSION).linux-amd64.tar.gz -C "redis_exporter-$(VERSION).linux-amd64"
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/redis_exporter-$(VERSION).linux-amd64"
	#cp -Rv redis_exporter-0.0.1.linux-amd64 "$(PWD)/rpmbuild/SOURCES/redis_exporter-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz redis_exporter-$(VERSION).linux-amd64.tar.gz redis_exporter-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/redis_exporter.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-redis-exporter -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/redis_exporter/rpmbuild/RPMS/x86_64/redis-exporter-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)
clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-redis-exporter-$(VERSION)"
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-redis-exporter-$(VERSION).linux-amd64.tar.gz"

clean-all:
	rm -rf "$(PWD)/rpmbuild"
