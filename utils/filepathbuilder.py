import pathlib
import os


def build_file_path(filename, target_path) -> str:
    """ build a file_path """
    file_path = os.path.abspath(filename)
    p = pathlib.Path(file_path)
    src_path = p.parents[0]
    filename = p.name

    # print(src_path, filename)

    if target_path:
        target_path = os.path.abspath(target_path)
    else:
        target_path = src_path
    target_path = os.path.join(target_path, "pseudo")

    # print("path of target folder:", target_path)

    os.makedirs(target_path, exist_ok=True)
    file_path = os.path.join(target_path, filename)

    # print("path of target file:", file_path)

    return file_path
