---
title: Дослідження та розробка системи на основі RAG
titleTemplate: '%s'
info: |
  ## Дипломна робота
  Retrieval-Augmented Generation для створення галузевого помічника

  Чубирка Віктор Васильович
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
fonts:
  sans: 'Roboto'
  mono: 'Fira Code'
layout: cover
background: https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1920
backgroundSize: cover
---

## Дослідження та розробка системи на основі RAG для створення галузевого помічника на базі великої мовної моделі.

<div class="pt-12">
  <span class="text-sm opacity-75">
    Виконав: Чубирка Віктор Васильович<br>
    Науковий керівник: Глебена Мирослава Іванівна<br>
    кандидат фізико-математичних наук, доцент
  </span>
</div>

<div class="abs-br m-6 text-sm opacity-50">
  Ужгород – 2025
</div>

<!--
Шановні члени комісії вітаю всіх, мене звати Віктор, мій наукой керівник, це Мирослава Іванівна. Я хочу вам розказати про мою дипломну роботу, на тему, "Дослідження та розробка системи на основі РАГ для сворення галузевого поміщника на базі великої мовної моделі".
Щож це таке і як це їсти давайте розбиратись.
-->

---
layout: default
---

# Актуальність теми

<div class="text-gray-400 mb-6">Інтеграція AI у реальні бізнес-процеси — головний виклик сучасного IT</div>

<div class="grid grid-cols-3 gap-4">

<v-click>
<div class="p-4 rounded-xl bg-blue-500/10 border border-blue-500/30 h-full">
  <div class="text-3xl mb-3 text-center">🎯</div>
  <div class="text-sm text-gray-300 text-center">Світ відходить від "загальних чат-ботів" до систем, які розуміються на нюансах <span class="text-blue-400 font-semibold">конкретної галузі</span></div>
</div>
</v-click>

<v-click>
<div class="p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 h-full">
  <div class="text-3xl mb-3 text-center">📊</div>
  <div class="text-4xl font-bold text-amber-400 text-center mb-2">80%</div>
  <div class="text-sm text-gray-300 text-center">галузевих знань зберігаються в <span class="text-amber-400 font-semibold">неструктурованому</span> виді</div>
</div>
</v-click>

<v-click>
<div class="p-4 rounded-xl bg-purple-500/10 border border-purple-500/30 h-full">
  <div class="text-3xl mb-3 text-center">📚</div>
  <div class="text-sm text-gray-300 text-center">Зростає потреба в системах для <span class="text-purple-400 font-semibold">орієнтації</span> у великій кількості документів</div>
</div>
</v-click>

</div>

<v-click>
<div class="mt-6 p-4 rounded-xl bg-gradient-to-r from-green-500/20 to-emerald-500/20 border border-green-500/40 text-center">
  <span class="text-2xl mr-2">🚀</span>
  <span class="text-lg text-green-300 font-semibold">Актуальність:</span>
  <span class="text-gray-200"> створення моста між потужністю LLM та зовнішнім джерелом знань</span>
</div>
</v-click>

<!--
З приходом Штучного Інтелекту у світ він наче змінився. Навіть у нас на захисті є вагомий кусок робіт які повязані зі Штучним Інетелектом. За статистикою більшість інформації яка існує вона зберігається в неструктурованому вигялді. Від цього і зростає потреба в системах яка зможе допомогти орієнтуватись в цьому хаосі інформації.

Актуальність моєї роботи полягає у створенні моста між потужністю сучасних мовних моделей та зовнішнім джерелом знань."
-->

---
layout: default
---

# Що таке RAG?

<div class="text-lg text-gray-400 mb-6">
Retrieval-Augmented Generation — архітектурний підхід, що поєднує:
</div>

<div class="grid grid-cols-3 gap-6">

<div class="p-4 rounded-xl bg-blue-500/10 border border-blue-500/30">
  <div class="text-3xl mb-2">🔍</div>
  <div class="text-xl font-bold text-blue-400 mb-2">Retrieval</div>
  <div class="text-sm text-gray-300">Пошук релевантної інформації з бази знань</div>
</div>

<div class="p-4 rounded-xl bg-purple-500/10 border border-purple-500/30">
  <div class="text-3xl mb-2">🔗</div>
  <div class="text-xl font-bold text-purple-400 mb-2">Augmented</div>
  <div class="text-sm text-gray-300">Збагачення запиту знайденим контекстом</div>
</div>

<div class="p-4 rounded-xl bg-green-500/10 border border-green-500/30">
  <div class="text-3xl mb-2">✨</div>
  <div class="text-xl font-bold text-green-400 mb-2">Generation</div>
  <div class="text-sm text-gray-300">Формування відповіді на основі контексту</div>
</div>

</div>

<div class="mt-8 p-4 rounded-lg bg-yellow-500/10 border-l-4 border-yellow-500">
  <span class="text-yellow-400 font-semibold">💡 Ключова ідея:</span> Поєднати потужності LLM з зовнішнім джерелом знань
