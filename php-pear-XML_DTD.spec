%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	DTD
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - parsing of DTD files and DTD validation of XML files
Summary(pl):	%{_pearname} - analizowanie plików DTD oraz sprawdzanie DTD plików XML
Name:		php-pear-%{_pearname}
Version:	0.4.2
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e920218231845ed64b56f293a2a3480c
URL:		http://pear.php.net/package/XML_DTD/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parsing of DTD files and DTD validation of XML files. The XML
validation is done with the php sax parser, the xml extension, it does
not use the domxml extension.

Currently supports most of current XML specification, including
entities, elements and attributes. Some uncommon parts of the
specification may still be unsupported.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa s³u¿y do analizowania plików DTD i sprawdzania poprawno¶ci
plików XML wzglêdem DTD. Kontrola poprawno¶ci XML-a jest wykonywana
analizatorem php sax, rozszerzeniem xml, bez u¿ycia rozszerzenia
domxml.

Aktualnie pakiet obs³uguje wiêkszo¶æ aktualnej specyfikacji XML-a,
w³±cznie z encjami, elementami i atrybutami. Niektóre rzadko u¿ywane
czê¶ci specyfikacji mog± byæ jeszcze nie obs³ugiwane.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{README.txt,TODO.txt,tests}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
