from ollama import chat

# Tarixiy chatni saqlovchi ro'yxat
chat_history = [
    {
        'role': 'system',
        'content': 'Sen aqlli yordamchisan va o‘zbek tilida javob berasan.'
    }
]

def chat_with_model(query='', model='llama3.1:latest'):

    # Foydalanuvchining so‘rovini tarixga qo‘shish
    chat_history.append({'role': 'user', 'content': query})

    stream = chat(
        model=model,
        messages=chat_history,
        stream=True,
    )

    response_text = ''
    for chunk in stream:
        content = chunk['message']['content']
        print(content, end='', flush=True)
        response_text += content

    # Assistant javobini tarixga qo‘shish
    chat_history.append({'role': 'assistant', 'content': response_text})


def main():
    while True:
        query = input('\nSo\'rang (chiqish uchun \'exit\' yozing.): ')

        if query.lower() in ['exit', 'quit', 'q']:
            print('Dastur tugatildi.')
            break
        elif query.strip() == '':
            print('Iltimos, savol kiriting.')
            continue
        else:
            chat_with_model(query=query)


if __name__ == '__main__':
    main()