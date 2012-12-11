%define upstream_name    Perl6-Form
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Implements the Perl 6 'form' built-in
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl6/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Perl6::Export)
BuildRequires:	perl(Scalar::Util)
BuildArch:	noarch

%description
Formats are Perl 5's mechanism for creating text templates with fixed-width
fields. Those fields are then filled in using values from prespecified
package variables.

Unlike Perl 5, Perl 6 doesn't have a 'format' keyword. Or the associated
built-in formatting mechanism. Instead it has a Form.pm module. And a
'form' function.

Like a Perl 5 'format' statement, the 'form' function takes a series of
format (or "picture") strings, each of which is immediately followed by a
suitable set of replacement values. It interpolates those values into the
placeholders specified within each picture string, and returns the result:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 655158
- rebuild for updated spec-helper

* Tue Dec 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 481335
- import perl-Perl6-Form


* Tue Dec 22 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
