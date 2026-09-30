## Dependency Upgrader CLI

A command-line utility to verify and resolve outdated package dependencies in Python projects.

### Installation

```bash
pip install dependency-upgrader-cli
```

### Usage

To check for outdated packages, run:

```bash
dependency-upgrader verify-requirements requirements.txt
```

To upgrade packages automatically, add the `--upgrade` flag:

```bash
dependency-upgrader verify-requirements requirements.txt --upgrade
```
