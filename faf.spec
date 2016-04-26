#
# Conditional build:
%bcond_without	tests		# build without tests
%bcond_with	systemd		# systemd
%bcond_without	webui		# webui

%define faf_version 0.12.344+g9ae0
Summary:	Software Problem Analysis Tool
Name:		faf
Version:	%{faf_version}
Release:	0.1
License:	GPL v3+
Group:		Development/Libraries
Source0:	https://fedorahosted.org/released/faf/%{name}-%{version}.tar.xz
# Source0-md5:	ece001cf20798c696a1947796eab37da
URL:		https://github.com/abrt/faf/
BuildRequires:	autoconf
BuildRequires:	intltool
BuildRequires:	libtool
Requires:	pg-semver
Requires:	postgresql
Requires:	postgresql-server
Requires:	python-SQLAlchemy >= 0.8
Requires:	python-argparse
Requires:	python-psycopg2 >= 2.5
Requires:	python-rpm
Requires:	python-setuptools
BuildArch:	noarch
%if %{with tests}
BuildRequires:	createrepo
BuildRequires:	packagedb-cli
BuildRequires:	pg-semver
BuildRequires:	postgresql
BuildRequires:	postgresql-server
BuildRequires:	python-SQLAlchemy >= 0.8
BuildRequires:	python-argparse
BuildRequires:	python-bugzilla
BuildRequires:	python-modules
BuildRequires:	python-psycopg2 >= 2.5
BuildRequires:	python-rpm
BuildRequires:	python-setuptools
BuildRequires:	python-testing.postgresql
BuildRequires:	satyr-python >= 0.16
BuildRequires:	yum
%endif
%if %{with webui}
BuildRequires:	python-bunch
BuildRequires:	python-flask >= 0.10
BuildRequires:	python-flask-openid
BuildRequires:	python-flask-rstpages
BuildRequires:	python-flask-sqlalchemy
BuildRequires:	python-flask-wtf
BuildRequires:	python-jinja2 >= 2.7
BuildRequires:	python-openid-teams
%endif

%if %{_host_cpu} == "x32"
%define	build_arch %{_target_platform}
%else
%define	build_arch %{_host}
%endif

%description
faf is a programmable tool for analysis of packages, packaging issues,
bug reports and other artifacts produced during software development.

%package webui
Summary:	%{name}'s WebUI rewrite
Requires:	%{name} = %{faf_version}
Requires:	apache-mod_wsgi
Requires:	httpd
Requires:	python-bunch
Requires:	python-flask >= 0.10
Requires:	python-flask-openid
Requires:	python-flask-rstpages
Requires:	python-flask-sqlalchemy
Requires:	python-flask-wtf
Requires:	python-jinja2 >= 2.7
Requires:	python-openid-teams

%description webui
A WebUI rewrite

%package problem-coredump
Summary:	%{name}'s coredump plugin
Requires:	%{name} = %{faf_version}
Requires:	satyr-python >= 0.9

%description problem-coredump
A plugin for %{name} handling user-space binary crashes.

%package problem-java
Summary:	%{name}'s java plugin
Requires:	%{name} = %{faf_version}
Requires:	satyr-python >= 0.9

%description problem-java
A plugin for %{name} handling java problems.

%package problem-kerneloops
Summary:	%{name}'s kerneloops plugin
Requires:	%{name} = %{faf_version}
Requires:	satyr-python >= 0.9

%description problem-kerneloops
A plugin for %{name} handling kernel oopses.

%package problem-python
Summary:	%{name}'s python plugin
Requires:	%{name} = %{faf_version}
Requires:	satyr-python >= 0.9

%description problem-python
A plugin for %{name} handling python scripts problems.

%package problem-ruby
Summary:	%{name}'s ruby plugin
Requires:	%{name} = %{faf_version}
Requires:	satyr-python >= 0.16

%description problem-ruby
A plugin for %{name} handling ruby scripts problems.

%package yum
Summary:	%{name}'s yum plugin
Requires:	%{name} = %{faf_version}
Requires:	yum
Requires:	yum-utils

%description yum
A plugin for %{name} implementing unified access to yum repositories.

%package opsys-centos
Summary:	%{name}'s CentOS operating system plugin
Requires:	%{name} = %{faf_version}
Requires:	%{name}-yum = %{faf_version}

