#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : python-cinderclient
Version  : 4.1.0
Release  : 34
URL      : http://tarballs.openstack.org/python-cinderclient/python-cinderclient-4.1.0.tar.gz
Source0  : http://tarballs.openstack.org/python-cinderclient/python-cinderclient-4.1.0.tar.gz
Source99 : http://tarballs.openstack.org/python-cinderclient/python-cinderclient-4.1.0.tar.gz.asc
Summary  : OpenStack Block Storage API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-cinderclient-bin
Requires: python-cinderclient-python3
Requires: python-cinderclient-license
Requires: python-cinderclient-python
Requires: Babel
Requires: Sphinx
Requires: keystoneauth1
Requires: openstackdocstheme
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: reno
Requires: simplejson
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

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

%description python3
python3 components for the python-cinderclient package.


%prep
%setup -q -n python-cinderclient-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539049771
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/python-cinderclient
cp LICENSE %{buildroot}/usr/share/doc/python-cinderclient/LICENSE
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
/usr/share/doc/python-cinderclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
