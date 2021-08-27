from textual.app import App
from textual.widgets import Footer, Placeholder
from textual.reactive import Reactive

from pythings.widgets import WelcomeScreen


class Pythings(App):

    show_menu = Reactive(True)

    async def on_load(self):
        await self.bind("h", "show_menu", "PyThings home menu", key_display="🏠")
        await self.bind("s", "quit", "PyThings Settings", key_display="⚙️ ")
        await self.bind("q", "quit", "Quit PyThings", key_display="🏁")

    async def on_mount(self) -> None:
        welcome = WelcomeScreen()
        self.menu = Placeholder(name="Main menu")

        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(
            welcome, edge="left", name="welcome"
        )
        await self.view.dock(self.menu, edge="left", size=40, z=1)

    def watch_show_menu(self, show_bar: bool) -> None:
        """Called when show_bar changes."""
        self.menu.animate("layout_offset_x", 0 if show_bar else -40)

    async def action_show_menu(self):
        self.show_menu = not self.show_menu


