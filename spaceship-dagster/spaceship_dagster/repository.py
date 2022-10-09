from dagster import load_assets_from_package_module, repository

from spaceship_dagster import assets


@repository
def spaceship_dagster():
    return [load_assets_from_package_module(assets)]
