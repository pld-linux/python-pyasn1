
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pyasn1

Summary:	ASN.1 tools for Python
Summary(pl.UTF-8):	Narzędzia ASN.1 dla Pythona
Name:		python-%{module}
Version:	0.1.7
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyasn1/%{module}-%{version}.tar.gz
# Source0-md5:	2cbd80fcd4c7b1c82180d3d76fee18c8
URL:		http://pyasn1.sourceforge.net/
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-distribute
BuildRequires:	python-modules >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-distribute
BuildRequires:	python3-modules >= 1:3.3
%endif
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Obsoletes:	%{name}-examples
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
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif
%if %{with python3}
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README CHANGES TODO doc/*
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README CHANGES TODO doc/*
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*.egg-info
%endif
