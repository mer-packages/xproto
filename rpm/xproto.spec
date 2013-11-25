Name:       xproto
Summary:    X.Org X11 Protocol xproto
Version:    7.0.25
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/xproto-%{version}.tar.bz2

%description
This package provides the headers and specification documents defining
the X Window System Core Protocol, Version 11.

%prep
%setup -q -n xproto-%{version}/xproto

%build

%autogen --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/xproto.pc
%{_includedir}/X11/XWDFile.h
%{_includedir}/X11/XF86keysym.h
%{_includedir}/X11/Xalloca.h
%{_includedir}/X11/Xwindows.h
%{_includedir}/X11/Xatom.h
%{_includedir}/X11/Xarch.h
%{_includedir}/X11/Xmd.h
%{_includedir}/X11/ap_keysym.h
%{_includedir}/X11/Xw32defs.h
%{_includedir}/X11/Xfuncs.h
%{_includedir}/X11/X.h
%{_includedir}/X11/Xfuncproto.h
%{_includedir}/X11/Xosdefs.h
%{_includedir}/X11/keysym.h
%{_includedir}/X11/Xproto.h
%{_includedir}/X11/keysymdef.h
%{_includedir}/X11/HPkeysym.h
%{_includedir}/X11/Xos.h
%{_includedir}/X11/Xdefs.h
%{_includedir}/X11/DECkeysym.h
%{_includedir}/X11/Xwinsock.h
%{_includedir}/X11/Xthreads.h
%{_includedir}/X11/Xprotostr.h
%{_includedir}/X11/Xpoll.h
%{_includedir}/X11/Sunkeysym.h
%{_includedir}/X11/Xos_r.h
#%doc %{_docdir}/xproto/encoding.xml
#%doc %{_docdir}/xproto/glossary.xml
#%doc %{_docdir}/xproto/keysyms.xml
#%doc %{_docdir}/xproto/sect1-9.xml
#%doc %{_docdir}/xproto/x11protocol.xml


