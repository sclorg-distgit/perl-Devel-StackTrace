%{?scl:%scl_package perl-Devel-StackTrace}

Name:           %{?scl_prefix}perl-Devel-StackTrace
Summary:        Perl module implementing stack trace and stack trace frame objects
Version:        2.01
Epoch:          1
Release:        3%{?dist}
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-StackTrace/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Devel-StackTrace-%{version}.tar.gz
BuildArch:      noarch

# --with release_tests ... also check "RELEASE_TESTS".
# Disabled by default
%bcond_with release_tests

# --with author_tests ... also check "AUTHOR_TESTS".
# Disabled by default
%bcond_with author_tests

BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(bytes)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%if %{with release_tests}
# for improved tests
BuildRequires:  %{?scl_prefix}perl(Exception::Class::Base)
BuildRequires:  %{?scl_prefix}perl(Pod::Coverage::TrustPod)
BuildRequires:  %{?scl_prefix}perl(Test::CPAN::Changes)
BuildRequires:  %{?scl_prefix}perl(Test::EOL)
BuildRequires:  %{?scl_prefix}perl(Test::NoTabs)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) > 1.41
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  %{?scl_prefix}perl(Test::Pod::LinkCheck)
BuildRequires:  %{?scl_prefix}perl(Test::Pod::No404s)
BuildRequires:  %{?scl_prefix}perl(Test::Portability::Files)
BuildRequires:  %{?scl_prefix}perl(Test::Synopsis)
BuildRequires:  %{?scl_prefix}perl(LWP::Protocol::https)
%endif

%if %{with author_tests}
BuildRequires:  %{?scl_prefix}perl(Pod::Coverage::TrustPod)
BuildRequires:  %{?scl_prefix}perl(Test::CPAN::Changes)
BuildRequires:  %{?scl_prefix}perl(Test::EOL)
BuildRequires:  %{?scl_prefix}perl(Test::NoTabs)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) > 1.41
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  %{?scl_prefix}perl(Test::Spelling) >= 0.12
BuildRequires:  %{?scl_prefix}perl(Test::Synopsis)
%endif

%description
The Devel::StackTrace module contains two classes, Devel::StackTrace
and Devel::StackTraceFrame.  The goal of this object is to encapsulate
the information that can found through using the caller() function, as
well as providing a simple interface to this data.

The Devel::StackTrace object contains a set of Devel::StackTraceFrame
objects, one for each level of the stack.  The frames contain all the
data available from caller() as of Perl 5.6.0.

%prep
%setup -q -n Devel-StackTrace-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test %{?with_release_tests:RELEASE_TESTING=1} %{?with_author_tests:AUTHOR_TESTING=1}%{?scl:'}

%files
%doc Changes
%doc LICENSE
%{perl_vendorlib}/Devel
%{_mandir}/man3/*

%changelog
* Tue Jul 12 2016 Petr Pisar <ppisar@redhat.com> - 1:2.01-3
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.01-2
- Perl 5.24 rebuild

* Fri Mar 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2.01-1
- Update to 2.01.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2.00-4
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.00-2
- Perl 5.22 rebuild

* Mon Nov 03 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2,00-1
- Upstream update.
- Reflect upstream changes to BR:'s.

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.34-2
- Perl 5.20 rebuild

* Sat Jun 28 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.34-1
- Upstream update.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.32-1
- Upstream update.
- Activate AUTHOR_TESTING.
- Update BRs.

* Fri Jan 17 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.31-1
- Upstream update.
- Fix bogus %%changelog entry.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:1.30-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.30-1
- Upstream update.
- Reflect new BR:'s.
- Modernize spec-file.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1:1.27-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.27-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.27-1
- Upstream update.

* Wed Nov 03 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.26-1
- Upstream update.

* Sun Sep 12 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.25-1
- Upstream update.
- Spec overhaul.
- Add %%bcond_with release_tests

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.22-5
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.22-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:1.22-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.22-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.20-2
- BR: perl(Test::Kwalitee).

* Sat Dec 13 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.20-1
- Upstream update.
- Bump epoch.

* Fri Aug 08 2008 Ralf Corsépius <rc040203@freenet.de> - 1.1902-1
- Upstream update.

* Wed Jun 25 2008 Ralf Corsépius <rc040203@freenet.de> - 1.1901-1
- Upstream update.

* Fri May 16 2008 Ralf Corsépius <rc040203@freenet.de> - 1.18-2
- Bump release.

* Mon Apr 07 2008 Ralf Corsépius <rc040203@freenet.de> - 1.18-1
- Upstream update.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.16-2
- Rebuild for perl 5.10 (again)

* Sun Feb 03 2008 Ralf Corsépius <rc040203@freenet.de> - 1.16-1
- Upstream update.
- Activate IS_MAINTAINER-tests.
- BR: perl(Test::Pod::Coverage).

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.15-3
- rebuild for new perl

* Wed Aug 29 2007 Ralf Corsépius <rc040203@freenet.de> - 1.15-2
- Update License.

* Mon Apr 30 2007 Ralf Corsépius <rc040203@freenet.de> - 1.15-1
- Upstream update.

* Sat Mar 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.14-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-2
- Mass rebuild.

* Tue Apr 04 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 1.12-2
- Rebuild for perl-5.8.8.

* Sun Oct 02 2005 Ralf Corsepius <rc040203@freenet.de> - 1.12-1
- Upstream update.
