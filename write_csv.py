import csv


class WriteCSV:
    def __init__(self):
        self.filename = None
        self.headers = None
        self.payload = None
        self.header_added = False
        self.writer = None
        self.csv_file = None

    def write_header(self, filename, headers):
        self.filename = filename
        self.headers = headers
        with open(self.filename + '.csv', 'a', newline='') as self.csv_file:
            writer = csv.DictWriter(self.csv_file, fieldnames=self.headers)
            if not self.header_added:
                # add header to csv
                # print("writing header in csv....")
                writer.writeheader()
                self.header_added = True

    def write_data(self, filename, data):
        self.filename = filename
        self.payload = data
        with open(self.filename + '.csv', 'a', newline='') as self.csv_file:
            writer = csv.DictWriter(self.csv_file, fieldnames=self.headers)
            if self.header_added:
                # add data row to csv
                # print("writing row in csv....")
                # print(self.payload)
                writer.writerow(self.payload)

    def __del__(self):
        self.filename = None
        self.headers = None
        self.payload = None
        self.header_added = False
        self.writer = None
        self.csv_file.close()