%description opsys-centos
A plugin for %{name} implementing support for CentOS operating system.

%package opsys-fedora
Summary:	%{name}'s Fedora operating system plugin
Requires:	%{name} = %{faf_version}
Requires:	koji
Requires:	packagedb-cli

%description opsys-fedora
A plugin for %{name} implementing support for Fedora operating system.

%package opsys-rhel
Summary:	%{name}'s Red Hat Enterprise Linux operating system plugin
Requires:	%{name} = %{faf_version}

%description opsys-rhel
A plugin for %{name} implementing support for Red Hat Enterprise Linux
operating system.

%package action-save-reports
Summary:	%{name}'s save-reports plugin
Requires:	%{name} = %{faf_version}

%description action-save-reports
A plugin for %{name} implementing save-reports action

%package action-archive-reports
Summary:	%{name}'s archive-reports plugin
Requires:	%{name} = %{faf_version}
Requires:	tar
Requires:	xz

%description action-archive-reports
A plugin for %{name} implementing archive-reports action

%package action-create-problems
Summary:	%{name}'s create-problems plugin
Requires:	%{name} = %{faf_version}
Requires:	satyr-python >= 0.9

%description action-create-problems
A plugin for %{name} implementing create-problems action

%package action-shell
Summary:	%{name}'s shell plugin
Requires:	%{name} = %{faf_version}
Requires:	python-ipython-console

%description action-shell
A plugin for %{name} allowing to run IPython shell

%package action-pull-releases
Summary:	%{name}'s pull-releases plugin
Requires:	%{name} = %{faf_version}

%description action-pull-releases
A plugin for %{name} implementing pull-releases action

%package action-pull-reports
Summary:	%{name}'s pull-reports plugin
Requires:	%{name} = %{faf_version}

%description action-pull-reports
A plugin for %{name} implementing pull-reports action

%package action-pull-components
Summary:	%{name}'s pull-components plugin
Requires:	%{name} = %{faf_version}

%description action-pull-components
A plugin for %{name} implementing pull-components action

%package action-pull-associates
Summary:	%{name}'s pull-associates plugin
Requires:	%{name} = %{faf_version}

%description action-pull-associates
A plugin for %{name} implementing pull-associates action

%package action-find-components
Summary:	%{name}'s find-components plugin
Requires:	%{name} = %{faf_version}

%description action-find-components
A plugin for %{name} implementing find-components action

%package action-find-crash-function
Summary:	%{name}'s find-crash-function plugin
Requires:	%{name} = %{faf_version}

%description action-find-crash-function
A plugin for %{name} implementing find-crash-function action

%package action-repo
Summary:	%{name}'s repo plugin
Requires:	%{name} = %{faf_version}

%description action-repo
A plugin for %{name} implementing repoadd, repolist and reposync
actions

%package action-retrace
Summary:	%{name}'s retrace plugin
Requires:	%{name} = %{faf_version}
Requires:	binutils
Requires:	elfutils >= 0.155

%description action-retrace
A plugin for %{name} implementing retrace action

%package action-arch
Summary:	%{name}'s arch plugin
Requires:	%{name} = %{faf_version}

%description action-arch
A plugin for %{name} implementing archadd action

%package action-sf-prefilter
Summary:	%{name}'s action-sf-prefilter plugin
Requires:	%{name} = %{faf_version}
Requires:	%{name}-solutionfinder-prefilter
Provides:	%{name}-action-kb = 0.12
Obsoletes:	faf-action-kb < 0.12

%description action-sf-prefilter
A plugin for %{name} implementing Solution finder Prefilter actions

%package action-c2p
Summary:	%{name}'s coredump to packages plugin
Requires:	%{name} = %{faf_version}

%description action-c2p
A plugin for %{name} implementing c2p (coredump to packages) action

%package action-bugtracker
Summary:	%{name}'s plugins for bugtracker administration
Requires:	%{name} = %{faf_version}
Requires:	%{name}-bugtracker-bugzilla = %{faf_version}

%description action-bugtracker
A plugin for bugtracker management

%package action-external-faf
Summary:	%{name}'s external-faf plugin
Requires:	%{name} = %{faf_version}

%description action-external-faf
A plugin for %{name} implementing extfaf* actions

