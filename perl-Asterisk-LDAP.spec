%define module Asterisk-LDAP

Name:		perl-%{module}
Version:	0.6.0
Release:	%mkrel 3
Summary:	Methods for generating Asterisk configuration from LDAP
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://projects.alkaloid.net/e107_plugins/content/content.php?content.6
Source0:	http://projects.alkaloid.net/dist/asterisk-ldap-%{version}.tar.bz2
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module should make it simple to write scripts that customize Asterisk's
configuration based on data from the LDAP tree. These methods and mechanisms
have been written with customization of the final product (configuration files)
in mind.

%prep
%setup -q -n asterisk-ldap-%{version} 

# fix attribs
chmod -R 755 examples
chmod 644 COPYING ChangeLog INSTALL LICENSE README* TODO asterisk.schema

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc examples COPYING ChangeLog INSTALL LICENSE README* TODO asterisk.schema
%{perl_vendorlib}/Asterisk
%{_mandir}/*/*
