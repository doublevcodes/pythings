from textual.view import View
from textual.widgets import Static


class Contents(View):
    """
    Contents is a class that subclasses from textual.view, and is one of the views of the app
    for the list of concepts that the user can learn.
    """

    CONTENTS = (
        "Getting started",
        "Variables and data types",
        "Control flow: Conditionals",
        "Control flow: Iteration",
    )

    instances = []

    @classmethod
    def create(cls) -> Static:
        """This will create the formatted contents of the list of concepts to learn in the Concepts view."""

        for i, item in enumerate(cls.CONTENTS):
            formatted = f"{i}. {item}"
            instance = Static(formatted)
            cls.instances.append(instance)
            yield instance
