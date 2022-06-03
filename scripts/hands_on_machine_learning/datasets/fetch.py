import pathlib
import tarfile
import wget


DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/'


HOUSING_URL = DOWNLOAD_ROOT + 'datasets/housing/housing.tgz'

def housing(destination_dir: pathlib.Path, url: str = HOUSING_URL):
    """
    path should be a directory, the actual file is extracted from a .tgz file
    """
    destination_dir.mkdir(parents=True, exist_ok=True)
    tgz_path = destination_dir / 'housing.tgz'
    wget.download(url=url, out=str(tgz_path))

    tgz_file = tarfile.open(tgz_path)
    tgz_file.extractall(path=destination_dir)
    tgz_file.close()
