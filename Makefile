# Makefile to create local web server (lighttpd) 
# Convenient for developing in Windows Subsystem for Linux

LIGHTPID = lighttpd.pid
default:
	make -C docs html

deploy: undeploy default lighttpd.conf
	( lighttpd -D -f lighttpd.conf & echo $$! > $(LIGHTPID))

undeploy:
	- if [ -f $(LIGHTPID) ]; then kill $$(cat $(LIGHTPID)); fi

lighttpd.conf: lighttpd.conf.in
	sed "s#%PWD%#$(PWD)/docs/build/html#" lighttpd.conf.in > $@

help:
	echo "Targets:"
	echo "   default - create html documentation in docs subdir"
	echo "   deploy - create docs, run lighttpd on port 3000 (kill lighttpd if necessary)"
	echo "   undeploy - kill lighttpd"
