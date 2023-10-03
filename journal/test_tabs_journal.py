import unittest
from unittest.mock import patch

from django.contrib.auth import get_user_model


from journal.models import (
    SciELOJournal,
    Journal,
    OfficialJournal,
    Collection,
    Subject,
)

from journal.outputs.tabs_journal import (
    add_extraction_date,
    add_tabs_journal,
    add_issn_scielo,
    add_issns,
    add_title_at_scielo,
    add_title_thematic_areas,
    add_title_current_status,
)

User = get_user_model()


class TabsJournalTest(unittest.TestCase):
    def setUp(self):
        user, created = User.objects.get_or_create(username="teste_user", password="teste_user")
        self.collection = Collection()
        self.collection.acron3 = "bol"
        self.collection.save()

        self.official_journal = OfficialJournal.create_or_update(
            user=user,
            title="Official Journal Title",
            issn_print="0000-0000",
            issn_electronic="1111-1111",
            issnl="2222-2222",
            foundation_year=None
        )
        self.journal = Journal.create_or_update(
            user=user,
            official_journal=self.official_journal,
            title="Journal Title",
            short_title=None,
            other_titles=None,
        )
        self.journal.subject.add(Subject.create_or_update(code="Health Sciences", user=user))
        self.journal.subject.add(Subject.create_or_update(code="Exact and Earth Sciences", user=user))

        self.scielo_journal = SciELOJournal.create_or_update(
            user=user,
            collection=self.collection,
            issn_scielo="0000-0000",
            journal=self.journal,
            journal_acron=None
        )
        self.scielo_journal.status = "Current"

    @patch('journal.outputs.tabs_journal.get_date')
    def test_add_tabs_journal(self, mock_get_date):
        obtained = {}

        mock_get_date.return_value = "1900-01-01"

        add_extraction_date(obtained)

        add_tabs_journal(self.scielo_journal, collection="bol", dict_data=obtained)

        expected = {
            "extraction date": "1900-01-01",
            "study unit": "journal",
            "collection": "bol",
            "ISSN SciELO": "0000-0000",
            "ISSN's": "0000-0000;1111-1111;2222-2222"
        }

        self.assertDictEqual(expected, obtained)

    @patch('journal.outputs.tabs_journal.get_date')
    def test_add_extraction_date(self, mock_get_date):
        obtained = {}

        mock_get_date.return_value = "1900-01-01"

        add_extraction_date(obtained)

        expected = {
            "extraction date": "1900-01-01"
        }

        self.assertDictEqual(expected, obtained)

    def test_add_issn_scielo(self):
        obtained = {}

        add_issn_scielo(self.scielo_journal, obtained)

        expected = {
            "ISSN SciELO": "0000-0000"
        }

        self.assertDictEqual(expected, obtained)

    def test_add_issns_object_is_journal(self):
        obtained = {}

        add_issns(self.journal, obtained)

        expected = {
            "ISSN's": "0000-0000;1111-1111;2222-2222"
        }

        self.assertDictEqual(expected, obtained)

    def test_add_issns_object_is_official_journal(self):
        obtained = {}

        add_issns(self.official_journal, obtained)

        expected = {
            "ISSN's": "0000-0000;1111-1111;2222-2222"
        }

        self.assertDictEqual(expected, obtained)

    def test_add_issns_object_is_scielo_journal(self):
        obtained = {}

        add_issns(self.scielo_journal, obtained)

        expected = {
            "ISSN's": "0000-0000;1111-1111;2222-2222"
        }

        self.assertDictEqual(expected, obtained)


if __name__ == '__main__':
    unittest.main()
