import pathlib
import os


def derive_output_target(filename, target_path) -> dict:
    def derive_folder_path_and_filename(fname: str) -> dict:
        abspath = os.path.abspath(fname)
        p = pathlib.Path(abspath)
        return dict(folder_path=p.parents[0], filename=p.name)

    info = derive_folder_path_and_filename(filename)

    # if a custom output folder was provided at the command line
    if target_path:
        folder_path = os.path.abspath(target_path)
    else:
        folder_path = info['folder_path']
    return dict(folder_path=folder_path, file_path=info['filename'])
