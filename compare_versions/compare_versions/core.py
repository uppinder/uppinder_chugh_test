from .helpers import *


# Assume a version number is represented according to https://semver.org/.
# MAJOR.MINOR.PATCH
def compare_versions(version_a, version_b):
	if (not is_valid_version(version_a)) or (not is_valid_version(version_b)):
		raise ValueError

	return compare_versions_(version_a, version_b)