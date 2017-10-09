Name:           dnf-update-timer
Version:        0.0.2
Release:        2%{?dist}
Summary:        ensure that `dnf update` is run daily

License:        gplv2
URL:            https://github.com/vbatts/dnf-update-timer

Source0:        dnf-update.service
Source1:        dnf-update.timer
Source2:        yum-update.service
Source3:        yum-update.timer

BuildArch:      noarch

# for the rpm macros
BuildRequires:  systemd

%if 0%{?rhel} > 6
Requires:       yum
%else
Requires:       dnf
%endif
Requires:       systemd

%description
%{summary}.

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
%if 0%{?rhel} > 6
cp -av %{SOURCE0} $RPM_BUILD_ROOT/%{_unitdir}/yum-update.service
cp -av %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/yum-update.timer
%else
cp -av %{SOURCE0} $RPM_BUILD_ROOT/%{_unitdir}/dnf-update.service
cp -av %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/dnf-update.timer
%endif

%post
%if 0%{?rhel} > 6
%{_bindir}/systemctl enable yum-update.timer
%{_bindir}/systemctl restart yum-update.timer
%else
%{_bindir}/systemctl enable dnf-update.timer
%{_bindir}/systemctl restart dnf-update.timer
%endif

%preun
# On upgrades, this happens _after_ the new package is installed, so it invalidates itself
#%{_bindir}/systemctl disable dnf-update.timer

%files
%if 0%{?rhel} > 6
/%{_unitdir}/yum-update.service
/%{_unitdir}/yum-update.timer
%else
/%{_unitdir}/dnf-update.service
/%{_unitdir}/dnf-update.timer
%endif


%changelog
* Wed May 31 2017 Vincent Batts <vbatts@thisco.de>
- initial setup
