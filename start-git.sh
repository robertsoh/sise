#! /usr/bin/env sh
wget https://git.minsa.gob.pe/snippets/1/raw
mv raw pre-commit
git init
mv pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
