from setuptools import setup, find_packages

setup(
    name="the-littlest-jupyterhub",
    use_scm_version={"write_to": "tljh/_version.py"},
    # 7.0.0 drops support for Python 3.6
    setup_requires=["setuptools_scm==6.4.2"],
    description="A small JupyterHub distribution",
    url="https://github.com/jupyterhub/the-littlest-jupyterhub",
    author="Jupyter Development Team",
    author_email="jupyter@googlegroups.com",
    license="3 Clause BSD",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "ruamel.yaml==0.17.*",
        "jinja2",
        "pluggy==1.*",
        "passlib",
        "backoff",
        "requests",
        "bcrypt",
        "jupyterhub-traefik-proxy==0.3.*",
    ],
    entry_points={
        "console_scripts": [
            "tljh-config = tljh.config:main",
        ]
    },
)
