import atheris
import sys


def check_permission(permission: str) -> bool:
    if permission == 'fuzzing_is_available':
        return False
    elif permission == 'fuzzing_is_not_available':
        return True
    elif permission == 'check_permission':
        return True

    return True


def do_calc(permission: str) -> int:
    is_available = check_permission(permission)

    if is_available:
        return 2 + 2
    else:
        return -1


def run_fuzzing(data: bytes):
    dp = atheris.FuzzedDataProvider(data)
    permission_legth = dp.ConsumeIntInRange(0, 32)
    permission = dp.ConsumeUnicodeNoSurrogates(permission_legth)
    do_calc(permission)

atheris.Setup(sys.argv, run_fuzzing)
atheris.Fuzz()