%package action-external-faf-clone-bz
Summary:	%{name}'s external-faf-clone-bz plugin
Requires:	%{name} = %{faf_version}
Requires:	%{name}-action-external-faf = %{faf_version}

%description action-external-faf-clone-bz
A plugin for %{name} implementing extfafclonebz action

%package action-add-compat-hashes
Summary:	%{name}'s add-compat-hashes plugin
Requires:	%{name} = %{faf_version}

%description action-add-compat-hashes
A plugin for %{name} implementing addcompathashes action

%package action-mark-probably-fixed
Summary:	%{name}'s mark-probably-fixed plugin
Requires:	%{name} = %{faf_version}

%description action-mark-probably-fixed
A plugin for %{name} implementing mark-probably-fixed action

%package action-stats
Summary:	%{name}'s stats plugin
Requires:	%{name} = %{faf_version}

%description action-stats
A plugin for %{name} implementing statistics generation

%package action-retrace-remote
Summary:	%{name}'s retrace-remote plugin
Requires:	%{name} = %{faf_version}
Requires:	python-requests

%description action-retrace-remote
A plugin for %{name} implementing remote retracing

%package action-attach-centos-bugs
Summary:	%{name}'s attach-centos-bugs plugin
Requires:	%{name} = %{faf_version}
Requires:	%{name}-bugtracker-centos-mantis = %{faf_version}

%description action-attach-centos-bugs
A plugin for %{name} implementing attaching of bugs from CentOS Mantis
bugtracker

%package action-fedmsg-notify
Summary:	%{name}'s fedmsg-notify plugin
Requires:	%{name} = %{faf_version}
Requires:	%{name}-fedmsg = %{faf_version}

%description action-fedmsg-notify
A plugin for %{name} implementing notification into Fedmsg

%package action-cleanup-task-results
Summary:	%{name}'s cleanup-task-results plugin
Requires:	%{name} = %{faf_version}

%description action-cleanup-task-results
A plugin for %{name} implementing cleanup of old task results.

%package bugtracker-bugzilla
Summary:	%{name}'s bugzilla support
Requires:	%{name} = %{faf_version}
Requires:	python-bugzilla

%description bugtracker-bugzilla
A plugin adding bugzilla support to %{name}

%package bugtracker-fedora-bugzilla
Summary:	%{name}'s bugzilla support for Fedora
Requires:	%{name} = %{faf_version}
Requires:	%{name}-bugtracker-bugzilla = %{faf_version}

%description bugtracker-fedora-bugzilla
A plugin adding support for bugzilla used by Fedora

%package bugtracker-rhel-bugzilla
Summary:	%{name}'s bugzilla support for RHEL
Requires:	%{name} = %{faf_version}
Requires:	%{name}-bugtracker-bugzilla = %{faf_version}

%description bugtracker-rhel-bugzilla
A plugin adding support for bugzilla used by Red Hat Enterprise Linux

%package solutionfinder-prefilter
Summary:	%{name}'s solution-finder-prefilter plugin
Requires:	%{name} = %{faf_version}

%description solutionfinder-prefilter
A plugin for %{name} implementing the Prefilter solution finder

%package solutionfinder-probable-fix
Summary:	%{name}'s solution-finder-probable-fix plugin
Requires:	%{name} = %{faf_version}

%description solutionfinder-probable-fix
A plugin for %{name} implementing the Probale Fix solution finder

%package blueprint-symbol-transfer
Summary:	%{name}'s symbol transfer blueprint
Requires:	%{name} = %{faf_version}
Requires:	%{name}-webui = %{faf_version}
Requires:	faf = %{faf_version}

%description blueprint-symbol-transfer
A plugin for %{name} implementing symbol transfer plugin.

%package blueprint-celery-tasks
Summary:	%{name}'s Celery tasks blueprint
Requires:	%{name} = %{faf_version}
Requires:	%{name}-celery-tasks = %{faf_version}
Requires:	%{name}-webui = %{faf_version}
Requires:	faf = %{faf_version}
Requires:	python-bunch

%description blueprint-celery-tasks
A plugin for %{name} implementing Celery tasks blueprint plugin.

%package migrations
Summary:	%{name}'s database migrations
Requires:	%{name} = %{faf_version}
Requires:	python-alembic >= 0.5

%description migrations
Database migrations using alembic

%package bugtracker-mantis
Summary:	%{name}'s mantis support
Requires:	%{name} = %{faf_version}
Requires:	python-suds

