Summary:	A little globber
Name:		nodejs-glob
Version:	4.0.5
Release:	1
License:	ISC
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/glob/-/glob-%{version}.tgz
# Source0-md5:	bca4be8504515a5d01d0205a20f9f8d6
URL:		https://github.com/isaacs/node-glob
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-inherits < 3
Requires:	nodejs-inherits >= 2
Requires:	nodejs-minimatch < 2
Requires:	nodejs-minimatch >= 1.0.0
Requires:	nodejs-once < 2
Requires:	nodejs-once >= 1.3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a glob implementation in JavaScript. It uses the minimatch
library to do its matching.

%prep
%setup -qc
mv package/* .

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
