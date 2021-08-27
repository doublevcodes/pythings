from rich.text import Text
from textual.view import View
from textual.widgets import Static


class Contents(View):
    CONTENTS = (
        "Getting started",
        "Variables and data types",
        "Control flow: Conditionals",
        "Control flow: Iteration",
    )

    instances = []

    @classmethod
    def create(cls):
        for i, item in enumerate(cls.CONTENTS):
            formatted = f"{i}. {item}"
            instance = Static(formatted)
            cls.instances.append(instance)
            yield instance
