#include "Menu.hpp"
#include "Game.hpp"
#include "Global.hpp"

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

    void Menu::Add(ControlBase* obj)
    {
        m_Objects.push_back(obj);
    }
}
