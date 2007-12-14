Summary:	An X Window System based news reader
Name:		xrn
Version:        9.02
Release:        %mkrel 15
License:	BSD
Group:		Networking/News
BuildRequires:	X11-devel, bison, flex, libxpm-devel, xorg-x11 imake

Source0:	%{name}-%{version}.tar.bz2
Source1:	xrn
Patch0:		xrn-9.02-rh.patch.bz2
Patch1:		xrn-imake.patch.bz2

URL:		ftp://ftp.x.org/contrib/applications/xrn
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
A simple Usenet News reader for the X Window System.  Xrn allows you to
point and click your way through reading, replying and posting news
messages.

Install the xrn package if you need a simple news reader for X.

%prep

%setup -q
%patch0 -p1
%patch1 -p1

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%make install install.man DESTDIR=$RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT/%{_menudir}
install -m 644 %SOURCE1 $RPM_BUILD_ROOT/%{_menudir}



%post
%{update_menus}
  
%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.Linux TODO COMMON-PROBLMS COPYRIGHT CREDITS
%config(noreplace) %_sysconfdir/X11/app-defaults/XRn
%_bindir/xrn
%_mandir/man1/xrn.1*
%_libdir/X11/app-defaults/XRn
%_libdir/X11/app-defaults

%{_menudir}/*


