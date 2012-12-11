Name:           python-daemon
Version:        1.6
Release:        3
Summary:        Library to implement a well-behaved Unix daemon process
Group:          Development/Python
License:        Python
URL:            http://pypi.python.org/pypi/python-daemon
Source0:        http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
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
%{__python} setup.py install --root %{buildroot}
rm -fr %{buildroot}%{python_sitelib}/tests

%files
%doc ChangeLog LICENSE.GPL-2 LICENSE.PSF-2
%{python_sitelib}/daemon/
%{python_sitelib}/python_daemon-%{version}-py%{py_ver}.egg-info/


%changelog
* Wed Nov 10 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1.6-2mdv2011.0
+ Revision: 595657
- rebuild for python-2.7

* Sun Aug 29 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.6-1mdv2011.0
+ Revision: 574088
- Remove %%check because tests break build
- new version 1.6

* Thu Mar 18 2010 Caio Begotti <caio1982@mandriva.org> 1.5.5-1mdv2010.1
+ Revision: 525012
- import python-daemon

