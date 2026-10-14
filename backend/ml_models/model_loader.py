# We will be using transfromers from Hugging face
# Many are no longer maintained, just for starters we will be using 
# the robeta transformer, then reasearch on other models again
import logging

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from app.core.config import settings

logger = logging.getLogger(__name__)


class ModelLoader:
    def __init__(self, model_name: str | None = None, cache_dir: str | None = None):
        # Fall back to values from .env / config.py if nothing is passed in
        self.model_name = model_name or settings.MODEL_NAME
        self.cache_dir = cache_dir or settings.MODEL_CACHE_DIR

        # Use the GPU if one is available, otherwise the CPU
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Private: nothing is loaded until load() is called
        self._tokenizer = None
        self._model = None

    @property
    def is_loaded(self) -> bool:
        return self._model is not None and self._tokenizer is not None

    def load(self) -> None:
        """Download (first run only) and load the model into memory."""
        if self.is_loaded:
            return  # Already loaded, don't do the expensive work twice

        logger.info("Loading model '%s' on %s", self.model_name, self.device)
        try:
            self._tokenizer = AutoTokenizer.from_pretrained(
                self.model_name, cache_dir=self.cache_dir
            )
            self._model = AutoModelForSequenceClassification.from_pretrained(
                self.model_name, cache_dir=self.cache_dir
            )
            self._model.to(self.device)
            self._model.eval()  # Inference mode: disables dropout, etc.
        except Exception as exc:
            # Leave the loader in a clean "not loaded" state
            self._tokenizer = None
            self._model = None
            logger.exception("Failed to load model '%s'", self.model_name)
            raise RuntimeError(f"Could not load model '{self.model_name}'") from exc

        logger.info("Model loaded. Labels: %s", self._model.config.id2label)

    @property
    def tokenizer(self):
        if not self.is_loaded:
            self.load()  # Lazy fallback if startup loading was skipped
        return self._tokenizer

    @property
    def model(self):
        if not self.is_loaded:
            self.load()
        return self._model

    @property
    def labels(self) -> dict[int, str]:
        """Maps output index -> label name, e.g. {0: 'Fake', 1: 'Real'}."""
        return self.model.config.id2label



# One shared instance for the whole app. To be always imported, no new one to be created.
model_loader = ModelLoader()