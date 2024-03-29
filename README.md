# Вводная информация HTML
HTML - Hypertext Markup Language

Язык разметки гипертекста
```
Представляет собой систему таблиц и списков для отображения информации
Для построения разметки используются теги
Структура тега:
<div>Content</div>
<div> - открывающий тег
</div> - зыкрывающий тег
Content - содержимое тега
Целиком эта структура называется элементом
Открывающий тег может нести атрибуты элемента, которые перечисляются через
пробел в формате
attrname=«value»
Основные глобальные атрибуты (которые есть у всех тегов)
class - указывает стилистический класс
id - уникальный индентификатор элемента
hidden - указывает на то, что элемент скрытый (не отображается) но он доступен
через скрипты
style - для передачи стилей css
Полный перечень глобальный атрибутов с описанием доступен по ссылке:
http://htmlbook.ru/samhtml5/globalnye-atributy
Структура HTML документа
• <!DOCTYPE html> — доктайп. В прошлом, когда HTML был молод (около
1991/1992), доктайпы должны были выступать в качестве ссылки на набор
правил, которым HTML страница должна была следовать, чтобы считаться
хорошим HTML, что могло означать автоматическую проверку ошибок и
другие полезные вещи. Однако в наши дни, никто не заботится об этом, и
они на самом деле просто исторический артефакт, который должен быть
включён для того, что бы все работало правильно. На данный момент это
все, что вам нужно знать.
• <html></html> — Этот элемент оборачивает весь контент на всей странице,
и иногда известен как корневой элемент.
• <head></head> — Этот элемент выступает в качестве контейнера для всего,
что вы пожелаете включить на HTML страницу, но не являющегося
контентом, который вы показываете пользователям вашей страницы. К ним
относятся такие вещи, как ключевые слова и описание страницы, которые
будут появляться в результатах поиска, CSS стили нашего контента,
кодировка и многое другое.
• <body></body> — В нем содержится весь контент, который вы хотите
показывать пользователям, когда они посещают вашу страницу, будь то
текст, изображения, видео, игры, проигрываемые аудиодорожки или что-то
ещё.

• <meta charset="utf-8"> — этот элемент устанавливает UTF-8 кодировку
вашего документа, которая включает в себя большинство символов из всех
известных человечеству языков. По сути, теперь документ может
обрабатывать любой текстовый контент, который вы в него вложите. Нет
причин не устанавливать её, так как это может помочь избежать некоторых
проблем в дальнейшем.
• <title></title> — Этот элемент устанавливает заголовок для вашей страницы,
который является названием, появляющимся на вкладке браузера
загружаемой страницы, и используется для описания страницы, когда вы
добавляете её в закладки/избранное.
<img> - Тег для подключения картинки, не имеет закрывающего тега
Атрибуты:
src - ссылка/путь на картинку
alt - альтернативное содержимое (текст) который будет отображаться если
картинка не доступна, а так же будет отображаться если навести курсор на
картинку даже если она прогружена
<h1></h1> (от 1 до 6) - Заголовки, считается, что заголовок первого уровня h1
должен присутствовать в единственном экземпляре в отличии от остальных
<p></p> - Абзац
<ul></ul> - Ненумерованный список
<ol></ol> - Нумерованный список
Элементы списков оборачиваются в тег <li></li>
<a></a> - Ссылка
Атрибуты:
href - ссылка на ресурс или элемент страницы
<div></div> - Основной блочный тег, служит для разметки страницы, такие теги
как header, footer, nav и тд являются тем же тегом div
Атрибуты:
align - Задает выравнивание содержимого тега
<script> - Служит для описания или подключения скриптов
Атрибуты:
async - Загружает скрипт асинхронно.
defer - Откладывает выполнение скрипта до тех пор, пока вся страница не будет
загружена полностью.
language - Устанавливает язык программирования на котором написан скрипт.
src - Адрес скрипта из внешнего файла для импорта в текущий документ.
type -Определяет тип содержимого тега <script>.
<b></b> - Делает текст жирным
<I></I> - Делает текст курсивным
<input> - Однострунное поле ввода
<textarea> - Многострунное поле ввода

CSS - Cascad Style Sheet
Каскадная таблица стилей, служит для описания стилистики содержимого
страницы
Анатомия:
div {
color: red;
}
Div - селектор, элемент или class/id элемента для которого/которых
прописываются стили
color - свойство
red - значение свойства
Все свойства перечисляются через ; а свойство и его значение через :
#some_id - для указания индентификатора
.some_class - для указания класса
Можно указывать несколько селекторов через запятую
`
Свойства и их возможные значения вы всегда можете найти здесь:
https://html5book.ru/osnovy-css/