</div>

<!--
Таким мостом і слугує наш РАГ - це архітектурний підхід у створені чатботі,  який складається з цих трьох компонентів, про які я згодом розповім. І його головна суть - це поєднати потужності сучасниз ЛЛМ з зовнішнім джерелом знань
-->

---
layout: default
---

# RAG на практиці

<v-click>

<div class="p-5 rounded-2xl bg-gradient-to-r from-cyan-500/20 via-blue-500/20 to-cyan-500/20 border-2 border-cyan-400/50 text-center mb-6">
  <div class="text-4xl mb-2">📚 📄 📑 📰 📋</div>
  <div class="text-2xl font-bold text-cyan-300">База Знань</div>
  <div class="text-sm text-gray-400 mt-1">PDF • DOCX • TXT • HTML • Markdown</div>
</div>

</v-click>

<div class="grid grid-cols-3 gap-4">
<v-clicks>

<div class="p-4 rounded-xl bg-blue-500/15 border-2 border-blue-400/50 text-center">
  <div class="text-4xl font-black text-blue-400 mb-2">R</div>
  <div class="text-2xl mb-2">🔍</div>
  <div class="text-sm font-semibold text-blue-300">Retrieval</div>
  <div class="text-xs text-gray-400 mt-2">Шукаємо релевантні<br/>🧩 фрагменти</div>
</div>

<div class="p-4 rounded-xl bg-purple-500/15 border-2 border-purple-400/50 text-center">
  <div class="text-4xl font-black text-purple-400 mb-2">A</div>
  <div class="text-2xl mb-2">🔗</div>
  <div class="text-sm font-semibold text-purple-300">Augmented</div>
  <div class="text-xs text-gray-400 mt-2">Додаємо<br/>📋 системний промпт</div>
</div>

<div class="p-4 rounded-xl bg-green-500/15 border-2 border-green-400/50 text-center">
  <div class="text-4xl font-black text-green-400 mb-2">G</div>
  <div class="text-2xl mb-2">✨</div>
  <div class="text-sm font-semibold text-green-300">Generation</div>
  <div class="text-xs text-gray-400 mt-2">🤖 LLM генерує<br/>💬 відповідь</div>
</div>

</v-clicks>
</div>

<v-click>

<div class="flex justify-center items-center gap-3 mt-6 text-2xl">
  <span>📚</span>
  <span class="text-blue-400 text-blue">←</span>
  <span class="font-bold text-blue-400">R</span>
  <span class="text-blue">→</span>
  <span class="font-bold text-purple-400">A</span>
  <span class="text-purple-400">→</span>
  <span class="font-bold text-green-400">G</span>
  <span class="text-green-400">→</span>
  <span>💬</span>
</div>

</v-click>

<!--
Отже як це виглядає на практиці 
У нас є наша База Знань, це можуть бути наші будь які документи, файли, табличкі будт що, чому ми довіряємо
Як це працює у нас є наша база знань після чого ми в цій базі знань шукаємо кусочок інформації яка нас цікавить доповнюємо її системним промптом, де пишемо, щоб відповідь базувалась тільки на заданому джерелі, після чого це все відправляєм на генерацію в нашу ллм і отримуєм відповідь.
-->

---
layout: default
---

# Завантажити документ у ChatGPT

<div class="grid grid-cols-2 gap-6">

<v-click>
<div class="rounded-xl overflow-hidden border-2 border-gray-600">
  <img src="./assets/gpt-question.png" class="w-full" />
</div>
</v-click>

<v-click>
<div class="rounded-xl overflow-hidden border-2 border-gray-600">
  <img src="./assets/gpt-answer.png" class="w-full" />
</div>
</v-click>

</div>

<v-click>

<div class="mt-8 p-4 rounded-lg bg-yellow-500/10 border-l-4 border-yellow-500 text-center">
  <span class="text-xl text-yellow-300 font-semibold ml-2">Але чи це RAG?</span> <span class="text-2xl">🤔</span>
</div>

</v-click>

<!--
Якщо я добре пояснив то у вас може виникнути питання?
Я ж можу просто взяти документ загрузити його в той же чат ГПТ добавити туди системний промпт і отримати відповідь.

І так це працює, але чи буде це РАГ?
-->

---
layout: default
---

# Так, це RAG... але з обмеженнями

<div class="space-y-6 mt-12">
<v-clicks>

<div class="flex items-center gap-4 p-5 rounded-xl bg-red-500/10 border-2 border-red-500/30">
  <span class="text-4xl">❌</span>
  <span class="text-xl text-red-300">Контекстне вікно <span class="font-bold text-red-400">~128K токенів</span></span>
</div>

<div class="flex items-center gap-4 p-5 rounded-xl bg-red-500/10 border-2 border-red-500/30">
  <span class="text-4xl">❌</span>
  <span class="text-xl text-red-300">Документ <span class="font-bold text-red-400">"забувається"</span> після сесії</span>
</div>

