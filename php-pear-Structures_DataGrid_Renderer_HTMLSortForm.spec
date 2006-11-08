%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_Renderer_HTMLSortForm
%define		_status		beta
%define		_pearname	Structures_DataGrid_Renderer_HTMLSortForm
Summary:	%{_pearname} - Sorting form renderer for Structures_DataGrid
Summary(pl):	%{_pearname} - renderer formularza sortuj±cego dla Structures_Datagrid
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7baf1af4fc9984edd1b83dcb90f54a20
URL:		http://pear.php.net/package/Structures_DataGrid_Renderer_HTMLSortForm/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm >= 3.2.5
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This driver renders an HTML form to let the user easily sort the
datagrid, using multiple fields and directions. It uses the
HTML_Quickform package to do so.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza sterownik renderera generuj±cy formularz HTML
pozwalaj±cy u¿ytkownikowi na ³atwe sortowanie tabel danych korzystaj±c
z ró¿nych pól oraz typów sortowania. Wykorzystana jest do tego klasa
HTML_QuickForm.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/Renderer/HTMLSortForm.php
