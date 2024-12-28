# Zen Browser

Fork of the repo made by sneexy [here](https://git.gay/sneexy/copr/src/branch/main/zen-browser)

## Available Packages

- Zen browser generic : `zen-browser`
- Zen browser specific (AVX2) : `zen-browser-avx2`
- Zen browser twilight generic : `zen-browser-twilight` (supports arm64)
- Zen browser twilight specific (AVX2) : `zen-browser-twilight-avx2`

--------------

## Installation Instructions

1. Enable `firminunderscore/zen-browser` [Copr](https://copr.fedorainfracloud.org/) repository according to your package manager.

```Shell
# If you are using dnf... (you need to have 'dnf-plugins-core' installed)
sudo dnf copr enable firminunderscore/zen-browser

# If you are using yum... (you need to have 'yum-plugins-copr' installed)
sudo yum copr enable firminunderscore/zen-browser
```

2. (Optional) Update your package list.

```Shell
sudo dnf check-update
```

3. Execute the following command to install the package.

```Shell
sudo dnf install zen-browser
```

4. Launch the application from the Application Menu or execute following command in terminal.

```Shell
zen-browser
```