<div class="flex items-center gap-4 p-5 rounded-xl bg-red-500/10 border-2 border-red-500/30">
  <span class="text-4xl">❌</span>
  <span class="text-xl text-red-300">Відправка документа кожен раз = <span class="font-bold text-red-400">зайва витрата токенів</span> та <span class="font-bold text-red-400">UAH</span></span>
</div>

</v-clicks>
</div>

---
layout: default
---

# Керуючись best practices, мною була розроблена архітектура

<div class="grid grid-cols-2 gap-8 mt-12">

<v-click>
<div class="p-6 rounded-xl bg-amber-500/10 border-2 border-amber-400/50 text-center">
  <div class="text-5xl mb-3">📚</div>
  <div class="text-2xl font-bold text-amber-400 mb-2">База знань</div>
  <div class="text-sm text-gray-400">Knowledge Base</div>
  <div class="mt-4 p-3 rounded-lg bg-amber-500/10">
    <div class="text-sm font-semibold text-amber-300">📥 Етап індексації</div>
    <div class="text-xs text-gray-400 mt-1">Виконується один раз або при оновленні документів</div>
  </div>
</div>
</v-click>

<v-click>
<div class="p-6 rounded-xl bg-blue-500/10 border-2 border-blue-400/50 text-center">
  <div class="text-5xl mb-3">⚡</div>
  <div class="text-2xl font-bold text-blue-400 mb-2">Конвеєр RAG</div>
  <div class="text-sm text-gray-400">RAG Pipeline</div>
  <div class="mt-4 p-3 rounded-lg bg-blue-500/10">
    <div class="text-sm font-semibold text-blue-300">🔄 Етап виконання</div>
    <div class="text-xs text-gray-400 mt-1">Виконується в реальному часі для кожного запиту</div>
  </div>
</div>
</v-click>

</div>

<v-click>

<div class="mt-8 text-center text-gray-500">
Розглянемо кожен компонент детальніше...
</div>

</v-click>


---
layout: default
---

# Етап індексації: Завантаження документів

<div class="flex flex-col items-center mt-4">

<v-click>
<div class="flex items-center gap-4 mb-6">
  <span class="text-5xl">👤</span>
  <span class="text-3xl text-gray-400">завантажує</span>
</div>
</v-click>

<v-click>
<div class="p-6 rounded-2xl bg-gradient-to-r from-amber-500/20 via-orange-500/20 to-amber-500/20 border-2 border-amber-400/50 text-center">
  <div class="flex gap-4 justify-center text-4xl mb-4">
    <span>📄</span><span>📝</span><span>📋</span><span>🌐</span>
  </div>
  <div class="text-xl font-bold text-amber-300 mb-2">Великі документи</div>
  <div class="grid grid-cols-5 gap-1 mt-4">
    <div class="h-2 bg-amber-400/60 rounded"></div>
    <div class="h-2 bg-amber-400/50 rounded"></div>
    <div class="h-2 bg-amber-400/60 rounded"></div>
    <div class="h-2 bg-amber-400/50 rounded"></div>
    <div class="h-2 bg-amber-400/60 rounded"></div>
    <div class="h-2 bg-amber-400/50 rounded"></div>
    <div class="h-2 bg-amber-400/60 rounded"></div>
    <div class="h-2 bg-amber-400/50 rounded"></div>
    <div class="h-2 bg-amber-400/60 rounded"></div>
    <div class="h-2 bg-amber-400/50 rounded"></div>
  </div>
  <div class="text-sm text-gray-400 mt-3">PDF • DOCX • TXT • HTML • Markdown</div>
</div>
</v-click>

<v-click>
<div class="mt-6 p-4 rounded-lg bg-amber-500/10 border-l-4 border-amber-500">
  <span class="text-amber-400 font-semibold">📊 Приклад:</span>
  <span class="text-gray-300">10,000+ сторінок корпоративної документації</span>
</div>
</v-click>

</div>

---
layout: default
---

# Етап індексації: Chunking

