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

---
layout: default
---

# Актуальність теми

Інтеграція AI у реальні бізнес-процеси — головний виклик сучасного IT.

<v-clicks>

*  Світ відходить від "загальних чат-ботів" до вузькопрофільних асистентів, які розуміють специфіку конкретної галузі.
*  Близько **80%** галузевиз знань зберігаються в неструктурованому виді, які складно використовувати для швидкого пошуку.
*  Зростає потреба в системах, які можуть автоматично обробляти складні запити клієнтів без залучення людини-оператора.

</v-clicks>

<v-click>


> **🚀Актуальність полягає:** у створенні моста між потужністю великих мовних моделей та специфічними, закритими даними підприємства.

</v-click>

---
layout: default
---

# Переваги LLM

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## 🚀 Переваги LLM

<v-clicks>

- 🎯 **Універсальність** - один інструмент для багатьох задач
- 🧠 **Контекстне розуміння** - аналіз нюансів мови
- 💬 **Легкість використання** - взаємодія природною мовою
- 🚀 **Zero/Few-shot** - виконання нових задач без перенавчання
- 🌍 **Багатомовність** - підтримка десятків мов

</v-clicks>

</div>

<div>

## 📋 Сфери застосування

<v-clicks>

- 📝 **Генерація контенту** - тексти, маркетинг, звіти
- 🤖 **Інтелектуальні чат-боти**
- 📋 **Узагальнення** - резюме документів
- 🌐 **Машинний переклад** 
- 💻 **Написання коду** 

</v-clicks>

</div>

</div>

<v-click>

<div class="mt-6 bg-amber-50 p-4 rounded-lg border-2 border-amber-300 text-gray-800 text-center">

### 🤔 Але чи можуть LLM замінити експертів у спеціалізованих галузях?

</div>

</v-click>

---
layout: default
---

# Обмеження базових LLM

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## ⚙️ Технічні обмеження

<v-clicks>

- 📅 **Knowledge Cutoff** - знання обмежені датою тренування
- 🔒 **Приватні дані** - немає доступу до корпоративних документів
- 📏 **Контекстне вікно** - обмежений обсяг вхідних даних
- 🎓 **Галузева специфіка** - незнання вузької термінології

</v-clicks>

</div>

<div>

## ⚠️ Проблеми достовірності

<v-clicks>

- 🟠 **Галюцинації** - генерація вигаданих фактів
- ❓ **Неможливість верифікації** - немає посилань на джерела
- 📊 **Застаріла статистика** - неактуальні числові дані
- 🚨 **Правдоподібні, але хибні твердження** 

</v-clicks>

</div>

</div>

<v-click>

<div class="mt-6 bg-amber-50 p-4 rounded-lg border-2 border-amber-300 text-gray-800 text-center">

### 📋 Подивимось на конкретні приклади

</div>

</v-click>

---
layout: default
---

# Типові сценарії невдач

<div class="grid grid-cols-3 gap-3 mt-4">

<v-click>
<div class="bg-red-50 p-3 rounded-lg border-2 border-red-200 text-gray-800">
<div class="text-sm font-bold text-red-700">❌ Запит:</div>
<div class="text-xs italic text-gray-700">"Які останні новини про компанію X?"</div>
<div class="text-xs mt-2 text-red-600">→ LLM не знає актуальних подій</div>
<div class="text-xs font-bold mt-2">🔴 Knowledge Cutoff</div>
</div>
</v-click>

<v-click>
<div class="bg-orange-50 p-3 rounded-lg border-2 border-orange-200 text-gray-800">
<div class="text-sm font-bold text-orange-700">❌ Запит:</div>
<div class="text-xs italic text-gray-700">"Знайди в інструкції термін гарантії"</div>
<div class="text-xs mt-2 text-orange-600">→ LLM не має доступу до документів</div>
<div class="text-xs font-bold mt-2">🟡 Приватні дані</div>
</div>
</v-click>

