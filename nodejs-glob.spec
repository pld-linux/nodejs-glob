Summary:	A little globber
Name:		nodejs-glob
Version:	3.1.9
Release:	1
License:	MIT
Group:		Libraries
URL:		https://github.com/isaacs/node-glob
Source0:	http://registry.npmjs.org/glob/-/glob-%{version}.tgz
# Source0-md5:	1c1b7fdec76f75797cf4d053bf7a1178
Requires:	nodejs
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs-graceful-fs
Requires:	nodejs-inherits
Requires:	nodejs-minimatch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a glob implementation in JavaScript. It uses the minimatch
library to do its matching.

%prep
%setup -q -n package

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/glob
cp -pr glob.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/glob

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/glob
%{_examplesdir}/%{name}-%{version}
