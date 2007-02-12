%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	DTD
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - parsing of DTD files and DTD validation of XML files
Summary(pl.UTF-8):	%{_pearname} - analizowanie plików DTD oraz sprawdzanie DTD plików XML
Name:		php-pear-%{_pearname}
Version:	0.4.2
Release:	3
Epoch:		0
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e920218231845ed64b56f293a2a3480c
URL:		http://pear.php.net/package/XML_DTD/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-XML_Tree >= 2.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parsing of DTD files and DTD validation of XML files. The XML
validation is done with the PHP sax parser, the xml extension, it does
not use the domxml extension.

Currently supports most of current XML specification, including
entities, elements and attributes. Some uncommon parts of the
specification may still be unsupported.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa służy do analizowania plików DTD i sprawdzania poprawności
plików XML względem DTD. Kontrola poprawności XML-a jest wykonywana
analizatorem PHP sax, rozszerzeniem xml, bez użycia rozszerzenia
domxml.

Aktualnie pakiet obsługuje większość aktualnej specyfikacji XML-a,
włącznie z encjami, elementami i atrybutami. Niektóre rzadko używane
części specyfikacji mogą być jeszcze nie obsługiwane.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{README.txt,TODO.txt}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
