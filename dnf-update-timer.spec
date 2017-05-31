Name:           dnf-update-timer
Version:        0.0.1
Release:        2%{?dist}
Summary:        ensure that `dnf update` is run daily

License:        gplv2
URL:            https://github.com/vbatts/dnf-update-timer
Source0:        dnf-update.service
Source1:        dnf-update.timer

BuildArch:      noarch

Requires:       dnf
Requires:       systemd

%description
%{summary}.

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
cp -av %{SOURCE0} $RPM_BUILD_ROOT%{_unitdir}/dnf-update.service
cp -av %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/dnf-update.timer

%post
%{_bindir}/systemctl enable dnf-update.timer

%preun
%{_bindir}/systemctl disable dnf-update.timer

%files
/%{_unitdir}/dnf-update.service
/%{_unitdir}/dnf-update.timer


%changelog
* Wed May 31 2017 Vincent Batts <vbatts@thisco.de>
- initial setup
