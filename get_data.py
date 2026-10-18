import io, zipfile, urllib.request, urllib.error, pathlib

BASE = "https://s3.amazonaws.com/tripdata/"
OUT = pathlib.Path("data")
OUT.mkdir(exist_ok=True)

def fetch(name):
    try:
        with urllib.request.urlopen(BASE + name) as r:
            print("  OK:", name)
            return r.read()
    except urllib.error.HTTPError as e:
        print("  ", e.code, name)
        return None

def extract(data):
    z = zipfile.ZipFile(io.BytesIO(data))
    for member in z.namelist():
        if member.startswith("__MACOSX"):
            continue
        if member.endswith(".zip"):
            extract(z.read(member))
        elif member.endswith(".csv"):
            (OUT / pathlib.Path(member).name).write_bytes(z.read(member))

missing = []
for m in range(1, 7):
    stem = f"2020{m:02d}-citibike-tripdata"
    print("Trying", stem)
    data = fetch(stem + ".csv.zip") or fetch(stem + ".zip")
    if data:
        extract(data)
    else:
        missing.append(stem)

if missing:
    print("Monthly files not found, trying the 2020 yearly archive...")
    data = fetch("2020-citibike-tripdata.zip")
    if data:
        extract(data)
        missing = []

print("Missing:", missing if missing else "none")
