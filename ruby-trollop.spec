Summary:	Yet another commandline option parsing library
Name:		ruby-trollop
Version:	1.15
Release:	1
License:	Ruby
Source0:	http://rubyforge.org/frs/download.php/64572/trollop-%{version}.tgz
# Source0-md5:	e234198bcea979758a293e129ee7be4e
Group:		Development/Languages
URL:		http://trollop.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trollop is YAFCLAP --- yet another fine commandline argument
processing library for Ruby.

%prep
%setup -q -n trollop-%{version}
install %{_datadir}/setup.rb .

%build
ruby setup.rb config --rbdir=%{ruby_rubylibdir} --sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{ruby_rubylibdir}/*.rb
