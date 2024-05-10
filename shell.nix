# shell.nix

{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs.python39Packages; [
    requests
    beautifulsoup4
  ];
}

