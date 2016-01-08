Summary:	A little globber
Name:		nodejs-glob
Version:	3.2.9
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/node-glob
Source0:	http://registry.npmjs.org/glob/-/glob-%{version}.tgz
# Source0-md5:	cb72303f23a3b6539b1b52019cd8f791
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-inherits < 3
Requires:	nodejs-inherits >= 2
Requires:	nodejs-minimatch < 0.3.0
Requires:	nodejs-minimatch >= 0.2.11
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
