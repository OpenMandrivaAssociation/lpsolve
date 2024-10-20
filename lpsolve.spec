# ld: ../lib/CodeGen/LexicalScopes.cpp:160: llvm::LexicalScope *llvm::LexicalScopes::getOrCreateRegularScope(const llvm::DILocalScope *): Assertion `cast<DISubprogram>(Scope)->describes(MF->getFunction())' failed.
%define _disable_lto 1

Summary:	A Mixed Integer Linear Programming (MILP) solver
Name:		lpsolve
Version:	5.5.2.5
Release:	5
Group:		System/Libraries 
License:	LGPLv2+
Url:		https://sourceforge.net/projects/lpsolve
Source0:	http://downloads.sourceforge.net/lpsolve/lp_solve_%{version}_source.tar.gz
Source100:	lpsolve.rpmlintrc
Patch0:		lpsolve-5.5.0.11.cflags.patch

%description
Mixed Integer Linear Programming (MILP) solver lpsolve solves pure linear,
(mixed) integer/binary, semi-continuous and special ordered sets (SOS) models.

%package devel
Requires:	%{name} = %{version}-%{release}
Summary:	Files for developing with lpsolve
Group:		Development/C

%description devel
Includes and definitions for developing with lpsolve 

%prep
%autosetup -n lp_solve_5.5 -p1

%build
export c=%{__cc}
sed -i "s!^c=.*!c=$c!g" lpsolve55/ccc lp_solve/ccc
cd lpsolve55
sh -x ccc
rm bin/ux*/liblpsolve55.a
cd ../lp_solve
sh -x ccc

%install
install -d %{buildroot}%{_bindir} %{buildroot}%{_libdir} %{buildroot}%{_includedir}/lpsolve
install -p -m 755 \
        lp_solve/bin/ux*/lp_solve %{buildroot}%{_bindir}
install -p -m 755 \
        lpsolve55/bin/ux*/liblpsolve55.so %{buildroot}%{_libdir}
install -p -m 644 \
        lp*.h %{buildroot}%{_includedir}/lpsolve

%files
%{_bindir}/lp_solve
%{_libdir}/liblpsolve55.so

%files devel
%doc README.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL_LGPL.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL_README.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL-overview.txt
%{_includedir}/lpsolve

