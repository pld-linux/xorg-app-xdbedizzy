Summary:	xdbedizzy application - demo of DBE creating a double buffered spinning scene
Summary(pl.UTF-8):	Aplikacja xdbedizzy - demo DBE tworzące podwójnie buforowaną obracaną scenę
Name:		xorg-app-xdbedizzy
Version:	1.1.0
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xdbedizzy-%{version}.tar.bz2
# Source0-md5:	7e730d15679490bd00a8b69e775b3487
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdbedizzy application is a demo of the X11 Double Buffer Extension
(DBE) creating a double buffered spinning scene.

%description -l pl.UTF-8
Aplikacja xdbedizzy to demonstracja rozszerzenie podwójnego
buforowania X11 (Double Buffer Extension), tworząca podwójnie
buforowaną obracaną scenę.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xdbedizzy
%{_mandir}/man1/xdbedizzy.1x*