%description bugtracker-mantis
A plugin adding mantis support to %{name}

%package bugtracker-centos-mantis
Summary:	%{name}'s Mantis support for CentOS
Requires:	%{name} = %{faf_version}
Requires:	%{name}-bugtracker-mantis = %{faf_version}

%description bugtracker-centos-mantis
A plugin adding support for Mantis used by CentOS

%package fedmsg
Summary:	%{name}'s Fedmsg support
Requires:	%{name} = %{faf_version}
Requires:	fedmsg

%description fedmsg
Base for Fedmsg support.

%package fedmsg-realtime
Summary:	%{name}'s support for realtime Fedmsg notification sending
Requires:	%{name} = %{faf_version}
Requires:	%{name}-fedmsg = %{faf_version}

%description fedmsg-realtime
Support for sending Fedmsg notifications as reports are saved.

%package celery-tasks
Summary:	%{name}'s task queue based on Celery
Requires:	%{name} = %{faf_version}
Requires:	python-celery >= 3.1

%description celery-tasks
Task queue using Celery.

%package celery-tasks-systemd-services
Summary:	%{name}'s Celery task queue systemd services
Requires:	%{name} = %{faf_version}
Requires:	systemd-units

%description celery-tasks-systemd-services
systemd services for the Celery task queue.

%prep
%setup -q

%build
./autogen.sh
%configure \
	--host=%{build_arch} \
	--build=%{build_arch} \
%if %{without systemd}
	--without-systemd
%endif

%{__make}

%if %{with tests}
%{__make} check || ( cat tests/test-suite.log; cat tests/webfaf/test-suite.log; exit 1 )
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# embedded action names
ln -s %{_bindir}/faf $RPM_BUILD_ROOT%{_bindir}/faf-c2p

# %{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/faf
install -d $RPM_BUILD_ROOT%{_sysconfdir}/faf/plugins
install -d $RPM_BUILD_ROOT%{_sysconfdir}/faf/templates

# %{_datadir}
install -d $RPM_BUILD_ROOT%{_datadir}/faf/web/media
install -d $RPM_BUILD_ROOT%{_datadir}/faf/web/static

# /var/spool
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/lob
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/reports
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/reports/incoming
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/reports/deferred
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/reports/saved
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/reports/archive
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/attachments/
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/attachments/incoming
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/attachments/deferred
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/attachments/saved
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/attachments/archive
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/dumpdirs
install -d $RPM_BUILD_ROOT%{_localstatedir}/spool/faf/openid_store

# /var/log
install -d $RPM_BUILD_ROOT%{_localstatedir}/log/faf/

%if %{with systemd}
install -d $RPM_BUILD_ROOT%{systemdtmpfilesdir}
install -d $RPM_BUILD_ROOT/run/faf-celery
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%if 0
%groupadd faf
%useradd -g faf -d /etc/faf -s /sbin/nologin faf
%endif

%if %{with systemd}
%post celery-tasks-systemd-services
%systemd_post faf-celery-beat.service
%systemd_post faf-celery-worker.service

%preun celery-tasks-systemd-services
%systemd_preun faf-celery-beat.service
%systemd_preun faf-celery-worker.service

%postun celery-tasks-systemd-services
%systemd_postun_with_restart faf-celery-beat.service
%systemd_postun_with_restart faf-celery-worker.service
%endif

%post webui
if [ "$1" = 1 ]; then
	# alphanumeric string of 50 characters
	RANDOM_STR=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1)
	sed -i "s#@SECRET_KEY@#$RANDOM_STR#g" %{_sysconfdir}/faf/plugins/web.conf
fi

%files
%defattr(644,root,root,755)
# %{_sysconfdir}
%dir %{_sysconfdir}/faf
%dir %{_sysconfdir}/faf/plugins
%dir %{_sysconfdir}/faf/templates
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/faf.conf

# /var/spool
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/lob
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/reports
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/reports/incoming
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/reports/saved
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/reports/deferred
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/reports/archive
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/attachments
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/attachments/incoming
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/attachments/deferred
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/attachments/saved
%dir %attr(775,faf,faf) %{_localstatedir}/spool/faf/attachments/archive

# /var/log
%dir %attr(775,faf,faf) %{_localstatedir}/log/faf

# %{_bindir}
%attr(755,root,root) %{_bindir}/faf

