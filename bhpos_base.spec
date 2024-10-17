Summary:	BananaPOS base stuff
Name:		bhpos_base
Version:	2.0.0
Release:	%mkrel 0.beta3.3
License:	GPL
Group:		System/Servers
URL:		https://www.bananahead.com
Source0:	ftp://bananahead.com/pub/bhpos2/stable/%{name}-%{version}.tar.bz2
Requires(post): pkgconfig >= 0.15.0
Requires(preun): pkgconfig >= 0.15.0
BuildRequires:	pkgconfig >= 0.15.0
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
bhpos_base is the base install stuff for the bhpos system.

%package	devel
Summary:	Development things for BananaPOS base
Group:		Development/C
Requires:	pkgconfig >= 0.15.0

%description	devel
The bhpos_base-devel package contains headers required for bhpos.

%prep

%setup -q -n %{name}-%{version}

# lib64 fixes
perl -pi -e "s|/lib/|/%{_lib}/|g" configure*

%build
rm -f configure
libtoolize --copy --force; aclocal; autoconf; automake

%configure2_5x

make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%{_datadir}/bhpos2.0/schedule
%{_datadir}/bhpos2.0/db

%files devel
%defattr(-,root,root)
%dir %{_includedir}/bhpos2.0
%attr(0644,root,root) %{_includedir}/bhpos2.0/*.h
%attr(0644,root,root) %{_libdir}/pkgconfig/*.pc




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.beta3.3mdv2011.0
+ Revision: 616749
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 2.0.0-0.beta3.2mdv2010.0
+ Revision: 424611
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2.0.0-0.beta3.1mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.beta3.1mdv2007.0
+ Revision: 131167
- Import bhpos_base

* Sat Feb 04 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.beta3.1mdk
- 2.0.0 beta3

* Sat Oct 22 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.2.3-4mdk
- Fix BuildRequires
- %%mkrel

* Tue May 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-3mdk
- really fix build on x86_64

* Tue May 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-2mdk
- fix build on x86_64

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.3-1mdk
- initial mandrake package

