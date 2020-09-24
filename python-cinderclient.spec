#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : python-cinderclient
Version  : 7.1.0
Release  : 45
URL      : http://tarballs.openstack.org/python-cinderclient/python-cinderclient-7.1.0.tar.gz
Source0  : http://tarballs.openstack.org/python-cinderclient/python-cinderclient-7.1.0.tar.gz
Source1  : http://tarballs.openstack.org/python-cinderclient/python-cinderclient-7.1.0.tar.gz.asc
Summary  : OpenStack Block Storage API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-cinderclient-bin = %{version}-%{release}
Requires: python-cinderclient-license = %{version}-%{release}
Requires: python-cinderclient-python = %{version}-%{release}
Requires: python-cinderclient-python3 = %{version}-%{release}
Requires: keystoneauth1
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: simplejson
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : keystoneauth1
BuildRequires : oslo.i18n
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : requests
BuildRequires : simplejson
BuildRequires : six

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the python-cinderclient package.
Group: Binaries
Requires: python-cinderclient-license = %{version}-%{release}

%description bin
bin components for the python-cinderclient package.


%package license
Summary: license components for the python-cinderclient package.
Group: Default

%description license
license components for the python-cinderclient package.


%package python
Summary: python components for the python-cinderclient package.
Group: Default
Requires: python-cinderclient-python3 = %{version}-%{release}

%description python
python components for the python-cinderclient package.


%package python3
Summary: python3 components for the python-cinderclient package.
Group: Default
Requires: python3-core
Provides: pypi(python_cinderclient)
Requires: pypi(keystoneauth1)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(prettytable)
Requires: pypi(requests)
Requires: pypi(simplejson)
Requires: pypi(six)

%description python3
python3 components for the python-cinderclient package.


%prep
%setup -q -n python-cinderclient-7.1.0
cd %{_builddir}/python-cinderclient-7.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594661604
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-cinderclient
cp %{_builddir}/python-cinderclient-7.1.0/LICENSE %{buildroot}/usr/share/package-licenses/python-cinderclient/457cde685921b35f8b6f04f965f332e1e9a50267
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cinder

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-cinderclient/457cde685921b35f8b6f04f965f332e1e9a50267

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
