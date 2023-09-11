from typing import Iterator, Optional

from pptx.shared import ParentedElementProxy, PartElementProxy
from pptx.shapes.shapetree import SlideShapes
from pptx.text.text import TextFrame

class _BaseSlide(PartElementProxy): ...

class NotesSlide(_BaseSlide):
    @property
    def notes_text_frame(self) -> Optional[TextFrame]: ...

class Slide(_BaseSlide):
    @property
    def has_notes_slide(self) -> bool: ...
    @property
    def notes_slide(self) -> NotesSlide: ...
    @property
    def shapes(self) -> SlideShapes: ...

class Slides(ParentedElementProxy):
    def __iter__(self) -> Iterator[Slide]: ...
    def __len__(self) -> int: ...
