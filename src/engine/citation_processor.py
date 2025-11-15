from typing import List, Optional
from llama_index.core.postprocessor.types import BaseNodePostprocessor
from llama_index.core.schema import NodeWithScore, QueryBundle, MetadataMode


class CitationNodePostprocessor(BaseNodePostprocessor):

    def __init__(self, metadata_mode: MetadataMode = MetadataMode.NONE):
        super().__init__()
        self._metadata_mode = metadata_mode

    def _postprocess_nodes(
        self,
        nodes: List[NodeWithScore],
        query_bundle: Optional[QueryBundle] = None,
    ) -> List[NodeWithScore]:
        new_nodes: List[NodeWithScore] = []

        for idx, node in enumerate(nodes, start=1):
            content = node.node.get_content(metadata_mode=self._metadata_mode)

            cited_text = f"Джерело {idx}:\n{content}"

            new_node = NodeWithScore(
                node=node.node.model_copy(),
                score=node.score,
            )
            new_node.node.set_content(cited_text)
            new_nodes.append(new_node)

        return new_nodes
