import requests
from bs4 import BeautifulSoup
import contextlib
import re

class Babla:
    def __init__(self, source_lang, target_lang):
        """Class takes a source language and a target language.
        For example:
        babla = Babla("english", "polish")
        """
        self.source_lang, self.target_lang = source_lang, target_lang


    def _bs4_info(self, word, source_lang, target_lang):
        headers = {"User-Agent":"Mozilla/5.0"}
        url = f'https://bab.la/dictionary/{source_lang}-{target_lang}/{word}'
        result = requests.get(url, headers=headers)
        soup = BeautifulSoup(result.text, 'html.parser')
        self.soup = soup


    def translation(self, word, exact_word = 1):
        """Yields found translations of word (without context)
        For example:
        >>> babla = Babla("english", "polish")
        >>> list(babla.translation("use"))
        ['użyć', 'używać', 'wykorzystać', 'wykorzystywać', 'zastosować', 'skorzystać', 'zażyć',...]
        """
        r = self._bs4_info(word, self.source_lang, self.target_lang)
        print(self.source_lang, self.target_lang)
        div_class = self.soup.find_all('div','quick-result-entry')
        ul_class = self.soup.find_all('ul','sense-group-results')

        for index, div in enumerate(div_class):
            with contextlib.suppress(IndexError):
                for ul in ul_class[index]:
                    with contextlib.suppress(AttributeError):
                            if exact_word == 1 and div.find("a",{"class":"babQuickResult"}).get_text("") == word or exact_word != 1:
                                for n in ul.find_all('a'):
                                    meaning_string = n.get_text('title')
                                    if meaning_string != '\ntitlevolume_uptitle\n':
                                        yield meaning_string


    def example(self, word, exact_word = 1):
        """Yields sentence examples for passed word.
        For example:
        >>> import itertools  # just like other methods, this one returns iterator
        >>> babla = Babla("english", "polish")
        >>> list(itertools.islice(babla.example("use", 0), 2)) # take first two examples
        ['The oil base used is mostly mustard oil, but in festivals ghee is used.',
        'The border was redrawn using information based on studies using geographic information science.']
        """
        
        r = self._bs4_info(word, self.source_lang, self.target_lang)
        eng_pattern = re.compile(rf'\b{word}\b(?!ed|ing|s)')
        
        with contextlib.suppress(AttributeError):
            cleanup = self.soup.find("div",{"class":"icon-link-wrapper dropdown cs-source-link"}).text
            for i in self.soup.find_all("div",{"class":"mono-examples"}):
                example_string = i.get_text('', strip=True)
                example_string = example_string.lstrip(cleanup)
                if exact_word == 1 and re.search(eng_pattern, example_string) or exact_word != 1:
                    yield example_string