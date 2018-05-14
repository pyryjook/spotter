from urwid import BoxAdapter, AttrWrap,font, Pile, SolidFill, Overlay, ListBox, BigText, Text, Filler, Padding, Divider, Button, connect_signal, AttrMap, SimpleFocusListWalker
from urwid_pydux import Component

class Menu(Component):
    prop_types = {
        'choices': list,
        'title': str,
        'go_to_prev': str,
        'exit_app': callable,
        'choose_item': callable
    }

    def component_will_mount(self, props):
        self.exit_app = props['exit_app']
        self.choose_item = props['choose_item']

    def menu(self, choices, go_to_prev):
        def get_button(label, id):
            button = Button(label, None, id)
            connect_signal(button, 'click', self.chosen_item, id)
            return button

        body = []
        for c in choices:
            button = get_button(c[0], c[1])
            body.append(AttrMap(button, None, focus_map='reversed'))
        
        body.append(Divider())
        body.append(get_button(go_to_prev[0], go_to_prev[1]))

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
        main = Filler(self.menu(props['choices'], props['go_to_prev']), valign='middle', height=('relative', 100))
        widgets = [title_elem, main]
        return Pile(widgets)
