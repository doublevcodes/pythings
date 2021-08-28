from textual.app import App
from textual.reactive import Reactive
from textual.widgets import Footer, Placeholder

from pythings.widgets import WelcomeScreen


class PyTUI(App):

    show_menu = Reactive(False)
    show_settings = Reactive(False)

    async def on_load(self):
        await self.bind("h", "show_menu", "PyTUI home menu", key_display="🏠 (h)")
        await self.bind("s", "show_settings", "PyTUI Settings", key_display="⚙️  (s)")
        await self.bind("q", "quit", "Quit PyTUI", key_display="🏁 (q)")

    async def on_mount(self) -> None:
        welcome = WelcomeScreen()
        self.menu = Placeholder(name="Main menu")
        self.settings = Placeholder(name="Settings")

        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(
            welcome, edge="left", name="welcome"
        )
        self.menu.animate("layout_offset_x", -40)
        await self.view.dock(self.menu, edge="left", size=40, z=1)
        self.settings.animate("layout_offset_x", 40)
        await self.view.dock(self.settings, edge="right", size=40, z=1)

    def watch_show_menu(self, show_bar: bool) -> None:
        """Called when show_bar changes."""
        self.menu.animate("layout_offset_x", 0 if show_bar else -40)

    async def action_show_menu(self):
        self.show_menu = not self.show_menu

    def watch_show_settings(self, show_settings: bool) -> None:
        self.settings.animate("layout_offset_x", 0 if show_settings else 40)

    async def action_show_settings(self):
        self.show_settings = not self.show_settings
