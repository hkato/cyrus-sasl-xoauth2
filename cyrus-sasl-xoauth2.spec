Name:           cyrus-sasl-xoauth2
Version:        0.2
Release:        1%{?dist}
Summary:        XOAUTH2 support for Cyrus SASL
Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/moriyoshi/cyrus-sasl-xoauth2
#Source0:        %{name}-%{version}.tar.gz
Source0:        https://github.com/moriyoshi/cyrus-sasl-xoauth2/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       cyrus-sasl cyrus-sasl-lib
BuildRequires:  cyrus-sasl-devel

%description
The %{name} package contains the Cyrus SASL plugins which support
XOAUTH2 mechanism.

%prep
%setup -q

%build
./autogen.sh
%configure --with-cyrus-sasl=%{_libdir} --disable-static
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/sasl2
./libtool --mode=install install -c libxoauth2.la %{buildroot}%{_libdir}/sasl2
rm -f %{buildroot}%{_libdir}/sasl2/libxoauth2.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/sasl2/libxoauth2.so*

%changelog
* Fri Sep 11 2020 Hideyuki KATO <hideyuki@kato.jp> 0.2-1
- Initial package release