# %{_prefix}/lib/python*/pyfaf
%dir %{py_sitescriptdir}/pyfaf
%{py_sitescriptdir}/pyfaf/__init__.py*
%{py_sitescriptdir}/pyfaf/checker.py*
%{py_sitescriptdir}/pyfaf/cmdline.py*
%{py_sitescriptdir}/pyfaf/common.py*
%{py_sitescriptdir}/pyfaf/config.py*
%{py_sitescriptdir}/pyfaf/local.py*
%{py_sitescriptdir}/pyfaf/retrace.py*
%{py_sitescriptdir}/pyfaf/rpm.py*
%{py_sitescriptdir}/pyfaf/queries.py*
%{py_sitescriptdir}/pyfaf/ureport.py*
%{py_sitescriptdir}/pyfaf/ureport_compat.py*

%dir %{py_sitescriptdir}/pyfaf/actions
%{py_sitescriptdir}/pyfaf/actions/__init__.py*
%{py_sitescriptdir}/pyfaf/actions/init.py*
%{py_sitescriptdir}/pyfaf/actions/componentadd.py*
%{py_sitescriptdir}/pyfaf/actions/hash_paths.py*
%{py_sitescriptdir}/pyfaf/actions/opsysadd.py*
%{py_sitescriptdir}/pyfaf/actions/opsysdel.py*
%{py_sitescriptdir}/pyfaf/actions/opsyslist.py*
%{py_sitescriptdir}/pyfaf/actions/releaseadd.py*
%{py_sitescriptdir}/pyfaf/actions/releaselist.py*
%{py_sitescriptdir}/pyfaf/actions/releasemod.py*
%{py_sitescriptdir}/pyfaf/actions/match_unknown_packages.py*

%dir %{py_sitescriptdir}/pyfaf/bugtrackers
%{py_sitescriptdir}/pyfaf/bugtrackers/__init__.py*

%dir %{py_sitescriptdir}/pyfaf/opsys
%{py_sitescriptdir}/pyfaf/opsys/__init__.py*

%dir %{py_sitescriptdir}/pyfaf/problemtypes
%{py_sitescriptdir}/pyfaf/problemtypes/__init__.py*

%dir %{py_sitescriptdir}/pyfaf/repos
%{py_sitescriptdir}/pyfaf/repos/__init__.py*

%dir %{py_sitescriptdir}/pyfaf/solutionfinders
%{py_sitescriptdir}/pyfaf/solutionfinders/__init__.py*

%dir %{py_sitescriptdir}/pyfaf/storage
%{py_sitescriptdir}/pyfaf/storage/__init__.py*
%{py_sitescriptdir}/pyfaf/storage/bugzilla.py*
%{py_sitescriptdir}/pyfaf/storage/bugtracker.py*
%{py_sitescriptdir}/pyfaf/storage/custom_types.py*
%{py_sitescriptdir}/pyfaf/storage/debug.py*
%{py_sitescriptdir}/pyfaf/storage/externalfaf.py*
%{py_sitescriptdir}/pyfaf/storage/events.py*
%{py_sitescriptdir}/pyfaf/storage/sf_prefilter.py*
%{py_sitescriptdir}/pyfaf/storage/llvm.py*
%{py_sitescriptdir}/pyfaf/storage/opsys.py*
%{py_sitescriptdir}/pyfaf/storage/mantisbt.py*
%{py_sitescriptdir}/pyfaf/storage/problem.py*
%{py_sitescriptdir}/pyfaf/storage/project.py*
%{py_sitescriptdir}/pyfaf/storage/report.py*
%{py_sitescriptdir}/pyfaf/storage/symbol.py*
%{py_sitescriptdir}/pyfaf/storage/user.py*
%{py_sitescriptdir}/pyfaf/storage/jsontype.py*
%{py_sitescriptdir}/pyfaf/storage/task.py*

%dir %{py_sitescriptdir}/pyfaf/storage/fixtures
%{py_sitescriptdir}/pyfaf/storage/fixtures/__init__.py*
%{py_sitescriptdir}/pyfaf/storage/fixtures/data.py*
%{py_sitescriptdir}/pyfaf/storage/fixtures/randutils.py*

