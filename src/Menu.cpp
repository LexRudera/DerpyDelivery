#include "Menu.hpp"
#include "Menu\Label.hpp"

namespace me
{
    Menu::Menu()
    {
        //ctor
    }

    Menu::~Menu()
    {
        //dtor
    }

    void Menu::Tick()
    {

    }

    void Menu::Add(ControlBase* obj)
    {

    }

    Menu* Menu::MainMenu()
    {
        Menu* t = new Menu();
        t->Add(new Label());
        return t;
    }
}
