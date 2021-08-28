import textwrap
from typing import Optional

from rich.align import Align, VerticalCenter
from rich.console import Console, ConsoleOptions, RenderableType, RenderResult
from rich.panel import Panel
from rich.style import StyleType
from textual import events
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import ButtonPressed


class WelcomeScreen(Widget):

    def render(self) -> Panel:
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
    def __init__(self, label: RenderableType, style: StyleType = "") -> None:
        self.label = label
        self.style = style

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        width = options.max_width
        height = 3

        yield Align.center(
            self.label, vertical="middle", style=self.style, width=width, height=height
        )


class ContinueButton(Widget):
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
        return ContinueButtonRenderable(self.label, style=self.button_style)

    async def on_click(self, event: events.Click) -> None:
        await self.emit(ButtonPressed(self))