<v-click>
<div class="bg-yellow-50 p-3 rounded-lg border-2 border-yellow-200 text-gray-800">
<div class="text-sm font-bold text-yellow-700">❌ Запит:</div>
<div class="text-xs italic text-gray-700">"Яка статистика продажів за Q3 2024?"</div>
<div class="text-xs mt-2 text-yellow-600">→ LLM може вигадати дані</div>
<div class="text-xs font-bold mt-2">🟠 Галюцинації</div>
</div>
</v-click>

</div>

<div class="grid grid-cols-2 gap-3 mt-3 mx-auto max-w-2xl">

<v-click>
<div class="bg-blue-50 p-3 rounded-lg border-2 border-blue-200 text-gray-800">
<div class="text-sm font-bold text-blue-700">❌ Запит:</div>
<div class="text-xs italic text-gray-700">"Що таке КЗ-5 у нашому регламенті?"</div>
<div class="text-xs mt-2 text-blue-600">→ LLM не знає внутрішніх скорочень</div>
<div class="text-xs font-bold mt-2">🔵 Галузева термінологія</div>
</div>
</v-click>

<v-click>
<div class="bg-purple-50 p-3 rounded-lg border-2 border-purple-200 text-gray-800">
<div class="text-sm font-bold text-purple-700">❌ Запит:</div>
<div class="text-xs italic text-gray-700">"Дай посилання на джерело цієї інформації"</div>
<div class="text-xs mt-2 text-purple-600">→ LLM не може підтвердити інформацію</div>
<div class="text-xs font-bold mt-2">❓ Неможливість верифікації</div>
</div>
</v-click>

</div>

<v-click>

<div class="mt-4 bg-amber-50 p-3 rounded-lg text-center border-2 border-amber-300 text-gray-800">

### 💡 Як RAG вирішує ці проблеми?

</div>

</v-click>

---
layout: default
---

# RAG вирішує ці проблеми

<div class="grid grid-cols-3 gap-6 mt-6">

<v-click>
<div class="text-center">
<div class="bg-red-100 p-3 rounded-t-lg border-2 border-red-300 text-gray-800">
<div class="text-sm">🔴 Knowledge Cutoff</div>
<div class="text-xs text-red-600">Застарілі знання</div>
</div>
<div class="text-2xl py-2">⬇️</div>
<div class="bg-green-100 p-3 rounded-b-lg border-2 border-green-300 text-gray-800">
<div class="text-sm">📚 Актуальна база знань</div>
<div class="text-xs text-green-600">Оновлення в реальному часі</div>
</div>
</div>
</v-click>

<v-click>
<div class="text-center">
<div class="bg-orange-100 p-3 rounded-t-lg border-2 border-orange-300 text-gray-800">
<div class="text-sm">🟠 Галюцинації</div>
<div class="text-xs text-orange-600">Вигадані факти</div>
</div>
<div class="text-2xl py-2">⬇️</div>
<div class="bg-green-100 p-3 rounded-b-lg border-2 border-green-300 text-gray-800">
<div class="text-sm">📖 Цитування джерел</div>
<div class="text-xs text-green-600">Верифіковані відповіді</div>
</div>
</div>
</v-click>

<v-click>
<div class="text-center">
<div class="bg-yellow-100 p-3 rounded-t-lg border-2 border-yellow-300 text-gray-800">
<div class="text-sm">🟡 Приватні дані</div>
<div class="text-xs text-yellow-600">Немає доступу</div>
</div>
<div class="text-2xl py-2">⬇️</div>
<div class="bg-green-100 p-3 rounded-b-lg border-2 border-green-300 text-gray-800">
<div class="text-sm">🏢 Корпоративні документи</div>
<div class="text-xs text-green-600">Повна інтеграція</div>
</div>
</div>
</v-click>

</div>

<v-click>

<div class="mt-6 bg-blue-50 p-4 rounded-lg text-center border-2 border-blue-200 text-gray-800">

### 🎯 RAG = Retrieval-Augmented Generation
**Поєднання потужності LLM з достовірними джерелами знань**

</div>

</v-click>

---
layout: default
---

# Типова архітектура RAG складається з **двох ключових компонентів**:

<div class="grid grid-cols-2 gap-8 mt-8">

<v-click>
<div class="bg-amber-50 p-6 rounded-lg border-2 border-amber-300 text-gray-800">