%dir %{py_sitescriptdir}/pyfaf/utils
%{py_sitescriptdir}/pyfaf/utils/__init__.py*
%{py_sitescriptdir}/pyfaf/utils/contextmanager.py*
%{py_sitescriptdir}/pyfaf/utils/date.py*
%{py_sitescriptdir}/pyfaf/utils/decorators.py*
%{py_sitescriptdir}/pyfaf/utils/format.py*
%{py_sitescriptdir}/pyfaf/utils/hash.py*
%{py_sitescriptdir}/pyfaf/utils/parse.py*
%{py_sitescriptdir}/pyfaf/utils/proc.py*
%{py_sitescriptdir}/pyfaf/utils/storage.py*
%{py_sitescriptdir}/pyfaf/utils/web.py*

# %{_datadir}/faf
%dir %{_datadir}/faf
%{_datadir}/faf/fixtures/lob_download_location

%dir %{_datadir}/faf/fixtures/sql
%{_datadir}/faf/fixtures/sql/archs.sql
%{_datadir}/faf/fixtures/sql/archstags.sql
%{_datadir}/faf/fixtures/sql/buildarchs.sql
%{_datadir}/faf/fixtures/sql/builds.sql
%{_datadir}/faf/fixtures/sql/buildstags.sql
%{_datadir}/faf/fixtures/sql/buildsys.sql
%{_datadir}/faf/fixtures/sql/opsys.sql
%{_datadir}/faf/fixtures/sql/opsyscomponents.sql
%{_datadir}/faf/fixtures/sql/opsysreleases.sql
%{_datadir}/faf/fixtures/sql/opsysreleasescomponents.sql
%{_datadir}/faf/fixtures/sql/packages.sql
%{_datadir}/faf/fixtures/sql/taginheritances.sql
%{_datadir}/faf/fixtures/sql/tags.sql

%files webui
%defattr(644,root,root,755)
# %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd/conf.d/faf-web.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/web.conf

# %{_prefix}/lib/python*/pyfaf
%dir %{py_sitescriptdir}/webfaf
%{py_sitescriptdir}/webfaf/__init__.py*
%{py_sitescriptdir}/webfaf/config.py*
%{py_sitescriptdir}/webfaf/dumpdirs.py*
%{py_sitescriptdir}/webfaf/filters.py*
%{py_sitescriptdir}/webfaf/forms.py*
%{py_sitescriptdir}/webfaf/hub.wsgi
%{py_sitescriptdir}/webfaf/login.py*
%{py_sitescriptdir}/webfaf/problems.py*
%{py_sitescriptdir}/webfaf/reports.py*
%{py_sitescriptdir}/webfaf/stats.py*
%{py_sitescriptdir}/webfaf/summary.py*
%{py_sitescriptdir}/webfaf/utils.py*
%{py_sitescriptdir}/webfaf/webfaf_main.py*

%dir %{py_sitescriptdir}/webfaf/blueprints
%{py_sitescriptdir}/webfaf/blueprints/__init__.py*

%dir %{py_sitescriptdir}/webfaf/templates
%{py_sitescriptdir}/webfaf/templates/_helpers.html
%{py_sitescriptdir}/webfaf/templates/403.html
%{py_sitescriptdir}/webfaf/templates/404.html
%{py_sitescriptdir}/webfaf/templates/413.html
%{py_sitescriptdir}/webfaf/templates/500.html
%{py_sitescriptdir}/webfaf/templates/about.rst
%{py_sitescriptdir}/webfaf/templates/base.html
%{py_sitescriptdir}/webfaf/templates/rstpage.html

%dir %{py_sitescriptdir}/webfaf/templates/dumpdirs
%{py_sitescriptdir}/webfaf/templates/dumpdirs/list.html
%{py_sitescriptdir}/webfaf/templates/dumpdirs/new.html

%dir %{py_sitescriptdir}/webfaf/templates/problems
%{py_sitescriptdir}/webfaf/templates/problems/item.html
%{py_sitescriptdir}/webfaf/templates/problems/list.html
%{py_sitescriptdir}/webfaf/templates/problems/list_table_rows.html
%{py_sitescriptdir}/webfaf/templates/problems/multiple_bthashes.html
%{py_sitescriptdir}/webfaf/templates/problems/waitforit.html

