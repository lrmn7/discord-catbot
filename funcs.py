from rich import print as printf
import datetime as dt
import random as r
import os


def get_ts() -> str:
    """
    It gets the current time and returns it in a string format
    :return: A string of the current time in the format:
              DD/MM/YY HH:MM:SS
    """
    # Gets the current time
    timezone_diff = dt.timedelta(hours=5.5)
    tz_info       = dt.timezone(timezone_diff, name="GMT")
    curr_time     = dt.datetime.now(tz_info)
    return curr_time.strftime('%d/%m/%y %H:%M:%S')


def get_file_path(eyebleach_path: str,
                  allowed_exts: list = ['png', 'jpg', 'jpeg', 'mp4'],
                  max_size=None,
                  amount: int = 1) -> list:
    # Gets all the files
    all_files = os.listdir(eyebleach_path)
    # Shuffles them
    r.shuffle(all_files)
    # Sets variables to use to determine the length of the loop
    found_files = []
    # Loops through them until it finds a valid file
    for fname in all_files:
        fp = os.path.join(eyebleach_path, fname)
        # Checks if its cache
        if fname.startswith('.'):         continue
        # Checks if its of a valid extension
        ext = os.path.splitext(fname)[1][1:]
        if ext not in allowed_exts:       continue
        # Checks if it's a video cache made by instagrapi/moviepy
        if fname.endswith('.mp4.jpg'):    continue
        # Checks if it satisfies the size limit
        size = os.path.getsize(fp)
        if max_size is not None:
            if size > max_size:           continue
        # Adds the file info to the list
        found_files.append({'fp': fp, 'fname': fname, 'ext': ext, 'size': size})
        # If the amount of files is reached, it breaks the loop
        if len(found_files) >= amount:
            break

    # If no valid file was found, returns None
    if not found_files:
        return None
    return found_files


def logme(text: str):
    printf(text)
    with open('log.txt', 'a') as f:
        f.write(f'{text}\n')
