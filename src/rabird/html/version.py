import pydgutils.version as pydguversion

version_info = pydguversion.VersionInfo(0, 0, 1, pydguversion.RL_FINAL, 0)
__version__ = pydguversion.version_info_to_str(version_info)
