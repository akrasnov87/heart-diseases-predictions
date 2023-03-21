# Прогнозирование сердечно-сосудистых заболеваний

На основе предоставленных данных спрогнозировать риск сердечно-сосудистых заболеваний (ССЗ):
* age - возраст (дней с рождения)
* gender - пол
* height - рост
* weight - вес
* ap_hi - верхнее давление
* ap_lo - нижнее давление
* cholesterol - холестерин
* gluc - глюкоза
* smoke - курит или нет
* alco - злоупотребляет алкоголем
* active - ведёт активных образ жизни
* cardio - признак наличия сердечных заболеваний

Метрика для оценки качества **ROC-AUC** по целевому признаку **cardio**

## Структура проекта

* train.csv - тренировочные данные
* test.csv - данные для тестирования
* submission.csv - дополнительный файл, который формировался для получения результата на [kaggle](https://www.kaggle.com)
* notebook906ef33a06.ipynb - тетрадка со скриптами для формирования модели
* app.py - скрипт для запуска веб-интерфейса для тестирования модели
* heart.model - обученная модель, будет создана после выполения notebook.ipynb

## Шаги запуска

### Обучение модели

Запускаем тетрадку ***notebook.ipynb*** и результатом выполнения будет модель heart.model, которая сохраниться в корне проекта.

**Примечание**: при запуске убедиться, что библиотеки *numpy, pandas, matplotlib, seaborn, tqdm, sklearn, joblib* установлены.

### Тестирование в веб-интерфейсе

Веб-интерфейс разработан при помощи библиотеки [streamlit](https://docs.streamlit.io/library/get-started/installation).

<pre>
pip install streamlit
</pre>

Для запука выполнить команду <code>python -m streamlit run app.py</code>. 

**Внимание**: перед запуском скрипта убедиться, что в корне проекта есть файл **heart.model**

**Примечание**: запуск скрипта может отличаться и зависит от операционной системы, подробнее смотреть на [официальном сайте](https://docs.streamlit.io/library/get-started) разработчика. 

## Примечание автора

Проект не является медицинским решением и требует доработок.