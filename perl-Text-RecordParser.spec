#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-RecordParser
Version  : 1.6.5
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/K/KC/KCLARK/Text-RecordParser-1.6.5.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KC/KCLARK/Text-RecordParser-1.6.5.tar.gz
Summary  : 'Parse record-oriented data in a text file'
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Text-RecordParser-bin = %{version}-%{release}
Requires: perl-Text-RecordParser-man = %{version}-%{release}
Requires: perl-Text-RecordParser-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor)
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(IO::Scalar)
BuildRequires : perl(List::MoreUtils)
BuildRequires : perl(Module::Install)
BuildRequires : perl(Readonly)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Text::Autoformat)

%description
NAME
Text::RecordParser - read record-oriented files
SYNOPSIS
use Text::RecordParser;

%package bin
Summary: bin components for the perl-Text-RecordParser package.
Group: Binaries

%description bin
bin components for the perl-Text-RecordParser package.


%package dev
Summary: dev components for the perl-Text-RecordParser package.
Group: Development
Requires: perl-Text-RecordParser-bin = %{version}-%{release}
Provides: perl-Text-RecordParser-devel = %{version}-%{release}
Requires: perl-Text-RecordParser = %{version}-%{release}

%description dev
dev components for the perl-Text-RecordParser package.


%package man
Summary: man components for the perl-Text-RecordParser package.
Group: Default

%description man
man components for the perl-Text-RecordParser package.


%package perl
Summary: perl components for the perl-Text-RecordParser package.
Group: Default
Requires: perl-Text-RecordParser = %{version}-%{release}

%description perl
perl components for the perl-Text-RecordParser package.


%prep
%setup -q -n Text-RecordParser-1.6.5
cd %{_builddir}/Text-RecordParser-1.6.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tab2graph
/usr/bin/tablify
/usr/bin/tabmerge

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::RecordParser.3
/usr/share/man/man3/Text::RecordParser::Object.3
/usr/share/man/man3/Text::RecordParser::Tab.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tab2graph.1
/usr/share/man/man1/tablify.1
/usr/share/man/man1/tabmerge.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Text/RecordParser.pm
/usr/lib/perl5/vendor_perl/5.30.1/Text/RecordParser/Object.pm
/usr/lib/perl5/vendor_perl/5.30.1/Text/RecordParser/Tab.pm
