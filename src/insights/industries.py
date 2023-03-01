from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    """ industry = set(
        [index['industry'] for index in read(path) if index['industry']]
        )
    return industry """
    industry = set(
        [index['industry'] for index in read(path) if index['industry']]
        )
    return industry


# print(get_unique_industries('data/jobs.csv'))

def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    # raise NotImplementedError
    filter_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filter_jobs.append(job)
    return filter_jobs


# print(filter_by_industry(read('data/jobs.csv'), "NJfor Mondays"))