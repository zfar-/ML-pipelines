from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="spaceship_dagster",
        packages=find_packages(exclude=["spaceship_dagster_tests"]),
        install_requires=[
            "dagster",
        ],
        extras_require={"dev": ["dagit", "pytest"]},
    )
