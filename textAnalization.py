# Добавить сравнение по википедии

import re


def get_text(file_name):
    if(len(file_name)<15 and file_name.endswith('.txt')):
        return open(file_name,'r', encoding = 'utf-8').read()
    return file_name


def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n
    current_column = range(n+1)
    for i in range(1, m+1):
       previous_column, current_column = current_column, [i]+[0]*n
       for j in range(1,n+1):
          add, delete, change = previous_column[j]+1, current_column[j-1]+1, previous_column[j-1]
          if a[j-1] != b[i-1]:
             change += 1
          current_column[j] = min(add, delete, change)

    return current_column[n]


def check_equal_parts(text,patern):
    sum_of_identity = 0
    identity_list = []
    for sentence in text:
        if(sentence in patern):
            sum_of_identity+=1
            identity_list.append(sentence)

    print('Equal parts = ' + str(sum_of_identity))
    if(sum_of_identity != 0):
        print('persent of identity = {:.0%}'.format(sum_of_identity/len(text)))
        print(identity_list)
    return sum_of_identity

# Добавить сравнение похожести всего текста
def fuzzy_comparison():
    minLen = 100
    for i in split_patern: 
        for j in split_text:
           if(distance(j,i)/max(len(i),len(j))<minLen):
               text_result = j
               patern_result = i
               minLen = distance(j,i)/max(len(i),len(j))
    print('С точностью {:.0%} "{}" совпал с "{}"'.format(minLen,text_result,patern_result))


def main():
    text_name = input('Print text or filename for analization: ')
    patern = input('Print patern text or filename for analization: ')

    text = get_text(text_name).replace('\n','')
    patern = get_text(patern).replace('\n','')

    split_text = [i for i in re.split(r'[.?!]', text) if i != '']
    split_patern = [i for i in re.split(r'[.?!]', patern) if i != '']

    check_equal_parts(split_text,split_patern)
    fuzzy_comparison()
    

if __name__ == '__main__':
    main()