Простой телегам бот для генерации случайных изображений животных таких как: кот, собака, капибара, панда, лиса.

Идею бота взял у https://github.com/Svvaliv/AnimalsBot/tree/main

Запуск бота через Docker:

1. Создать в проекте файл .env по примеру как в .env.example
2. docker build -t AnimalsBot .
3. docker run --name animals_bot AnimalsBot
