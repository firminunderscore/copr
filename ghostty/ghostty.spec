%global debug_package %{nil}

Name:           ghostty
Version:        1.0.0
Release:        1%{?dist}
Summary:        Ghostty - A fast, feature-rich, and cross-platform terminal emulator

License:        MIT
URL:            https://ghostty.org
Source0:        https://github.com/ghostty-org/ghostty/archive/v%{version}.tar.gz

BuildRequires:  gtk4-devel, zig, libadwaita-devel, fontconfig-devel, freetype-devel, glib2-devel, gtk4-devel, harfbuzz-devel, libadwaita-devel, libpng-devel, oniguruma-devel, pandoc-cli, pixman-devel, pkg-config, zig, zlib-ng-devel
Requires:       gtk4, libadwaita, fontconfig, freetype, glib2, harfbuzz, libpng, oniguruma, pixman, zlib-ng

%description
Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration. 

%prep
%setup -q -n ghostty-%{version}

%build
ZIG_GLOBAL_CACHE_DIR=/tmp/offline-cache ./nix/build-support/fetch-zig-cache.sh
zig build \
    --summary all \
    --prefix "%{buildroot}%{_prefix}" \
    --system "/tmp/offline-cache/p" \
    -Doptimize=ReleaseFast \
    -Dcpu=baseline

%files
%license LICENSE
%{_bindir}/ghostty
%{_prefix}/share/applications/com.mitchellh.ghostty.desktop
%{_prefix}/share/bash-completion/completions/ghostty.bash
%{_prefix}/share/bat/syntaxes/ghostty.sublime-syntax
%{_prefix}/share/fish/vendor_completions.d/ghostty.fish
%{_prefix}/share/ghostty
%{_prefix}/share/icons/hicolor/128x128/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/16x16/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/256x256/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/32x32/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/512x512/apps/com.mitchellh.ghostty.png
%{_prefix}/share/kio/servicemenus/com.mitchellh.ghostty.desktop
%{_prefix}/share/man/man1/ghostty.1
%{_prefix}/share/man/man5/ghostty.5
%{_prefix}/share/nvim/site/ftdetect/ghostty.vim
%{_prefix}/share/nvim/site/ftplugin/ghostty.vim
%{_prefix}/share/nvim/site/syntax/ghostty.vim
%{_prefix}/share/terminfo/g/ghostty
%{_prefix}/share/terminfo/ghostty.termcap
%{_prefix}/share/terminfo/ghostty.terminfo
%{_prefix}/share/terminfo/x/xterm-ghostty
%{_prefix}/share/vim/vimfiles/ftdetect/ghostty.vim
%{_prefix}/share/vim/vimfiles/ftplugin/ghostty.vim
%{_prefix}/share/vim/vimfiles/syntax/ghostty.vim
%{_prefix}/share/zsh/site-functions/_ghostty

%changelog
%autochangelog
