%define upstream_name    Asterisk-LDAP
%define upstream_version 0.6.0

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	11

Summary:	Methods for generating Asterisk configuration from LDAP
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://projects.alkaloid.net/e107_plugins/content/content.php?content.6
Source0:	http://projects.alkaloid.net/dist/asterisk-ldap-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module should make it simple to write scripts that customize Asterisk's
configuration based on data from the LDAP tree. These methods and mechanisms
have been written with customization of the final product (configuration files)
in mind.

%prep
%setup -q -n asterisk-ldap-%{upstream_version}

# fix attribs
chmod -R 755 examples
chmod 644 COPYING ChangeLog INSTALL LICENSE README* TODO asterisk.schema

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc examples COPYING ChangeLog INSTALL LICENSE README* TODO asterisk.schema
%{perl_vendorlib}/Asterisk
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.6.0-8mdv2011.0
+ Revision: 680479
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.6.0-7mdv2011.0
+ Revision: 504578
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.6.0-6mdv2010.0
+ Revision: 430262
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-5mdv2009.0
+ Revision: 255342
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-3mdv2008.1
+ Revision: 136901
- spec cleanup
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.0-1mdv2007.0
+ Revision: 73300
- import perl-Asterisk-LDAP-0.6.0-1mdv2007.0

* Fri Jun 16 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-1mdv2007.0
- initial Mandriva package

