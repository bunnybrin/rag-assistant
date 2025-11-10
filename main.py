from src.services.indexing_service import IndexingService

service = IndexingService()

status = service.get_index_status()

if status["exists"]:
    print(f"📂 Знайдено існуючий індекс з {status['total_documents']} документами")
    print("🔄 Завантаження індексу...")
    index = service.load_existing_index()
    print("✅ Індекс успішно завантажено!")
    doc_count = status['total_documents']
else:
    print("🆕 Індекс не знайдено. Створення нового індексу...")
    result = service.index_documents()
    print(f"✅ {result.message}")
    doc_count = service.get_index_status()['total_documents']

print(f"\n📊 Готово! Індекс містить {doc_count} документів")