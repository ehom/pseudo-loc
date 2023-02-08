import os
import utils


def customize_filename(func):
    def func_wrapper(filename, folder) -> dict:
        result = func(filename, folder)
        result['file_path'] = os.path.join(result['folder_path'], result['file_path'])
        return result
    return func_wrapper


def customize_folder_path(func):
    def func_wrapper(filename, folder) -> dict:
        result = func(filename, folder)
        result['folder_path'] = os.path.join(result['folder_path'], "pseudo")
        return result
    return func_wrapper


@customize_filename
@customize_folder_path
def customize(filename, folder_path):
    return utils.derive_output_target(filename, folder_path)