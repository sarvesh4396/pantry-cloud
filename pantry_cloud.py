import requests, json

BASE_URL = "https://getpantry.cloud/apiv1/pantry/"
HEADERS = {"Content-Type": "application/json"}


class Utility:
    # Write json File
    def write_json(self, path, data):
        try:
            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file)
        except TypeError:
            with open(path, "w", encoding="utf-8") as file:
                json.dump(json.dumps(data), file)
        except Exception as e:
            print(f"Got Exception {e}.\nPlease report.")

    # Read json file
    def read_json(self, path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                return json.load(file)
        except Exception as e:
            print(f"Got Exception {e}.\nPlease report.")
            exit(0)


class Pantry(Utility):
    def __init__(self, api_key=None) -> None:
        if api_key:
            self.api_key = api_key
        else:
            raise "Provide an API Key."