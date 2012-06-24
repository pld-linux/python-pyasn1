
%define		module	pyasn1

Summary:	ASN.1 tools for Python
Summary(pl):	Narz�dzia ASN.1 dla Pythona
Name:		python-%{module}
Version:	0.0.4a
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyasn1/%{module}-%{version}.tar.gz
# Source0-md5:	85a1c06c34b301efbf08bb8c52e43f15
URL:		http://pyasn1.sourceforge.net/
BuildRequires:	python >= 2.2.1
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is dedicated to implementation of ASN.1 types (concrete
syntax) and codecs (transfer syntaxes) for Python programming
environment.

%description -l pl
Celem tego projektu jest implementacja typ�w (konkretnej sk�adni) i
kodowania (sk�adni przesy�ania) ASN.1 dla �rodowiska programowania
Python.

%package examples
Summary:	Example programs for Python pyasn1 module
Summary(pl):	Programy przyk�adowe do modu�u Pythona pyasn1
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Python pyasn1 module.

%description examples -l pl
Ten pakiet zawiera przyk�adowe programy do modu�u Pythona pyasn1.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES TODO doc/*
%{py_sitescriptdir}/%{module}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
