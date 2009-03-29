Summary:	An X Window System based news reader
Name:		xrn
Version:        9.02
Release:        %mkrel 19
License:	BSD
Group:		Networking/News
BuildRequires:	libxaw-devel bison flex libxpm-devel imake
BuildRequires:	libxp-devel

Source0:	%{name}-%{version}.tar.bz2
Patch0:		xrn-9.02-rh.patch
Patch1:		xrn-imake.patch
Patch2:		xrn-9.02-fix-str-fmt.patch

URL:		ftp://ftp.x.org/contrib/applications/xrn
BuildRoot:	%_tmppath/%name-%version-%release-root

# Avoid problems with symlinks - xrn used to think it owned /usr/lib/X11
Requires(pre): x11-server-common > 1.4.0.90-12

%description
A simple Usenet News reader for the X Window System.  Xrn allows you to
point and click your way through reading, replying and posting news
messages.

Install the xrn package if you need a simple news reader for X.

%prep

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
xmkmf
perl -p -i -e "s|XAPPLOADDIR = .*|XAPPLOADDIR = %{_datadir}/X11/app-defaults|" Makefile
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%make install install.man DESTDIR=$RPM_BUILD_ROOT
# A link to ../../../etc/X11/app-defaults is made and named lib in x86_64
APPDEF=%{buildroot}/usr/lib/X11/app-defaults
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


%if %mdkversion < 200900
%post
%{update_menus}
%endif
  
%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.Linux TODO COMMON-PROBLMS COPYRIGHT CREDITS
%{_datadir}/X11/app-defaults/XRn
%_bindir/xrn
%_mandir/man1/xrn.1*
%{_datadir}/applications/mandriva-*.desktop
