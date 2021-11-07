import sys
import unittest
from pathlib import Path
from bs4 import BeautifulSoup
import os

BASENAME = 'lesson10-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
task_path = basepath.joinpath('part1', 'comments')
os.chdir(task_path)

class SettingsTestCase(SkyproTestCase):
    def setUp(self):
        with open("comments.html", 'r') as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, 'Комментарии',
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
            'p': 'абзатц'}
        users_text = {
            1: {'@happycorgi': ['Очень мило, мне все нравится!']},
            2: {'@inpiration_ru': ['Так держать, работаем дальше!']},
            3: {'@techirktsk': ['Eee!']},
        }
        
        for div, index in zip(html_div_list, range(3)):
            for key in tags.keys():
                value = tags.get(key)
                self.assertIsNotNone(
                    getattr(div, key), f"%@Проверьте что {index+1} блок содержит {value}"
                )
            item = users_text.get(index+1).items()
            [[user, values]] = item
            p_list = div.find_all('p')
            self.assertIsNotNone(
                p_list.a,
                f"%@Проверьте что {index+1} блок содержит абзатц со ссылкой."
            )
            self.assertEqual(
                p_list[0].a.text, user,
                f"%@Проверьте что {index+1} блок содержит ссылку с правильным пользователем."
            )
            self.assertEqual(
                p_list[1].text, values[0],
                f"%@Проверьте что {index+1} блок содержит правильный текст с комментарием."
            )

if __name__ == "__main__":
    unittest.main()