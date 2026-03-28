import subprocess

def get_last_commit_diff() -> str:
    result = subprocess.run(
        ["git", "diff", "HEAD~1", "HEAD"],
        capture_output=True,
        text=True,
        check=False
    )
    if result.returncode != 0:
        return ""
    return result.stdout
