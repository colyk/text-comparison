# add the comparison on Wikipedia articles
import re

def get_text(file_name):
    if(len(file_name)<15 and file_name.endswith('.txt')):
        try:
            file = open(file_name,'r', encoding = 'utf-8')
            return file.read()
        except:
            print(file_name+' does not exist!')
            exit(0)
    if (len(file_name)== 0):
        print('Your text is too short!')
        exit(0)
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
    print('Equal parts:  {}({})'.format(sum_of_identity,max(len(text),len(patern))))

    if(sum_of_identity == max(len(text),len(patern))):
        print('This text is fully copied!')
        exit(0)


def sentence_comparison(split_text,split_patern, precision = 0.7):
    matched_dict = {}
    minLen = 100
    for i in split_patern: 
        minLen = 100
        for j in split_text:
            if(distance(j,i)/max(len(i),len(j))<minLen):
                text_result = j
                patern_result = i
                minLen = distance(j,i)/max(len(i),len(j))
                if(1-minLen > precision):    
                    matched_dict[j] = i
    for i, j in matched_dict.items():
        print('With a precision more than 70% text: "{}" matched with: "{}"'.format(i,j))
    if(len(matched_dict)>1):
        exit(0)


def text_similarity(text, patern_text):
    similarity = distance(text,patern_text)/max(len(text),len(patern_text))
    print('The similarity of the whole text {:.0%}'.format(1 - similarity))
    if(similarity < 0.3):
        print('This text is likely a rip-off!')
        exit(0)

        
def main():
    text_name = input('Write the text or filename for analysis: ')
    patern = input('Write the text patern text or filename for analysis: ')
   
    text = get_text(text_name).replace('\n','')
    patern = get_text(patern).replace('\n','')

    split_text = [i for i in re.split(r'[.?!]', text) if i != '']
    split_patern = [i for i in re.split(r'[.?!]', patern) if i != '']

    check_equal_parts(split_text,split_patern)
    text_similarity(text, patern)
    sentence_comparison(split_text,split_patern)
    print("Your text is likely original!")
    

if __name__ == '__main__':
    main()