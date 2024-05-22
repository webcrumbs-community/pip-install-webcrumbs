import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webcrumbs",
    version="0.0.1",
    author="Webcrumbs Team",
    author_email="julia@webcrumbs.org",
    description="A placeholder for the first Webcrumbs pip package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/webcrumbs-community/pip-install-webcrumbs",
    project_urls={
        "Bug Tracker": "https://github.com/webcrumbs-community/pip-install-webcrumbs/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
