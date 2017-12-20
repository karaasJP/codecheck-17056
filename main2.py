# coding utf-8
import requests
import apikeys


def main():
    allsentence = ''
    while True:
        print(">>", end=" ") # 入力を受け付ける
        sentence = input()
        if sentence == 'end': # endと入力すると終了
            break
        response = textsuggest(sentence) # テキストサジェストAPI
        texts = response.text[46:-2].split(',') # レスポンスを分解
        text1 = texts[0][1:-1] # ひとつ目の文章を選択
        # print(sentence)
        allsentence += sentence + text1
        print(text1) # ひとつ目の文章を出力

    print(allsentence) # 終了後に全ての文章を出力
    print(len(allsentence)) # 全ての文章の長さを出力


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
