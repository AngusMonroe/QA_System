import os
import logging
import sys
import re
import jieba
import multiprocessing
import gensim

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def process_wiki(inp, outp):
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    i = 0

    output = open(outp, 'w', encoding='utf-8')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(b' '.join(text).decode('utf-8') + '\n')
        i = i + 1
        if i % 10000 == 0:
            logger.info('Saved ' + str(i) + ' articles')

    output.close()
    logger.info('Finished ' + str(i) + ' articles')

def remove_words(inp, outp):
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    output = open(outp, 'w', encoding='utf-8')
    inp = open(inp, 'r', encoding='utf-8')

    for line in inp.readlines():
        ss = re.findall('[\n\s*\r\u4e00-\u9fa5]', line)
        output.write("".join(ss))
    logger.info("Finished removed words!")

def separate_words(inp, outp):
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)


    output = open(outp, 'w', encoding='utf-8')
    inp = open(inp, 'r', encoding='utf-8')

    for line in inp.readlines():
        seg_list = jieba.cut(line.strip())
        output.write(' '.join(seg_list) + '\n')
    logger.info("finished separate words!")

def train_w2v_model(inp, outp1, outp2):
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    model = Word2Vec(LineSentence(inp), size=200, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())
    model.save(outp1)
    model.save_word2vec_format(outp2, binary=False)

def main():
    # process_wiki('./data/zhwiki-latest-pages-articles.xml.bz2', './data/wiki_cn.txt')
    # remove_words('./data/wiki_cn_jian.txt', './data/wiki_cn_jian_removed.txt')
    # separate_words('./data/wiki_cn_jian_removed.txt', './data/wiki_cn_jian_sep_removed.txt')
    train_w2v_model('./data/wiki_cn_jian_sep_removed.txt', './bin/300/w2v_model.bin', './bin/300/w2v_vector.bin')


if __name__ == '__main__':
    main()
    model = gensim.models.Word2Vec.load('./bin/300/w2v_model.bin')
    print(model.most_similar([u'李连杰', u'基金'], [u'成龙']))
