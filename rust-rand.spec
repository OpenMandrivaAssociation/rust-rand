%bcond_without check
%global debug_package %{nil}

%global crate rand

Name:           rust-%{crate}
Version:        0.8.3
Release:        3
Summary:        Random number generators and other randomness functionality

# Upstream license specification: MIT OR Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(libc) >= 0.2.22 with crate(libc) < 0.3.0)
BuildRequires:  (crate(rand_chacha) >= 0.3.0 with crate(rand_chacha) < 0.4.0)
BuildRequires:  (crate(rand_chacha/std) >= 0.3.0 with crate(rand_chacha/std) < 0.4.0)
BuildRequires:  (crate(rand_core/alloc) >= 0.6.0 with crate(rand_core/alloc) < 0.7.0)
BuildRequires:  (crate(rand_core/default) >= 0.6.0 with crate(rand_core/default) < 0.7.0)
BuildRequires:  (crate(rand_core/getrandom) >= 0.6.0 with crate(rand_core/getrandom) < 0.7.0)
BuildRequires:  (crate(rand_core/std) >= 0.6.0 with crate(rand_core/std) < 0.7.0)
BuildRequires:  (crate(rand_hc/default) >= 0.3.0 with crate(rand_hc/default) < 0.4.0)
%if %{with check}
BuildRequires:  (crate(bincode/default) >= 1.2.1 with crate(bincode/default) < 2.0.0)
BuildRequires:  (crate(rand_hc/default) >= 0.3.0 with crate(rand_hc/default) < 0.4.0)
BuildRequires:  (crate(rand_pcg/default) >= 0.3.0 with crate(rand_pcg/default) < 0.4.0)
%endif
%endif

%global _description %{expand:
Random number generators and other randomness functionality.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand) = 0.8.3
Requires:       cargo
Requires:       (crate(rand_core/default) >= 0.6.0 with crate(rand_core/default) < 0.7.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/default) = 0.8.3
Requires:       cargo
Requires:       crate(rand) = 0.8.3
Requires:       crate(rand/std) = 0.8.3
Requires:       crate(rand/std_rng) = 0.8.3

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/alloc) = 0.8.3
Requires:       cargo
Requires:       (crate(rand_core/alloc) >= 0.6.0 with crate(rand_core/alloc) < 0.7.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+getrandom-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/getrandom) = 0.8.3
Requires:       cargo
Requires:       (crate(rand_core/getrandom) >= 0.6.0 with crate(rand_core/getrandom) < 0.7.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+getrandom-devel %{_description}

This package contains library source intended for building other packages
which use "getrandom" feature of "%{crate}" crate.

%files       -n %{name}+getrandom-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/libc) = 0.8.3
Requires:       cargo
Requires:       (crate(libc) >= 0.2.22 with crate(libc) < 0.3.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages
which use "libc" feature of "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/log) = 0.8.3
Requires:       cargo
Requires:       (crate(log/default) >= 0.4.4 with crate(log/default) < 0.5.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages
which use "log" feature of "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/nightly) = 0.8.3
Requires:       cargo
Requires:       crate(rand) = 0.8.3

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+packed_simd-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/packed_simd) = 0.8.3
Requires:       cargo
Requires:       (crate(packed_simd_2/into_bits) >= 0.3.4 with crate(packed_simd_2/into_bits) < 0.4.0)
Requires:	(crate(packed_simd_2/default) >= 0.3.4 with crate(packed_simd_2/default) < 0.4.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+packed_simd-devel %{_description}

This package contains library source intended for building other packages
which use "packed_simd" feature of "%{crate}" crate.

%files       -n %{name}+packed_simd-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand_chacha-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/rand_chacha) = 0.8.3
Requires:       cargo
Requires:       (crate(rand_chacha) >= 0.3.0 with crate(rand_chacha) < 0.4.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+rand_chacha-devel %{_description}

This package contains library source intended for building other packages
which use "rand_chacha" feature of "%{crate}" crate.

%files       -n %{name}+rand_chacha-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand_hc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/rand_hc) = 0.8.3
Requires:       cargo
Requires:       (crate(rand_hc/default) >= 0.3.0 with crate(rand_hc/default) < 0.4.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+rand_hc-devel %{_description}

This package contains library source intended for building other packages
which use "rand_hc" feature of "%{crate}" crate.

%files       -n %{name}+rand_hc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/serde) = 0.8.3
Requires:       cargo
Requires:       (crate(serde/derive) >= 1.0.103 with crate(serde/derive) < 2.0.0)
Requires:	(crate(serde/default) >= 1.0.103 with crate(serde/default) < 2.0.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde1-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/serde1) = 0.8.3
Requires:       cargo
Requires:       (crate(serde/derive) >= 1.0.103 with crate(serde/derive) < 2.0.0)
Requires:	(crate(serde/default) >= 1.0.103 with crate(serde/default) < 2.0.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+serde1-devel %{_description}

This package contains library source intended for building other packages
which use "serde1" feature of "%{crate}" crate.

%files       -n %{name}+serde1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+simd_support-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/simd_support) = 0.8.3
Requires:       cargo
Requires:       crate(rand) = 0.8.3
Requires:       crate(rand/packed_simd) = 0.8.3

%description -n %{name}+simd_support-devel %{_description}

This package contains library source intended for building other packages
which use "simd_support" feature of "%{crate}" crate.

%files       -n %{name}+simd_support-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+small_rng-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/small_rng) = 0.8.3
Requires:       cargo
Requires:       crate(rand) = 0.8.3

%description -n %{name}+small_rng-devel %{_description}

This package contains library source intended for building other packages
which use "small_rng" feature of "%{crate}" crate.

%files       -n %{name}+small_rng-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/std) = 0.8.3
Requires:       cargo
Requires:       (crate(libc) >= 0.2.22 with crate(libc) < 0.3.0)
Requires:       (crate(rand_chacha/std) >= 0.3.0 with crate(rand_chacha/std) < 0.4.0)
Requires:       (crate(rand_core/std) >= 0.6.0 with crate(rand_core/std) < 0.7.0)
Requires:       crate(rand) = 0.8.3
Requires:       crate(rand/alloc) = 0.8.3
Requires:       crate(rand/getrandom) = 0.8.3

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std_rng-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rand/std_rng) = 0.8.3
Requires:       cargo
Requires:       (crate(rand_chacha) >= 0.3.0 with crate(rand_chacha) < 0.4.0)
Requires:       (crate(rand_hc/default) >= 0.3.0 with crate(rand_hc/default) < 0.4.0)
Requires:       crate(rand) = 0.8.3

%description -n %{name}+std_rng-devel %{_description}

This package contains library source intended for building other packages
which use "std_rng" feature of "%{crate}" crate.

%files       -n %{name}+std_rng-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
