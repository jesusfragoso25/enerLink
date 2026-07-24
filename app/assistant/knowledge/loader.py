from app.assistant.knowledge.knowledge_cache import KnowledgeCache


class KnowledgeLoader:

    _loaded = False

    @classmethod
    def load(cls):

        if cls._loaded:
            return

        KnowledgeCache.load()

        cls._loaded = True