from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    # raise NotImplementedError
    with open(path, encoding="utf-8") as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        info = []
        for unit in file_reader:
            info.append(unit)
        return info

# print(read('data/jobs.csv'))


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    # raise NotImplementedError
    jobs = set(
        [index['job_type'] for index in read(path) if index['job_type']]
        )
    return jobs

# print(get_unique_job_types('data/jobs.csv'))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    # raise NotImplementedError
    filter_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs

# print(filter_by_job_type(read('data/jobs.csv'), "FULL_TIME"))
