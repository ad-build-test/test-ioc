Name:           test-ioc
Version:        1.0.0
Release:        1%{?dist}
Summary:        test-ioc built for buildsystem testing
BuildArch:      x86_64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

# Requires:       
# TODO: Need to figure out if we want to specify dependencies here like all of them?
# Or just copy over the dependencies from the manifest CONFIG.yaml

%description
A demo RPM build

# Define the _prefix macro with a default value
%define _prefix /sdf/scratch/ad/build/lcls/epics/iocTop

%prep
%setup -q

# %build
# No build steps for this - can assume the tarball is already built

%install
# Install refers to installing the tarball on BUILDROOT/ of the rpm package
# Create the test-ioc directory in the buildroot
mkdir -p %{buildroot}%{_prefix}/%{name}-%{version}/bin
mkdir -p %{buildroot}%{_prefix}/%{name}-%{version}/db
mkdir -p %{buildroot}%{_prefix}/%{name}-%{version}/dbd
mkdir -p %{buildroot}%{_prefix}/%{name}-%{version}/iocBoot

# Copy contents from the unpacked tarball into the test-ioc directory
cp -a bin/* %{buildroot}%{_prefix}/%{name}-%{version}/bin
cp -a db/* %{buildroot}%{_prefix}/%{name}-%{version}/db
cp -a dbd/* %{buildroot}%{_prefix}/%{name}-%{version}/dbd
cp -a iocBoot/* %{buildroot}%{_prefix}/%{name}-%{version}/iocBoot

%clean
# No clean steps for this - since there is no building step

%files
# Files refer to copying the files to desired directories on target system
# This one has to be dynamic with %_prefix
# The install location is dynamic and determined at installation using '_prefix'
# ex: rpm -i test-ioc.rpm --prefix /sdf/scratch/ad/build/lcls/epics/iocTop

%{_prefix}/%{name}-%{version}/bin/*
%{_prefix}/%{name}-%{version}/db/*
%{_prefix}/%{name}-%{version}/dbd/*
%{_prefix}/%{name}-%{version}/iocBoot/*


%changelog
* Fri Aug 23 2024 Patrick Nisperos <pnispero@slac.stanford.edu> - 1.0.0
- First version being packaged