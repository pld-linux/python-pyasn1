#
# Conditional build:
%bcond_without	apidocs	# Sphinx documentation
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pyasn1

Summary:	ASN.1 tools for Python
Summary(pl.UTF-8):	Narzędzia ASN.1 dla Pythona
Name:		python-%{module}
Version:	0.4.4
Release:	1
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyasn1/
Source0:	https://files.pythonhosted.org/packages/source/p/pyasn1/%{module}-%{version}.tar.gz
# Source0-md5:	0d182b71e1f72fe147d7957bc90be7f2
URL:		https://github.com/etingof/pyasn1
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
%if %{with apidocs}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.5
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
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
This project is dedicated to implementation of ASN.1 types (concrete
syntax) and codecs (transfer syntaxes) for Python programming
environment.

%description -n python3-%{module} -l pl.UTF-8
Celem tego projektu jest implementacja typów (konkretnej składni) i
kodowania (składni przesyłania) ASN.1 dla środowiska programowania
Python.

%package apidocs
Summary:	Documentation for ASN.1 Python module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona ASN.1
Group:		Documentation

%description apidocs
Documentation for ASN.1 Python module.

%description apidocs -l pl.UTF-8
Dokumentacja do modułu Pythona ASN.1.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif
%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with apidocs}
PYTHONPATH=$(pwd)/build-py3/lib \
%{__make} -C docs html
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
%doc CHANGES.rst LICENSE.rst README.md TODO.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/pyasn1-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.rst README.md TODO.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/pyasn1-%{version}-py*.egg-info
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,pyasn1,*.html,*.js}
%endif
