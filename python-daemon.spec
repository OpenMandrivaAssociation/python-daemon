Name:           python-daemon
Version:        1.5.5
Release:        %mkrel 1
Summary:        Library to implement a well-behaved Unix daemon process
Group:          Development/Python
License:        Python
URL:            http://pypi.python.org/pypi/python-daemon
Source0:        http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  python-devel
BuildRequireS:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-lockfile
BuildRequires:  python-minimock

Requires:       python-lockfile

%description
This library implements the well-behaved daemon specification of
PEP 3143, "Standard daemon process library".

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}
rm -fr %{buildroot}%{python_sitelib}/tests

%clean
rm -rf %{buildroot}

%check
PYTHONPATH=$(pwd) nosetests

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE.GPL-2 LICENSE.PSF-2
%{python_sitelib}/daemon/
%{python_sitelib}/python_daemon-%{version}-py%{pyver}.egg-info/
