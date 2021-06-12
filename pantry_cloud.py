import requests, json


class Utility:
    # Write json File
    def write_json(self, path, data):
        try:
            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file)
        except TypeError:
            with open(path, "w", encoding="utf-8") as file:
                json.dump(json.dumps(data), file)

    # Read json file
    def read_json(self, path):
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            return json.load(file)