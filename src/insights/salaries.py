from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # raise NotImplementedError
    salaries = []
    max = 0
    salaries.append(
        [unit['max_salary'] for unit in read(path) if unit['max_salary']]
    )
    # return salaries[0]
    for salary in salaries[0]:
        try:

            if int(salary) > max:
                max = int(salary)
        except ValueError:
            max
    return max


# print(get_max_salary('data/jobs.csv'))


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    # raise NotImplementedError

    salaries = []
    min = 383416
    salaries.append(
        [unit['min_salary'] for unit in read(path) if unit['min_salary']]
    )
    # return salaries[0]
    for salary in salaries[0]:
        try:

            if int(salary) < min:
                min = int(salary)
        except ValueError:
            min
    return min


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    # raise NotImplementedError

    """ max_salary = job["max_salary"]
    min_salary = job["min_salary"] """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Não há min_salary ou max_salary")
    # Preciso saber se o salário mínimo ou máximo são somente números, para
    # isso usei o método str().isdigit()
    # https://www.programiz.com/python-programming/methods/string/isdigit
    if (
        not str(job["min_salary"]).isdigit()
        or not str(job["max_salary"]).isdigit()
    ):
        raise ValueError("Os valores precisam ser somente numéricos")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("O valor mínimo é maior que o máximo")
    # Há números negativos, então vamos tirar o sinal só para verficar
    # se é um número negativo e não uma coisa doida, tipo:
    # -12adf - isso não é um número negativo.
    # https://www.w3schools.com/python/ref_string_lstrip.asp
    if not str(salary).lstrip('-').isdigit():
        raise ValueError("Salary isn't a valid integer")
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    # raise NotImplementedError
    list_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs.append(job)
        except ValueError:
            print(ValueError)
    return list_jobs
