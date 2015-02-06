Summary:	An X Window System based news reader
Name:		xrn
Version:        9.02
Release:        21
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


%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 9.02-20mdv2010.0
+ Revision: 446269
- rebuild

* Sun Mar 29 2009 Funda Wang <fundawang@mandriva.org> 9.02-19mdv2009.1
+ Revision: 362105
- br libxp
- fix str fmt

* Sat Aug 09 2008 Thierry Vignaud <tvignaud@mandriva.com> 9.02-19mdv2009.0
+ Revision: 269841
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue May 06 2008 Paulo Andrade <pcpa@mandriva.com.br> 9.02-18mdv2009.0
+ Revision: 202137
- Another x86_64 build fix, as aparently libxorg-x11-devel only works
  properly on i586.
- Update BuildRequires and Requires(pre) to ensure this package will not
  overwrite symlinks.
- Install Xt resources file in proper directory and don't try to be owner
  of the base directory. This is required to allow x11-server-common being
  the owner package of most shared directories used by xorg packages.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 9.02-16mdv2008.1
+ Revision: 135559
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- fix build on x86_64
- adapt to new X11 layout
- buildrequires xmkmf
- buildrequires X11-devel instead of XFree86-devel
- import xrn


* Sun Jan 08 2006 Anssi Hannula <anssi@mandriva.org> 9.02-15mdk
- fix buildrequires for x86_64

* Fri Jul 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 9.02-14mdk
- Fix BuildRequires

* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 9.02-13mdk
- Rebuild

* Sat May 03 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 9.02-12mdk
- rebuild for rpm 4.2

* Thu Jan 10 2002 David BAUDENS <baudens@mandrakesoft.com> 9.02-11mdk
- Fix menu entry (png icon)

* Wed Aug 01 2001 Stefan van der Eijk <stefan@eijk.nu> 9.02-10mdk
- BuildRequires: bison, flex

* Thu Jan 11 2001 David BAUDENS <baudens@mandrakesoft.com> 9.02-9mdk
- BuildRequires: libxpm4-devel

* Sat Dec 16 2000 Etienne Faure  <etienne@mandraksoft.com> 9.02-8mdk
- cleaned menu entry
- added normal and large icons

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 9.02-7mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.02-6mdk
- major spec cleaning

* Thu Jul 19 2000 Etienne Faure <etienne@mandrakesoft.com> 9.02-5mdk
- added the /usr/doc/xrn folder to installed files
 
* Thu Jul 19 2000 etienne Faure <etienne@mandrakesoft.com> 9.02-4mdk
- bziped xrn.xpm icon

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 9.02-3mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 9.02-2mdk
- Added menu entry

* Tue Mar 28 2000 dam's <damien@mandrakesoft.com> 9.02-1mdk
- Release.

* Thu Nov 25 1999 Florent Villard <warly@mandrakesoft.com>
- spec file cleaning 

* Thu May  6 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- handle RPM_OPT_FLAGS
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- add wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
