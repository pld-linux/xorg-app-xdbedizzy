Summary:	xdbedizzy application
Summary(pl):	Aplikacja xdbedizzy
Name:		xorg-app-xdbedizzy
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/app/xdbedizzy-%{version}.tar.bz2
# Source0-md5:	ea4b09e575caaf6996196c3cfd2532cd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdbedizzy application.

%description -l pl
Aplikacja xdbedizzy.

%prep
%setup -q -n xdbedizzy-%{version}

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1x*