<v-click>
<div class="p-3 rounded-xl bg-gray-800/20 border border-gray-700">
  <div class="text-xs leading-relaxed text-gray-100" style="line-height: 1.9;">
    <span style="background: rgba(251, 146, 60, 0.7); padding: 3px 1px; box-decoration-break: clone; -webkit-box-decoration-break: clone;">Згідно «Положення про дипломну роботу (дипломний проект)», затвердженого Вченою радою ДВНЗ «УжНУ» (протокол № 14 від 13.12.2016 року) (зі змінами) дипломні роботи повинні бути виконані і представлені на кафедру не пізніше як за два тижні до захисту. На етапі представлення матеріалів робіт для розгляду на засіданні кафедри, проводиться перевірка на академічний плагіат.</span><span style="background: linear-gradient(90deg, rgba(251, 146, 60, 0.7) 0%, rgba(74, 222, 128, 0.7) 100%); padding: 3px 1px; box-decoration-break: clone; -webkit-box-decoration-break: clone;"> На етапі представлення матеріалів робіт для розгляду на засіданні кафедри, проводиться перевірка на академічний плагіат.</span><span style="background: rgba(74, 222, 128, 0.7); padding: 3px 1px; box-decoration-break: clone; -webkit-box-decoration-break: clone;"> Перевірка робіт здобувачів освіти на унікальність проводиться на основі наданого електронного варіанту роботи у форматах .docx (.doc) або *.pdf, за допомогою системи «StrikePlagiarism». Усі наукові роботи, що надійшли після офіційно встановленого терміну, можуть бути прийняті тільки за спеціальним розпорядженням завідувача кафедри.</span><span style="background: linear-gradient(90deg, rgba(74, 222, 128, 0.7) 0%, rgba(96, 165, 250, 0.7) 100%); padding: 3px 1px; box-decoration-break: clone; -webkit-box-decoration-break: clone;"> Усі наукові роботи, що надійшли після офіційно встановленого терміну, можуть бути прийняті тільки за спеціальним розпорядженням завідувача кафедри.</span><span style="background: rgba(96, 165, 250, 0.7); padding: 3px 1px; box-decoration-break: clone; -webkit-box-decoration-break: clone;"> Для бакалаврських і магістерських дипломних робіт передбачена процедура попереднього захисту. Наукові роботи студентів, які мають академічну заборгованість, до захисту не допускаються.</span><span style="background: linear-gradient(90deg, rgba(96, 165, 250, 0.7) 0%, rgba(192, 132, 252, 0.7) 100%); padding: 3px 1px; box-decoration-break: clone; -webkit-box-decoration-break: clone;"> Наукові роботи студентів, які мають академічну заборгованість, до захисту не допускаються.</span><span style="background: rgba(192, 132, 252, 0.7); padding: 3px 1px; box-decoration-break: clone; -webkit-box-decoration-break: clone;"> Захист курсових робіт проводиться у присутності комісії у складі наукового керівника та членів кафедри. Захист бакалаврських і магістерських робіт відбувається на відкритому засіданні Екзаменаційної комісії (ЕК).</span><span style="background: linear-gradient(90deg,  rgba(192, 132, 252, 0.7) 0%, rgba(244, 114, 182, 0.7) 100%); padding: 3px 1px; box-decoration-break: clone; -webkit-box-decoration-break: clone;"> Захист бакалаврських і магістерських робіт відбувається на відкритому засіданні Екзаменаційної комісії (ЕК).</span><span style="background: rgba(244, 114, 182, 0.7); padding: 3px 1px; box-decoration-break: clone; -webkit-box-decoration-break: clone;"> Порядок захисту дипломних робіт визначений «Положенням про організацію освітнього процесу в ДВНЗ «УжНУ» і «Положенням про атестацію здобувачів вищої освіти та екзаменаційну комісію УжНУ», які затверджені Вченою радою УжНУ.</span>
  </div>
</div>
</v-click>

<v-click>
<div class="flex gap-4 justify-center mt-3">
  <div class="flex items-center gap-2">
    <div style="width: 18px; height: 12px; background: rgba(251, 146, 60, 0.7); border-radius: 3px;"></div>
    <span class="text-xs text-gray-400">Chunk 1</span>
  </div>
  <div class="flex items-center gap-2">
    <div style="width: 18px; height: 12px; background: rgba(74, 222, 128, 0.7); border-radius: 3px;"></div>
    <span class="text-xs text-gray-400">Chunk 2</span>
  </div>
  <div class="flex items-center gap-2">
    <div style="width: 18px; height: 12px; background: rgba(96, 165, 250, 0.7); border-radius: 3px;"></div>
    <span class="text-xs text-gray-400">Chunk 3</span>
  </div>
  <div class="flex items-center gap-2">
    <div style="width: 18px; height: 12px; background: rgba(192, 132, 252, 0.7); border-radius: 3px;"></div>
    <span class="text-xs text-gray-400">Chunk 4</span>
  </div>
  <div class="flex items-center gap-2">
    <div style="width: 18px; height: 12px; background: rgba(244, 114, 182, 0.7); border-radius: 3px;"></div>
    <span class="text-xs text-gray-400">Chunk 5</span>
  </div>
  <div class="flex items-center gap-2">
    <div style="width: 18px; height: 12px; background: linear-gradient(90deg, rgba(251, 146, 60, 0.7), rgba(74, 222, 128, 0.7)); border-radius: 3px;"></div>
    <span class="text-xs text-purple-300">Overlap</span>
  </div>
</div>
</v-click>

<v-click>
<div class="flex gap-4 justify-center mt-3">
  <div class="p-2 px-3 rounded-lg bg-gray-800/50 flex items-center gap-2">
    <span class="text-base">📏</span>
    <span class="text-xs text-gray-400">~128 токенів на chunk</span>
  </div>
  <div class="p-2 px-3 rounded-lg bg-purple-500/20 border border-purple-400/30 flex items-center gap-2">
    <span class="text-base">🔄</span>
    <span class="text-xs text-purple-300">Overlap — збереження контексту</span>
  </div>
