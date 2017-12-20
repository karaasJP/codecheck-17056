# coding utf-8
import requests
import apikeys


def main():
    print("生成する文章の長さを指定してください >>", end=" ")
    setlength = int(input())
    print("先頭となる文を入力してください　>>", end=" ")
    sentence = input()
    while len(sentence) <= setlength:
        response = textsuggest(sentence)
        texts = response.text[46:-2].split(',')
        text1 = texts[0][1:-1]

        sentence = sentence + text1
        print(sentence)
        print(len(sentence))


def textsuggest(sentence):
    url = 'https://api.a3rt.recruit-tech.co.jp/text_suggest/v2/predict'
    text_suggest_api_key = apikeys.text_suggest_api_key

    response = requests.get(
        url,
        params={'apikey': text_suggest_api_key,
                'previous_description': sentence,
                'separation': '2',
                'style': 0})

    return(response)


if __name__ == '__main__':
    main()
