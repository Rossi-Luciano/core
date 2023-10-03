from datetime import datetime

from journal.exceptions import (
    AddIssnScieloToTabsError,
    AddIssnsToTabsError,
    AddTitleAtScieloError,
    AddTitleThematicAreasError,
    AddTitleCurrentStatusError,
)


def get_date():
    """
    Obtem a data de execução do código

    Returns
    -------
    str
        2023-08-30
    """
    return datetime.utcnow().strftime("%Y-%m-%d")


def add_extraction_date(dict_data={}):
    """
    Adiciona a data de extração dos dados em um dicionário

    Parameters
    ----------
    dict_data : dict
        Dicionário que receberá os dados

    Returns
    -------
    dict_data : dict
        Dicionário com dados adicionados, como por exemplo:
        {
            "extraction date": "1900-01-01"
        }
    """
    dict_data["extraction date"] = get_date()


def add_issn_scielo(scielo_journal, dict_data={}):
    """
    Adiciona o ISSN SciELO em um dicionário

    Parameters
    ----------
    scielo_journal : journal.models.SciELOJournal
        Objeto com dados de um periódico SciELO

    dict_data : dict
        Dicionário que receberá os dados

    Returns
    -------
    dict_data : dict
        Dicionário com dados adicionados, como por exemplo:
        {
            "ISSN SciELO": "0000-0000"
        }
    """
    try:
        dict_data["ISSN SciELO"] = scielo_journal.issn_scielo
    except AttributeError as e:
        raise AddIssnScieloToTabsError(e, scielo_journal)


def add_issns(scielo_journal, dict_data={}):
    """
    Adiciona uma série de ISSN's em um dicionário

    Parameters
    ----------
    scielo_journal : journal.models.SciELOJournal
        Objeto com dados de um periódico SciELO

    dict_data : dict
        Dicionário que receberá os dados

    Returns
    -------
    dict_data : dict
        Dicionário com dados adicionados, como por exemplo:
        {
            "ISSN's": "0000-0000;1111-1111;2222-2222"
        }
    """
    try:
        dict_data["ISSN's"] = ";".join([
            scielo_journal.journal.official.issn_print,
            scielo_journal.journal.official.issn_electronic,
            scielo_journal.journal.official.issnl
        ])
    except AttributeError as e:
        raise AddIssnsToTabsError(e, scielo_journal)


def add_title_at_scielo(scielo_journal, dict_data={}):
    """
    Adiciona o título do periódico em um dicionário

    Parameters
    ----------
    scielo_journal : journal.models.SciELOJournal
        Objeto com dados de um periódico SciELO

    dict_data : dict
        Dicionário que receberá os dados

    Returns
    -------
    dict_data : dict
        Dicionário com dados adicionados, como por exemplo:
        {
            "title at SciELO": "Journal Title"
        }
    """
    try:
        dict_data["title at SciELO"] = scielo_journal.journal.title
    except AttributeError as e:
        raise AddTitleAtScieloError(e, scielo_journal)


def add_title_thematic_areas(scielo_journal, dict_data={}):
    """
    Adiciona as áreas temáticas do periódico em um dicionário

    Parameters
    ----------
    scielo_journal : journal.models.SciELOJournal
        Objeto com dados de um periódico SciELO

    dict_data : dict
        Dicionário que receberá os dados

    Returns
    -------
    dict_data : dict
        Dicionário com dados adicionados, como por exemplo:
        {
            "title thematic areas": "Health Sciences;Exact and Earth Sciences",
            "title is agricultural sciences": 0,
            "title is applied social sciences": 0,
            "title is biological sciences": 0,
            "title is engineering": 0,
            "title is exact and earth sciences": 1,
            "title is health sciences": 1,
            "title is human sciences": 0,
            "title is linguistics, letters and arts": 0,
            "title is multidisciplinary": 0
        }
    """
    subjects = {
        "title is agricultural sciences": "Agricultural Sciences",
        "title is applied social sciences": "Applied Social Sciences",
        "title is biological sciences": "Biological Sciences",
        "title is engineering": "Engineering",
        "title is exact and earth sciences": "Exact and Earth Sciences",
        "title is health sciences": "Health Sciences",
        "title is human sciences": "Human Sciences",
        "title is linguistics, letters and arts": "Linguistic, Literature and Arts",
        "title is multidisciplinary": "Multidisciplinary"
    }

    try:
        thematic_areas = [subject.value for subject in scielo_journal.journal.subject.iterator()]
        dict_data["title thematic areas"] = ";".join(thematic_areas)
        for column, value in subjects.items():
            dict_data[column] = 1 if value in thematic_areas else 0
    except AttributeError as e:
        raise AddTitleThematicAreasError(e, scielo_journal)


    try:
        issn = None
        if type(obj) is OfficialJournal:
            issn = obj
        elif type(obj) is Journal:
            issn = obj.official
        elif type(obj) is SciELOJournal:
            issn = obj.journal.official
        dict_data["ISSN's"] = ";".join([issn.issn_print, issn.issn_electronic, issn.issnl])
    except AttributeError as e:
        raise AddIssnsToTabsError(e, obj)


def add_tabs_journal(obj, collection, dict_data={}):
    add_extraction_date(dict_data)
    dict_data.update({
        "study unit": "journal",
        "collection": collection
    })
    add_issn_scielo(obj, dict_data)
    add_issns(obj, dict_data)