</div>
</v-click>

---
layout: default
---

# Етап індексації: Embedding

<div class="grid grid-cols-3 gap-6 mt-8 items-center">

<v-click>
<div class="p-4 rounded-xl bg-orange-500/10 border-2 border-orange-400/50 text-center">
  <div class="text-3xl mb-2">📝</div>
  <div class="text-sm font-bold text-orange-300 mb-2">Chunk</div>
  <div class="text-xs text-gray-400 p-2 bg-gray-800/50 rounded font-mono">
    "Перевірку на плагіат здійснюють..."
  </div>
</div>
</v-click>

<v-click>
<div class="text-center">
  <div class="text-5xl mb-2">🧠</div>
  <div class="text-xl text-blue-400">→</div>
  <div class="text-sm text-gray-400 mt-2">Embedding<br/>Model</div>
</div>
</v-click>

<v-click>
<div class="p-4 rounded-xl bg-blue-500/10 border-2 border-blue-400/50 text-center">
  <div class="text-3xl mb-2">🔢</div>
  <div class="text-sm font-bold text-blue-300 mb-2">Vector</div>
  <div class="text-xs text-green-400 p-2 bg-gray-800/50 rounded font-mono">
    [0.021, -0.834,<br/>0.156, 0.742,<br/>-0.023, 0.891...]
  </div>
</div>
</v-click>

</div>

<v-click>
<div class="mt-8 p-4 rounded-lg bg-blue-500/10 border-l-4 border-blue-500 text-center">
  <div class="flex items-center justify-center gap-4">
    <span class="text-2xl">🤖</span>
    <span class="text-gray-300">Модель: <span class="font-bold text-blue-400">text-embedding-3-small</span></span>
    <span class="text-gray-500">|</span>
    <span class="text-gray-300">Розмірність: <span class="font-bold text-blue-400">1536</span></span>
  </div>
</div>
</v-click>

---
layout: default
---

# Етап індексації: Збереження в базу знань

<div class="flex items-center justify-center gap-12 mt-12">

<div class="flex flex-col gap-3">
<v-click>
    <div class="p-3 rounded-lg bg-blue-500/10 border border-blue-400/50">
      <span class="text-xs font-mono text-green-400">[0.021, -0.834, 0.156, ...]</span>
    </div>
    <div class="p-3 rounded-lg bg-blue-500/10 border border-blue-400/50">
      <span class="text-xs font-mono text-green-400">[0.156, 0.742, -0.023, ...]</span>
    </div>
    <div class="p-3 rounded-lg bg-blue-500/10 border border-blue-400/50">
      <span class="text-xs font-mono text-green-400">[-0.023, 0.891, 0.234, ...]</span>
    </div>
</v-click>
</div>

<v-click>
<div class="text-5xl text-green-400">→</div>
</v-click>

<v-click>
<div class="p-6 rounded-xl bg-green-500/10 border-2 border-green-400/50 text-center">
  <div class="text-5xl mb-3">🗄️</div>
  <div class="text-xl font-bold text-green-400">База знань</div>
  <div class="text-sm text-gray-400 mt-2">Vector Database</div>
</div>
</v-click>

</div>

<v-click>
<div class="mt-10 p-4 rounded-lg bg-green-500/10 border-l-4 border-green-500 text-center">
  <span class="text-2xl">✅</span>
  <span class="text-xl text-green-300 font-semibold ml-2">База знань готова до пошуку!</span>
</div>
</v-click>


---
layout: default
---

# Етап індексації RAG

<div class="flex justify-center items-center h-80">

```mermaid {scale: 0.8}
graph LR
    A["📚 Documents<br/>(Завантаження документів)"] --> B["✂️ Chunking<br/>(Нарізання на фрагменти)"]
    B --> D["🔢 Embedding<br/>(Векторизація тексту)"]
    D --> E["🗄️ Vector DB<br/>(Збереження)"]
    style A fill: #fff9c4, stroke: #f57f17, stroke-width: 2px, color: #1f2937
    style B fill: #ffccbc, stroke: #d84315, stroke-width: 2px, color: #1f2937
    style D fill: #b3e5fc, stroke: #0277bd, stroke-width: 2px, color: #1f2937
    style E fill: #c8e6c9, stroke: #388e3c, stroke-width: 2px, color: #1f2937
```

</div>

---
layout: default
---

# Конвеєр RAG: Запит користувача та Embedding

<div class="grid grid-cols-3 gap-6 mt-12 items-center">

<v-click>
<div class="p-4 rounded-xl bg-green-500/10 border-2 border-green-400/50 text-center">
  <div class="text-3xl mb-2">❓</div>
  <div class="text-sm font-bold text-green-300 mb-2">Запит</div>
  <div class="text-xs text-gray-400 p-2 bg-gray-800/50 rounded">
    "Які терміни подачі дипломної роботи?"
  </div>
</div>
</v-click>

