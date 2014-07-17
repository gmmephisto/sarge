%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define srcname sarge

Name:           python-%{srcname}
Version:        0.1.3
Release:        CROC1%{?dist}
Summary:        A wrapper for subprocess which provides command pipeline functionality.

Group:          Development/Libraries
License:        LGPL
URL:            https://pypi.python.org/pypi/sarge
Source0:        %{srcname}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  python-devel, python-setuptools


%description
The sarge package provides a wrapper for subprocess which provides command
pipeline functionality.
This package leverages subprocess to provide easy-to-use cross-platform command
pipelines with a Posix flavour: you can have chains of commands using ;, &,
pipes using | and |&, and redirection.


%prep
%setup -q -n %{srcname}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

find $RPM_BUILD_ROOT/ -name '*.egg-info' -exec rm -rf -- '{}' '+'


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc LICENSE CHANGES README.rst
%{python_sitelib}/*


%changelog
* Tue Jul 17 2014 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.3-CROC1
- Init release
