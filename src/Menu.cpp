#include "Menu.hpp"
#include "MenuControls/Label.hpp"
#include "MenuControls/Image.hpp"
#include "MenuControls/Button.hpp"
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

    void Menu::Tick()
    {
    }

    void Menu::Add(ControlBase* obj)
    {
        m_Objects.push_back(obj);
    }
}
