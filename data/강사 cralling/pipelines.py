
import csv


class RTPipeline(object):

    def __init__(self):
        self.writecsv = csv.writer(open("rt_new.csv", "w"))
        # self.writecsv.writerow(["title","score"])
        self.writecsv.writerow(["title"])

    def process_item(self, item, spider):
        row = list()
        row.append(item["title"])
        # row.append(item["score"])
        self.writecsv.writerow(row)
        return item
