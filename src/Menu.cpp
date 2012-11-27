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
        m_Objects.push_back(obj);
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