<v-click>
<div class="text-center">
  <div class="text-5xl mb-2">🧠</div>
  <div class="text-xl text-blue-400">→</div>
  <div class="text-sm text-gray-400 mt-2">Embedding<br/>Model</div>
</div>
</v-click>

<v-click>
<div class="p-4 rounded-xl bg-blue-500/10 border-2 border-blue-400/50 text-center">
  <div class="text-3xl mb-2">🔢</div>
  <div class="text-sm font-bold text-blue-300 mb-2">Query Vector</div>
  <div class="text-xs text-green-400 p-2 bg-gray-800/50 rounded font-mono">
    [0.021, -0.834,<br/>0.156, 0.742,<br/>-0.023, 0.891...]
  </div>
</div>
</v-click>

</div>

<v-click>
<div class="mt-10 p-4 rounded-lg bg-purple-500/10 border-l-4 border-purple-500">
  <div class="flex items-center justify-center gap-4">
    <span class="text-2xl">🔑</span>
    <span class="text-gray-300">Використовується <span class="font-bold text-purple-400">та сама модель</span>, що й для документів</span>
  </div>
</div>
<div class="mt-4 p-3 rounded-lg bg-gray-800/30 text-center">
  <span class="text-gray-400">Це забезпечує <span class="font-semibold text-blue-400">семантичну сумісність</span> векторів запиту та документів</span>
</div>
</v-click>

---
layout: default
---

# Конвеєр RAG: Семантичний пошук

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="flex flex-col items-center">
<v-click>
<div class="p-4 rounded-xl bg-blue-500/10 border-2 border-blue-400/50 text-center">
  <div class="text-3xl mb-2">🔢</div>
  <div class="text-sm font-bold text-blue-300 mb-2">Query Vector</div>
  <div class="text-xs text-green-400 p-2 bg-gray-800/50 rounded font-mono">
    [0.021, -0.834,<br/>0.156, 0.742,<br/>-0.023, 0.891...]
  </div>
</div>

<div class="text-3xl text-blue-400 mb-4 mt-4">↓</div>

<div class="p-4 rounded-xl bg-orange-500/10 border-2 border-orange-400/50 text-center">
  <div class="text-4xl mb-2">🔍</div>
  <div class="text-lg font-bold text-orange-300 mb-2">Retriever</div>
  <div class="text-xs text-gray-400">Cosine Similarity</div>
</div>
</v-click>
</div>

<v-click>
<div class="p-5 rounded-xl bg-green-500/10 border-2 border-green-400/50">
  <div class="text-center mb-4">
    <span class="text-3xl">🗄️</span>
    <span class="text-lg font-bold text-green-300 ml-2">Top-K результатів</span>
  </div>
  <div class="space-y-2">
    <div class="flex items-center gap-2 p-2 rounded bg-green-500/20 border border-green-400/30">
      <span class="text-green-400 font-bold">0.92</span>
      <span class="text-xs text-gray-300">Chunk про терміни подачі</span>
    </div>
    <div class="flex items-center gap-2 p-2 rounded bg-green-500/15 border border-green-400/20">
      <span class="text-green-400 font-bold">0.87</span>
      <span class="text-xs text-gray-300">Chunk про дипломні роботи</span>
    </div>
    <div class="flex items-center gap-2 p-2 rounded bg-green-500/10 border border-green-400/10">
      <span class="text-green-400 font-bold">0.81</span>
      <span class="text-xs text-gray-300">Chunk про вимоги кафедри</span>
    </div>
    <div class="flex items-center gap-2 p-2 rounded bg-gray-500/10 border border-gray-400/10">
      <span class="text-gray-500">0.34</span>
      <span class="text-xs text-gray-500">Нерелевантний chunk</span>
    </div>
  </div>
</div>
</v-click>

</div>

---
layout: default
---

# Конвеєр RAG: Reranker

<div class="grid grid-cols-3 gap-4 mt-8 items-center">

<v-click>
<div class="p-4 rounded-xl bg-green-500/10 border-2 border-green-400/50">
  <div class="text-center mb-3">
    <span class="text-2xl">📋</span>
    <span class="text-sm font-bold text-green-300 ml-2">Top-K результати</span>
  </div>
  <div class="space-y-2 text-xs">
    <div class="p-2 rounded bg-gray-800/50">1. Chunk про терміни</div>
    <div class="p-2 rounded bg-gray-800/50">2. Chunk про диплом</div>
    <div class="p-2 rounded bg-gray-800/50">3. Chunk про кафедру</div>
    <div class="p-2 rounded bg-gray-800/50">4. Chunk про вимоги</div>
    <div class="p-2 rounded bg-gray-800/50">5. Chunk про захист</div>
  </div>
</div>
</v-click>

<v-click>
<div class="text-center">
  <div class="text-4xl mb-2">🎯</div>
  <div class="text-3xl text-purple-400">→</div>
  <div class="text-sm text-gray-400 mt-2">Cross-Encoder<br/>Reranker</div>