### 📚 База знань (Knowledge Base)

**Етап індексації** — підготовка даних

<div class="mt-4 text-xs opacity-75">
Виконується один раз або при оновленні документів
</div>

</div>
</v-click>

<v-click>
<div class="bg-blue-50 p-6 rounded-lg border-2 border-blue-300 text-gray-800">

### ⚡ Конвеєр RAG (RAG Pipeline)

**Етап виконання** — обробка запитів

<div class="mt-4 text-xs opacity-75">
Виконується в реальному часі для кожного запиту
</div>

</div>
</v-click>

</div>

<v-click>

<div class="mt-8 text-center text-sm opacity-75">
Розглянемо кожен компонент детальніше...
</div>

</v-click>

---
layout: default
---

# Етап індексації RAG

<div class="flex justify-center items-center h-80">

```mermaid {scale: 0.8}
graph LR
    A["📚 Documents<br/>(Підготовка документів)"] --> B["✂️ Chunking<br/>(Нарізання на фрагменти)"]
    B --> D["🔢 Embedding<br/>(Векторизація тексту)"]
    D --> E["🗄️ Vector DB<br/>(Збереження)"]

    style A fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#1f2937
    style B fill:#ffccbc,stroke:#d84315,stroke-width:2px,color:#1f2937
    style D fill:#b3e5fc,stroke:#0277bd,stroke-width:2px,color:#1f2937
    style E fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#1f2937
```

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
layout: default
---

# Оптимізація RAG: 3 етапи покращення

<div class="mt-4 text-center text-sm opacity-80">

Базовий RAG працює, але для **надійного галузевого помічника** потрібна оптимізація на кожному етапі

</div>

<div class="mt-6 grid grid-cols-3 gap-4">

<v-click>
<div class="bg-green-50 p-4 rounded-lg border-2 border-green-300 text-gray-800">

### 1️⃣ Query Processing

**Обробка запиту**

<div class="text-xs mt-2">

*"Як це працює?"* → *"Поясни роботу модуля X в системі Y"*

</div>

<div class="text-xs mt-2 opacity-75">
Intent Detection, Query Rewriting, Query Expansion
</div>

</div>
</v-click>

<v-click>
<div class="bg-orange-50 p-4 rounded-lg border-2 border-orange-300 text-gray-800">

### 2️⃣ Retrieval

**Пошук**

<div class="text-xs mt-2">

*Знайти саме ті фрагменти, де є відповідь*

</div>

<div class="text-xs mt-2 opacity-75">
Hybrid Search, Metadata Filtering, Re-ranking
</div>

</div>
</v-click>

<v-click>
<div class="bg-blue-50 p-4 rounded-lg border-2 border-blue-300 text-gray-800">

### 3️⃣ Generation

**Генерація**

<div class="text-xs mt-2">

*Відповідь: "Термін гарантії 24 міс." [doc.pdf, стор.2]*

</div>

<div class="text-xs mt-2 opacity-75">
Prompt Engineering, Citation Addition
</div>

</div>
</v-click>

</div>

<v-click>

<div class="mt-6 text-center">

Розглянемо кожен етап детальніше...

</div>

</v-click>

---
layout: default
---

# 1️⃣ Query Processing - Обробка запиту

<div class="mt-4 text-center text-sm opacity-80">
Перетворення нечіткого запиту користувача на точний пошуковий вектор
</div>

<div class="mt-6 grid grid-cols-2 gap-4">

<v-click>
<div class="bg-gray-800 p-4 rounded-lg">

### 🔄 Переписати запит

*"Як це працює?"* → *"Поясни роботу модуля X"*

</div>
</v-click>

<v-click>
<div class="bg-gray-800 p-4 rounded-lg">

### ➕ Розширити синонімами

*"Не працює світло"* → *"зникла електрика", "вибило пробки"*

</div>
</v-click>

<v-click>

<v-click>
<div class="bg-gray-800 p-4 rounded-lg">

### 🎯 Визначити намір

*"Порівняй Python та Java"* → **Порівняння**
*"Підсумуй документ"* → **Узагальнення**

</div>
</v-click>

<div class="bg-gray-800 p-4 rounded-lg">

