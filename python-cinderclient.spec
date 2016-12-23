#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-cinderclient
Version  : 1.9.0
Release  : 25
URL      : http://tarballs.openstack.org/python-cinderclient/python-cinderclient-1.9.0.tar.gz
Source0  : http://tarballs.openstack.org/python-cinderclient/python-cinderclient-1.9.0.tar.gz
Summary  : OpenStack Block Storage API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-cinderclient-bin
Requires: python-cinderclient-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : msgpack-python-python
BuildRequires : os-testr-python
BuildRequires : oslo.utils-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-keystoneclient-python
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : tox
BuildRequires : virtualenv

%description
Python bindings to the OpenStack Cinder API
===========================================

%package bin
Summary: bin components for the python-cinderclient package.
Group: Binaries

%description bin
bin components for the python-cinderclient package.


%package python
Summary: python components for the python-cinderclient package.
Group: Default
Requires: oslo.utils-python
Requires: requests-python
Requires: simplejson

%description python
python components for the python-cinderclient package.


%prep
%setup -q -n python-cinderclient-1.9.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cinder

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
