# Created by BaiJiFeiLong@gmail.com at 2022/1/9 18:13

import distutils.log
import logging
import os

import colorlog
import setuptools.dist
from IceSpringPathLib import Path


def main():
    initLogging()
    os.chdir(Path(__file__).parent)
    doBuild()
    logging.info("Generated files:")
    for path in Path("target").glob("**/dist/*"):
        logging.info(f"\t{path} %.2f MB", path.stat().st_size / 1024 / 1024)


def initLogging():
    consoleLogPattern = "%(log_color)s%(asctime)s %(levelname)8s %(name)-16s %(message)s"
    logging.getLogger().handlers = [logging.StreamHandler()]
    logging.getLogger().handlers[0].setFormatter(colorlog.ColoredFormatter(consoleLogPattern))
    logging.getLogger().setLevel(logging.DEBUG)


def processCode(code: str) -> str:
    return "\n".join(['"""', "\n\n".join([
        "**Real** `Optional` type in `python`, not `@Nullable` annotation.",
        "Home: https://baijifeilong.github.io/2022/01/09/ice-spring-real-optional/index.html",
        "Github: https://github.com/baijifeilong/IceSpringRealOptional",
        "PyPI: https://pypi.org/project/IceSpringRealOptional",
        "Generated by BaiJiFeiLong@gmail.com",
        "License: MIT"
    ]), '"""']) + "\n\n" + code


def doBuild():
    projectName = "IceSpringRealOptional"
    readme = Path("README.md").read_text()
    Path("target").rmtree(ignore_errors=True)
    Path(projectName).copytree(Path(f"target/{projectName}"))
    for path in Path(f"target/{projectName}").glob("**/*.py"):
        path.write_text(processCode(path.read_text()))

    os.chdir(f"target")
    distutils.log.set_verbosity(1)
    for command in ["sdist", "bdist_wheel"]:
        setuptools.dist.Distribution(attrs=dict(
            script_name="",
            name=projectName,
            url=f"https://github.com/baijifeilong/{projectName}",
            license='MIT',
            author='BaiJiFeiLong',
            author_email='baijifeilong@gmail.com',
            version='1.2.4',
            description='Real Optional type in python, not @Nullable annotation.',
            packages=[f"{projectName}"],
            long_description=readme,
            long_description_content_type='text/markdown'
        )).run_command(command)
    os.chdir("..")


if __name__ == '__main__':
    main()
