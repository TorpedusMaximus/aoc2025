{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python313Full
    pkgs.python313Packages.numpy
    pkgs.python313Packages.scipy
    pkgs.python313Packages.scikit-learn
    pkgs.python313Packages.pandas
    pkgs.gcc13
  ];

  shellHook = ''
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib pkgs.glibc ]}:$LD_LIBRARY_PATH
    export NIX_LD=${pkgs.stdenv.cc.bintools.dynamicLinker}

    if [ ! -d "./venv" ]; then
      python3.13 -m venv venv
      source ./venv/bin/activate
    else
      source ./venv/bin/activate
    fi
  '';
}
