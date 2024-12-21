Name:           adbenq
Version:        0.2.4
Release:        1%{?dist}
Summary:        ADBenQ

License:        AGPLv3
URL:            https://github.com/Zarox28/ADBenQ/

%global debug_package %{nil}

Source0:        https://github.com/Zarox28/ADBenQ/archive/refs/heads/main.zip
Source1:        adbenq.desktop
Source2:        adbenq

BuildRequires:  python3-pip
Requires:       python3 >= 3.9
Requires:       python3-pip
Requires:       python3-pyside6
Requires:       scrcpy
Requires:       android-tools
Requires:       python3-platformdirs

%description
"Control your BenQ TV like a boss 🖥️✨" he said

%prep
%autosetup -n ADBenQ-main

%build
pip3 install pure-python-adb --break-system-packages

%install
# Install desktop file
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install icon
install -Dm0644 src/icons/linux.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

# Install application files
mkdir -p %{buildroot}/opt/%{name}
cp -r * %{buildroot}/opt/%{name}/

# Install binary
%__install -D -m 0755 %{SOURCE2} -t %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_bindir}/%{name}
/opt/%{name}

%changelog
* Thu Oct 12 2023 Firmin <email@example.com> - v0.2.0.r7.g2b5a07e-1
- Initial package