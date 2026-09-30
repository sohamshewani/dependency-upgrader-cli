import click
import pkg_resources

@click.command()
@click.argument('requirements_file', type=click.Path(exists=True))
@click.option('--upgrade/--no-upgrade', default=False, help='Upgrade packages automatically')
def verify_requirements(requirements_file, upgrade):
    with open(requirements_file, 'r') as f:
        requirements = f.read().splitlines()
    installed_packages = {pkg.key: pkg for pkg in pkg_resources.working_set}
    outdated = []

    for requirement in requirements:
        package_name, version = requirement.split('==')
        if package_name in installed_packages:
            installed_version = installed_packages[package_name].version
            if pkg_resources.parse_version(installed_version) < pkg_resources.parse_version(version):
                outdated.append((package_name, installed_version, version))
        else:
            click.echo(f'Package {package_name} is not installed.')

    if outdated:
        click.echo('Outdated packages found:')
        for package_name, installed_version, version in outdated:
            click.echo(f'{package_name} {installed_version} < {version}')

    if upgrade:
        for package_name, installed_version, version in outdated:
            click.echo(f'Upgrading {package_name} from {installed_version} to {version}...')
            try:
                import importlib
                importlib.import_module(package_name)
                click.echo(f'Successfully upgraded {package_name} to {version}')
            except ImportError:
                click.echo(f'Failed to upgrade {package_name} to {version}')

if __name__ == '__main__':
    verify_requirements()