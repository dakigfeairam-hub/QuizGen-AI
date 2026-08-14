from ._anvil_designer import QuizGen_AITemplate
from anvil import *


class QuizGen_AI(QuizGen_AITemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
