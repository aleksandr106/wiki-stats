#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            s=f.readline()
            s=s.split()
            (n, _nlinks) = (int(s[0]), int(s[1])) # TODO: прочитать из файла
            
            self._titles = []
            self._edges=array.array('L',[0]*_nlinks)
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            # TODO: прочитать граф из файла
            for i in range(int(s[0])):
                k=f.readline()
                self._titles.append(k[:-1])
                k=f.readline()
                k=k.split()
                self._sizes[i]=int(k[0])
                self._redirect[i]=int(k[1])
                self._links[i]=int(k[2])
                self._offset[i+1]=self._offset[i]+self._links[i]   #исправить тип integer
                for j in range(int(k[2])):
                    m=f.readline()
                    self._edges[j+self._offset[i]]=int(m)
        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._links[_id]

    def get_links_from(self, _id):
        return self._edges[self._offset[_id]:self._offset[_id+1]]
    def get_id(self, title):
        i=0
        while i<len(self._titles) and self._titles[i]!=title:
            i+=1
        if i>=len(self._titles):
            return 'Статья не найдена'
        else:
            return i

    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        if self._redirect[_id]!=0:
            return True
        else:
            return False

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':
        print('Использование: wiki_stats.py wiki_small.txt')
        wg = WikiGraph()
        wg.load_from_file('wiki_small.txt')
        print(type(wg._links[1]))
        perenapravlenia=0
        minssilok=len(wg._links)
        kolminssilok=0
        maxssilok=0
        kolmaxssilok=0
        statay_s_maxssilok=''
        srednee_kolssilok=0
        for i in range(len(wg._titles)):
            if wg.is_redirect(i):
               perenapravlenia+=1
            if wg.get_number_of_links_from(i)<minssilok:
                minssilok=wg.get_number_of_links_from(i)
                kolminssilok=1
            elif wg.get_number_of_links_from(i)==minssilok:
                kolminssilok+=1
            if wg.get_number_of_links_from(i)>maxssilok:
                maxssilok=wg.get_number_of_links_from(i)
                kolmaxssilok=1
                statay_s_maxssilok=wg.get_title(i)
            elif wg.get_number_of_links_from(i)==maxssilok:
                kolmaxssilok+=1
                statay_s_maxssilok=statay_s_maxssilok+wg.get_title(i)
            srednee_kolssilok+=wg.get_number_of_links_from(i)
        vnesh_ssilok=[0]*len(wg._titles)
        for i in (wg._edges):
            vnesh_ssilok[i]+=1
        min_vnesh_ssilok=min(vnesh_ssilok)
        max_vnesh_ssilok=max(vnesh_ssilok)
        kol_min_vnesh_ssilok=0
        kol_max_vnesh_ssilok=0
        statay_s_max_vnesh_ssilok=''
        srednee_kol_vnesh_ssilok=0
        for i in range(len(vnesh_ssilok)):
            srednee_kol_vnesh_ssilok+=vnesh_ssilok[i]
            if min_vnesh_ssilok==vnesh_ssilok[i]:
                kol_min_vnesh_ssilok+=1
            if max_vnesh_ssilok==vnesh_ssilok[i]:
                kol_max_vnesh_ssilok+=1
                statay_s_max_vnesh_ssilok+=wg.get_title(i)
        srednee_kol_vnesh_ssilok=srednee_kol_vnesh_ssilok/len(vnesh_ssilok)
        print('Количество статей с перенаправлениями:',perenapravlenia)
        print('Минимальное количество ссылок из статьи:', minssilok)
        print('Количество статей с минимальным количеством ссылок:', kolminssilok)
        print('Максимальное количество ссылок из статьи:',maxssilok)
        print('Количество статей с максимальным количеством ссылок:',kolmaxssilok)
        print('Статья с наибольшим количеством ссылок:', statay_s_maxssilok)
        print('Среднее количество ссылок в статье:', srednee_kolssilok/len(wg._titles))
        print('Минимальное количество ссылок на статью:',min_vnesh_ssilok)
        print('Количество статей с минимальным количеством внешних ссылок:', kol_min_vnesh_ssilok)
        print('Максимальное количество ссылок на статью:',max_vnesh_ssilok)
        print('Количество статей с максимальным количеством внешних ссылок:',kol_max_vnesh_ssilok)
        print('Статья с наибольшим количеством внешних ссылок:',statay_s_max_vnesh_ssilok)
        print('Среднее количество внешних ссылок на статью:',srednee_kol_vnesh_ssilok)


    # TODO: статистика и гистограммы
