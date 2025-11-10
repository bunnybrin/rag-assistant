from typing import List, Dict
from llama_index.core.schema import NodeWithScore


class CitationExtractor:
    @staticmethod
    def extract_sources(source_nodes: List[NodeWithScore]) -> List[Dict]:
        sources = []

        for i, node_with_score in enumerate(source_nodes):
            node = node_with_score.node
            score = node_with_score.score

            source_info = {
                "index": i + 1,
                "score": round(score, 4) if score else None,
                "text": node.get_content()[:200] + "..." if len(node.get_content()) > 200 else node.get_content(),
                "metadata": {}
            }

            if hasattr(node, 'metadata') and node.metadata:
                metadata = node.metadata
                source_info["metadata"] = {
                    "file_name": metadata.get("file_name", "Unknown"),
                    "file_path": metadata.get("file_path", ""),
                    "page_label": metadata.get("page_label", ""),
                }

            sources.append(source_info)

        return sources

    @staticmethod
    def format_sources_for_display(sources: List[Dict]) -> str:
        if not sources:
            return "Джерела не знайдені"

        formatted = []
        for source in sources:
            file_name = source["metadata"].get("file_name", "Unknown")
            page = source["metadata"].get("page_label", "")
            score = source["score"]

            source_text = f"[{source['index']}] {file_name}"
            if page:
                source_text += f" (сторінка {page})"
            if score:
                source_text += f" - релевантність: {score}"

            formatted.append(source_text)

        return "\n".join(formatted)
