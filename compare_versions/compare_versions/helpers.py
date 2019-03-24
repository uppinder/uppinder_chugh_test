import re


def is_valid_version(version):
	pattern = re.compile(r"^([0-9]|[1-9][0-9])[.]([0-9]|[1-9][0-9])[.]([0-9]|[1-9][0-9])([-](alpha|beta)([.]([0-9]|[1-9][0-9]))?)?")

	if pattern.match(version):
		return True
	return False


def _compare_pre_release(pre_release_a, pre_release_b):
	if pre_release_a == '' and len(pre_release_b) > 0:
		return 1
	elif len(pre_release_a) > 0 and pre_release_b == '':
		return -1

	if pre_release_a.startswith('beta') and pre_release_b.startswith('alpha'):
		return 1
	elif pre_release_a.startswith('alpha') and pre_release_b.startswith('beta'):
		return -1

	pre_release_a = pre_release_a.split('.')
	pre_release_b = pre_release_b.split('.')

	if len(pre_release_a) == 2 and len(pre_release_b) == 1:
		return 1
	if len(pre_release_a) == 1 and len(pre_release_b) == 2:
		return -1

	if int(pre_release_a[1]) > int(pre_release_b[1]):
		return 1
	if int(pre_release_a[1]) < int(pre_release_b[1]):
		return -1


def compare_versions_(version_a, version_b):
	# Two versions are equal if they have the same string representation
	# (Assuming no trailing zeros in version numbers)
	if version_a == version_b:
		return 0

	major_a, minor_a, patch_a = version_a.split('.', maxsplit=2)
	major_b, minor_b, patch_b = version_b.split('.', maxsplit=2)

	if major_a != major_b:
		return 1 if major_a > major_b else -1

	if minor_a != minor_b:
		return 1 if minor_a > minor_b else -1
	
	pre_release_a, pre_release_b = '',''
	if '-' in patch_a:
		patch_a, pre_release_a = patch_a.split('-')
	if '-' in patch_b:
		patch_b, pre_release_b = patch_b.split('-')

	if patch_a != patch_b:
		return 1 if patch_a > patch_b else -1

	return _compare_pre_release(pre_release_a, pre_release_b)
