Name:           gsm
Version:        1.0.18
Release:        4
Summary:        GSM speech compressor Shared libraries and Utilities
License:        MIT
URL:            http://www.quut.com/gsm/
Source0:        http://www.quut.com/gsm/%{name}-%{version}.tar.gz

# below patches are from redhat.
Patch0:         gsm-makefile.patch
Patch1:         gsm-warnings.patch

Provides:       gsm-tool
Obsoletes:      gsm-tool

%description
Contains the library for a GSM speech compressor, libgsm implements the European
GSM 06.10 provisional standard for full-rate speech transcoding, prI-ETS 300 036,
which uses RPE/LTP (residual pulse excitation/long term prediction) coding at 13 kbit/s.
GSM 06.10 compresses frames of 162 13-bit samples (8 kHz sampling rate) into 260 bits.

%package        devel
Summary:        Development files for gsm
Requires:       %{name}%{_isa} = %{version}-%{release}
%description    devel
Contains header files and development libraries for libgsm.

%package        help
Summary:        Help files for gsm
%description    help
Contains documents and manuals files for gsm

%prep
%autosetup -n %{name}-1.0-pl18 -p1


%build
make LDFLAGS="%{?__global_ldflags}" %{?_smp_mflags} all

%install
install -d %{buildroot}{%{_bindir},%{_includedir}/gsm,%{_libdir},%{_mandir}/{man1,man3}}

make install INSTALL_ROOT=%{buildroot}%{_prefix} GSM_INSTALL_INC=%{buildroot}%{_includedir}/gsm \
             GSM_INSTALL_LIB=%{buildroot}%{_libdir}

ln -s gsm/gsm.h %{buildroot}%{_includedir}

echo ".so toast.1" > %{buildroot}%{_mandir}/man1/tcat.1
echo ".so toast.1" > %{buildroot}%{_mandir}/man1/untoast.1

%check
[ -f %{buildroot}%{_libdir}/libgsm.so.%{version} ]
export LDFLAGS="%{?__global_ldflags}"
make addtst

%ldconfig_post
%ldconfig_postun

%files
%license COPYRIGHT
%{_libdir}/libgsm.so.*
%{_bindir}/tcat
%{_bindir}/*oast

%files devel
%dir %{_includedir}/gsm
%{_includedir}/*
%{_libdir}/libgsm.so

%files help
%doc ChangeLog MACHINES README
%{_mandir}/man*/*

%changelog
* Wed Sep 18 2019 chenzhenyu <chenzhenyu13@huawei.com> - 1.0.8-4
- Package init
