#include "Menu.hpp"
#include "Menu\Label.hpp"
#include <string>

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
        sf::String temp;
        temp = "derp";
        Menu* t = new Menu();
        t->Add(new Label("SomeString"));
        return t;
    }
}
