import kaggle
import os

kaggle.api.authenticate()
print("authenticated")
if not os.path.exists("./input"):
    os.mkdir("./input")
kaggle.api.dataset_download_files('shayanfazeli/heartbeat', path='./input', unzip=True)