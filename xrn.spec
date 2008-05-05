Summary:	An X Window System based news reader
Name:		xrn
Version:        9.02
Release:        %mkrel 17
License:	BSD
Group:		Networking/News
BuildRequires:	X11-devel, bison, flex, libxpm-devel, xorg-x11 imake

Source0:	%{name}-%{version}.tar.bz2
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
perl -p -i -e "s|XAPPLOADDIR = .*|XAPPLOADDIR = %{_datadir}/X11/app-defaults|" Makefile
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%make install install.man DESTDIR=$RPM_BUILD_ROOT
# A link to ../../../etc/X11/app-defaults is made
APPDEF=%{buildroot}%{_libdir}/X11/app-defaults
if   [ -L $APPDEF ]; then rm    $APPDEF
elif [ -d $APPDEF ]; then rmdir $APPDEF
fi

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-xrn.desktop
[Desktop Entry]
Type=Application
Categories=News;
Name=Xrn
Comment=News reader
Exec=/usr/bin/xrn
Icon=news_section
EOF


%post
%{update_menus}
  
%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.Linux TODO COMMON-PROBLMS COPYRIGHT CREDITS
%{_datadir}/X11/app-defaults/XRn
%_bindir/xrn
%_mandir/man1/xrn.1*
%{_datadir}/applications/mandriva-*.desktop
