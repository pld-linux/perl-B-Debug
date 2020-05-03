#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	B
%define		pnam	Debug
Summary:	B::Debug - walk Perl syntax tree, printing debug info about ops
Summary(pl.UTF-8):	B::Debug - przejście po drzewie składniowym Perla z wypisywaniem informacji o operacjach
Name:		perl-B-Debug
Version:	1.26
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/B/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	260ec0e2c2b18af1d42911bfaf6b7477
URL:		https://metacpan.org/release/B-Debug
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Walk Perl syntax tree, printing debug info about ops.

%description -l pl.UTF-8
Przejście po drzewie składniowym Perla z wypisywaniem informacji
diagnostycznych o operacjach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/B/Debug.pm
%{_mandir}/man3/B::Debug.3pm*
