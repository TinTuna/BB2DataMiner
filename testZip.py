import zipfile
with zipfile.ZipFile("ReplayStubs/0b69d36b97d781814b46d138e61de3cb_2023-02-26_12_43_03.bbrz", 'r') as zip_ref:
    zip_ref.extractall("ReplayStubs")