%dir %{py_sitescriptdir}/webfaf/templates/reports
%{py_sitescriptdir}/webfaf/templates/reports/associate_bug.html
%{py_sitescriptdir}/webfaf/templates/reports/attach.html
%{py_sitescriptdir}/webfaf/templates/reports/diff.html
%{py_sitescriptdir}/webfaf/templates/reports/item.html
%{py_sitescriptdir}/webfaf/templates/reports/list.html
%{py_sitescriptdir}/webfaf/templates/reports/list_table_rows.html
%{py_sitescriptdir}/webfaf/templates/reports/new.html
%{py_sitescriptdir}/webfaf/templates/reports/waitforit.html

%dir %{py_sitescriptdir}/webfaf/templates/stats
%{py_sitescriptdir}/webfaf/templates/stats/by_date.html

%dir %{py_sitescriptdir}/webfaf/templates/summary
%{py_sitescriptdir}/webfaf/templates/summary/index.html
%{py_sitescriptdir}/webfaf/templates/summary/index_plot_data.html

# %{_datadir}/faf/
%dir %{_datadir}/faf/web
%dir %{_datadir}/faf/web/static
%dir %{_datadir}/faf/web/static/js
%dir %{_datadir}/faf/web/static/css
%{_datadir}/faf/web/static/js/*.js
%{_datadir}/faf/web/static/fonts/*.otf
%{_datadir}/faf/web/static/fonts/*.woff
%{_datadir}/faf/web/static/fonts/*.eot
%{_datadir}/faf/web/static/fonts/*.svg
%{_datadir}/faf/web/static/fonts/*.ttf
%{_datadir}/faf/web/static/css/*.css

# /var/spool/faf
%dir %attr(770, faf, faf) %{_localstatedir}/spool/faf/dumpdirs
%dir %attr(770, faf, faf) %{_localstatedir}/spool/faf/openid_store

%files problem-coredump
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/coredump.conf
%{py_sitescriptdir}/pyfaf/problemtypes/core.py*

%files problem-java
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/java.conf
%{py_sitescriptdir}/pyfaf/problemtypes/java.py*

%files problem-kerneloops
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/kerneloops.conf
%{py_sitescriptdir}/pyfaf/problemtypes/kerneloops.py*

%files problem-python
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/python.conf
%{py_sitescriptdir}/pyfaf/problemtypes/python.py*

%files problem-ruby
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/ruby.conf
%{py_sitescriptdir}/pyfaf/problemtypes/ruby.py*

%files yum
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/yum.conf
%{py_sitescriptdir}/pyfaf/repos/yum.py*

%files opsys-centos
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/centos.conf
%{py_sitescriptdir}/pyfaf/opsys/centos.py*

%files opsys-fedora
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/fedora.conf
%{py_sitescriptdir}/pyfaf/opsys/fedora.py*

%files opsys-rhel
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/opsys/rhel.py*

%files action-save-reports
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/save-reports.conf
%{py_sitescriptdir}/pyfaf/actions/save_reports.py*

%files action-archive-reports
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/archive_reports.py*

%files action-create-problems
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/create-problems.conf
%{py_sitescriptdir}/pyfaf/actions/create_problems.py*

%files action-shell
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/shell.py*

%files action-pull-releases
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/pull_releases.py*

%files action-pull-reports
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/pull-reports.conf
%{py_sitescriptdir}/pyfaf/actions/pull_reports.py*

%files action-pull-components
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/pull_components.py*

%files action-pull-associates
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/pull_associates.py*

%files action-find-components
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/find_components.py*

%files action-find-crash-function
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/find_crash_function.py*

%files action-repo
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/repoadd.py*
%{py_sitescriptdir}/pyfaf/actions/repoassign.py*
%{py_sitescriptdir}/pyfaf/actions/repodel.py*
%{py_sitescriptdir}/pyfaf/actions/repoinfo.py*
%{py_sitescriptdir}/pyfaf/actions/repoimport.py*
%{py_sitescriptdir}/pyfaf/actions/repolist.py*
%{py_sitescriptdir}/pyfaf/actions/repomod.py*
%{py_sitescriptdir}/pyfaf/actions/reposync.py*

%files action-retrace
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/retrace.conf
%{py_sitescriptdir}/pyfaf/actions/retrace.py*

%files action-arch
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/archadd.py*
%{py_sitescriptdir}/pyfaf/actions/archlist.py*

%files action-sf-prefilter
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/sf_prefilter_patadd.py*
%{py_sitescriptdir}/pyfaf/actions/sf_prefilter_patshow.py*
%{py_sitescriptdir}/pyfaf/actions/sf_prefilter_soladd.py*
%{py_sitescriptdir}/pyfaf/actions/sf_prefilter_solshow.py*

%files action-c2p
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/faf-c2p
%{py_sitescriptdir}/pyfaf/actions/c2p.py*

%files action-bugtracker
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/bugtrackerlist.py*
%{py_sitescriptdir}/pyfaf/actions/pull_abrt_bugs.py*
%{py_sitescriptdir}/pyfaf/actions/pull_bug.py*
%{py_sitescriptdir}/pyfaf/actions/update_bugs.py*

%files action-stats
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/stats.py*

%files action-external-faf
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/extfafadd.py*
%{py_sitescriptdir}/pyfaf/actions/extfafshow.py*
%{py_sitescriptdir}/pyfaf/actions/extfafmodify.py*
%{py_sitescriptdir}/pyfaf/actions/extfafdelete.py*
%{py_sitescriptdir}/pyfaf/actions/extfaflink.py*

%files action-external-faf-clone-bz
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/clonebz.conf
%{py_sitescriptdir}/pyfaf/actions/extfafclonebz.py*

%files action-add-compat-hashes
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/addcompathashes.py*

%files action-mark-probably-fixed
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/mark_probably_fixed.py*

%files action-retrace-remote
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/retrace_remote.py*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/retrace-remote.conf

%files action-attach-centos-bugs
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/attach_centos_bugs.py*

%files action-fedmsg-notify
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/fedmsg_notify.py*

%files action-cleanup-task-results
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/actions/cleanup_task_results.py*

%files bugtracker-bugzilla
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/bugtrackers/bugzilla.py*

%files bugtracker-fedora-bugzilla
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/bugtrackers/fedorabz.py*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/fedorabz.conf

%files bugtracker-rhel-bugzilla
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/bugtrackers/rhelbz.py*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/rhelbz.conf

%files solutionfinder-prefilter
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/solutionfinders/prefilter_solution_finder.py*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/sf-prefilter.conf

%files solutionfinder-probable-fix
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/solutionfinders/probable_fix_solution_finder.py*

%files blueprint-symbol-transfer
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/symbol-transfer.conf
%{py_sitescriptdir}/webfaf/blueprints/symbol_transfer.py*

%files blueprint-celery-tasks
%defattr(644,root,root,755)
%{py_sitescriptdir}/webfaf/blueprints/celery_tasks.py*
%{py_sitescriptdir}/webfaf/templates/celery_tasks/action_run.html
%{py_sitescriptdir}/webfaf/templates/celery_tasks/index.html
%{py_sitescriptdir}/webfaf/templates/celery_tasks/results_item.html
%{py_sitescriptdir}/webfaf/templates/celery_tasks/results_list.html
%{py_sitescriptdir}/webfaf/templates/celery_tasks/schedule_item.html

%files migrations
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/storage/migrations/alembic.ini
%{py_sitescriptdir}/pyfaf/storage/migrations/__init__.py*
%{py_sitescriptdir}/pyfaf/storage/migrations/env.py*
%{py_sitescriptdir}/pyfaf/storage/migrations/versions/*.py*
%attr(755,root,root) %{_bindir}/faf-migrate-db

%files bugtracker-mantis
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/bugtrackers/mantisbt.py*

%files bugtracker-centos-mantis
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/bugtrackers/centosmantisbt.py*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/centosmantisbt.conf

%files fedmsg
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/fedmsg.conf

%files fedmsg-realtime
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyfaf/storage/events_fedmsg.py*

%files celery-tasks
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/plugins/celery_tasks.conf
%{py_sitescriptdir}/pyfaf/celery_tasks/__init__.py*
%{py_sitescriptdir}/pyfaf/celery_tasks/schedulers.py*

%if %{with systemd}
%files celery-tasks-systemd-services
%defattr(644,root,root,755)
%{systemdunitdir}/faf-celery-beat.service
%{systemdunitdir}/faf-celery-worker.service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/celery-beat-env.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faf/celery-worker-env.conf
%{systemdtmpfilesdir}/faf-celery-tmpfiles.conf
%dir %attr(775,faf,faf) /run/faf-celery/
%endif
