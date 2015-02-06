Name:           python-daemon
Version:        1.6
Release:        4
Summary:        Library to implement a well-behaved Unix daemon process
Group:          Development/Python
License:        Python
URL:            http://pypi.python.org/pypi/python-daemon
Source0:        http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-lockfile
BuildRequires:  python-minimock
Requires:       python-lockfile

%define debug_package %{nil}

%description
This library implements the well-behaved daemon specification of
PEP 3143, "Standard daemon process library".

%prep
%setup -q

%build

%install
python setup.py install --root %{buildroot}
rm -fr %{buildroot}%{py_puresitedir}/tests

%files
%doc ChangeLog LICENSE.GPL-2 LICENSE.PSF-2
%{py_puresitedir}/daemon/
%{py_puresitedir}/python_daemon-%{version}-py%{py_ver}.egg-info/
