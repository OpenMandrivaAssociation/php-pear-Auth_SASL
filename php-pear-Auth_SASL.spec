%define		_class		Auth
%define		_subclass	SASL
%define		upstream_name	%{_class}_%{_subclass}

Summary:	Generate responses to common SASL mechanisms
Name:		php-pear-%{upstream_name}
Version:	1.0.6
Release:	4
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Auth_SASL/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

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
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-2mdv2012.0
+ Revision: 741743
- fix major breakage by careless packager

* Mon Nov 28 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-1
+ Revision: 735157
- new version

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-3
+ Revision: 667483
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 607089
- rebuild

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-1mdv2010.1
+ Revision: 508988
- update to new version 1.0.4

* Tue Nov 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-2mdv2010.1
+ Revision: 464361
- use rpm filetriggers to register starting from mandriva 2010.1

* Sat Sep 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-1mdv2010.0
+ Revision: 449295
- new version
- use pear installer
- use fedora %%post/%%postun

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2010.0
+ Revision: 440935
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdv2009.1
+ Revision: 321899
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2009.0
+ Revision: 236804
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 15640
- 1.0.2


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdv2007.0
+ Revision: 81381
- Import php-pear-Auth_SASL

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- initial Mandriva package (PLD import)

