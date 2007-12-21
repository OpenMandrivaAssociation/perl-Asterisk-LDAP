Summary:	Asterisk::LDAP - Methods for generating Asterisk configuration from LDAP
Name:		perl-Asterisk-LDAP
Version:	0.6.0
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://projects.alkaloid.net
Source0:	http://projects.alkaloid.net/dist/asterisk-ldap-%{version}.tar.bz2
BuildRequires:	perl-devel
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
%{perl_vendorlib}/Asterisk/LDAP.pm
%{_mandir}/*/*



