%define upstream_name    Asterisk-LDAP
%define upstream_version 0.6.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 7

Summary:	Methods for generating Asterisk configuration from LDAP
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://projects.alkaloid.net/e107_plugins/content/content.php?content.6
Source0:	http://projects.alkaloid.net/dist/asterisk-ldap-%{upstream_version}.tar.bz2

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
