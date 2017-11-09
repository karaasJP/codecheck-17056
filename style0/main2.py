# coding utf-8
import requests
import apikeys


def main():
    allsentence = ''
    while True:
        print(">>", end=" ")
        sentence = input()
        if sentence == 'end':
            break
        response = textsuggest(sentence)
        texts = response.text[46:-2].split(',')
        text1 = texts[0][1:-1]
        # print(sentence)
        allsentence += sentence + text1
        print(text1)

    print(allsentence)
    print(len(allsentence))


def textsuggest(sentence):
    url = 'https://api.a3rt.recruit-tech.co.jp/text_suggest/v2/predict'
    text_suggest_api_key = apikeys.text_suggest_api_key

    response = requests.get(
        url,
        params={'apikey': text_suggest_api_key,
                'previous_description': sentence,
                'separation': '2',
                'style': '73b4ee57-e3e2-4c94-82ff-6bdd2660dfb9'})

    return(response)


if __name__ == '__main__':
    main()
