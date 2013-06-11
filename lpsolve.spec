Name:      lpsolve
Summary:   A Mixed Integer Linear Programming (MILP) solver
Version:   5.5.2.0
Release:   %mkrel 4
Source:    http://downloads.sourceforge.net/lpsolve/lp_solve_%{version}_source.tar.gz
Group:     System/Libraries 
URL:       http://sourceforge.net/projects/lpsolve
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:   LGPLv2+

Patch0:    lpsolve-5.5.0.11.cflags.patch

%description
Mixed Integer Linear Programming (MILP) solver lpsolve solves pure linear,
(mixed) integer/binary, semi-continuous and special ordered sets (SOS) models.

%package devel
Requires: lpsolve = %{version}-%{release}
Summary: Files for developing with lpsolve
Group: Development/C

%description devel
Includes and definitions for developing with lpsolve 

%prep
%setup -q -n lp_solve_5.5
%patch0 -p1 -b .cflags.patch
#sparc and s390 need -fPIC  lets sed it                                              
%ifarch sparcv9 sparc64 s390 s390x                                                   
sed -i -e 's|-fpic|-fPIC|g' lpsolve55/ccc                                            
%endif 

%build
cd lpsolve55
sh -x ccc
rm bin/ux*/liblpsolve55.a
cd ../lp_solve
sh -x ccc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}/lpsolve
install -p -m 755 \
        lp_solve/bin/ux*/lp_solve $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 \
        lpsolve55/bin/ux*/liblpsolve55.so $RPM_BUILD_ROOT%{_libdir}
install -p -m 644 \
        lp*.h $RPM_BUILD_ROOT%{_includedir}/lpsolve

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL_LGPL.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL_README.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL-overview.txt
%{_bindir}/lp_solve
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/lpsolve



%changelog

* Sat Jan 12 2013 umeabot <umeabot> 5.5.2.0-4.mga3
+ Revision: 359007
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sat Jan 05 2013 malo <malo> 5.5.2.0-3.mga3
+ Revision: 339526
- fix RPM group

* Sun Jan 23 2011 dmorgan <dmorgan> 5.5.2.0-2.mga1
+ Revision: 35293
- Adapt for mageia
- imported package lpsolve

