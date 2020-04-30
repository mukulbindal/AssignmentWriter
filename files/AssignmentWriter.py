from PIL import Image
import numpy as np
import random
import datetime
import pickle


class Assignment_Writer:
    FONT_SIZE_WIDTH = 33
    FONT_SIZE_HEIGHT = 36
    CHARACTER_PER_LINE = 50
    FONT_COLOR = (30, 30, 30)
    FONT_SIZE = (32, 32)
    tab_left = 20
    tab_right = 15
    def __init__(self, page, string, FONT_SIZE=(32, 32), FONT_SIZE_WIDTH=33, FONT_SIZE_HEIGHT=36,
                 FONT_COLOR=(30, 30, 30) , tab_left = 20 , tab_right = 15):
        self.page = page
        string = string.replace(" ", "$")
        string = string.replace(".", "@")
        self.tab_right = tab_right
        self.tab_left = tab_left
        self.string = string
        self.FONT_COLOR = FONT_COLOR
        self.FONT_SIZE = FONT_SIZE
        self.FONT_SIZE_HEIGHT = FONT_SIZE_HEIGHT
        self.FONT_SIZE_WIDTH = FONT_SIZE[0]
        self.CHARACTER_PER_LINE = max(page.shape[1] // (self.FONT_SIZE[0] - 23) - self.tab_right,
                                      page.shape[1] // (self.FONT_SIZE_WIDTH - 23) - self.tab_right)
        font_size = str(self.FONT_SIZE[0]) + 'x' + str(self.FONT_SIZE[1])
        fp = open(font_size + ".pickle", "rb")
        self.words = pickle.load(fp)
        print(page.shape)

    def write_char(self, start_i, start_j, character):
        for i in range(character.shape[0]):
            for j in range(character.shape[1]):
                if character[i][j][0] < 10:
                    try:
                        self.page[start_i + i][start_j + j] = self.FONT_COLOR
                    except IndexError:
                        pass

    def process(self):
        string = self.string.split('\n')
        text = []
        for i in string:
            x = i.split("$")
            length = 0
            for j in x:
                if length + len(j) >= self.CHARACTER_PER_LINE:  # replace 21 with desired width
                    text.append('\n')
                    text.append(j)
                    length = len(j)
                else:
                    text.append(j)
                length += len(j)
            text.append('\n')
        text = "$".join(text)
        self.text = text

    def write(self):
        start_j = self.tab_left
        start_i = 20
        N, M, MM = self.page.shape
        for i in self.text:
            if i != '\n' and start_j < M:
                try:
                    ind = random.randint(0, len(self.words[i]) - 1)
                    character = self.words[i][ind]
                except KeyError:
                    character = self.words['$'][0]

                self.write_char(start_i, start_j, character)
                start_j += self.FONT_SIZE_WIDTH - 23
            else:
                start_j = self.tab_left
                start_i += self.FONT_SIZE_HEIGHT
            if start_i > N:
                print("exeeded")
                break

    def generate(self):
        self.process()
        self.write()

    def show(self):
        self.new_page = Image.fromarray(self.page)
        self.new_page.show()

    def save(self):
        self.new_page.save(open('output/' + str(datetime.datetime.now())[0:16] + '.jpg', 'wb'))



page = Image.open('pagea4.jpg')
page = page.resize((850, 1280))
page_list = np.asarray(page)
page_list = page_list.copy()
a = AssignmentWriter(page=page_list, string="".join(open("text.txt", 'r').readlines()) , FONT_SIZE=(36,36) , FONT_COLOR=(0,0,0) , FONT_SIZE_HEIGHT=30)
a.generate()
a.show()
a.save()
