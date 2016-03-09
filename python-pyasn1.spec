#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pyasn1

Summary:	ASN.1 tools for Python
Summary(pl.UTF-8):	Narzędzia ASN.1 dla Pythona
Name:		python-%{module}
Version:	0.1.9
Release:	1
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pyasn1/
Source0:	https://pypi.python.org/packages/source/p/pyasn1/%{module}-%{version}.tar.gz
# Source0-md5:	f00a02a631d4016818659d1cc38d229a
URL:		http://pyasn1.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
%if %{with tests}
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
%endif
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Obsoletes:	python-pyasn1-examples
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is dedicated to implementation of ASN.1 types (concrete
syntax) and codecs (transfer syntaxes) for Python programming
environment.

%description -l pl.UTF-8
Celem tego projektu jest implementacja typów (konkretnej składni) i
kodowania (składni przesyłania) ASN.1 dla środowiska programowania
Python.

%package -n python3-%{module}
Summary:	ASN.1 tools for Python
Summary(pl.UTF-8):	Narzędzia ASN.1 dla Pythona
Group:		Libraries/Python

%description -n python3-%{module}
This project is dedicated to implementation of ASN.1 types (concrete
syntax) and codecs (transfer syntaxes) for Python programming
environment.

%description -n python3-%{module} -l pl.UTF-8
Celem tego projektu jest implementacja typów (konkretnej składni) i
kodowania (składni przesyłania) ASN.1 dla środowiska programowania
Python.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif
%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt THANKS.txt TODO.txt doc/*.html
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/pyasn1-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt THANKS.txt TODO.txt doc/*.html
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/pyasn1-%{version}-py*.egg-info
%endif
