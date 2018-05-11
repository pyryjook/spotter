from urwid import BoxAdapter, AttrWrap,font, Pile, SolidFill, Overlay, ListBox, BigText, Text, Filler, Padding, Divider, Button, connect_signal, AttrMap, SimpleFocusListWalker
from urwid_pydux import Component

from actions import show_top_songs

class MainMenu(Component):
    prop_types = {
        'choices': list,
        'title': str,
        'exit_app': callable,
        'choose_item': callable
    }

    def component_will_mount(self, props):
        self.exit_app = props['exit_app']
        self.choose_item = props['choose_item']

    def menu(self, choices):
        body = [Divider()]
        for c in choices:
            button = Button(c[0], None, c[1])
            connect_signal(button, 'click', self.chosen_item, c[1])
            body.append(AttrMap(button, None, focus_map='reversed'))
        return ListBox(SimpleFocusListWalker(body))

    def chosen_item(self, button, choice):
        if choice == 'exit':
            self.exit_app()
        else:
            self.choose_item(choice)

    def render_component(self, props):
        title_elem = BigText(props['title'],  font.HalfBlock5x4Font())
        title_elem = Padding(title_elem, 'center', None)
        title_elem = AttrWrap(title_elem, 'bigtext')
        title_elem = Filler(title_elem, 'top', 4)
        # title_elem = BoxAdapter(title_elem, 7)
        main = Filler(self.menu(props['choices']), valign='middle', height=('relative', 100))
        widgets = [title_elem, main]
        return Pile(widgets)
        # txt = Text(props['title'])

        # return Filler(txt, 'top')
