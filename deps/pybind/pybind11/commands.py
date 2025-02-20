import os

DIR = os.path.abspath(os.path.dirname(__file__))


def get_include(user: bool = False) -> str:  # pylint: disable=unused-argument
    """
    Return the path to the pybind include directory. The historical "user"
    argument is unused, and may be removed.
    """
    installed_path = os.path.join(DIR, "include")
    source_path = os.path.join(os.path.dirname(DIR), "include")
    return installed_path if os.path.exists(installed_path) else source_path


def get_cmake_dir() -> str:
    """
    Return the path to the pybind CMake module directory.
    """
    cmake_installed_path = os.path.join(DIR, "share", "cmake", "pybind")
    if os.path.exists(cmake_installed_path):
        return cmake_installed_path

    msg = "pybind not installed, installation required to access the CMake files"
    raise ImportError(msg)


def get_pkgconfig_dir() -> str:
    """
    Return the path to the pybind pkgconfig directory.
    """
    pkgconfig_installed_path = os.path.join(DIR, "share", "pkgconfig")
    if os.path.exists(pkgconfig_installed_path):
        return pkgconfig_installed_path

    msg = "pybind not installed, installation required to access the pkgconfig files"
    raise ImportError(msg)
