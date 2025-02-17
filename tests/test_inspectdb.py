from tests._utils import run_shell


def test_inspect(new_aerich_project):
    run_shell("aerich init -t settings.TORTOISE_ORM")
    run_shell("aerich init-db")
    ret = run_shell("aerich inspectdb -t product")
    assert ret.startswith("from tortoise import Model, fields")
    assert "fields.DatetimeField" in ret
    assert "fields.FloatField" in ret
