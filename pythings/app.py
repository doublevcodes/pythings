from textual.app import App
from textual.reactive import Reactive
from textual.widgets import Footer, Placeholder

from pythings.widgets import WelcomeScreen


class PyTUI(App):
    show_menu = Reactive(False)
    show_settings = Reactive(False)

    async def on_load(self) -> None:
        """
        When loading the app, binds keys to their respective purposes.
        H - show the menu
        S - show the settings
        Q - quit the application
        """
        await self.bind("h", "show_menu", "PyTUI home menu", key_display="🏠 (h)")
        await self.bind("s", "show_settings", "PyTUI Settings", key_display="⚙️  (s)")
        await self.bind("q", "quit", "Quit PyTUI", key_display="🏁 (q)")

    async def on_mount(self) -> None:
        """
        When the app is initializing and is finished loading.
        On initialization, numerous views are docked such as "welcome", a footer, etc.
        """
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
        """
        This is an action that will watch the show_menu attribute and is called when it changes.
        This will be part of the animation for when the menu appears or disappears.
        The arguments are:
            - show_bar: a boolean representing the class attribute show_menu which denotes whether the menu is
            being displayed or not.
        """
        self.menu.animate("layout_offset_x", 0 if show_bar else -40)

    async def action_show_menu(self) -> None:
        """
        The key H binds this function to displaying and removing the menu from the display screen.
        This will reverse the current state of the menu, where if it is already displaying and the user
        presses H, it will not display anymore, otherwise, it will display.
        """
        self.show_menu = not self.show_menu

    def watch_show_settings(self, show_settings: bool) -> None:
        """
        This is a watch action, which will be called once the show_settings attribute is changed.
        This watch action will animate the settings to disappear or appear depending on show_settings.
        The arguments are:
            - show settings: a boolean that denotes whether the settings is currently on or off, which is also
            an instance attribute.
        """
        self.settings.animate("layout_offset_x", 0 if show_settings else 40)

    async def action_show_settings(self) -> None:
        """
        This will reverse the instance attribute show_settings, when the S key is pressed.
        If the settings are already being displayed, this will change the show_settings attribute to False,
        and therefore call the watch action which animates out the settings. Otherwise, this will animate the settings
        to be displayed.
        """
        self.show_settings = not self.show_settings