</div>
</v-click>

<v-click>
<div class="p-4 rounded-xl bg-purple-500/10 border-2 border-purple-400/50">
  <div class="text-center mb-3">
    <span class="text-2xl">✨</span>
    <span class="text-sm font-bold text-purple-300 ml-2">Переранжовано</span>
  </div>
  <div class="space-y-2 text-xs">
    <div class="p-2 rounded bg-purple-500/20 border border-purple-400/30">1. Chunk про терміни <span class="text-purple-400">↑</span></div>
    <div class="p-2 rounded bg-purple-500/15">2. Chunk про захист <span class="text-green-400">↑↑</span></div>
    <div class="p-2 rounded bg-purple-500/10">3. Chunk про вимоги <span class="text-green-400">↑</span></div>
    <div class="p-2 rounded bg-gray-800/50 text-gray-500">4. Chunk про диплом <span class="text-red-400">↓</span></div>
    <div class="p-2 rounded bg-gray-800/50 text-gray-500">5. Chunk про кафедру <span class="text-red-400">↓</span></div>
  </div>
</div>
</v-click>

</div>

<v-click>
<div class="mt-10 p-3 rounded-lg bg-yellow-500/10 border-l-4 border-yellow-500 text-center">
  <span class="text-yellow-400 font-semibold">💡</span>
  <span class="text-gray-300">Reranker аналізує <span class="font-bold text-yellow-400">пару (запит, chunk)</span> разом для кращого розуміння</span>
</div>
</v-click>

---
layout: default
---

# Конвеєр RAG: Генерація відповіді

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="space-y-2">
<v-click>
<div class="p-2 rounded-lg bg-purple-500/10 border border-purple-400/50">
  <div class="flex items-center gap-2 mb-1">
    <span class="text-sm">📋</span>
    <span class="text-xs font-bold text-purple-300">Системний промпт</span>
  </div>
  <div class="text-xs text-gray-400 p-2 bg-gray-900/50 rounded font-mono leading-relaxed">
    "Відповідай лише на основі джерел.<br/>
    Ставь посилання [1][2].<br/>
    Відповідай українською."
  </div>
</div>
</v-click>

<v-click>
<div class="p-2 rounded-lg bg-amber-500/10 border border-amber-400/50">
  <div class="flex items-center gap-2 mb-1">
    <span class="text-sm">📚</span>
    <span class="text-xs font-bold text-amber-300">Контекст (після reranker)</span>
  </div>
  <div class="text-xs text-gray-400 p-2 bg-gray-900/50 rounded space-y-1">
    <div>[1] Chunk про терміни подачі</div>
    <div>[2] Chunk про захист</div>
    <div>[3] Chunk про вимоги</div>
  </div>
</div>
</v-click>

<v-click>
<div class="p-2 rounded-lg bg-green-500/10 border border-green-400/50">
  <div class="flex items-center gap-2 mb-1">
    <span class="text-sm">❓</span>
    <span class="text-xs font-bold text-green-300">Запит</span>
  </div>
  <div class="text-xs text-gray-400 p-2 bg-gray-900/50 rounded font-mono">
    "Які терміни подачі дипломної роботи?"
  </div>
</div>
</v-click>
</div>

<div class="flex flex-col items-center justify-center">
<v-click>
<div class="p-3 rounded-xl bg-blue-500/10 border-2 border-blue-400/50 text-center mb-3">
  <div class="text-4xl">🤖</div>
  <div class="text-sm font-bold text-blue-300">LLM</div>
</div>
</v-click>

<v-click>
<div class="text-2xl text-green-400 mb-3">↓</div>
</v-click>

<v-click>
<div class="p-3 rounded-xl bg-gray-800/50 border-2 border-gray-600">
  <div class="flex items-center gap-2 mb-2">
    <span class="text-lg">💬</span>
    <span class="text-sm font-semibold text-gray-300">Відповідь:</span>
  </div>
  <div class="p-2 rounded-lg bg-gray-900/50 text-gray-200 text-xs leading-relaxed">
    "Дипломні роботи повинні бути представлені на кафедру <span class="text-green-400 font-semibold">не пізніше як за два тижні до захисту</span> <span class="text-blue-400">[1]</span>."
  </div>
</div>
</v-click>
</div>

</div>

---
layout: default
---

# Конвеєр RAG

<div class="flex justify-center items-center h-80">

```mermaid {scale: 0.7}
graph LR
    A["❓ Запит користувача"] --> B["🔢 Embedding"]
    B --> C["🔍 Пошуковий агент<br/>(Retriever)"]
    C <--> D["📚 База знань<br/>(Контекст)"]
    C --> E["📝 Системний промпт"]
    E --> F["🤖 LLM"]
    F --> G["✅ Відповідь"]

    style A fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#1f2937
    style B fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#1f2937
    style C fill:#ffccbc,stroke:#d84315,stroke-width:2px,color:#1f2937
    style D fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#1f2937
    style E fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#1f2937
    style F fill:#b3e5fc,stroke:#0277bd,stroke-width:2px,color:#1f2937
    style G fill:#b2dfdb,stroke:#00695c,stroke-width:2px,color:#1f2937
```

