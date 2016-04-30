Name     : golang-github-gorilla-context 
Version  : 0 
Release  : 7
URL      : https://github.com/gorilla/context/archive/1c83b3eabd45b6d76072b66b746c20815fb2872d/context-1c83b3e.tar.gz
Source0  : https://github.com/gorilla/context/archive/1c83b3eabd45b6d76072b66b746c20815fb2872d/context-1c83b3e.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires: go

%description
context
=======
[![Build Status](https://travis-ci.org/gorilla/context.png?branch=master)](https://travis-ci.org/gorilla/context)

%prep
%setup -q -n context-1c83b3eabd45b6d76072b66b746c20815fb2872d

%build

%install
%global gopath /usr/lib/golang
%global library_path github.com/gorilla/context
rm -rf %{buildroot}
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for file in $(find . -iname "*.go") ; do
     install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
     cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
done

%check
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/gorilla/context/context.go
/usr/lib/golang/src/github.com/gorilla/context/context_test.go
/usr/lib/golang/src/github.com/gorilla/context/doc.go
