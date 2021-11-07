import sys
import unittest
from pathlib import Path
from bs4 import BeautifulSoup


BASENAME = 'lesson10-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class WelcomeTestCase(SkyproTestCase):
    def setUp(self):
        with open("tag.html", 'r') as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_main_span(self):
        span = self.main.span
        self.assertIsNotNone(
            span,
            "%@Проверьте, что добавили тег 'строка'(span)")
        span_tags = self.main.find_all('span', recursive=False)
        len_span = len(span_tags)
        self.assertEqual(
            len_span, 2,
            ("%@Проверьте что добавили все теги строка в блок main."
             f" Должно быть 2, тогда как у вас {len_span}"))
        expected_text = ['Посты по тегу', '3 поста']
        span_text = (span_text.text for span_text in span_tags)
        for expected, text, index in zip(expected_text, span_text, range(2)):
            self.assertEqual(
                expected, text,
                f"%@Проверьте что {index} строка в блоке main содержит правильный текст"
            )

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, '#Природа',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")


    def test_blocks(self):
        html_div = self.main.div
        self.assertIsNotNone(
            html_div,
            "%@Проверьте, что добавили блоки в тег main"
        )
        html_div_list = self.main.find_all('div')
        ln_div_list = len(html_div_list)
        self.assertEqual(
            ln_div_list, 3,
            ("%@Проверьте, что у Вас правильное"
             f" количество блоков. У Вас {ln_div_list},"
             " тогда как должно быть 3.")
        )
        tags = {
            'hr': 'орионтальный разделитель', 
            'a':'тег со ссылкой', 
            'span':'тег со строкой'}
        users_text = {
            1: {'@happycorgi': 'Очень мило, мне все нравится!'},
            2: {'@techirktsk': 'Нашел землю. Такая хорошенькая! Съем ее!'},
            3: {'@awwawwaww': 'Смотрите, какой у меня пуховик, классно смотрится на фоне звездного неба, да?'},
        }
        for div, index in zip(html_div_list, range(3)):
            for key in tags.keys():
                value = tags.get(key)
                self.assertIsNotNone(
                    getattr(div, key), f"%@Проверьте что {index+1} блок содержит {value}"
                )
            item = users_text.get(index+1).items()
            [[user, text]] = item
            self.assertEqual(
                div.a.text, user,
                f"%@Проверьте что {index+1} блок содержит ссылку с правильным пользователем."
            )
            self.assertEqual(
                div.span.text, text,
                f"%@Проверьте что {index+1} блок содержит правильный текст с комментарием."
            )

if __name__ == "__main__":
    unittest.main()