</div>

---
layout: center
---

# Демонстрація системи

<div class="text-center mt-12">

<div class="text-6xl mb-6">🖥️</div>
<div class="text-2xl text-gray-300 mb-4">Практична реалізація RAG-системи</div>
<div class="text-lg text-gray-500">Галузевий помічник для роботи з документами</div>

</div>

---
layout: center
---

<h1 class="text-center">Інтерфейс екрану документів</h1>

<div class="text-gray-400 mb-4 text-center">
Екран, де користувач може переглянути документи, з якими він може працювати
</div>

<div class="flex justify-center">
  <img src="./assets/image6.png" class="rounded-xl border-2 border-gray-600 max-h-96" />
</div>

---
layout: center
---

<h1 class="text-center">Відображення документа в системі</h1>

<div class="text-gray-400 mb-4 text-center">
При кліку на документ користувач може переглянути його відображення в системі, по якому відбувається пошук
</div>

<div class="flex justify-center">
  <img src="./assets/image1.png" class="rounded-xl border-2 border-gray-600 max-h-96" />
</div>

---
layout: center
---

<h1 class="text-center">Інтерфейс головного екрану</h1>

<div class="text-gray-400 mb-4 text-center">
Головний екран системи для взаємодії з галузевим помічником
</div>

<div class="flex justify-center">
  <img src="./assets/image4.png" class="rounded-xl border-2 border-gray-600 max-h-96" />
</div>

---
layout: center
---

<h1 class="text-center">Приклад роботи галузевого помічника</h1>

<div class="text-gray-400 mb-4 text-center">
Демонстрація роботи RAG-системи: запит користувача та відповідь на основі документів
</div>

<div class="flex justify-center">
  <img src="./assets/image2.png" class="rounded-xl border-2 border-gray-600 max-h-96" />
</div>

---
layout: center
---

<h1 class="text-center">Верифікація джерела відповіді</h1>

<div class="text-gray-400 mb-4 text-center">
Можливість перевірити джерело, з якого система сформувала відповідь
</div>

<div class="flex justify-center">
  <img src="./assets/image8.png" class="rounded-xl border-2 border-gray-600 max-h-96" />
</div>

---
layout: center
---

<h1 class="text-center">Розуміння контексту розмови</h1>

<div class="text-gray-400 mb-4 text-center">
Система розуміє контекст діалогу — запит "40%" автоматично пов'язується з попереднім обговоренням відсотку унікальності
</div>

<div class="flex justify-center">
  <img src="./assets/image3.png" class="rounded-xl border-2 border-gray-600 max-h-96" />
</div>

---
layout: center
---

<h1 class="text-center">Коли система не може відповісти</h1>

<div class="text-gray-400 mb-4 text-center">
Приклад ситуації, коли система не може надати відповідь на основі наявних джерел
</div>

<div class="flex justify-center">
  <img src="./assets/image7.png" class="rounded-xl border-2 border-gray-600 max-h-96" />
</div>

---
layout: center
---

<h1 class="text-center mb-10">Висновки</h1>

<div class="grid grid-cols-2 gap-8 max-w-4xl mx-auto">

<v-click>

<div class="bg-gradient-to-br from-green-900/40 to-green-800/20 p-6 rounded-2xl border border-green-500/30">
  <div class="text-4xl mb-4 text-center">✅</div>
  <h3 class="text-xl font-bold text-green-400 mb-3 text-center">RAG — необхідний підхід</h3>
  <p class="text-gray-300 text-center">
    Для ефективного використання LLM як галузевого помічника необхідно застосовувати архітектуру RAG
  </p>
</div>

</v-click>

<v-click>

<div class="bg-gradient-to-br from-orange-900/40 to-orange-800/20 p-6 rounded-2xl border border-orange-500/30">
  <div class="text-4xl mb-4 text-center">⚙️</div>
  <h3 class="text-xl font-bold text-orange-400 mb-3 text-center">Універсальність — складна задача</h3>
  <p class="text-gray-300 text-sm">
    Створення універсального помічника вимагає індивідуального налаштування:
  </p>
  <ul class="text-gray-400 text-sm mt-2 space-y-1">
    <li>системного промпта під предметну область</li>
    <li>стратегії реренкінгу для типів документів</li>
    <li>параметрів чанкінгу під структуру контенту</li>
  </ul>
</div>

</v-click>

</div>

---
layout: center
class: text-center
---

# Дякую за увагу! 🎉

<div class="text-xl mt-8">

## Retrieval-Augmented Generation
### Майбутнє інтелектуальних помічників

</div>

<div class="mt-12 text-lg opacity-75">

**Чубирка Віктор Васильович**

Ужгородський Національний Університет

2025

</div>

<div class="mt-8">

### Готовий відповісти на ваші запитання 💬

</div>
