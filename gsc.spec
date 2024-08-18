Name:       {{{ git_dir_name }}}
Version:    1.2
Release:    1%{?dist}
Summary:    Hubble Guide Star Catalog (GSC)
License:    GPLv3

%undefine _disable_source_fetch
URL:        https://github.com/ValNyz/gsc
VCS:        {{{ git_dir_vcs }}}
Source0:    https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/tar.gz?bincats/GSC_1.2#/%{name}-%{version}.tar.gz
Patch0:     Makefile.patch
Patch1:     decode.c.patch
Patch2:     get_head.c.patch
Patch3:     gsc.c.patch
Patch4:     to_d.c.patch
Patch5:     genred.c.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules

# I will solve this later
Conflicts:  gambit-c

%description
The GSC 1.2 catalog from u-strasbg.fr

%prep
%setup -q -c %{name}-%{version}
%patch 0 -p0
%patch 1 -p0
%patch 2 -p0
%patch 3 -p0
%patch 4 -p0
%patch 5 -p0

%build
cd src
%make_build

%install
cd src
%make_install

cd ..
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/GSC
install -D -m 755 bin/decode $RPM_BUILD_ROOT%{_bindir}
install -D -m 755 bin/gsc $RPM_BUILD_ROOT%{_bindir}
install -D -m 644 bin/regions* $RPM_BUILD_ROOT%{_bindir}
install -D -m 644 regions* $RPM_BUILD_ROOT%{_datadir}/GSC
install -D -m 644 N* -d $RPM_BUILD_ROOT%{_datadir}/GSC
install -D -m 644 S* -d $RPM_BUILD_ROOT%{_datadir}/GSC

%files
%{_datadir}/GSC/*
%{_bindir}/decode
%{_bindir}/gsc
%{_bindir}/regions*


%changelog
{{{ git_dir_changelog }}}

* Thu Nov  5 2020 Jim Howard <jh.xsnrg@gmail.com>
- updated to build directly

* Sun Jul  6 2014 Christian Dersch <chrisdersch@gmail.com>
- initial build