### 🔀 Розбиття на підзапити

*"Ціна товару X та умови доставки?"*
→ 1. Ціна? 2. Доставка?

</div>
</v-click>

</div>

---
layout: default
---

# 2️⃣ Retrieval Optimization - Пошук


<div class="mt-4 text-center text-sm opacity-80">
Максимізація релевантності результатів пошуку
</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### 🏷️ Metadata Filtering

<v-clicks>

**Фільтрація за атрибутами**

</v-clicks>

<v-click>

<div class="bg-blue-50 p-2 rounded mt-2 text-xs text-gray-800">
<b>📅 За датою:</b> "Накази за 2024" → <code class="text-gray-200">year: 2024</code>
</div>

</v-click>

<v-click>

<div class="bg-purple-50 p-2 rounded mt-1 text-xs text-gray-800">
<b>👤 За роллю:</b> "Інструкція для менеджерів" → <code class="text-gray-200">role: manager</code>
</div>

</v-click>

<v-click>

<div class="bg-green-50 p-2 rounded mt-1 text-xs text-gray-800">
<b>🔢 За версією:</b> "Документація v2.5" → <code class="text-gray-200">version: 2.5</code>
</div>

</v-click>

<v-click>

<div class="bg-orange-50 p-2 rounded mt-1 text-xs text-gray-800">
<b>🔒 За доступом:</b> "Конфіденційні звіти" → <code class="text-gray-200">access: confidential</code>
</div>

</v-click>

</div>

<div>

### 🔀 Hybrid Search

<v-click>

**Поєднання двох підходів:**

</v-click>

<v-clicks>

1. **BM25 (Keyword)**
   - Точні співпадіння
   - Номери, коди, назви

2. **Vector Search (Semantic)**
   - Розуміння сенсу
   - Синоніми, контекст

</v-clicks>

<v-click>

<div class="bg-green-50 p-3 rounded mt-3 text-sm text-gray-800">
<b>Результат:</b> Знаходить документи які:<br/>
✅ Концептуально відповідають запиту<br/>
✅ Містять точні терміни
</div>

</v-click>

</div>

</div>

---
layout: default
---

# Re-ranking - Переранжування

<div class="mt-4">

## 🎯 Проблема
Після гібридного пошуку маємо **багато кандидатів**, але не всі релевантні

</div>

<div class="mt-6">

## ⚙️ Рішення: Cross-Encoder

<v-clicks>

1. **Попередній відбір:** Швидкий пошук → Топ-50 кандидатів
2. **Глибоке оцінювання:** Cross-Encoder аналізує кожен фрагмент
3. **Точне ранжування:** Залишає тільки 5-10 найкращих

</v-clicks>

</div>

<v-click>

<div class="mt-8 bg-gradient-to-r from-blue-50 to-green-50 p-6 rounded-lg text-gray-800">

### 📊 Приклад: "Які штрафи за порушення термінів подачі звіту?"

<div class="grid grid-cols-2 gap-4 mt-4">

<div>
<b>❌ До Re-ranking:</b>
<ol class="text-sm">
<li>Правила подачі звіту</li>
<li>Історія змін у звітності</li>
<li>...(позиція 35) Таблиця санкцій</li>
</ol>
</div>

<div>
<b>✅ Після Re-ranking:</b>
<ol class="text-sm">
<li><b>Таблиця санкцій</b> ← найрелевантніше!</li>
<li>(інші відсіяні)</li>
</ol>
</div>

</div>

</div>

</v-click>

---
layout: default
---

# 3️⃣ Generation - Prompt Engineering

<div class="mt-2 text-center text-sm opacity-80">
Як змусити LLM правильно інтерпретувати знайдену інформацію
</div>

<div class="grid grid-cols-5 gap-3 mt-6">

<v-click>
<div class="bg-purple-50 p-3 rounded-lg text-center text-gray-800 border-2 border-purple-200">
<div class="text-2xl">🎭</div>
<div class="font-bold text-sm mt-1">Роль</div>
<div class="text-xs mt-2 opacity-80">"Ти — галузевий експерт з технічної підтримки"</div>
</div>
</v-click>

