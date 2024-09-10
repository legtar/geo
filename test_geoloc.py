import subprocess

def test_geoloc_util():
    result = subprocess.run(['python', 'geoloc_util.py', 'Madison,WI', '12345'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Madison' in result.stdout
    assert '12345' in result.stdout

if __name__ == "__main__":
    test_geoloc_util()
    print("All tests passed!")
