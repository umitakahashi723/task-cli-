import json, os
import task          # 导入我们自己的模块

def test_add():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
    task.main(["task", "add", "unit test", "-p", "high"])
    data = task.load_tasks()
    assert len(data) == 1
    assert data[0]["title"] == "unit test"
    assert data[0]["priority"] == "high"

def test_list(capsys):
    task.main(["task", "list"])
    out, _ = capsys.readouterr()
    assert "unit test" in out
