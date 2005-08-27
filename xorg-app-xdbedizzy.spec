Summary:	xdbedizzy application
Summary(pl):	Aplikacja xdbedizzy
Name:		xorg-app-xdbedizzy
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xdbedizzy-%{version}.tar.bz2
# Source0-md5:	0ea7a400623520081f0757acb208b7da
Patch0:		xdbedizzy-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdbedizzy application.

%description -l pl
Aplikacja xdbedizzy.

%prep
%setup -q -n xdbedizzy-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
