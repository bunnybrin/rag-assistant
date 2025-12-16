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

*  Світ відходить від "загальних чат-ботів" до систем, які розуміються на нюансах конкретної галузі.
*  Близько **80%** галузевих знань зберігаються в неструктурованому виді, які складно використовувати для швидкого пошуку.
*  Зростає потреба в системах, які будуть допомагати людині орієнтуватись у великій кількості неструктурованих документів.

</v-clicks>

<v-click>


> **🚀Актуальність полягає:** у створенні моста між потужністю великих мовних моделей та зовнішним джерелом знань.

</v-click>

---
layout: default
---

# Що таке RAG?

<div class="text-lg text-gray-400 mb-6">
Retrieval-Augmented Generation — архітектурний підхід, що поєднує:
</div>

<div class="grid grid-cols-3 gap-6">
<v-clicks>

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

</v-clicks>
</div>

<v-click>

<div class="mt-8 p-4 rounded-lg bg-yellow-500/10 border-l-4 border-yellow-500">
  <span class="text-yellow-400 font-semibold">💡 Ключова ідея:</span> Поєднати потужності LLM з зовнішнім джерелом знань
</div>

</v-click>

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
