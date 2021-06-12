import requests, json, os

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

    def is_path(self, path):
        return os.path.exists(path)


class Pantry(Utility):
    def __init__(self, api_key=None) -> None:
        if api_key:
            self.api_key = api_key
        else:
            raise "Provide an API Key."

    def show_account(self, outputfile=None):
        self.outputfile = outputfile
        url = f"{BASE_URL}{self.api_key}"
        self.res = requests.get(url, headers=HEADERS)
        return self.check_response()

    def basket(self, basket=None, outputfile=None):
        self.outputfile = outputfile
        if basket:
            url = f"{BASE_URL}{self.api_key}/basket/{basket}"
            self.res = requests.get(url, headers=HEADERS)
            return self.check_response()

    def update(self, basket=None, outputfile=None):
        self.outputfile = outputfile
        if basket:
            url = f"{BASE_URL}{self.api_key}/basket/{basket}"
            data = self.read_json(path=self.outputfile)
            self.res = requests.put(url, headers=HEADERS, data=json.dumps(data))
            return self.check_response()

    def create(self, basket=None, inputfile=None):
        if basket:
            url = f"{BASE_URL}{self.api_key}/basket/{basket}"
            if inputfile:
                if self.is_path(inputfile):
                    data = self.read_json(path=inputfile)
                    self.res = requests.post(
                        url, headers=HEADERS, data=json.dumps(data)
                    )
                else:
                    raise f"Not a valid path : {inputfile}"
            else:
                self.res = requests.post(url, headers=HEADERS)
            return self.check_response()

    def delete(self, basket=None):
        if basket:
            url = f"{BASE_URL}{self.api_key}/basket/{basket}"
            self.res = requests.delete(url, headers=HEADERS)
            return self.check_response()

    def check_response(self):
        data = None
        if self.res:
            try:
                data = self.res.json()
            except TypeError:
                data = self.res.text

        if self.outputfile:
            self.write_json(path=self.outputfile, data=data)

        return data