<v-click>
<div class="bg-yellow-50 p-3 rounded-lg text-center text-gray-800 border-2 border-yellow-200">
<div class="text-2xl">📋</div>
<div class="font-bold text-sm mt-1">Інструкції</div>
<div class="text-xs mt-2 opacity-80">Формат відповіді, стиль, мова</div>
</div>
</v-click>

<v-click>
<div class="bg-green-50 p-3 rounded-lg text-center text-gray-800 border-2 border-green-200">
<div class="text-2xl">📚</div>
<div class="font-bold text-sm mt-1">Контекст</div>
<div class="text-xs mt-2 opacity-80">Знайдені фрагменти документів</div>
</div>
</v-click>

<v-click>
<div class="bg-red-50 p-3 rounded-lg text-center text-gray-800 border-2 border-red-200">
<div class="text-2xl">⛔</div>
<div class="font-bold text-sm mt-1">Заборони</div>
<div class="text-xs mt-2 opacity-80">"Не вигадуй! Тільки з контексту!"</div>
</div>
</v-click>

<v-click>
<div class="bg-blue-50 p-3 rounded-lg text-center text-gray-800 border-2 border-blue-200">
<div class="text-2xl">📖</div>
<div class="font-bold text-sm mt-1">Цитування</div>
<div class="text-xs mt-2 opacity-80">"Вказуй джерело кожного факту"</div>
</div>
</v-click>

</div>

<v-click>

<div class="mt-4 bg-gray-900 p-3 rounded-lg text-xs font-mono">
<span class="text-purple-400">Роль:</span> <span class="text-gray-300">Ти — експерт технічної підтримки. Твоя задача допомагати користувачам з їх питаннями</span><br/>
<span class="text-yellow-400">Інструкції:</span> <span class="text-gray-300">Відповідай лаконічно. Обовязково цитуй джерела.</span><br/>
<span class="text-green-400">Контекст:</span> <span class="text-gray-300">Контекст: <span class="text-gray-500">[Знайдені документи]</span></span><br/>
<span class="text-red-400">Обмеження:</span> <span class="text-gray-300">Відповідай тільки з контексту! Якщо джерел не знайдено, то так і скажи</span><br/>
<span class="text-blue-400">Запит:</span> <span class="text-gray-300">Питання користувача: <span class="text-gray-500">[Запит користувача]</span></span>
</div>

</v-click>

---
layout: default
---

# 3️⃣ Generation - Приклад відповіді

<div class="flex justify-center mt-8">
<div class="max-w-2xl w-full">

<div class="bg-gray-100 p-4 rounded-lg text-gray-800">
<b>❓ Запит:</b> "Коли починається зимова сесія для 5 курсу?"
</div>

<v-click>

<div class="mt-4 bg-blue-50 p-6 rounded-lg text-gray-800 border-l-4 border-blue-500">

<div class="font-medium">✅ Відповідь системи:</div>

<div class="mt-3">
Зимова екзаменаційна сесія для студентів **5 курсу** розпочинається **13 січня 2025 року** та триватиме до 26 січня.
</div>
<div class="text-xs text-blue-600 mt-1">📎 [Графік_навчального_процесу_2024-2025.pdf, стор. 3]</div>

<div class="mt-3">
Розклад екзаменів буде опубліковано на сайті факультету не пізніше ніж за **2 тижні** до початку сесії.
</div>
<div class="text-xs text-blue-600 mt-1">📎 [Положення_про_організацію_освітнього_процесу.docx, п. 5.4]</div>

</div>

</v-click>

<v-click>

<div class="mt-4 flex gap-4 justify-center text-sm">
<div class="bg-green-100 px-3 py-2 rounded text-gray-800">✅ Точна відповідь</div>
<div class="bg-green-100 px-3 py-2 rounded text-gray-800">✅ Цитати джерел</div>
<div class="bg-green-100 px-3 py-2 rounded text-gray-800">✅ Без галюцинацій</div>
</div>

</v-click>

</div>
</div>

---
layout: section
---

# РОЗДІЛ 3
## Практична реалізація системи

---
layout: default
---

# Архітектура розробленої системи

<div class="flex justify-center mt-4">

