from studyBackend.urls import router
from .views import BookViewSets, ArticleViewSets
router.register(r'book/book', BookViewSets)
router.register(r'book/article', ArticleViewSets)
