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
task_path = basepath.joinpath('part1', 'rules')
os.chdir(task_path)

class SettingsTestCase(SkyproTestCase):
    def setUp(self):
        with open("rules.html", 'r') as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, 'Правила сервиса',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")

    def test_paragraphs(self):
        paragraphs = self.main.p
        self.assertIsNotNone(
            paragraphs,
            "%@Проверьте, что добавили абзатцы в тег main"
        )
        expected = {
            0: ['i', ("Сервис предоставляется как "
                      "есть. Если вы не хотите чтобы "
                      "фото стало общедоступным - не "
                      "заружайте его.")],
            1: ['i', ("Мы храним Ваши данные и "
                      "следим за Вами, но не для того, "
                      "чтобы продать Ваши данные, "
                      "просто мы любопытные.")],
            2: ['a', "Я соглашаюсь"],
            3: ['a',"Мне нужно подумать"],
        }
        expected_len = len(expected)
        paragraphs = self.main.find_all('p', recursive=False)
        current_len = len(paragraphs)
        self.assertEqual(
            current_len, expected_len,
            (f"%@Проверьте, что добавили все абзатцы. У Вас их {current_len}, "
             f"тогда как должно быть {expected_len}"))


        for paragraph, index in zip(paragraphs, range(len(expected))):
            tag = getattr(paragraph, expected.get(index)[0])
            self.assertIsNotNone(
                tag, 
                f"%@Проверьте, что добавили все теги {tag.name} в абзатцы"
            )
            self.assertEqual(
                tag.text, expected.get(index)[1],
                f"%@Проверьте, правильный ли текст в абзатце {index+1}")


if __name__ == "__main__":
    unittest.main()