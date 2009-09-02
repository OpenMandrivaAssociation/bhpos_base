Summary:	BananaPOS base stuff
Name:		bhpos_base
Version:	2.0.0
Release:	%mkrel 0.beta3.2
License:	GPL
Group:		System/Servers
URL:		http://www.bananahead.com
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


