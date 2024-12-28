%global debug_package %{nil}

Name:           ghostty
Version:        1.0.0
Release:        1%{?dist}
Summary:        Ghostty - Afast, feature-rich, and cross-platform terminal emulator

License:        MIT
URL:            https://ghostty.org
Source0:        https://github.com/ghostty-org/ghostty/archive/v%{version}.tar.gz

BuildRequires:  gtk4-devel, zig, libadwaita-devel

%description
Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration. 

%prep
%autosetup

%build
zig build -Doptimize=ReleaseFast

%install
install -Dm0755 zig-out/bin/ghostty %{buildroot}%{_bindir}/ghostty
install -Dm0644 zig-out/share/applications/com.mitchellh.ghostty.desktop %{buildroot}%{_datadir}/applications/com.mitchellh.ghostty.desktop
install -Dm0644 zig-out/share/bash-completion/completions/ghostty.bash %{buildroot}%{_datadir}/bash-completion/completions/ghostty
install -Dm0644 zig-out/share/fish/vendor_completions.d/ghostty.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/ghostty.fish
install -Dm0644 zig-out/share/bat/syntaxes/ghostty.sublime-syntax %{buildroot}%{_datadir}/bat/syntaxes/ghostty.sublime-syntax

# Shell integration
install -Dm0644 zig-out/share/ghostty/shell-integration/bash/bash-preexec.sh %{buildroot}%{_datadir}/ghostty/shell-integration/bash/bash-preexec.sh
install -Dm0644 zig-out/share/ghostty/shell-integration/bash/ghostty.bash %{buildroot}%{_datadir}/ghostty/shell-integration/bash/ghostty.bash
install -Dm0644 zig-out/share/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish %{buildroot}%{_datadir}/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish
install -Dm0644 zig-out/share/ghostty/shell-integration/zsh/ghostty-integration %{buildroot}%{_datadir}/ghostty/shell-integration/zsh/ghostty-integration

# Themes
find zig-out/share/ghostty/themes -type f -exec install -Dm0644 {} %{buildroot}%{_datadir}/ghostty/themes/ \;

%files
%license LICENSE
%{_bindir}/ghostty
%{_datadir}/applications/com.mitchellh.ghostty.desktop
%{_datadir}/bash-completion/completions/ghostty
%{_datadir}/fish/vendor_completions.d/ghostty.fish
%{_datadir}/bat/syntaxes/ghostty.sublime-syntax
%{_datadir}/ghostty/

%changelog
* Sat Dec 28 2024 Firmin <firmin@example.com> - 1.0.0-1
- Initial packaging