```mermaid {scale: 0.75}
graph TB
    subgraph Frontend["🖥️ Frontend (Vue.js)"]
        UI["Інтерфейс користувача"]
    end

    subgraph Backend["⚙️ Backend (FastAPI)"]
        API["REST API"]
        QP["Query Processing"]
        RE["Retrieval Engine"]
        GE["Generation Engine"]
    end

    subgraph Data["💾 Дані"]
        VDB["Vector DB<br/>(ChromaDB)"]
        LLM["LLM API<br/>(OpenAI/Anthropic)"]
        DOCS["Документи"]
    end

    UI --> API
    API --> QP
    QP --> RE
    RE --> VDB
    VDB --> GE
    GE --> LLM
    DOCS --> VDB

    style Frontend fill:#e1f5fe
    style Backend fill:#f3e5f5
    style Data fill:#e8f5e9
```

</div>

<div class="grid grid-cols-3 gap-4 mt-6 text-sm">

<v-click>
<div class="bg-blue-50 p-3 rounded text-gray-800">
<b>Frontend</b><br/>
Vue.js, TypeScript<br/>
Інтерактивний UI
</div>
</v-click>

<v-click>
<div class="bg-purple-50 p-3 rounded text-gray-800">
<b>Backend</b><br/>
FastAPI, Python<br/>
RAG Pipeline
</div>
</v-click>

<v-click>
<div class="bg-green-50 p-3 rounded text-gray-800">
<b>Дані</b><br/>
ChromaDB<br/>
OpenAI Embeddings
</div>
</v-click>

</div>

---
layout: default
---

# Ключові компоненти реалізації

<div class="grid grid-cols-2 gap-6 mt-6">

<div>

### 🔍 Підсистема пошуку

<v-clicks>

- **Semantic Chunking**
  - Розумне розбиття тексту
  - Збереження контексту

- **Hybrid Search**
  - BM25 + Vector Search
  - Оптимальна релевантність

- **Re-ranking**
  - Cross-Encoder моделі
  - Фінальна фільтрація

</v-clicks>

</div>

<div>

### 🤖 Модуль генерації

<v-clicks>

- **Prompt Engineering**
  - Динамічні системні промпти
  - Context Injection

- **Citation System**
  - Автоматичне додавання джерел
  - Метадані документів

- **Post-processing**
  - Форматування відповідей
  - Виявлення галюцинацій

</v-clicks>

</div>

</div>

<v-click>

<div class="mt-8 bg-gradient-to-r from-purple-50 to-blue-50 p-6 rounded-lg text-gray-800">

## 🎯 Результат реалізації

**Працюючий прототип** галузевого помічника з можливістю:
- ✅ Точного пошуку інформації в документах
- ✅ Генерації відповідей з цитуванням джерел
- ✅ Роботи з різними типами документів
- ✅ Інтуїтивного веб-інтерфейсу

</div>

</v-click>

---
layout: section
---

# Висновки

---
layout: default
---

# Висновки та результати

<div class="grid grid-cols-2 gap-6 mt-6">

<div>

## ✅ Виконані завдання

<v-clicks>

1. **Досліджено архітектуру LLM**
   - Transformer, Attention
   - Обмеження та проблеми

2. **Обґрунтовано переваги RAG**
   - Актуальність даних
   - Верифікація фактів

3. **Розроблено архітектуру**
   - Модульна структура
   - Оптимізований pipeline

4. **Реалізовано прототип**
   - Індексація документів
   - Гібридний пошук
   - Генерація з цитуванням

</v-clicks>

</div>

<div>

<v-click>

## 🎯 Практична цінність

**Створено функціонуючу систему** яка:

- 📚 Працює з галузевими документами
- 🔍 Знаходить релевантну інформацію
- ✅ Генерує точні відповіді
- 📖 Цитує джерела
- 🚀 Легко масштабується

</v-click>

<v-click>

## 🔮 Перспективи розвитку

- 🤖 Агентські системи (Agentic RAG)
- 🛠️ Function Calling
- 📊 Автоматична оцінка якості
- 🌐 Багатомовна підтримка
- 🔐 Розширена безпека

</v-click>

</div>

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
