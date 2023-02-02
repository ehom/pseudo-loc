import pathlib
import os


def derive_output_target(filename, target_path) -> dict:
    def get_filename_info(fname: str) -> dict:
        abspath = os.path.abspath(fname)
        p = pathlib.Path(abspath)

        return {
            "abspath_folder": p.parents[0],
            "filename": p.name
        }

    info = get_filename_info(filename)

    if target_path:
        folder_path = os.path.abspath(target_path)
    else:
        folder_path = info['abspath_folder']
    folder_path = os.path.join(folder_path, "pseudo")

    file_path = os.path.join(folder_path, info['filename'])

    return {
        "folder_path": folder_path,
        "file_path": file_path
    }
