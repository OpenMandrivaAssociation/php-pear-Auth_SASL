%define		_class		Auth
%define		_subclass	SASL
%define		upstream_name	%{_class}_%{_subclass}

Summary:	Generate responses to common SASL mechanisms
Name:		php-pear-%{upstream_name}
Version:	1.0.6
Release:	13
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Auth_SASL/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Provides code to generate responses to common SASL mechanisms,
including: Digest-MD5, CramMD5, Plain, Anonymous, Login (Pseudo
mechanism).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml

