VERSION=`grep "__version__" qvevri/__init__.py | cut -d" " -f 3 | sed 's|"\(.*\)"|\1|'`

all:
	export GITBRANCH=master
	debuild
	debclean

build:
	gbp buildpackage --git-debian-branch=${GITBRANCH}

clean:
	debclean

test:
	rm tests/fixtures/pga.db -f
	nosetests
	flake8 qvevri

cover:
	rm tests/fixtures/pga.db -f
	rm tests/coverage/ -rf
	nosetests --with-coverage --cover-package=qvevri --cover-html --cover-html-dir=tests/coverage

pgp-renew:
	osc signkey --extend home:strycore
	osc rebuildpac home:strycore --all

changelog-add:
	dch -i

changelog-edit:
	dch -e

upload:
	scp build/qvevri_${VERSION}.tar.xz qvevri.net:/srv/releases/

upload-ppa:
	dput ppa:qvevri-team/qvevri build/qvevri_${VERSION}*_source.changes

upload-staging:
	dput --force ppa:qvevri-team/qvevri-staging build/qvevri_${VERSION}*_source.changes

snap:
	snapcraft clean qvevri -s pull
	snapcraft
