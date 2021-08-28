import textwrap
from typing import Optional
from rich.console import RenderableType, RenderResult, Console, ConsoleOptions
from rich.style import StyleType
from rich.panel import Panel
from rich.align import Align, VerticalCenter
from rich.console import Console, ConsoleOptions, RenderableType, RenderResult
from rich.panel import Panel
from rich.style import StyleType
from textual import events
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import ButtonPressed


class WelcomeScreen(Widget):
    """
    Class for the welcome screen of PyTUI.
    Sublcasses from texutal.widget.Widget
    Includes rendering of the beginning screen.
    """
    def render(self) -> Panel:
        """Renders ASCII art for the welcome screen."""
        return Panel(
            Align.center(
                VerticalCenter(
                    textwrap.dedent(
                        r"""
                                                                                           [blue]██████[/blue]
                        [green]ooooooooo.               ooooooooooooo ooooo     ooo ooooo[/green]        [blue]█▄██████[/blue]
                        [green]`888   `Y88.             8'   888   `8 `888'     `8' `888'[/green]          [blue]█████[/blue] [yellow]██[/yellow]
                         [green]888   .d88' oooo    ooo      888       888       8   888[/green]      [blue]█████████[/blue]  [yellow]███[/yellow]
                         [green]888ooo88P'   `88.  .8'       888       888       8   888[/green]     [blue]█████[/blue]      [yellow]█████[/yellow]
                         [green]888           `88..8'        888       888       8   888[/green]      [blue]███[/blue]  [yellow]█████████[/yellow]
                         [green]888            `888'         888       `88.    .8'   888[/green]       [blue]██[/blue] [yellow]█████[/yellow]
                        [green]o888o            .8'         o888o        `YbodP'    o888o[/green]        [yellow]██████▀█[/yellow]
                                     [green].o..P'[/green]                                                [yellow]██████[/yellow]
                                     [green]`Y8P'[/green]
                        """  # noqa: E501
                    )
                )
            ),
            title="Welcome to PyTUI",
        )


class ContinueButtonRenderable:
    """
    'Renderable' for the ContinueButton.
    Used as a helper class for the continue button.
    """
    def __init__(self, label: RenderableType, style: StyleType = "") -> None:
        self.label = label
        self.style = style

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """
        Dunder method custommed to renderable classes for Rich.
        The arguments denote:
            - console: a Console instance from rich that is a special console for rich purposes.
            - options: a ConsoleOptions instance from rich that denotes options for the special rich console.
        """
        width = options.max_width
        height = 3

        yield Align.center(
            self.label, vertical="middle", style=self.style, width=width, height=height
        )


class ContinueButton(Widget):
    """
    The ContinueButton widget for PyTUI.
    Subclasses from textual.widget.Widget
    """

    def __init__(
        self,
        label: RenderableType,
        name: Optional[str] = None,
        style: StyleType = "white on dark_blue",
    ):
        super().__init__(name=name)
        self.name = name or str(label)
        self.button_style = style

        self.label = label

    label: Reactive[RenderableType] = Reactive("")

    def render(self) -> RenderableType:
        """
        Renders the ContinueButtonRenderable class under self.label, a reactive type.
        Allows a renderable widget.
        """
        return ContinueButtonRenderable(self.label, style=self.button_style)

    async def on_click(self, event: events.Click) -> None:
        """
        Event for when the Continue Button is clicked, under textual.events.Click
        Right now, it merely emits the ButtonPressed widget from Textual, with the instance passed in.
        """
        await self.emit(ButtonPressed(self))