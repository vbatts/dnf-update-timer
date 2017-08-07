
pwd := $(shell pwd)

all: rpm srpm


rpm:
	rpmbuild \
		--define '_sourcedir $(pwd)' \
		--define '_specdir $(pwd)' \
		--define '_builddir $(pwd)' \
		--define '_srcrpmdir $(pwd)' \
		--define '_rpmdir $(pwd)' \
		--nodeps \
		-bb ./dnf-update-timer.spec

srpm:
	rpmbuild \
		--define '_sourcedir $(pwd)' \
		--define '_specdir $(pwd)' \
		--define '_builddir $(pwd)' \
		--define '_srcrpmdir $(pwd)' \
		--define '_rpmdir $(pwd)' \
		--nodeps \
		-bs ./dnf-update-timer.spec

clean:
	rm -rf *~ *.rpm noarch
